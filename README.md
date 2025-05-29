## Grading-System
Grading sytem with email response and descriptive response pdf that reviews the test

# This Program will
- Use Answers to generate Score
- Generate PDF report with score
- Send Response to the student thereafter

# Libraries Used in the Script

## 1. Built-in Python Libraries (No Installation Required)
These libraries come with Python by default:

- **`smtplib`** → For sending emails using the SMTP protocol.
- **`os`** → For file handling and deleting generated PDFs.
- **`time`** → For adding delays (e.g., `time.sleep(2)`).
- **`email.mime.text` (`MIMEText`)** → For creating the body of an email.
- **`email.mime.multipart` (`MIMEMultipart`)** → For handling email attachments.
- **`email.mime.base` (`MIMEBase`)** → For encoding and attaching files.
- **`email.encoders`** → For encoding attachments in emails.

## 2. External Library (Requires Installation)
The following library must be installed manually:

- **`reportlab`** → Used for generating PDFs.
  - **Submodules used:**
    - `reportlab.lib.pagesizes.letter` → Defines standard page size (letter format).
    - `reportlab.pdfgen.canvas` → Used to draw text and generate PDF reports.

### Installation Command:
To install `reportlab`, run:
```sh
pip install reportlab
```

### Usage: pass your test results to the student answers folder and enjoy
