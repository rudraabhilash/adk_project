#RAG, evals, Tool Calling: The Triple Threat for Production LLMs

# 1️⃣ RAG — Retrieval-Augmented Generation
# What is RAG?

# RAG = LLM + External Knowledge Retrieval

# Instead of forcing an LLM to remember everything, we:

# Retrieve relevant information from external sources

# Inject it into the prompt

# Let the LLM generate the answer grounded in facts

# 🧠 LLMs reason. Databases remember.

# Why RAG exists (hard evidence)

# LLMs:

# Are static after training

# Hallucinate when unsure

# Cannot access private or real-time data

# 📌 RAG fixes this by grounding responses in retrieved facts.

# RAG Flow (step-by-step)
# User Question
#    ↓
# Embedding Model
#    ↓
# Vector Database (similarity search)
#    ↓
# Relevant Chunks
#    ↓
# LLM Prompt
#    ↓
# Grounded Answer

# Real-world RAG examples

# Company policy chatbot

# Financial / legal document Q&A

# Internal wiki search

# Medical literature assistants

# Famous RAG stack components

# Embeddings: OpenAI / sentence-transformers

# Vector DBs: FAISS, Pinecone, Weaviate

# LLMs: GPT-4, Claude, LLaMA

# 📌 Key advantage:
# Accuracy ↑, hallucination ↓, private data safe

# 2️⃣ Evals — Evaluation of LLMs
# What are Evals?

# Evals = systematic testing of LLM behavior

# Traditional software has unit tests.
# LLMs need behavioral tests.

# Why Evals are mandatory

# LLMs are:

# Probabilistic

# Non-deterministic

# Sensitive to prompts, data drift, updates

# 📌 Without evals → silent regressions in production.

# Types of LLM Evals
# 🔹 Functional Evals

# Is the answer correct?

# Did it follow instructions?

# 🔹 Safety Evals

# Toxicity

# Bias

# Data leakage

# 🔹 RAG-Specific Evals

# Was the retrieved context used?

# Was hallucination avoided?

# 🔹 Tool-Use Evals

# Did the model call the correct tool?

# Were arguments correct?

# Example Eval (conceptual)
# Input: "Summarize this contract"
# Expected:
# - Includes termination clause
# - Excludes personal opinions
# - Uses bullet points


# Score across many samples → deployment decision.

# Famous eval frameworks

# OpenAI Evals

# LangSmith

# TruLens

# DeepEval

# 📌 Enterprise truth:
# No evals = no production AI.

# 3️⃣ Tool Calling — LLMs Acting, Not Just Talking
# What is Tool Calling?

# Tool calling lets an LLM decide to call external systems instead of responding in text.

# LLM = brain
# Tools = hands

# Why tool calling matters

# LLMs cannot:

# Query live databases

# Send emails

# Execute code

# Fetch real-time data

# 📌 Tool calling turns LLMs into agents.

# Tool Calling Flow
# User Request
#    ↓
# LLM Reasoning
#    ↓
# Tool Decision
#    ↓
# API / DB / Code Execution
#    ↓
# Result back to LLM
#    ↓
# Final Response

# *****************************************************************************************
# *****************************************************************************************

# 🖍️ Part 1: LLMs + Vector DBs (the big picture)
# Crayon version

# LLM = the kid who explains things beautifully

# Vector DB = the magical box that remembers similar crayons fast

# Embedding model = machine that turns crayons into numbers

# LLMs do not remember your data.
# Vector DBs do not talk well.

# 👉 Together, they form RAG (Retrieval-Augmented Generation).

# What RAG (Retrieval-Augmented Generation) actually means

# RAG = LLM + Retrieval layer + Grounding logic

# An LLM + vector database is necessary, but not sufficient, to qualify as a proper RAG system.

# “RAG is not just an LLM plus a vector database; it’s an architecture where 
# retrieval, grounding(Only speak using what I gave you), and generation are explicitly 
# separated, with the vector database being only the retrieval component.”

# Minimal RAG (what people usually mean)
# User query
#    ↓
# Embedding model
#    ↓
# Vector DB (semantic search)
#    ↓
# Top-K chunks
#    ↓
# LLM prompt
#    ↓
# Answer

# ****************************************************************************************
# Full RAG architecture (production-grade)
# A production-grade RAG system needs four distinct layers:

# 1. Knowledge ingestion & indexing

# Document loading (PDF, HTML, DB, APIs)

# Chunking strategy (size, overlap)

# Metadata extraction

# Embedding generation

# Evidence:
# Bad chunking alone can reduce retrieval accuracy by 30–50% (OpenAI + Pinecone benchmarks).

# 2. Retrieval layer (Vector DB + logic)

# Vector similarity search (cosine / dot / L2)

# Filters (time, source, user, permissions)

# Hybrid search (BM25 + vectors)

# Re-ranking (cross-encoders)

# Vector DBs (like FAISS, Pinecone) only do nearest-neighbor search, not relevance reasoning.

# 3. Grounding & prompt orchestration
# Prompt orchestration = giving clear instructions + structure as below:
# what role it’s playing
# what rules it must follow
# how to process the context
# how to format the answer

# *****************************************************************
# LLMs fail in two different ways:
# ❌ They invent facts
# ❌ They use facts badly (wrong order, wrong emphasis, wrong logic)

# Grounding fixes (1)
# Prompt orchestration fixes (2)
# Grounding rules sound like:

# “Use ONLY the provided context”
# “Do not add outside knowledge”
# “If not mentioned, say ‘not provided’”
# “Cite the sentence you used”
# These rules define the boundary of reality.
# Think of grounding as drawing a fence.

# Orchestration rules sound like:

# “First list facts, then summarize”
# “Answer in bullet points”
# “Group by category”
# “Compare A vs B”
# “Think step-by-step”
# “Explain in simple language”
# These don’t define truth — they define procedure.
# Think of orchestration as giving a workflow.

# *******************************************************
# Context selection (how many chunks?)

# De-duplication

# Ordering (chronological vs semantic)

# Prompt templates

# Citation enforcement

# Without this, LLMs hallucinate even with correct retrieval.

# Proof:
# Meta’s RAG paper shows hallucination persists unless grounding instructions are explicit.

# 4. Generation layer (LLM + output control)
# Controlled decoding

# Tool use (optional)

# Answer formatting

# Guardrails

# The LLM is the final reasoning engine, not the source of truth.


# A RAG system is a pattern where an LLM generates responses 
# grounded in externally retrieved knowledge at inference time.

# *************************************************************************************
# Scenario (same for both)

# You retrieved the following chunk from your vector database:

# Document excerpt:
# Drug X clinical trial results:
# - Common side effects: nausea, headache
# - No severe adverse events were reported


# Now let’s see what happens.

# ❌ BEFORE: RAG without grounding (bad prompt)
# Prompt sent to LLM
# Answer the following question.

# Context:
# Drug X clinical trial results:
# - Common side effects: nausea, headache
# - No severe adverse events were reported

# Question:
# What are the side effects of Drug X?

# Typical LLM output (looks good, but wrong)

# Drug X commonly causes nausea, headache, fatigue, and dizziness.
# No severe adverse effects have been reported.

# ⚠️ Problem:

# Fatigue and dizziness were never in the document

# The LLM added them because:

# They are common side effects in general

# The prompt didn’t forbid guessing

# This is hallucination.

# ✅ AFTER: RAG with grounding + orchestration (good prompt)
# Prompt sent to LLM
# You are answering strictly based on the provided context.

# Rules:
# 1. Use ONLY the information explicitly stated in the context.
# 2. Do NOT add any medical knowledge outside the context.
# 3. If a side effect is not mentioned, do not include it.
# 4. Quote the exact line from the context for each side effect.

# Context:
# Drug X clinical trial results:
# - Common side effects: nausea, headache
# - No severe adverse events were reported

# Question:
# List all side effects of Drug X mentioned in the context.

# LLM output (correct and grounded)

# Side effects mentioned:

# Nausea — “Common side effects: nausea, headache”

# Headache — “Common side effects: nausea, headache”

# Severe adverse events:
# None reported — “No severe adverse events were reported”

# ✅ No guessing
# ✅ No extra knowledge
# ✅ Every claim tied to text
# ***********************************************************************************
# One more example (Q&A style)
# ❌ Before
# Context:
# Company revenue in 2023 was $10M.

# Question:
# What was the revenue growth compared to 2022?


# LLM answer:

# The company showed strong revenue growth compared to 2022.

# ❌ Hallucinated comparison.

# ✅ After
# Rules:
# - Answer only using the context
# - If comparison data is missing, say "Not provided"

# Context:
# Company revenue in 2023 was $10M.

# Question:
# What was the revenue growth compared to 2022?


# LLM answer:

# Revenue growth compared to 2022 is not provided in the context.

# ✔ Correct
# ✔ Honest
# ✔ Grounded
# ***********************************************************************************
# 🖍️ Part 1: LLMs + Vector DBs (the big picture)
# Crayon version

# LLM = the kid who explains things beautifully

# Vector DB = the magical box that remembers similar crayons fast

# Embedding model = machine that turns crayons into numbers

# LLMs do not remember your data.
# Vector DBs do not talk well.

# 👉 Together, they form RAG (Retrieval-Augmented Generation).



# 🧠 Part 2: Step-by-step Python (minimal, real, correct)

# We’ll simulate:

# Convert text → vectors
# Store vectors in FAISS
# Search similar vectors
# Feed results to an LLM

from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Blue crayons are calming and cool",
    "Red crayons are energetic and bold",
    "Sky blue color feels peaceful",
    "Bananas are yellow fruits",
]

# Convert text → vectors
doc_vectors = model.encode(documents)

print(doc_vectors.shape)
# (4, 384) → 4 crayons, each with 384-number color meaning

# 📦 Step 2: Store vectors in FAISS (vector DB)
import faiss
dimension = doc_vectors.shape[1]
# Create FAISS index (flat = exact search)
index = faiss.IndexFlatL2(dimension)
# Add vectors
index.add(np.array(doc_vectors))
print("Total crayons stored:", index.ntotal)
# 🧠 What FAISS is doing
# Organizes vectors in memory
# Uses math to avoid checking every item


# 🔍 Step 3: Similarity search (magic moment ✨)

query = "I like calm blue colors"
query_vector = model.encode([query])
# Find top 2 closest vectors
distances, indices = index.search(np.array(query_vector), k=2)
for i in indices[0]:
    print(documents[i])


# Output (conceptually)
# Blue crayons are calming and cool
# Sky blue color feels peaceful


# 🖍️ Crayon magic
# You didn’t say “blue crayons” exactly—
# yet the system understood the meaning.

