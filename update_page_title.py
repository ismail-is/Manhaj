"""
Replace the old page-hero sections in all inner pages with
the Page Title section from the template.
"""
import re

# Page config: filename -> (page_title_h2, breadcrumb_text)
pages = {
    "education.html":     ("Education",      "Education"),
    "dawa.html":          ("Da'wah",         "Da'wah"),
    "publications.html":  ("Publications",   "Publications"),
    "social-service.html":("Social Service", "Social Service"),
    "blog.html":          ("Blog",           "Blog"),
    "contact.html":       ("Contact",        "Contact Us"),
}

# The new Page Title HTML template
def make_page_title(h2_text, crumb_text):
    return f'''<!-- Page Title -->
    <section class="page-title" style="background-image:url(assets/main-img/background/page-title.jpg)">
        <div class="auto-container">
\t\t\t<h2>{h2_text}</h2>
\t\t\t<ul class="bread-crumb clearfix">
\t\t\t\t<li><a href="index.html">Home</a></li>
\t\t\t\t<li>{crumb_text}</li>
\t\t\t</ul>
        </div>
    </section>
    <!-- End Page Title -->'''

# Regex to match the page-hero section (no comment prefix in these files)
hero_pattern = re.compile(
    r'<section class="page-hero">\s*.*?</section>',
    re.DOTALL
)

for filename, (h2, crumb) in pages.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_title = make_page_title(h2, crumb)
        
        if 'class="page-hero"' in content:
            new_content = hero_pattern.sub(new_title, content, count=1)
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"Regex did not match in {filename}")
        else:
            print(f"No page-hero found in {filename}, skipping")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("\nDone!")
