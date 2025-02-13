# CVE-2025-MIST
## Account Takeover via Arbitrary API Token Creation

## 📜 Description

**Mist Community Edition (CE) v4.7.1** contains a critical **Broken Access Control vulnerability**, allowing an **unauthenticated attacker** to generate an arbitrary API token for any user or administrator account. This flaw is triggered by manipulating the API token creation request, requiring only the victim’s email address for exploitation. Successful exploitation results in **Account Takeover**, granting the attacker full access to the victim's account.

A **proof-of-concept (PoC) Python script** is provided in this repository, automating the exploitation of this vulnerability by generating an arbitrary API token and performing the necessary steps to hijack a victim’s account.

## 📌 Affected Version
 - Mist Community Edition (CE) v4.7.1
 - Other versions prior to v4.7.1 may also be affected

## ⚠️ Disclaimer

This project is intended for **educational and ethical research purposes only**. Unauthorized testing on systems without **explicit permission** is illegal. Use responsibly and only on systems you own or have permission to test.

## 🎯 Features

- 🚀 **Automatic API Token Generation**
- 🔄 **CSRF Token & Session Cookie Extraction**
- 🔓 **Login Bypass via API Token**
- 🎭 **Session Hijacking & Account Takeover**

## 🎬 Exploit Demonstration

### 🔹 Script Running  
The script generates an API token, fetches the necessary CSRF token and temporary session cookie, and logs into the account.

![Script Running](/assets/script_running.gif)

### 🔹 Account Access via Cookie  
After obtaining a valid session cookie, the attacker can manually edit their browser's session to hijack the victim's account.

![Account Access](/assets/account_access.gif)

## 🎬 Exploit Demonstration (Manual)

<a href="https://www.youtube.com/watch?v=Lc6EIhNivXI" target="_blank">
  <img src="https://img.youtube.com/vi/Lc6EIhNivXI/maxresdefault.jpg"/>
</a>

## 🛠️ Usage

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/stolichnayer/CVE-2025-MIST.git
cd CVE-2025-MIST
```

### 2️⃣ Install Dependencies

To set up the environment, install the necessary Python dependencies by running the following command:

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Exploit

Once the dependencies are installed, run the PoC script:

```sh
python exploit.py
```
### 4️⃣ Exploiting the Session Cookie

After the script's successful login, use the generated session cookie to access the victim’s account:

- Open Developer Tools in your browser (F12 or Ctrl+Shift+I).

- Navigate to **Storage > Cookies** and locate `session.id`.

- Replace the value with the one retrieved by the script.

- Refresh the page and gain full access to the victim’s account.

## 🧑‍💻 Discovery

The **CVE-2025-XXXX** vulnerability was discovered by **Alex Perrakis** (Stolichnayer).

## 🔗 References:
- [Mist CE Github Repository](https://github.com/mistio/mist-ce)

