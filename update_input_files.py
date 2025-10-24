#!/usr/bin/env python3
"""
Update input folder files by:
1. Comparing key features with JSON files
2. Adding Business Objects from JSON files
3. Adding structure specifications
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set


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
                    'data': data
                }
        except Exception as e:
            print(f"Error loading {json_file}: {e}")

    return json_data


def extract_capabilities_from_input(content: str) -> List[Tuple[str, str, List[str]]]:
    """Extract domain, capability names and key features from input file."""
    capabilities = []

    # Split by ### to get domains
    domain_sections = re.split(r'^###\s+', content, flags=re.MULTILINE)

    for section in domain_sections[1:]:  # Skip first empty split
        lines = section.split('\n')
        domain_line = lines[0].strip()

        # Extract domain name (before "with its business capabilities")
        domain_match = re.match(r'^(.+?)\s+\([^)]+\)\s+with', domain_line)
        if domain_match:
            domain_name = domain_match.group(1).strip()
        else:
            domain_name = domain_line.split('(')[0].strip()

        # Find all capabilities (####) in this domain
        cap_sections = re.split(r'^####\s+', '\n'.join(lines), flags=re.MULTILINE)

        for cap_section in cap_sections[1:]:  # Skip first empty split
            cap_lines = cap_section.split('\n')
            cap_line = cap_lines[0].strip()

            # Extract capability name
            cap_name_match = re.match(r'\*\*(.+?)\*\*', cap_line)
            if cap_name_match:
                cap_name = cap_name_match.group(1).strip()
            else:
                cap_name = cap_line.strip()

            # Extract key features
            key_features = []
            in_key_functions = False

            for line in cap_lines[1:]:
                line = line.strip()
                if 'Key Functions:' in line or 'Key Features:' in line:
                    in_key_functions = True
                    # Check if features are on same line
                    remainder = line.split(':', 1)[1].strip() if ':' in line else ''
                    if remainder:
                        features = [f.strip() for f in remainder.split(';') if f.strip()]
                        key_features.extend(features)
                elif in_key_functions:
                    if line.startswith('-'):
                        feature = line[1:].strip()
                        if feature:
                            key_features.append(feature)
                    elif line and not line.startswith('###') and not line.startswith('####'):
                        # Multi-line or semicolon-separated features
                        features = [f.strip() for f in line.split(';') if f.strip()]
                        key_features.extend(features)
                    elif not line:
                        in_key_functions = False

            capabilities.append((domain_name, cap_name, key_features))

    return capabilities


def compare_key_features(input_features: List[str], json_features: List[str]) -> Tuple[List[str], List[str]]:
    """Compare key features and return missing ones."""
    # Normalize for comparison
    input_set = set(f.lower().strip() for f in input_features)
    json_set = set(f.lower().strip() for f in json_features)

    missing_in_input = []
    missing_in_json = []

    for feature in json_features:
        if feature.lower().strip() not in input_set:
            missing_in_input.append(feature)

    for feature in input_features:
        if feature.lower().strip() not in json_set:
            missing_in_json.append(feature)

    return missing_in_input, missing_in_json


def get_business_objects(json_data: Dict) -> List[str]:
    """Extract business object names from JSON data."""
    business_objects = json_data['domain']['capability'].get('business_objects', [])
    return [bo['name'] for bo in business_objects if bo.get('name')]


def process_input_file(input_file: Path, json_index: Dict) -> Dict:
    """Process an input file and return analysis results."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    capabilities = extract_capabilities_from_input(content)

    results = {
        'file': input_file.name,
        'capabilities': [],
        'total_capabilities': len(capabilities),
        'matched': 0,
        'not_found': 0
    }

    for domain, cap_name, input_features in capabilities:
        if cap_name in json_index:
            results['matched'] += 1
            json_cap = json_index[cap_name]['data']['domain']['capability']
            json_features = [kf['name'] for kf in json_cap.get('key_features', [])]
            business_objects = get_business_objects(json_index[cap_name]['data'])

            missing_in_input, missing_in_json = compare_key_features(input_features, json_features)

            results['capabilities'].append({
                'domain': domain,
                'name': cap_name,
                'input_features': input_features,
                'json_features': json_features,
                'missing_in_input': missing_in_input,
                'missing_in_json': missing_in_json,
                'business_objects': business_objects,
                'has_differences': len(missing_in_input) > 0 or len(missing_in_json) > 0
            })
        else:
            results['not_found'] += 1
            results['capabilities'].append({
                'domain': domain,
                'name': cap_name,
                'input_features': input_features,
                'json_features': [],
                'missing_in_input': [],
                'missing_in_json': input_features,
                'business_objects': [],
                'has_differences': True,
                'not_found_in_json': True
            })

    return results


def generate_report(all_results: List[Dict]) -> str:
    """Generate a comprehensive report."""
    report = []
    report.append("=" * 80)
    report.append("INPUT FILES ANALYSIS REPORT")
    report.append("=" * 80)

    total_caps = 0
    total_matched = 0
    total_not_found = 0
    total_with_diff = 0

    for result in all_results:
        report.append(f"\n## File: {result['file']}")
        report.append(f"   Total Capabilities: {result['total_capabilities']}")
        report.append(f"   Matched with JSON: {result['matched']}")
        report.append(f"   Not Found in JSON: {result['not_found']}")

        total_caps += result['total_capabilities']
        total_matched += result['matched']
        total_not_found += result['not_found']

        caps_with_diff = sum(1 for c in result['capabilities'] if c['has_differences'])
        total_with_diff += caps_with_diff
        report.append(f"   Capabilities with Differences: {caps_with_diff}")

        # Show capabilities with differences
        for cap in result['capabilities']:
            if cap['has_differences']:
                report.append(f"\n   ### {cap['name']} (Domain: {cap['domain']})")

                if cap.get('not_found_in_json'):
                    report.append(f"       ⚠️  NOT FOUND IN JSON REPOSITORY")

                if cap['missing_in_input']:
                    report.append(f"       Missing in Input (in JSON):")
                    for feature in cap['missing_in_input']:
                        report.append(f"         + {feature}")

                if cap['missing_in_json']:
                    report.append(f"       Missing in JSON (in Input):")
                    for feature in cap['missing_in_json']:
                        report.append(f"         - {feature}")

                if cap['business_objects']:
                    report.append(f"       Business Objects: {', '.join(cap['business_objects'])}")

    report.append("\n" + "=" * 80)
    report.append("SUMMARY")
    report.append("=" * 80)
    report.append(f"Total Capabilities: {total_caps}")
    report.append(f"Matched: {total_matched}")
    report.append(f"Not Found: {total_not_found}")
    report.append(f"With Differences: {total_with_diff}")
    report.append("=" * 80)

    return "\n".join(report)


def main():
    """Main function to analyze input files."""
    print("Loading JSON repository data...")
    json_index = load_all_json_data()
    print(f"Loaded {len(json_index)} capabilities from JSON files")

    input_dir = Path("input")
    if not input_dir.exists():
        print("Error: input folder not found")
        return

    md_files = list(input_dir.glob("*.md"))
    print(f"\nFound {len(md_files)} MD files in input folder")

    all_results = []

    for md_file in md_files:
        print(f"\nProcessing {md_file.name}...")
        results = process_input_file(md_file, json_index)
        all_results.append(results)

    # Generate report
    report = generate_report(all_results)

    # Save report
    report_file = Path("input/analysis_report.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n✓ Report saved to: {report_file}")
    print("\n" + report)


if __name__ == "__main__":
    main()
