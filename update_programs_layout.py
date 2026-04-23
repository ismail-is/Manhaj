import re
import os

files = [
    r"d:\Manhaj Al Ambiya\website\main\education.html",
    r"d:\Manhaj Al Ambiya\website\main\dawa.html",
    r"d:\Manhaj Al Ambiya\website\main\publications.html",
    r"d:\Manhaj Al Ambiya\website\main\social-service.html"
]

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Pattern for Program Section rows
    # We want to catch the row and columns and replace them with our flex layout
    
    # 1. First, find all blocks between <div class="container"> and the next </div> that matches our structure
    # Actually, a safer approach is to specifically target the img tags and their parents.
    
    # The current standard block we are looking for:
    # <div class="container">
    #   <div class="row align-items-center g-5 [flex-row-reverse]">
    #     <div class="col-lg-6">
    #       <div style="overflow:hidden;border-radius:12px;box-shadow:0 20px 60px rgba(0,0,0,0.12);">
    #         <img src="..." alt="..." style="width:100%;height:420px;object-fit:cover;display:block;transition:transform 0.5s;" ...>
    #       </div>
    #     </div>
    #     <div class="col-lg-6">
    
    # Regex to match the container content
    pattern = re.compile(
        r'<div class="container">\s*<div class="row align-items-center g-5\s*(flex-row-reverse)?">\s*<div class="col-lg-6">\s*<div style="overflow:hidden;border-radius:12px;box-shadow:0 20px 60px rgba\(0,0,0,0\.12\);">\s*<img src="([^"]+)" alt="([^"]+)" style="width:100%;height:420px;object-fit:cover;display:block;transition:transform 0.5s;"([^>]+)>\s*</div>\s*</div>\s*<div class="col-lg-6">',
        re.DOTALL
    )

    def replacement(match):
        is_reverse = "flex-row-reverse" in (match.group(1) or "")
        img_src = match.group(2)
        img_alt = match.group(3)
        img_extra = match.group(4)
        
        row_style = 'display: flex; align-items: center; gap: 60px; justify-content: center; flex-wrap: wrap;'
        if is_reverse:
            row_style += ' flex-direction: row-reverse;'
            
        new_block = f'''<div class="container" style="max-width: 1400px;">
        <div style="{row_style}">
          <!-- Image Column -->
          <div class="fade-up" style="flex: 0 0 600px; max-width: 600px;">
            <div style="width: 600px; height: 550px; overflow:hidden; border-radius: 24px; box-shadow: 0 25px 50px rgba(156, 49, 144, 0.12);">
              <img src="{img_src}" alt="{img_alt}" style="width: 100%; height: 100%; display:block; object-fit: cover; transition:transform 0.5s;"{img_extra}>
            </div>
          </div>
          <!-- Content Column -->
          <div class="fade-up" style="flex: 1; min-width: 320px; max-width: 650px;">'''
        return new_block

    new_content = pattern.sub(replacement, content)
    
    # Also need to close the divs correctly. 
    # The old structure had:
    #   </div> (col-lg-6)
    #   </div> (row)
    # </div> (container)
    
    # In my new structure I have:
    #   </div> (fade-up content column)
    #   </div> (flex row)
    # </div> (container)
    # So the closing tags should remain the same (two </div> after the content).
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")

for f in files:
    if os.path.exists(f):
        update_file(f)
    else:
        print(f"File not found: {f}")
