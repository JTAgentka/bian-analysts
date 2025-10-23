# BIAN Capability Documentation

This repository contains BIAN (Banking Industry Architecture Network) capability documentation in both Markdown and JSON formats.

## Structure

The repository is organized by divisions and domains:

- **Customer and Distribution** (45 capabilities)
  - Channel Management
  - Customer Management
  - Interaction Management
  - Partner Management

- **Enterprise Enabling** (12 capabilities)
  - Legal Support Management
  - Task Management

- **Enterprise Management and Controlling** (32 capabilities)
  - Fraud Incident Management
  - Policy Management
  - Risk Management

- **Marketing and Sales** (25 capabilities)
  - Brand Management
  - Campaign Management
  - Event Management
  - Lead Management
  - Loyalty Management
  - Market Management
  - Message Management
  - Offer Management
  - Sales Plan Management

- **Product and Service Enabling** (100 capabilities)
  - Agreement Management
  - Collateral Management
  - Financial Instrument Management
  - Investment Portfolio Management
  - Issued Device Management
  - Money Movement Management
  - Order Management
  - Payment Management
  - Product Management
  - Trade Finance Management
  - Trust Management

## File Formats

Each capability is documented in two formats:

1. **Markdown (.md)** - Human-readable documentation with sections for:
   - Domain Expertise
   - Role Definition
   - Executive Summary
   - Example of Use
   - Key Features
   - API BIAN Portal Links

2. **JSON (.json)** - Structured data format with:
   - Division and domain information
   - Capability details (name, definition, role, example)
   - Key features with descriptions
   - API links
   - Placeholders for business objects, process links, and impact analysis

## Total Capabilities

214 BIAN capabilities documented across all divisions.

## Conversion Tool

The repository includes `md_to_json_converter.py` which automatically converts Markdown files to JSON format following the BIAN capability structure.

## Usage

To regenerate JSON files from Markdown sources:

```bash
python3 md_to_json_converter.py
```

## API References

All capabilities include links to their respective BIAN API documentation on SwaggerHub.
