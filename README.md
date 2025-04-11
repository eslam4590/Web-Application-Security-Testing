# Web Application Security Testing

This repository contains scripts and documentation used to conduct security testing on a sample web application to identify vulnerabilities such as **SQL Injection**, **Cross-Site Scripting (XSS)**, and **Authentication Flaws**.

## 📌 Project Objective

The goal of this project is to:
- Demonstrate basic manual and automated security testing techniques.
- Identify common web vulnerabilities (e.g., SQLi, XSS, and Auth flaws).
- Document findings and recommend mitigation strategies.

---

## 🧪 Testing Scope

### ✅ Vulnerabilities Covered
- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- **Authentication Bypass / Weak Credentials**

---

## 🛠️ Tools Used

- [Python](https://www.python.org/)
- [Requests Library](https://docs.python-requests.org/)
- [Burp Suite (Optional)](https://portswigger.net/burp)
- [OWASP ZAP (Optional)](https://www.zaproxy.org/)
- [SQLmap (Optional)](https://sqlmap.org/)

---

## 🧾 Scripts

### 1. `sql_injection_test.py`
Tests for SQL injection by injecting common payloads into login forms.

### 2. `xss_test.py`
Tests for reflected XSS by injecting JavaScript payloads into search or input fields.

### 3. `auth_flaws_test.py`
Tests login forms for authentication bypass using common and malicious login credentials.

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Install dependencies:

bash
Copy
Edit
pip install requests
Modify the URLs in each script to match your target web application.

Run each script:

bash
Copy
Edit
python sql_injection_test.py
python xss_test.py
python auth_flaws_test.py
⚠️ Disclaimer
This project is for educational and ethical testing purposes only. Do not use these scripts on systems you do not own or have explicit permission to test. Unauthorized access or testing is illegal.

📄 License
This project is open-source and available under the MIT License.

🙌 Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

