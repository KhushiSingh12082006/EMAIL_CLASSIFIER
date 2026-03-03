📧 AETHER SCAN

1.AI-Based Email Security Detection System

AETHER SCAN is an intelligent Email Classification & Security Detection System built using Django + BERT.
It analyzes email content to determine whether an email is SAFE or NON-SAFE and also identifies the email category such as phishing, promotional, scam, or security alert.

This project was developed as part of the IBM Tecnovate Program / IBM Internship.

Presentation Link
https://1drv.ms/p/c/2034eba96d41ae6d/IQCmoQarXM6ySaTr-SXt8HqKAZxC_hIi5mAf1QWsOskoEUQ?e=rf2I9d

Screenshots of the UI are available in the static/ folder for better project visualization.

2.Features

AI-powered email classification using a fine-tuned BERT model

Detection of SAFE and NON-SAFE emails

Rule-based email category identification

Modern animated UI with Glassmorphism design

Confidence score visualization using a gauge meter

Session-based email history tracking

Dynamic background animations

Email Categories Supported

Phishing

Promotional

Scam / Fraud

Security Alert

General / Safe Communication

3.Tech Stack

Backend
Django (Python)

Machine Learning
Fine-tuned BERT
PyTorch
HuggingFace Transformers

Frontend
HTML
CSS
JavaScript
Bootstrap

4.Deployment
Django production-ready setup

Project Structure
email_classifier/
│
├── classifier/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── email_classifier/
│
├── model/                 (Ignored in GitHub)
│
├── static/
│   └── images/
│
├── templates/
│   └── index.html
│
├── manage.py
├── db.sqlite3
└── README.md
Model Handling (Important)

The trained BERT model is not included in this GitHub repository to avoid large file issues.

Model Download Link (Required)
https://drive.google.com/file/d/1MxN9aEQr9QUmCy1cxAbTCNaPnvIH4ptx/view?usp=drive_link

After downloading:

Extract the ZIP file

Place the extracted folder inside

email_classifier/model/

Expected structure:

model/
└── phishing_bert_final/
    ├── config.json
    ├── pytorch_model.bin
    ├── tokenizer.json
    └── vocab.txt
Installation & Setup

Clone the repository

git clone <repository-url>
cd email_classifier

Create a virtual environment

python -m venv venv

Activate it

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

Install dependencies

pip install django torch transformers whitenoise

Apply migrations

python manage.py migrate

Run the server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/
How It Works

User enters email text

BERT model predicts SAFE or NON-SAFE status

Confidence score is generated

Rule-based logic assigns email category

UI updates with gauge meter, status, category, and history

5.Future Scope

Multi-class email classification

OCR-based text extraction from images and attachments

Explainable AI for prediction reasoning

Real-time email client integration

Cloud deployment and mobile support
