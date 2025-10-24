#!/usr/bin/env python3
"""
Convert Markdown files to JSON format for BIAN capability documentation.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional


def extract_capability_name(content: str) -> str:
    """Extract capability name from the first ### heading."""
    match = re.search(r'^###\s+(.+?)\s*-\s*Domain Expertise', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    # Fallback: try to get first ### heading
    match = re.search(r'^###\s+(.+?)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()

    return ""


def extract_section_content(content: str, heading: str) -> str:
    """Extract content under a specific heading."""
    # Try #### format first
    pattern = rf'^####\s+{re.escape(heading)}\s*\n(.*?)(?=^####|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        return match.group(1).strip()

    # Try numbered format (e.g., "#### 2. Role Definition")
    pattern = rf'^####\s+\d+\.\s+{re.escape(heading)}\s*\n(.*?)(?=^####|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        return match.group(1).strip()

    # Try ### format as fallback
    pattern = rf'^###\s+{re.escape(heading)}\s*\n(.*?)(?=^###|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        return match.group(1).strip()

    return ""


def extract_api_link(content: str) -> str:
    """Extract API BIAN Portal link."""
    # Try "#### API BIAN Portal Link" or "#### API Details"
    patterns = [
        r'####\s+\d*\.?\s*API\s+BIAN\s+Portal\s+Link\s*\n(.+?)(?=\n\n|$)',
        r'####\s+API\s+BIAN\s+Portal\s+Link\s*\n(.+?)(?=\n\n|$)',
        r'###\s+API\s+BIAN\s+Portal\s+Link\s*\n(.+?)(?=\n\n|$)',
        r'####\s+API\s+Details\s*\n.*?BIAN\s+Portal\s+Link.*?\[(.+?)\]\((.+?)\)',
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            text = match.group(0)
            # Extract clean URL from markdown link or direct URL
            url_match = re.search(r'https?://app\.swaggerhub\.com/apis/[^\s\)\]]+', text)
            if url_match:
                return url_match.group(0)

    return ""


def extract_key_features(content: str) -> List[str]:
    """Extract key features as a list."""
    features = []

    # Find Key Features section - try both formats
    section = extract_section_content(content, "Key Features")
    if not section:
        return features

    # Extract bullet points
    lines = section.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('-') or line.startswith('•'):
            feature = line[1:].strip()
            if feature:
                features.append(feature)
        elif re.match(r'^\d+\.', line):  # Handle numbered lists
            feature = re.sub(r'^\d+\.\s*', '', line).strip()
            if feature:
                features.append(feature)

    return features


def extract_core_business_object(content: str) -> Dict[str, str]:
    """Extract core business object name and description."""
    obj_name = ""

    # Try inline format: **Core Business Object:** ObjectName
    match = re.search(r'\*\*Core Business Object:\*\*\s*(.+?)(?=\n|$)', content)
    if match:
        obj_name = match.group(1).strip()
    else:
        # Try section format: #### Core Business Object or #### 4. Core Business Object
        section = extract_section_content(content, "Core Business Object")
        if section:
            obj_name = section.split('\n')[0].strip()

    # Clean up the object name
    if obj_name:
        # Remove any HTML/link references like (object_25.html?object=31474)
        obj_name = re.sub(r'\s*\([^)]*\.html[^)]*\)\s*', '', obj_name)
        # Remove markdown formatting (**, ###, -, etc.)
        obj_name = re.sub(r'^[#*\-\s]+', '', obj_name)
        obj_name = re.sub(r'[*:]+$', '', obj_name)
        obj_name = obj_name.strip()

        # Check if valid
        if obj_name and obj_name.lower() not in ['not specified', 'n/a', 'none', 'not specified in the document']:
            return {"name": obj_name, "description": ""}

    return {"name": "", "description": ""}


def generate_feature_description(feature_name: str, definition: str, role: str) -> str:
    """Generate contextual description for a key feature."""
    # Create a concise description focused on the feature itself
    feature_lower = feature_name.lower()

    # Simple, focused description based on the feature
    if definition:
        # Extract the main purpose from definition (first sentence)
        main_purpose = definition.split('.')[0] if '.' in definition else definition
        return f"Enables {feature_lower} to support {main_purpose.lower()}"

    # Fallback to just describing what the feature enables
    return f"Enables {feature_lower}"


def parse_md_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """Parse a single MD file and return JSON structure."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # Extract division and domain from path
    parts = file_path.parts
    # Find where the division starts (after the root)
    division = ""
    domain_name = ""

    # Go through parts to find division (top-level folder) and domain (sub-folder)
    for i, part in enumerate(parts):
        if part in ["Customer and Distribution", "Enterprise Enabling",
                    "Enterprise Management and Controlling", "Marketing and Sales",
                    "Product and Service Enabling"]:
            division = part
            if i + 1 < len(parts) - 1:  # -1 because last part is the file
                domain_name = parts[i + 1]
            break

    # Extract content sections
    capability_name = extract_capability_name(content)
    definition = extract_section_content(content, "Executive Summary")
    role = extract_section_content(content, "Role Definition")
    example = extract_section_content(content, "Example of Use")
    api_link = extract_api_link(content)
    core_business_obj = extract_core_business_object(content)

    # Extract and process key features
    features = extract_key_features(content)
    key_features = []

    for feature in features:
        key_features.append({
            "name": feature,
            "description": generate_feature_description(feature, definition, role),
            "type": "Implemented",
            "mode": "Active",
            "it_mappings": [
                {
                    "provider_system": "",
                    "consumer_systems": [""],
                    "api_function": "",
                    "integration_type": "REST | GraphQL | SOAP | Event | Batch",
                    "data_object": "",
                    "implementation_status": "Active | Passive | Deprecated",
                    "attributes": [
                        {
                            "name": "",
                            "meaning": ""
                        }
                    ]
                }
            ]
        })

    # Build business objects list
    business_objects = []
    if core_business_obj["name"]:
        business_objects.append({
            "name": core_business_obj["name"],
            "description": core_business_obj["description"],
            "integration_mappings": [
                {
                    "provider_system": "",
                    "consumer_systems": [""],
                    "topic_name": "",
                    "integration_type": "Kafka | Event Stream | Batch",
                    "implementation_status": "Active | Passive | Deprecated",
                    "attributes": [
                        {
                            "name": "",
                            "meaning": ""
                        }
                    ]
                }
            ]
        })

    # Build JSON structure with new format
    json_data = {
        "domain": {
            "name": domain_name,
            "area": division,
            "knowhow": [
                {
                    "fact_id": "",
                    "title": "",
                    "description": "",
                    "related_to": "",
                    "category": ""
                }
            ],
            "capability": {
                "name": capability_name,
                "definition": definition,
                "role": role,
                "example": example,
                "status": "Inactive",
                "pattern": {},
                "core_systems": [],
                "api_bian_link": api_link,
                "key_features": key_features,
                "business_objects": business_objects,
                "process_links": [
                    {
                        "process_name": "",
                        "execution_mode": "Manual | Semi-Automated | Automated",
                        "step_order": 0,
                        "avg_duration_sec": 0
                    }
                ],
                "impact_analysis": {
                    "note": ""
                }
            }
        }
    }

    return json_data


def main():
    """Main function to process all MD files."""
    base_dir = Path(".")

    # Find all MD files
    md_files = list(base_dir.glob("**/*.md"))

    # Exclude README.md
    md_files = [f for f in md_files if f.name != "README.md"]

    print(f"Found {len(md_files)} MD files to process")

    success_count = 0
    error_count = 0

    for md_file in md_files:
        # Skip hidden directories
        if any(part.startswith('.') for part in md_file.parts):
            continue

        print(f"Processing: {md_file}")

        # Parse MD file
        json_data = parse_md_file(md_file)

        if json_data is None:
            error_count += 1
            continue

        # Generate JSON file path (same location, .json extension)
        json_file = md_file.with_suffix('.json')

        # Write JSON file
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            print(f"  ✓ Created: {json_file}")
            success_count += 1
        except Exception as e:
            print(f"  ✗ Error writing {json_file}: {e}")
            error_count += 1

    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"  Successful: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total: {len(md_files)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
