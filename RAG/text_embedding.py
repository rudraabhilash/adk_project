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
