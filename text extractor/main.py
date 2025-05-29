import pymupdf

doc = pymupdf.open(r"text extractor\documents\test.docx")
out = open(r"text extractor\output.txt", "wb")
print(doc.page_count)
for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()