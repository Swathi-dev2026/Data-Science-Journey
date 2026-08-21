
import re

text = "My phone number is 9872341243."

result = re.search(r"\d+", text)

print(result.group())