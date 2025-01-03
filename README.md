# Resume Parser with GROQ LLM

A Streamlit-based application that uses GROQ's LLM to parse resumes in PDF format and extract structured information.

## Architecture

```
resume-parser/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and environment variables
├── requirements.txt      # Project dependencies
├── utils/               # Utility modules
│   ├── resume_parser.py    # Core resume parsing logic using GROQ
│   ├── contact_extractor.py # Contact information extraction
│   ├── pdf_converter.py    # PDF conversion utilities
│   └── text_extractor.py   # Text extraction from documents
```

### Component Responsibilities

- **app.py**: Main Streamlit interface handling file uploads and displaying results
- **config.py**: Manages environment variables and configuration settings
- **utils/**:
  - **resume_parser.py**: Coordinates the parsing process using GROQ's LLM
  - **contact_extractor.py**: Extracts email and phone using regex patterns
  - **pdf_converter.py**: Handles PDF to DOCX conversion
  - **text_extractor.py**: Extracts text from PDF and DOCX files

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your GROQ API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Upload one or more PDF resumes through the web interface

3. Click "Parse Resumes" to process the files

4. View the extracted information for each resume:
   - Personal Information
   - Skills
   - Experience
   - Education

5. Download all results as a CSV file using the provided button

## Features

- Multi-file upload support
- Regex-based contact information extraction
- LLM-powered information extraction
- Progress tracking for multiple files
- CSV export functionality
- Error handling and status reporting

## Dependencies

- groq: GROQ LLM API client
- streamlit: Web interface
- pandas: Data handling and CSV export
- python-docx: DOCX file processing
- pdf2docx: PDF to DOCX conversion
- PyPDF2: PDF text extraction
- python-dotenv: Environment variable management

## Error Handling

The application includes comprehensive error handling for:
- File upload issues
- PDF text extraction failures
- API communication errors
- JSON parsing errors

## Output Format

The parsed results are returned in JSON format:
```json
{
    "name": "Full Name",
    "email": "email@example.com",
    "phone": "123-456-7890",
    "skills": ["skill1", "skill2"],
    "experience": ["experience1", "experience2"],
    "education": ["education1", "education2"]
}
```