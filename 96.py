# 96	Extract all URLs from a paragraph using Regex.
import re

paragraph = """
Visit https://www.google.com for searching.
You can also check https://github.com and http://example.com.
"""

pattern = r'https?://[^\s]+'

urls = re.findall(pattern, paragraph)

print("URLs found:")

for url in urls:
    print(url)