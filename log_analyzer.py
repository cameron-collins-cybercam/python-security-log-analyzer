from collections import defaultdict

log_file = "sample-log.txt"

failed_attempts = defaultdict(int)

print("Security Log Analysis Started\n")

with open(log_file, "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:

            parts = line.split("ip=")
            ip = parts[1].strip()

            failed_attempts[ip] += 1

print("Failed Login Summary:\n")

for ip, count in failed_attempts.items():
    print(f"IP: {ip} | Failed Attempts: {count}")

    if count >= 3:
        print(f"ALERT: Possible brute force attack from {ip}\n")
