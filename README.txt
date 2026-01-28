# PDF Bookmark Creator - Instructions

## What You Need

1. Python installed on your computer (download from python.org)
2. Your PDF file exported from Canva
3. These files (all in the same folder):
   - `add_bookmarks.py` (the script)
   - `chapters.txt` (your chapter list)
   - `input.pdf` (your PDF from Canva - rename it to this)

## Setup (One-time only)

### Step 1: Install Python
- Go to https://python.org/downloads
- Download and install Python
- During installation, check "Add Python to PATH"

### Step 2: Install Required Library
Open Terminal/Command Prompt and type:
```bash
pip install pypdf
```

## How to Use

### Step 1: Prepare Your Files
1. Export your PDF from Canva
2. Rename it to `input.pdf`
3. Put it in the same folder as the script

### Step 2: Edit chapters.txt
1. Open `chapters.txt` in any text editor (Notepad, TextEdit, etc.)
2. Replace the example chapters with your actual chapters
3. Update the page numbers
4. Save the file

**Format:** `Chapter Name | Page Number`

**Example:**
```
Chapter 1: Introduction to Design | 1
Chapter 2: Color Theory | 12
Chapter 3: Typography Basics | 25
```

### Step 3: Run the Script
1. Open Terminal (Mac/Linux) or Command Prompt (Windows)
2. Navigate to the folder with your files:
   ```bash
   cd path/to/your/folder
   ```
3. Run the script:
   ```bash
   python add_bookmarks.py
   ```

### Step 4: Get Your Result
- A new file called `output_2026-01-27.pdf` will be created (with today's date)
- This file has all your bookmarks added!
- Open it in any PDF reader to see the bookmarks in the sidebar
- Each time you run the script, it creates a new file with the current date

## Changing File Names (Optional)

If you want to use different file names, edit these lines in `add_bookmarks.py`:

```python
input_pdf = "input.pdf"          # Change to your PDF name
chapters_file = "chapters.txt"   # Change chapters file name
```

The output file automatically includes the date (e.g., `output_2026-01-27.pdf`).
If you want to change the output naming format, look for this line:
```python
output_pdf = f"output_{date_str}.pdf"
```

## Troubleshooting

**Error: "python not found"**
- Make sure Python is installed and added to PATH
- Try `python3` instead of `python`

**Error: "No module named pypdf"**
- Run: `pip install pypdf`
- Or try: `pip3 install pypdf`

**Error: "chapters.txt not found"**
- Make sure all files are in the same folder
- Check the file name is exactly `chapters.txt`

**Error: "input.pdf not found"**
- Make sure your PDF is named `input.pdf`
- Or change the name in the script

## Tips

- Page numbers start from 1 (first page = 1)
- You can add comments in chapters.txt with #
- Empty lines are ignored
- If you update your PDF, just change the page numbers in chapters.txt and run again
- Keep the original chapters.txt as a backup

## Need Help?

The script will show helpful error messages if something goes wrong.
Read the error message - it usually tells you exactly what to fix!
