import re

with open(r'd:\Manhaj Al Ambiya\website\template\alquran\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
# Exact lines for footer in template are 1233 (1232 idx) to 1336 (1336 idx)
footer_code = ''.join(lines[1232:1336])

with open(r'd:\Manhaj Al Ambiya\website\main\index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

old_footer_regex = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
new_content = old_footer_regex.sub(footer_code, index_content)

with open(r'd:\Manhaj Al Ambiya\website\main\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print('Replaced Footer section')
