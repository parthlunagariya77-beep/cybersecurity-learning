sample_logs = [
    "LOGIN SUCCESS user=student",
    "LOGIN FAILED user=student",
    "LOGIN FAILED user=admin",
    "LOGIN SUCCESS user=guest",
    "LOGIN FAILED user=student",
]

failed_count = 0

for entry in sample_logs:
    if "LOGIN FAILED" in entry:
        failed_count += 1

print("Total log entries:", len(sample_logs))
print("Failed login entries:", failed_count)
