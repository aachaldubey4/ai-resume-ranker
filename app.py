import streamlit as st
from resume_parser import extract_text_from_pdf, calculate_score

st.title("📄 AI Resume Ranker (PDF Compatible)")

jd_text = st.text_area("Paste Job Description Here")

uploaded_files = st.file_uploader("Upload Resumes (PDF format)", accept_multiple_files=True, type=["pdf"])

if st.button("Rank Resumes") and jd_text:
    st.subheader("📊 Ranking Results")
    results = []

    for file in uploaded_files:
        try:
            resume_text = extract_text_from_pdf(file)
            score = calculate_score(resume_text, jd_text)
            results.append((file.name, round(score * 100, 2)))
        except Exception as e:
            st.error(f"❌ Error reading {file.name}: {e}")

    ranked = sorted(results, key=lambda x: x[1], reverse=True)
    for name, score in ranked:
        st.write(f"**{name}** ➜ Score: {score} %")
