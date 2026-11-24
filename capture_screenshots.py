"""
Automated Screenshot Generator for Agent Gatekeeper Prototype
Candidate: Vaishnavi Joshi (PGD202572385)
Generates high-resolution screenshots of the running web application
and PDF report pages.
"""

import os
from html2image import Html2Image
import pypdfium2 as pdfium

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_HTML = os.path.join(PROJ_DIR, "index.html")
REPORT_PDF = os.path.join(PROJ_DIR, "Agent_Gatekeeper_Report_PGD202572385.pdf")

# 1. Capture Web Dashboard Screenshots
hti = Html2Image(
    browser_executable=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    output_path=PROJ_DIR
)

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html_content = f.read()

# Capture Full Running Web Dashboard (Wide)
print("Capturing running website dashboard screenshot...")
hti.screenshot(
    html_str=html_content,
    save_as="screenshot_website_dashboard.png",
    size=(1366, 1100)
)

# Capture Running Website in Full HD
print("Capturing 1080p full overview...")
hti.screenshot(
    html_str=html_content,
    save_as="screenshot_website_full.png",
    size=(1920, 1200)
)

# 2. Render PDF Report Pages to High-Res PNG (300 DPI)
print("Rendering official 2-page report to high-resolution PNG...")
pdf = pdfium.PdfDocument(REPORT_PDF)
for i, page in enumerate(pdf):
    # Render at 3x scale (~216 DPI) for ultra-crisp resolution
    image = page.render(scale=3).to_pil()
    out_img = os.path.join(PROJ_DIR, f"report_page_{i+1}.png")
    image.save(out_img)
    print(f"Saved: {out_img}")

print("\nAll screenshots generated successfully!")
