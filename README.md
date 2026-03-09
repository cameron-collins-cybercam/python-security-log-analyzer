# Python Security Log Analyzer

This project demonstrates a simple cybersecurity tool written in Python that analyzes authentication logs to detect suspicious activity.

The tool scans log files and identifies patterns such as repeated login failures that may indicate brute force attacks.

---

## Features

- Detects failed login attempts
- Identifies suspicious IP addresses
- Flags potential brute force attacks
- Generates simple security alerts

---

## Technologies Used

Python  
Log Analysis  
Security Event Detection

---

## Example Detection

The script analyzes log entries such as:

LOGIN_FAILED user=admin ip=45.33.21.9

If an IP address exceeds a threshold of failed attempts, an alert is triggered.

---

## Example Output

ALERT: Possible brute force attack detected from IP 45.33.21.9
