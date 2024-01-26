import fitz 

# Create a new PDF and add pages
doc = fitz.open()
for i in range(1, 11):
    page = doc.new_page()
    page.insert_text((72, 72), f"Content of Page {i}", fontsize=12)

# Define TOC structure
toc = [
    [1, "Chapter 1", 1],
    [2, "Section 1.1", 2],
    [2, "Section 1.2", 3],
    [1, "Chapter 2", 4],
    [2, "Section 2.1", 5],
    # Add more chapters and sections as needed
]

# Add TOC to the PDF
doc.set_toc(toc)

# Save the PDF
doc.save("created_with_toc.pdf")
doc.close()
