🧠 AI Resume Screening System

An intelligent resume screening system developed by Md Javeed Khan, designed to automate candidate evaluation using advanced Large Language Models and structured pipeline processing.

🚀 Features
Resume & Job Description Input
Automated Skill Extraction
Intelligent Matching Analysis
Candidate Scoring System (0–100)
Explainable AI-based Feedback
End-to-End Pipeline Processing
PDF Resume Parsing Support
Debugging & Monitoring with Tracing
🛠 Tech Stack
Python
LangChain (LLM pipeline orchestration)
Groq API (LLaMA 3.3–70B)
LangSmith (Tracing & Debugging)
PyPDF2 (PDF Processing)
📂 Project Structure
ai-resume-screening/
│
├── prompts/
│   ├── extraction_prompt.py
│   ├── matching_prompt.py
│   ├── scoring_prompt.py
│   ├── explanation_prompt.py
│
├── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   ├── explanation_chain.py
│
├── data/
│   ├── resumes/
│   ├── job_description.txt
│
├── main.py
├── sample.pdf
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1. Clone Repository
git clone <your-repo-link>
cd ai-resume-screening
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai-resume-screening
🔑 API Keys
Groq API → https://console.groq.com/
LangSmith → https://smith.langchain.com/

(Both offer free developer access)

▶️ Run the Project
python main.py
📊 Pipeline Workflow
Resume → Skill Extraction → Matching → Scoring → Explanation → Tracing
🔍 Monitoring with LangSmith
Tracks each stage of the pipeline
Displays LLM inputs & outputs
Helps debug incorrect predictions
Enables performance optimization
📸 Output
Structured Terminal Output
Candidate Score (0–100)
Detailed Explanation Report
Logs in LangSmith Dashboard
🎯 Key Highlights

✔ Modular Pipeline Architecture
✔ Explainable AI Decisions
✔ Real-time LLM Processing
✔ Clean Code Structure
✔ Debuggable with Tracing

💡 Future Improvements
Streamlit Web Interface
Resume Ranking System
JSON Structured Output
Advanced Scoring Algorithm (ML-based)
Database Integration
👨‍💻 Author

Md Javeed Khan
📞 +91 8143747313
📧 mdjaveedkhanofficial@gmail.com

🌐 Portfolio: mdjaveedkhan.me
