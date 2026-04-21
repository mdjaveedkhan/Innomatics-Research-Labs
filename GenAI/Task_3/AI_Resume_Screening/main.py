import json
from dotenv import load_dotenv
from chains.pipeline import run_pipeline
from PyPDF2 import PdfReader

load_dotenv()


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run(label, resume, jd):
    print("\n" + "=" * 60)
    print(label)
    print("=" * 60)

    result = run_pipeline(resume, jd)

    print("\n👤 Candidate")
    print("Name:", result["extracted"].get("name", "N/A"))
    print("Email:", result["extracted"].get("email", "N/A"))

    print("\n📌 Extracted")
    print(json.dumps(result["extracted"], indent=2))

    print("\n📊 Match")
    print(json.dumps(result["matched"], indent=2))

    print("\n🎯 Score")
    print(result["score"])

    print("\n💡 Explanation")
    print(result["explanation"])


def main():
    print("\n🚀 AI Resume Screening System\n")

    jd = read_file("data/job_description.txt")

    choice = input("Enter resume PDF path (or Enter for demo): ").strip()

    if choice:
        resume = read_pdf(choice)
        run("📄 Uploaded Resume", resume, jd)
    else:
        strong = read_file("data/resumes/strong.txt")
        avg = read_file("data/resumes/average.txt")
        weak = read_file("data/resumes/weak.txt")

        run("💪 Strong", strong, jd)
        run("⚖️ Average", avg, jd)
        run("❌ Weak", weak, jd)


if __name__ == "__main__":
    main()