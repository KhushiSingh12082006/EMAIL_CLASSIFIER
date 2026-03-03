📧 AETHER SCAN – AI-Based Email Security Detection System

An intelligent Email Classification & Security Detection System built using Django + BERT, designed to detect whether an email is SAFE or NON-SAFE, along with identifying the email category such as phishing, promotional, security alert, etc. Screenshots are also present in static file, view it to get more clear vision of Project 

This project was developed as part of the IBM Internship / IBM Tecnovate Program.

Presentation Link : https://1drv.ms/p/c/2034eba96d41ae6d/IQCmoQarXM6ySaTr-SXt8HqKAZxC_hIi5mAf1QWsOskoEUQ?e=rf2I9d

1.Features

 AI-powered classification using a fine-tuned BERT model

 Detects SAFE vs NON-SAFE emails

Rule-based email category detection after model prediction

 Modern animated UI with Glassmorphism

 Confidence score visualization (Gauge Meter)

 Session history tracking

 Dynamic background animations

Email Categories Supported

Phishing

Promotional

Scam / Fraud

Security Alert

General / Safe Communication

🏗️ Tech Stack

Backend: Django (Python)

Model: Fine-tuned BERT (Transformers)

Frontend: HTML, CSS, JavaScript, Bootstrap

ML Libraries: PyTorch, HuggingFace Transformers

Deployment Ready

📁 Project Structure
email_classifier/
│
├── classifier/              # Django app
│   ├── views.py              # Model inference + rules
│   ├── urls.py
│   └── ...
│
├── email_classifier/        # Project settings
│
├── model/                   # (Ignored in GitHub)
│
├── static/
│   └── images/              # Background images
│
├── templates/
│   └── index.html            # Main UI
│
├── manage.py
├── db.sqlite3
└── README.md
Model Handling (Important)

 The trained BERT model is NOT included in this GitHub repository
This is intentional to avoid large file issues.

🔗 Download Model from Google Drive

 Model ZIP File (Required to Run Project):
(https://drive.google.com/file/d/1MxN9aEQr9QUmCy1cxAbTCNaPnvIH4ptx/view?usp=drive_link)

 After Downloading:

Extract the ZIP fill

Place the extracted folder inside:

email_classifier/model/

Expected structure:

model/
└── phishing_bert_final/
    ├── config.json
    ├── pytorch_model.bin
    ├── tokenizer.json
    ├── vocab.txt
⚙️ Installation & Setup
1️ Clone the Repository
git clone <your-github-repo-link>
cd email_classifier
2️ Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️ Install Dependencies
pip install django torch transformers whitenoise
4️ Apply Migrations
python manage.py migrate
5️ Run the Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
🧪 How It Works

User enters email text

BERT model predicts:

SAFE or NON-SAFE

Confidence score

Rule-based logic assigns category

UI updates:

Gauge

Status

Category

History log


