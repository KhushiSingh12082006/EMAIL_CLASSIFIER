from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ---------------------------
# GLOBAL (lazy-loaded)
# ---------------------------
tokenizer = None
model = None

MODEL_PATH = os.path.join(settings.BASE_DIR, "model", "phishing_bert_final_v")

# ---------------------------
# Load model only when needed
# ---------------------------
def load_model():
    global tokenizer, model
    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH,
            local_files_only=True
        )
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_PATH,
            local_files_only=True
        )
        model.eval()

# ---------------------------
# Home page
# ---------------------------
def home(request):
    return render(request, "index.html")

# ---------------------------
# Keyword-based type detection
# (ONLY after BERT decision)
# ---------------------------
def get_email_type(text, is_spam):
    text = text.lower()

    if is_spam:
        # 🔴 NON-SAFE categories
        if any(w in text for w in ["password", "verify", "login", "account", "otp"]):
            return "Phishing"

        if any(w in text for w in ["win", "prize", "free", "offer", "gift", "reward"]):
            return "Promotional Scam"

        if any(w in text for w in ["urgent", "immediately", "act now", "suspended"]):
            return "Threat / Urgency Scam"

        if any(w in text for w in ["bank", "upi", "transaction", "card", "refund"]):
            return "Financial Fraud"

        if any(w in text for w in ["click link", "open attachment", "download"]):
            return "Malware / Link Trap"

        if any(w in text for w in ["lottery", "bitcoin", "crypto", "investment"]):
            return "Investment Scam"

        if any(w in text for w in ["job offer", "salary", "hiring", "work from home"]):
            return "Fake Job Scam"
        
        if any(w in text for w in [
        "security alert", "unusual activity", "suspicious activity",
        "new device", "new login", "location change",
        "account compromised", "breach", "data leak"]):
            return "Security Alert"

        return "Suspicious / Unknown"


    else:
        # 🟢 SAFE categories
        if any(w in text for w in ["invoice", "receipt", "payment", "bill"]):
            return "Business / Finance"

        if any(w in text for w in ["meeting", "schedule", "calendar", "zoom"]):
            return "Work / Office"

        if any(w in text for w in ["order", "delivery", "shipped", "tracking"]):
            return "E-commerce"

        if any(w in text for w in ["welcome", "newsletter", "update"]):
            return "Newsletter"

        if any(w in text for w in ["exam", "assignment", "university", "class"]):
            return "Academic"

        if any(w in text for w in ["family", "friend", "party", "invitation"]):
            return "Personal"

        if any(w in text for w in ["support", "ticket", "issue resolved"]):
            return "Customer Support"
        
        
        if any(w in text for w in [
            "google", "google drive", "account activity",
            "secure your account", "new sign-in",
            "didn't allow", "trying to access your account",
    "       security alert", "security notice"]):
            return "Legitimate Security Notice"
        return "General / Safe"
# ---------------------------
# Prediction endpoint
# ---------------------------
@csrf_exempt
def predict(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"})

    text = request.POST.get("email", "").strip()
    if not text:
        return JsonResponse({"error": "Empty input"})

    try:
        load_model()

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1)

        confidence, predicted_class = torch.max(probs, dim=1)
        confidence = confidence.item()

        # IMPORTANT: adjust index if your model is reversed
        is_spam = predicted_class.item() == 1

        email_type = get_email_type(text, is_spam)

        return JsonResponse({
            "Spam_or_Not": "SPAM" if is_spam else "SAFE",
            "Confidence": round(confidence, 4),
            "Type": email_type
        })

    except Exception as e:
        return JsonResponse({"error": str(e)})