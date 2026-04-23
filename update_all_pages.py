import os
import re

files_to_update = [
    'about.html', 'education.html', 'dawa.html',
    'publications.html', 'social-service.html', 'blog.html', 'contact.html'
]

# Get the header code and footer code from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Remove preloader from index.html
if '<div class="preloader"></div>' in index_content:
    index_content = index_content.replace('<div class="preloader"></div>', '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Removed preloader from index.html.")

# Extract the header block from index.html
# It starts at <!-- Main Header / Style Five --> and ends before <!-- Slider Four -->
header_start_marker = "<!-- Main Header / Style Five -->"
header_end_marker = "<!-- End Header Five -->"
start_idx = index_content.find(header_start_marker)
end_idx = index_content.find(header_end_marker) + len(header_end_marker)
header_html = index_content[start_idx:end_idx]

# Extract template CSS (from <link href="assets/css... to family=Lexend...)
css_html = """  <link href="assets/css/bootstrap.css" rel="stylesheet">
  <link href="assets/css/style.css" rel="stylesheet">
  <link href="assets/css/responsive.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">"""

# Extract the footer scripts and popup (from <!-- Search Popup --> to the end of scripts)
footer_start_marker = "<!-- Search Popup -->"
footer_script_end_marker = '<script src="assets/js/script.js"></script>'
f_start_idx = index_content.find(footer_start_marker)
f_end_idx = index_content.find(footer_script_end_marker) + len(footer_script_end_marker)
footer_html = index_content[f_start_idx:f_end_idx]

for fname in files_to_update:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already updated (check for assets/css/style.css)
    if 'assets/css/style.css' in content:
        print(f"File {fname} is already updated.")
        # But we might need to remove preloader if present
        if '<div class="preloader"></div>' in content:
            content = content.replace('<div class="preloader"></div>', '')
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
        continue

    # 1. Update CSS in <head>
    content = content.replace('<link rel="stylesheet" href="styles.css">', css_html + '\n  <link rel="stylesheet" href="styles.css">')

    # 2. Add <div class="page-wrapper"> after <body>. Remove existing preloader just in case.
    content = content.replace('<body>', '<body>\n<div class="page-wrapper">')

    # 3. Replace the old navbar code.
    # The old navbar is enclosed loosely, but we know it starts with <nav class="navbar"
    # and the mobile menu ends with </div> right before <main> or <header class="page-hero">
    
    # Let's find the start of the navbar area:
    old_nav_start = content.find('<!-- ============================================================')
    if old_nav_start == -1:
        old_nav_start = content.find('<nav class="navbar" id="navbar">')
    
    old_nav_end = content.find('<header class="page-hero">')
    if old_nav_end == -1:
        old_nav_end = content.find('<main>')

    if old_nav_start != -1 and old_nav_end != -1:
        # replace everything between old_nav_start and old_nav_end with the new header
        content = content[:old_nav_start] + header_html + '\n\n  ' + content[old_nav_end:]
    
    # 4. Inject footer_html before closing </body> and close page-wrapper
    footer_inject_idx = content.find('</body>')
    # Remove the old script tag
    content = content.replace('<script src="script.js"></script>', '')
    
    insert_str = '\n</div><!-- End PageWrapper -->\n\n' + footer_html + '\n<script src="script.js"></script>\n'
    
    # Find </body> again because string indices might have changed
    footer_inject_idx = content.find('</body>')
    content = content[:footer_inject_idx] + insert_str + content[footer_inject_idx:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {fname}")

