import re

# Input and output file paths
input_file = "sample.txt"
output_file = "emails.txt"

# Read text
with open(input_file, "r") as f:
    text = f.read()

# Find all emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save to another file
with open(output_file, "w") as f:
    for email in emails:
        f.write(email + "\n")

print("✅ Extracted emails saved into emails.txt")
