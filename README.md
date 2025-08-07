# 🧠 TCPByte – Automation System for Client Email Outreach

This lightweight automation system was developed to improve client communication workflows at TCPByte by automating bulk email delivery with HTML content and tracking results in a structured report.

## 🚀 Purpose

To streamline institutional outreach by reducing manual follow-up tasks and ensuring professional delivery of service presentations via email.

## 💡 Key Features

- HTML email template with embedded company signature
- Secure email sending via SMTP (SSL)
- Dynamic email personalization (name + email)
- CSV-based contact input and results output
- Automatic deletion of old logs
- Real-time status feedback in terminal
- Generates a `results.csv` file with delivery status

## 📦 Stack

- **Python**
- Libraries: `pandas`, `smtplib`, `email.mime`, `getpass`, `os`
- CSV for input/output
- SMTP with SSL authentication

## 📁 How to Use

1. Clone the repository.
2. Place your contact list in a file named `contacts.csv` with the following columns:
   - `name`
   - `email`
3. Run the script. You’ll be prompted to enter your email password securely.
4. After sending, a `results.csv` file will be generated showing the delivery status of each email.

## 📌 Notes

- Do not include confidential credentials directly in the script.
- The script automatically deletes the previous `results.csv` before each execution.

