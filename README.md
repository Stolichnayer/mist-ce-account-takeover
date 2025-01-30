# Account Takeover via Arbitrary API Token Creation in Mist CE

## 📜 Description

This repository contains a proof-of-concept (PoC) script demonstrating a Broken Access Control vulnerability, leading to **Account Takeover (ATO)**, in Mist CE v4.7.1. 
By exploiting the ability to generate arbitrary API tokens without authentication, the script obtains a session cookie,  
allowing an attacker to impersonate a victim and access their account.

---

## ⚠️ Disclaimer

This project is intended for **educational and ethical research purposes only**.  
Unauthorized testing on systems without **explicit permission** is illegal.  
Use responsibly and only on systems you own or have permission to test.

---

## 🎯 Features

- 🚀 **Automatic API Token Generation**
- 🔄 **CSRF Token & Session Cookie Extraction**
- 🔓 **Login Bypass via API Token**
- 🎭 **Session Hijacking & Account Takeover**

---

## 🎬 Demonstration

### 🔹 Script Running  
The script generates an API token, fetches the necessary CSRF token and temporary session cookie, and logs into the account.

![Script Running](Script%20Running.gif)

### 🔹 Account Access via Cookie  
After obtaining a valid session cookie, the attacker can manually edit their browser's session to hijack the victim's account.

![Account Access](Account%20Access.gif)

---

## 🛠️ Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/stolichnayer/MistATO_PoC.git
cd MistATO_PoC
```

### 2️⃣ Install Dependencies

To set up the environment, install the necessary Python dependencies by running the following command:

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Exploit

Once the dependencies are installed, run the PoC script:

```sh
python MistATO_PoC.py
```
### 4️⃣ Exploiting the Session Cookie

After a successful login, use the stolen session cookie to access the victim’s account:

- Open Developer Tools in your browser (F12 or Ctrl+Shift+I).

- Navigate to **Storage > Cookies** and locate `session.id`.

- Replace the value with the one retrieved by the script.

- Refresh the page and gain full access to the victim’s account.

## 👨‍💻 Author

Alex Perrakis

GitHub: https://github.com/Stolichnayer


