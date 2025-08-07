# 🧠 TCPByte – Automation System for Client Email Outreach

This lightweight automation system was developed to improve client communication workflows at TCPByte by automating bulk email delivery with HTML content and tracking results in a structured report.

## 🚀 Purpose

To streamline institutional outreach by reducing manual follow-up tasks and ensuring professional delivery of service presentations via email.

## 💡 Key Features

- HTML email template with embedded company signature
- Secure email sending via SMTP SSL
- Dynamic email personalization (name + email)
- CSV-based contact input and results output
- Automatic deletion of old logs
- Real-time status feedback in terminal
- Generates a `resultados.csv` with delivery status

## 📦 Stack

- **Python**
- `pandas`, `smtplib`, `email.mime`, `getpass`, `os`
- SMTP with SSL authentication
- CSV file for contact input/output

## 📁 How to Use

1. Clone the repository.
2. Place your contact list in a file named `contactos.csv` with columns:
