import smtplib
import os, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_pdf_report(student_answers, correct_answers, explanations, i):
    """
    Generate a PDF report with answers and explanations.
    
    """
    filename = f"{i}Results"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 50, "Test Results")
    #
    score = sum(1 for a, b in zip(student_answers, correct_answers) if a == b)
    c.drawString(100, height - 70, f"Score: {score}/{len(correct_answers)}")
    y_position = height - 100

    for i, (student_ans, correct_ans, explanation) in enumerate(zip(student_answers, correct_answers, explanations), start=1):
        c.drawString(100, y_position, f"Q{i}: Your Answer: {student_ans}, Correct: {correct_ans}")
        y_position -= 20
        c.drawString(120, y_position, f"Explanation: {explanation}")
        y_position -= 30
        if y_position < 50:
            c.showPage()
            y_position = height - 50

    c.save()
    return filename


def send_test_score_with_pdf(answer_string: str, correct_answers: str, explanations: str, sender_email: str, sender_password: str, i):
    """
    Separates answers and emails
    Uses the correct answer's string to calculate the score
    Prepares the Email Subject and Body
    Starts using the SMTP module to send the email's
    
    """
    
    # Separate answers and email
    student_answers = answer_string[:15]
    student_email = answer_string[15:]
    
    print("Currently sending email to:", student_email.split("@")[0])
    student_email = "siphakwe@gmail.com"
    
    # Generate PDF with results and explanations
    pdf_filename = generate_pdf_report(student_answers, correct_answers, explanations, i)

    # Create the email
    score = sum(1 for a, b in zip(student_answers, correct_answers) if a == b)
    subject = "Your Test Score & Explanation"
    body = f"""
    Hello, {student_email.split("@")[0]}

    Your test results are ready. You scored {score}/{len(correct_answers)}.
    
    Please find attached a detailed PDF with your answers, correct answers, and explanations.

    Best regards,
    Simangaliso Innocent Phakwe
    """
    
    # Structure the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = student_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    # PDF formatting and writing
    # This woul be the same as creating a foundation and the building on it
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={pdf_filename}")
        msg.attach(part)


    try:
        # Connect to SMTP server and send email
        
        # Start the smtp server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # prompt login
        server.login(sender_email, sender_password)
        
        # Send Email
        server.sendmail(sender_email, student_email, msg.as_string(), i)
        
        # Quit server
        server.quit()
        print(f"Score and explanation sent to {student_email}")
        time.sleep(2)
    except Exception as e:
        print(f"Failed to send email: {e}")
