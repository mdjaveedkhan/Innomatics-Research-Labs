import json
from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain


def safe_json_load(text):
    try:
        text = text.strip()

        if text.startswith("```"):
            text = text.split("```")[1]

        start = text.find("{")
        end = text.rfind("}") + 1

        if start != -1 and end != -1:
            text = text[start:end]

        return json.loads(text)

    except Exception:
        return {}


def run_pipeline(resume, job_description):

    # 1. Extract
    extracted_text = extraction_chain(resume)
    extracted = safe_json_load(extracted_text)

    # 2. Match (FIXED: use extracted dict, not raw text)
    matched_text = matching_chain(extracted, job_description)
    matched = safe_json_load(matched_text)

    # 3. Score
    score = scoring_chain(matched_text).strip()

    # 4. Explanation (FIXED order)
    explanation = explanation_chain(
        score,
        matched_text,
        extracted_text
    ).strip()

    return {
        "extracted": extracted,
        "matched": matched,
        "score": score,
        "explanation": explanation
    }