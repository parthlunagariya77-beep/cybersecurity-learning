
print("=== Cybersecurity Basic Checker ===")

score = 0

updates = input("Is your software updated? (yes/no): ")
if updates.lower() == "yes":
    score += 1

antivirus = input("Is security protection enabled? (yes/no): ")
if antivirus.lower() == "yes":
    score += 1

mfa = input("Is two-factor authentication enabled? (yes/no): ")
if mfa.lower() == "yes":
    score += 1

print("\nYour Security Checklist Score:", score, "/3")

if score == 3:
    print("Great! All checklist items are enabled.")
else:
    print("Review the checklist items marked no.")

print("Note: This is a basic checklist, not a full security audit.")
