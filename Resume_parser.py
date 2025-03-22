import re
import spacy
import pdfminer.high_level


nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    return pdfminer.high_level.extract_text(pdf_path)

def extract_name(text):
    """Extract name using Named Entity Recognition (NER)."""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_email(text):
    """Extract email using regex."""
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None

def extract_phone(text):
    """Extract phone number using regex."""
    match = re.search(r"\+?\d[\d -]{8,}\d", text)
    return match.group() if match else None

def extract_skills(text):
    """Extract skills from resume text (extend this list as needed)."""
    skills = ["Python", "Machine Learning", "Data Science", "Java", "SQL", "TensorFlow", "AI"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return found_skills

def extract_resume_data(pdf_path):
    """Extract key details from a resume."""
    text = extract_text_from_pdf(pdf_path)
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
    }


if __name__ == "__main__":
    resume_path = "resume.pdf"  
    extracted_data = extract_resume_data(resume_path)
    print(extracted_data)
