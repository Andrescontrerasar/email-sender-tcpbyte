import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import os

# Remove previous results file if it exists
if os.path.exists("results.csv"):
    os.remove("results.csv")

# Load contact list from CSV
df = pd.read_csv("contacts.csv")

# Prompt for email password (not displayed)
password = getpass.getpass("Enter your email password (will not be shown): ")

# SMTP configuration
smtp_server = "your.smtp.server.com"
smtp_port = 465
sender_email = "your_email@example.com"

# Store results
results = []

# Process each contact
for index, row in df.iterrows():
    name = row["name"]
    recipient_email = row["email"]
    status = "❌ Failed"

    # Create email message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Technology Services Proposal – TCPByte"
    msg["From"] = sender_email
    msg["To"] = recipient_email

    # HTML email content
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; font-size: 15px; color: #333;">
        <p>Dear Director,</p>

        <p>I hope this message finds you well.</p>

        <p>My name is <strong>Andrés Contreras</strong>, representing <strong>TCPByte IT Services</strong>, a company dedicated to providing comprehensive technological solutions for educational institutions.</p>

        <p>We would like to introduce the following key services tailored to support your institution's digital transformation:</p>

        <ul>
            <li>🛠️ <strong>IT Support:</strong> On-site or remote troubleshooting and tech assistance.</li>
            <li>💻 <strong>Hardware Procurement:</strong> Personalized consultation for acquiring equipment suited to your school’s needs.</li>
            <li>🔧 <strong>Preventive Maintenance:</strong> Ongoing care to extend the lifespan of your devices.</li>
            <li>🧠 <strong>Smart Automation:</strong> Streamlined workflows using intelligent tools.</li>
            <li>🌐 <strong>Web Development & Software Solutions:</strong> Tailored platforms and modern websites.</li>
            <li>📅 <strong>Academic Timetable Planning 2025:</strong> Custom scheduling per teacher and course.</li>
        </ul>

        <p>We would be happy to arrange a meeting to discuss how we can support your institution’s goals.</p>

        <p>
            📞 <strong>[Your Phone]</strong><br>
            📧 <strong>[Your Email]</strong><br>
            🌐 <a href="https://yourwebsite.com" target="_blank">https://yourwebsite.com</a>
        </p>

        <img src="https://yourwebsite.com/signature.png" width="320" style="display:block; margin-top:15px;">
    </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    # Attempt to send email
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        print(f"✅ Email successfully sent to: {name} <{recipient_email}>")
        status = "✅ Sent"
    except Exception as e:
        print(f"❌ Failed to send to {recipient_email}: {e}")

    # Append result
    results.append({"name": name, "email": recipient_email, "status": status})

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("results.csv", index=False)
print("📄 Delivery report saved to 'results.csv'")

