import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# match <footer class="modern-footer-ref" ...>...</footer>
footer_match = re.search(r'(<footer class="modern-footer-ref".*?</footer\s*>)', text, re.DOTALL)
if not footer_match:
    print('Footer not found in index.html')
    exit(1)

new_footer = footer_match.group(1)
print(f'Found footer, length: {len(new_footer)}')

count = 0
for fname in glob.glob('*.html'):
    if fname == 'index.html':
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        file_text = f.read()
    
    # We will search for ANY existing footer, since previous ones have class modern-footer-ref OR main-footer
    if '<footer class=' in file_text:
        updated_text = re.sub(r'<footer class="(main-footer|modern-footer-ref)".*?</footer\s*>', new_footer, file_text, flags=re.DOTALL)
        if updated_text != file_text:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(updated_text)
            count += 1
            print(f'Updated {fname}')

print(f'Updated {count} files.')
