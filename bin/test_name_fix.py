#!/usr/bin/env python3
"""
Test the improved name extraction fix
"""

import sys
import os

# Add backend directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from generator import CoverLetterGenerator

def test_name_extraction():
    """Test the improved name extraction with problematic resume text."""
    print("🧪 Testing Improved Name Extraction")
    print("=" * 50)
    
    generator = CoverLetterGenerator()
    
    # Test case 1: AYAK MANNA CV (problematic case)
    ayak_resume = """I have 3 years of experience.

Career Objective

Pursing Computer Science with a passion for AI/ML development and Front-end Technologies. Eager to apply problem-solving skills and programming knowledge to contribute to innovative projects.

Education
Bachelor of Technology in Computer Science

Technical Skills
Python, Java, JavaScript, HTML, CSS

Languages Known
English, Hindi, Bengali

AYAK MANNA
Email: ayak@example.com
Phone: 1234567890"""
    
    print("📄 Test Case 1: AYAK MANNA Resume")
    user_info = generator.extract_user_info(ayak_resume)
    print(f"Extracted Name: {user_info.get('name', 'Candidate')}")
    print(f"Expected: AYAK MANNA")
    print(f"Result: {'✅ PASS' if user_info.get('name') == 'AYAK MANNA' else '❌ FAIL'}")
    print()
    
    # Test case 2: NILADRI BHANDARI (should work correctly)
    niladri_resume = """I have 4 years of experience. Career Objective
Education
Technical Skills/Additional Certification
Internships and Academic Achievements
Academic Projects
NILADRI BHANDARI
Lakshmikantpur, Kolkata
Email: niladri@example.com"""
    
    print("📄 Test Case 2: NILADRI BHANDARI Resume")
    user_info = generator.extract_user_info(niladri_resume)
    print(f"Extracted Name: {user_info.get('name', 'Candidate')}")
    print(f"Expected: NILADRI BHANDARI")
    print(f"Result: {'✅ PASS' if user_info.get('name') == 'NILADRI BHANDARI' else '❌ FAIL'}")
    print()
    
    # Test case 3: Resume with "Languages Known" at end
    problematic_resume = """John Doe
Software Engineer
5 years experience
Skills: Python, Java, JavaScript
Languages Known
English, Spanish, French"""
    
    print("📄 Test Case 3: Resume ending with 'Languages Known'")
    user_info = generator.extract_user_info(problematic_resume)
    print(f"Extracted Name: {user_info.get('name', 'Candidate')}")
    print(f"Expected: John Doe")
    print(f"Result: {'✅ PASS' if user_info.get('name') == 'John Doe' else '❌ FAIL'}")
    print()
    
    print("🎯 Name Extraction Fix Test Complete!")

if __name__ == "__main__":
    test_name_extraction()
