import re

def extract_contact_info(text):
    """Extract contact information using regex patterns."""
    if not text:
        return None, None
        
    # Email pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = re.search(email_pattern, text)
    email = email.group(0) if email else None

    # Phone patterns - multiple formats
    phone_patterns = [
        r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',  # (123) 456-7890
        r'\d{10}',  # 1234567890
        r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # 123-456-7890
        r'\+\d{1,3}\s?\d{10}'  # +1 1234567890
    ]
    
    phone = None
    for pattern in phone_patterns:
        match = re.search(pattern, text)
        if match:
            phone = match.group(0)
            break
            
    return email, phone