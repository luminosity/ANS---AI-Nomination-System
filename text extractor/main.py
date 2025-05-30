import os
import pymupdf
import pandas as pd

df = pd.DataFrame(
    {
        "text": [], 
    }
)

docs_path = r"text extractor\documents"
file_names = [os.path.join(docs_path, f) for f in os.listdir(docs_path) if os.path.isfile(os.path.join(docs_path, f))]

for file_name in file_names:
    doc = pymupdf.open(file_name)
    text = ""
    for page in doc: # iterate the document pages
        text = text + page.get_text() + "\f"
    df.loc[len(df)] = [text]

df.to_csv(r"text extractor\output.csv")