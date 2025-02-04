import streamlit as st
import pandas as pd
from utils.resume_parser import parse_resume

def main():
    st.title("Resume Parser")
    
    # Add description
    st.markdown("""
    Upload PDF resumes to extract key information using GROQ's LLM.
    The parser will extract:
    - Personal Information
    - Skills
    - Experience
    - Education
    """)
    
    uploaded_files = st.file_uploader(
        "Upload your resume(s)",
        type="pdf",
        help="Please upload PDF file(s)",
        accept_multiple_files=True
    )

    submit = st.button("Parse Resumes")
    
    if submit and uploaded_files:
        results = []
        progress_bar = st.progress(0)
        
        for idx, uploaded_file in enumerate(uploaded_files):
            if uploaded_file is not None:
                with st.spinner(f'Processing resume {idx + 1} of {len(uploaded_files)}...'):
                    response = parse_resume(uploaded_file)
                    results.append(response)
                    
                    # Show individual results
                    st.subheader(f"Resume {idx + 1} Results:")
                    st.json(response)
                    
                progress_bar.progress((idx + 1) / len(uploaded_files))
        
        if results:
            # Convert to DataFrame and offer CSV download
            df = pd.DataFrame(results)
            csv_file = df.to_csv(index=False)
            st.download_button(
                label="Download All Results as CSV",
                data=csv_file,
                file_name="parsed_resumes.csv",
                mime="text/csv",
            )

if __name__ == "__main__":
    main()

