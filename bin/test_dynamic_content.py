#!/usr/bin/env python3
"""
Test script to verify enhanced dynamic content generation
"""

import sys
import os

# Add backend directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from generator import CoverLetterGenerator

def test_dynamic_content():
    """Test the enhanced dynamic content generation."""
    print("🧪 Testing Enhanced Dynamic Content Generation")
    print("=" * 50)
    
    # Initialize generator
    generator = CoverLetterGenerator()
    
    # Test data
    job_info = {
        'position': 'Frontend Developer',
        'company': 'TCS',
        'skills': 'react, javascript, html, css',
        'company_values': 'innovation and excellence'
    }
    
    user_info = {
        'name': 'NILADRI BHANDARI',
        'skills': 'python, java, javascript, sql, git, tensorflow, flask, spring, mysql, html',
        'years': '5 years',
        'experience_level': 'experienced'
    }
    
    # Test different content types
    print("📋 Testing different content types:")
    print()
    
    content_types = ["company_alignment", "skills_demonstration", "value_proposition", "career_aspiration"]
    
    for content_type in content_types:
        content = generator._generate_dynamic_content(job_info, user_info, content_type)
        print(f"🔹 {content_type.upper()}: {content}")
        print()
    
    # Test full cover letter generation
    print("📄 Testing Full Cover Letter Generation:")
    print("=" * 50)
    
    job_description = """
    We are looking for an experienced Frontend Developer with expertise in React, JavaScript, and modern web technologies.
    The ideal candidate should have 5+ years of experience and strong skills in frontend frameworks.
    """
    
    user_input = "My name is NILADRI BHANDARI and I have 5 years. I am skilled in python, java, javascript, sql, git, tensorflow, flask, spring, mysql, html."
    
    cover_letter = generator.generate_cover_letter(
        job_description=job_description,
        user_input=user_input,
        company='TCS',
        target_role='Frontend Developer'
    )
    
    print("📝 Generated Cover Letter:")
    print("-" * 30)
    print(cover_letter)
    print("-" * 30)
    
    # Check for dynamic content markers
    print("\n🔍 Checking for enhanced content:")
    if "value_proposition" in cover_letter or "company_alignment" in cover_letter:
        print("❌ Template variables not replaced properly")
    else:
        print("✅ Template variables replaced successfully")
    
    # Check for varied content
    lines = cover_letter.split('\n')
    paragraphs = [line.strip() for line in lines if line.strip() and not line.strip().startswith(('Dear', 'Sincerely', 'NILADRI', 'I am', 'With best regards'))]
    
    print(f"\n📊 Content Analysis:")
    print(f"Total paragraphs: {len(paragraphs)}")
    print(f"Unique paragraphs: {len(set(paragraphs))}")
    
    if len(set(paragraphs)) == len(paragraphs):
        print("✅ All paragraphs are unique")
    else:
        print("❌ Some paragraphs are duplicated")

if __name__ == "__main__":
    test_dynamic_content()
