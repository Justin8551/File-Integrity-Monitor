# File Integrity Monitor (FIM)

![Security](https://img.shields.io/badge/security-monitored-red.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

This project is a Real-Time File Integrity Monitor implemented in Python, designed to detect unauthorized changes to files in a specified directory. It creates a cryptographic baseline of a directory and alert the user whenever a file is added, modified, or deleted.

Features:
- SHA-256 Hashing: Uses industrial-standard cryptographic hashing for file integrity verification.
- Real-Time Monitoring: Continuously monitors the directory every 3 seconds for changes.
- Alert System: Automatically creates log entries for detected changes, including timestamps and file details.
- Dynamic Baseline: Updates the internal state automatically after detecting changes, ensuring accurate monitoring over time.

Tehnical Details:
- The script calculates a unique hash of each file, since SHA-256 is collision-resistant, it provides a reliable way to detect changes. 
- Initial state is saved in a JSON file, and it is used as a reference for future comparisons.

Usage:
1. Place the `fim.py` script in the directory you want to monitor.
2. Run the script using Python 3.x: `python fim.py`

Author: Dumitru Gabriel Justin# File-Integrity-Monitor
