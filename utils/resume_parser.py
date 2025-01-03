import groq
import json
import re  # Added missing import
from config import GROQ_API_KEY
from .text_extractor import extract_text_from_pdf
from .contact_extractor import extract_contact_info

def parse_resume(file):
    """Parse resume and extract structured information."""
    try:
        client = groq.Client(api_key=GROQ_API_KEY)
        
        # Extract text directly from PDF
        resume_text = extract_text_from_pdf(file)
        if not resume_text:
            return {"error": "Failed to extract text from PDF", "status": "failed"}
        
        # Extract contact info using regex
        email, phone = extract_contact_info(resume_text)
        
        messages = [
            {
                "role": "system",
                "content": """You are a skilled ATS expert analyzing resumes. Extract and structure the following information:
                1. Full name
                2. Skills (technical and soft skills)
                3. Work experience (company names, titles, dates, and key responsibilities)
                4. Education (degrees, institutions, dates)
                
                Format the response as valid JSON with these exact fields: name, skills (array), experience (array), education (array)."""
            },
            {
                "role": "user",
                "content": f"Parse this resume and return only the JSON response:\n\n{resume_text}"
            }
        ]
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0,
        )
        
        response = chat_completion.choices[0].message.content
        
        # Extract just the JSON part from the response
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            response = json_match.group(0)
            
        try:
            parsed_response = json.loads(response)
            # Add the extracted contact info
            parsed_response['email'] = email
            parsed_response['phone'] = phone
            return parsed_response
            
        except json.JSONDecodeError:
            return {
                "error": "Could not parse response",
                "raw_response": response,
                "email": email,
                "phone": phone
            }
        
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }