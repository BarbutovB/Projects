# DNS Lookup Tool

## Description
A simple Python-based utility designed to fetch IP addresses (A Records) for any given domain name. This tool is intended for basic network reconnaissance and security monitoring tasks.

## Features
- Converts domain names (e.g., google.com) into IPv4 addresses.
- Includes error handling for invalid domains or connection issues.
- Lightweight and uses zero external dependencies.

## How It Works
The script utilizes Python's built-in `socket` library to perform a DNS lookup through the operating system's resolver. This is a fundamental step in the "Reconnaissance" phase of a security audit.


## Usage
1. Run the script:
   ```bash
   python dns_lookup.py
