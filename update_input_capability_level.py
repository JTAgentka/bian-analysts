#!/usr/bin/env python3
"""
Update input MD files with:
1. Structure specification notes
2. Business objects at CAPABILITY level (####)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple


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


def get_business_objects_for_capability(cap_name: str, json_index: Dict) -> List[str]:
    """Get business objects for a specific capability."""
    if cap_name in json_index:
        bus_objs = json_index[cap_name]['data']['domain']['capability'].get('business_objects', [])
        return [bo['name'] for bo in bus_objs if bo.get('name')]
    return []


def normalize_capability_name(cap_text: str) -> str:
    """Extract and normalize capability name from input text."""
    # Remove leading dash and asterisks
    cap_text = re.sub(r'^-?\s*\*\*', '', cap_text)
    cap_text = re.sub(r'\*\*.*$', '', cap_text)
    cap_text = cap_text.strip()
    return cap_text


def update_input_file(input_file: Path, json_index: Dict) -> str:
    """Update an input MD file with structure notes and business objects at capability level."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add structure specification at the top
    header = """## Structure Specification
**Note:** In this document:
- `###` denotes **Domain** level (e.g., Agreement Management, Payment Management)
- `####` denotes **Capability** level (e.g., Payment Initiation, Credit Facility)

---

"""

    # Remove old header if exists
    content = re.sub(r'## Structure Specification.*?---\s*\n', '', content, flags=re.DOTALL)

    # Insert new header after the first ## heading
    lines = content.split('\n')
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            insert_idx = i + 1
            break

    lines.insert(insert_idx, '\n' + header)
    content = '\n'.join(lines)

    # Remove old domain-level business object lines
    content = re.sub(r'^\s+\*\*Business Objects \(Owner\):\*\*.*$', '', content, flags=re.MULTILINE)

    # Now add business objects at capability level
    updated_lines = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]
        updated_lines.append(line)

        # Check if this is a capability line (####)
        if line.startswith('####'):
            # Extract capability name
            cap_match = re.search(r'####\s+[-\*\s]*\*\*(.+?)\*\*', line)
            if cap_match:
                cap_name_raw = cap_match.group(1).strip()
                cap_name = normalize_capability_name(cap_name_raw)

                # Get business objects for this capability
                business_objects = get_business_objects_for_capability(cap_name, json_index)

                if business_objects:
                    # Check if BO already added on next few lines
                    has_bo = False
                    for j in range(i + 1, min(i + 5, len(lines))):
                        if '**Business Object' in lines[j]:
                            has_bo = True
                            break
                        if lines[j].startswith('####'):
                            break

                    if not has_bo:
                        # Add business objects line
                        bo_text = ', '.join(business_objects)
                        updated_lines.append(f"  **Business Object (Owner):** {bo_text}")

        i += 1

    return '\n'.join(updated_lines)


def main():
    """Main function to update input files."""
    print("Loading JSON repository data...")
    json_index = load_all_json_data()
    print(f"Loaded {len(json_index)} capabilities from JSON files\n")

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
    print("Backups saved with .backup extension")
    print("=" * 70)


if __name__ == "__main__":
    main()
