# 1. Load all PDFs from folder
docs = []
for file in os.listdir("pdfs"):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(f"pdfs/{file}")
        docs.extend(loader.load())