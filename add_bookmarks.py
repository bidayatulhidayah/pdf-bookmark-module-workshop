#!/usr/bin/env python3
"""
PDF Bookmark Creator
Reads chapters from chapters.txt and adds bookmarks to your PDF
"""

from pypdf import PdfReader, PdfWriter
from datetime import datetime

def read_chapters(filename='chapters.txt'):
    """Read chapter names and page numbers from text file"""
    chapters = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Expected format: "Chapter Name | Page Number"
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) == 2:
                        chapter_name = parts[0].strip()
                        page_num = parts[1].strip()
                        
                        try:
                            page_num = int(page_num)
                            chapters.append((chapter_name, page_num))
                        except ValueError:
                            print(f"Warning: Line {line_num} has invalid page number: {page_num}")
                    else:
                        print(f"Warning: Line {line_num} format incorrect: {line}")
                else:
                    print(f"Warning: Line {line_num} missing '|' separator: {line}")
        
        return chapters
    
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        print("Please create a chapters.txt file in the same folder.")
        return []

def add_bookmarks_to_pdf(input_pdf, output_pdf, chapters):
    """Add bookmarks to PDF file"""
    
    if not chapters:
        print("No chapters found to add!")
        return False
    
    try:
        # Read the original PDF
        reader = PdfReader(input_pdf)
        writer = PdfWriter()
        
        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Add bookmarks
        print("\nAdding bookmarks:")
        for chapter_name, page_num in chapters:
            # PDF pages are 0-indexed, so subtract 1
            writer.add_outline_item(chapter_name, page_num - 1)
            print(f"  ✓ {chapter_name} → Page {page_num}")
        
        # Write the new PDF
        with open(output_pdf, 'wb') as f:
            writer.write(f)
        
        print(f"\n✅ Success! Bookmarks added to: {output_pdf}")
        return True
    
    except FileNotFoundError:
        print(f"Error: {input_pdf} not found!")
        print("Please make sure your PDF file is in the same folder.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 50)
    print("PDF Bookmark Creator")
    print("=" * 50)
    
    # File names - you can change these if needed
    input_pdf = "input.pdf"          # Your original PDF from Canva
    chapters_file = "chapters.txt"   # Text file with chapter info
    
    # Generate output filename with date (format: output_2026-01-27.pdf)
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_pdf = f"output_{date_str}.pdf"
    
    print(f"\nReading chapters from: {chapters_file}")
    chapters = read_chapters(chapters_file)
    
    if chapters:
        print(f"Found {len(chapters)} chapters")
        print(f"\nProcessing: {input_pdf}")
        add_bookmarks_to_pdf(input_pdf, output_pdf, chapters)
    else:
        print("\nPlease create a chapters.txt file with your chapter information.")
        print("See the example format in chapters.txt")

if __name__ == "__main__":
    main()
