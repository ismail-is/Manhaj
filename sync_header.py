import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# match <header class="main-header header-style-five">...</header>
header_match = re.search(r'(<header class="main-header header-style-five">.*?</header\s*>)', text, re.DOTALL)
if not header_match:
    print('Header not found in index.html')
    exit(1)

new_header = header_match.group(1)
print(f'Found header, length: {len(new_header)}')

count = 0
for fname in glob.glob('*.html'):
    if fname == 'index.html':
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        file_text = f.read()
    
    if '<header class="main-header header-style-five"' in file_text:
        updated_text = re.sub(r'<header class="main-header header-style-five">.*?</header\s*>', new_header, file_text, flags=re.DOTALL)
        if updated_text != file_text:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(updated_text)
            print(f'Updated {fname}')
            count += 1
        else:
            print(f'No change for {fname}')

print(f'Updated {count} files.')
