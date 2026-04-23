import os
import re

files_to_sync = [
    'about.html', 'education.html', 'dawa.html',
    'publications.html', 'social-service.html', 'blog.html', 'contact.html'
]

# Get the snippets from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Extract Header
header_start_marker = "<!-- Main Header / Style Five -->"
header_end_marker = "<!-- End Header Five -->"
h_start = index_content.find(header_start_marker)
h_end = index_content.find(header_end_marker) + len(header_end_marker)

if h_start == -1 or h_end == -1:
    print("Could not find header markers in index.html")
    header_html = None
else:
    header_html = index_content[h_start:h_end]

# 2. Extract Footer
footer_start_marker = '<!-- Footer Style -->'
footer_end_marker = '<!-- End Footer Style -->'
f_start = index_content.find(footer_start_marker)
f_end = index_content.find(footer_end_marker) + len(footer_end_marker)

if f_start == -1 or f_end == -1:
    print("Could not find footer markers in index.html")
    footer_html = None
else:
    footer_html = index_content[f_start:f_end]

# Regex to match the old footer or new footer
old_footer_regex = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
new_footer_regex = re.compile(r'<!-- Footer Style -->.*?<!-- End Footer Style -->', re.DOTALL)

for fname in files_to_sync:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Sync Header
    if header_html:
        th_start = content.find(header_start_marker)
        th_end = content.find(header_end_marker) + len(header_end_marker)
        if th_start != -1 and th_end != -1:
            content = content[:th_start] + header_html + content[th_end:]

    # Sync Footer
    if footer_html:
        # Check if old footer exists
        if old_footer_regex.search(content):
            content = old_footer_regex.sub(footer_html, content)
        elif new_footer_regex.search(content):
            content = new_footer_regex.sub(footer_html, content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Synced layout for {fname}")
