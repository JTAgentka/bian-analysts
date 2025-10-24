#!/usr/bin/env python3
"""
Update input MD files with:
1. Structure specification notes
2. Business objects from JSON repository
"""

import json
import re
from pathlib import Path
from typing import Dict, List


def load_all_json_data() -> Dict[str, Dict]:
    """Load all JSON files and index by capability name."""
    json_data = {}
    base_dir = Path(".")

    for json_file in base_dir.glob("**/*.json"):
        # Skip input folder and hidden directories
        if 'input' in json_file.parts or any(part.startswith('.') for part in json_file.parts):
            continue

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                cap_name = data['domain']['capability']['name']
                json_data[cap_name] = {
                    'file': str(json_file),
                    'data': data,
                    'domain': data['domain']['name']
                }
        except Exception as e:
            pass

    return json_data


def get_business_objects_for_domain(domain_name: str, json_index: Dict) -> List[str]:
    """Get all business objects for capabilities in a domain."""
    business_objects = []

    for cap_name, cap_data in json_index.items():
        if cap_data['domain'] == domain_name:
            bus_objs = cap_data['data']['domain']['capability'].get('business_objects', [])
            for bo in bus_objs:
                if bo.get('name'):
                    business_objects.append(bo['name'])

    return sorted(set(business_objects))


def update_input_file(input_file: Path, json_index: Dict) -> str:
    """Update an input MD file with structure notes and business objects."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add structure specification at the top
    header = """## Structure Specification
**Note:** In this document:
- `###` denotes **Domain** level (e.g., Agreement Management, Payment Management)
- `####` denotes **Capability** level (e.g., Payment Initiation, Credit Facility)

---

"""

    # Check if header already exists
    if "## Structure Specification" not in content:
        # Insert after the first ## heading
        lines = content.split('\n')
        insert_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('## '):
                insert_idx = i + 1
                break

        lines.insert(insert_idx, '\n' + header)
        content = '\n'.join(lines)

    # Extract domains and add business objects
    updated_content = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]
        updated_content.append(line)

        # Check if this is a domain heading (###)
        if line.startswith('###') and not line.startswith('####'):
            # Extract domain name
            domain_match = re.match(r'^###\s+(.+?)\s+\([^)]+\)', line)
            if domain_match:
                domain_name = domain_match.group(1).strip()

                # Get business objects for this domain
                business_objects = get_business_objects_for_domain(domain_name, json_index)

                if business_objects:
                    # Check if Business Objects section already exists
                    has_bo_section = False
                    for j in range(i + 1, min(i + 20, len(lines))):
                        if '**Business Objects' in lines[j]:
                            has_bo_section = True
                            break
                        if lines[j].startswith('###'):
                            break

                    if not has_bo_section:
                        # Add Business Objects section
                        bo_section = [
                            f"  **Business Objects (Owner):** {', '.join(business_objects)}"
                        ]
                        updated_content.extend(bo_section)

        i += 1

    return '\n'.join(updated_content)


def main():
    """Main function to update input files."""
    print("Loading JSON repository data...")
    json_index = load_all_json_data()
    print(f"Loaded {len(json_index)} capabilities from JSON files\n")

    # Group capabilities by domain for reporting
    domain_capabilities = {}
    for cap_name, cap_data in json_index.items():
        domain = cap_data['domain']
        if domain not in domain_capabilities:
            domain_capabilities[domain] = []
        domain_capabilities[domain].append(cap_name)

    print(f"Found {len(domain_capabilities)} unique domains\n")

    input_dir = Path("input")
    if not input_dir.exists():
        print("Error: input folder not found")
        return

    md_files = list(input_dir.glob("*.md"))
    print(f"Found {len(md_files)} MD files in input folder\n")

    for md_file in md_files:
        print(f"Processing {md_file.name}...")

        try:
            updated_content = update_input_file(md_file, json_index)

            # Create backup
            backup_file = md_file.with_suffix('.md.backup')
            with open(md_file, 'r', encoding='utf-8') as f:
                with open(backup_file, 'w', encoding='utf-8') as backup:
                    backup.write(f.read())

            # Write updated content
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"  ✓ Updated {md_file.name} (backup saved as {backup_file.name})")

        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")

    print("\n" + "=" * 70)
    print("Update complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
