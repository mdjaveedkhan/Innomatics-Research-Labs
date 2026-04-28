# 🚀 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant designed to deliver accurate, context-aware responses using a PDF knowledge base.

The system combines:

* Semantic search using embeddings
* Large Language Model (LLM) reasoning
* Graph-based workflow orchestration using LangGraph
* Human-in-the-Loop (HITL) escalation for reliability

This ensures the system avoids hallucinations and provides trustworthy answers in real-world customer support scenarios.

---

## 🎯 Objectives

* Process and understand a PDF knowledge base
* Retrieve relevant context using vector embeddings
* Generate accurate responses using an LLM
* Apply decision-making via workflow orchestration
* Escalate complex queries to human agents

---

## 🏗️ System Architecture (High-Level)

**Core Flow:**

User Query → Retrieval → Context Injection → LLM → Decision → Output / HITL

### Key Components:

* **Document Ingestion Pipeline**
* **Embedding System**
* **Vector Database (ChromaDB)**
* **Retriever**
* **LLM (Gemini / OpenAI)**
* **LangGraph Workflow Engine**
* **Routing Layer**
* **HITL Module**

---

## 📂 Project Structure

```text
.
├── data/                      # Input PDF knowledge base
├── docs/                      # Documentation (HLD, LLD, Technical Docs)
│   ├── HLD.md
│   ├── LLD.md
│   └── Technical_Documentation.md
├── src/
│   └── rag_support_bot/
│       ├── config.py          # Configuration settings
│       ├── ingestion.py       # PDF loading, chunking, embedding
│       ├── intent.py          # Intent detection logic
│       ├── llm.py             # LLM interaction (Gemini/OpenAI)
│       ├── hitl.py            # Human-in-the-Loop handling
│       ├── retrieval.py       # Vector search logic
│       ├── routing.py         # Decision-making & conditional routing
│       ├── state.py           # Graph state management
│       └── workflow.py        # LangGraph workflow definition
├── tests/
│   └── test_routing.py
├── ingest.py                  # Script for PDF ingestion
├── run.py                     # Main application entry point
├── requirements.txt
└── .env.example
```

---

## ⚙️ Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Update API keys and configuration values inside `.env`.

---

## 📥 Data Ingestion

Place your knowledge base PDF inside the `data/` folder.

Run ingestion:

```bash
python ingest.py --pdf data/customer_support_kb.pdf
```

This step:

* Loads the PDF
* Splits it into chunks
* Converts chunks into embeddings
* Stores them in ChromaDB

---

## ▶️ Running the Application

```bash
python run.py
```

You can now interact with the assistant via CLI.

---

## 🔄 Query Processing Flow

1. User inputs a query
2. Intent detection module analyzes the query
3. Retriever fetches relevant chunks from ChromaDB
4. LLM generates a context-aware response
5. Confidence evaluation is performed
6. Conditional routing:

   * ✅ `auto_reply` → Direct response returned
   * ⚠️ `escalate_human` → Routed to HITL module

---

## 🔀 Conditional Routing Logic

The system decides response path based on:

* Confidence score
* Context relevance
* Query complexity

### Routing Outcomes:

* **Auto Response** → High confidence + relevant context
* **Human Escalation** → Low confidence / missing context

---

## 👨‍💻 Human-in-the-Loop (HITL)

When escalation is triggered:

* Query is forwarded to a human agent
* Human response is collected
* Final answer is returned to the user
* Interaction is logged for future improvement

---

## 🧠 Key Concepts Implemented

| Concept        | Implementation                      |
| -------------- | ----------------------------------- |
| RAG            | Retrieval + LLM response generation |
| PDF Processing | `ingestion.py`                      |
| Embeddings     | Vector representation of text       |
| Vector DB      | ChromaDB                            |
| Retrieval      | `retrieval.py`                      |
| Workflow       | LangGraph (`workflow.py`)           |
| Routing        | `routing.py`                        |
| HITL           | `hitl.py`                           |

---

## 🧪 Testing

Run unit tests:

```bash
pytest -q
```

---

## 📄 Documentation Export

### Using Pandoc:

```bash
pandoc docs/HLD.md -o docs/HLD.pdf
pandoc docs/LLD.md -o docs/LLD.pdf
pandoc docs/Technical_Documentation.md -o docs/Technical_Documentation.pdf
```

### Alternative:

Use VS Code → Print to PDF

---

## ⚠️ Challenges & Trade-offs

* Chunk size vs retrieval accuracy
* Latency vs response quality
* Handling ambiguous queries
* Avoiding hallucinations

---

## 🚀 Future Enhancements

* Multi-document support
* Web-based UI
* Memory integration
* Feedback-based learning
* Deployment on cloud

---

## 👤 Author

**Md Javeed Khan**
📧 [mdjaveedkhanofficial@gmail.com](mailto:mdjaveedkhanofficial@gmail.com)
📱 +91 8143747313
🌐 Portfolio: mdjaveedkhan.me

---

## 📌 Final Note

This project demonstrates how combining retrieval systems, LLMs, and workflow orchestration can build reliable AI systems for real-world applications.

---
