from langchain_community.llms import Ollama
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os

# 1. Load all PDFs from folder
docs = []
for file in os.listdir("pdfs"):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(f"pdfs/{file}")
        docs.extend(loader.load())

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# 3. Create embeddings
embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# 4. Store in vector DB
db = Chroma.from_documents(chunks, embedding)

# 5. Retriever
retriever = db.as_retriever()

# 6. LLaMA via Ollama
llm = Ollama(model="llama3")

# 7. RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# 8. Chat loop
print("Chat based on your documents & not generic answers! Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    answer = qa.run(query)
    print(f"AI: {answer}\n")