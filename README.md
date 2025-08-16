# 📄 ATS Resume Analyzer

An interactive **Streamlit web app** that analyzes resumes against job descriptions using **Google’s Gemini AI**.  
It simulates both:  
- **HR-style professional evaluation** (strengths & weaknesses)  
- **ATS-style evaluation** (percentage match, missing keywords, overall thoughts)  

---

## 🚀 Features
- Upload your resume in **PDF format**  
- Paste a **job description**  
- Get a **professional HR evaluation**  
- Get an **ATS score with missing keywords**  
- Handles API quota errors with auto-retry  
- Simple, clean **Streamlit UI**  

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** – user interface  
- **PyPDF2** – resume text extraction  
- **Google Generative AI (Gemini 2.5 Flash)** – AI-powered evaluation  
- **dotenv** – API key management  

---

## 📂 Project Structure
├── app.py              # Main Streamlit app  
├── requirements.txt    # Python dependencies  
├── .env                # Environment variables (API keys)  
└── README.md           # Project documentation



---

## 🎯 Usage

1. Paste a **job description** into the text area.  
2. Upload your **resume (PDF)**.  
3. Choose one of the analysis modes:  
   - **Tell Me About the Resume** → HR-style professional evaluation  
   - **Percentage Match** → ATS-style match, missing keywords, and thoughts  
4. View results directly in the app.  

---


## 🔑 Example Output

**HR Mode:**  
- Strengths in relation to job requirements  
- Weaknesses / gaps  
- Overall candidate evaluation  

**ATS Mode:**  
- Percentage match score  
- Missing keywords  
- Overall ATS-style thoughts  

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a pull request.  

---

## 📜 License
This project is licensed under the **MIT License**.  

---

✨ Built with ❤️ using **Python, Streamlit, and Google Gemini **
