# Account Takeover via Arbitrary API Token Creation
<table>
  <tr>
    <td width="150" rowspan="2">
      <a href="https://github.com/mistio/mist-ce" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/1569127?s=200&v=4" alt="Summer Pearl Logo" width="120"/>
      </a>
    </td>
    <td>
      <h1>Mist Community Edition</h1>
      <h3> An Open-Source Multicloud Management Platform</h3>
    </td>
  </tr>
  <tr>
    <td>
      <table>
        <tr>
          <td>
            🔗 <a href="https://github.com/mistio/mist-ce" target="_blank">Mist Github Repository</span></a>
          </td>
          <td style="padding-left: 15px;">
            🚀 <a href="https://github.com/mistio/mist-ce/releases/tag/v4.7.2" target="_blank"> Patched Version (v4.7.2) </span></a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

## 📜 Description

Mist Community Edition (CE) versions prior to 4.7.2 contain an unauthenticated API token generation vulnerability. By manipulating token creation requests with a known victim email address, attackers can generate valid API tokens for any user or administrator account, leading to full account takeover. This flaw bypasses all authentication controls and requires no user interaction.

A proof-of-concept (PoC) python script is provided in this repository, automating the exploitation of this vulnerability by generating an arbitrary API token and performing the necessary steps to hijack a victim’s account.

## 🔍 Affected Versions

| Status       | Version         |
|--------------|-----------------|
| 🔴 Vulnerable |  ≤ `4.7.1`      |
| 🟢  Fixed     |  &nbsp;&nbsp;`4.7.2`      |   

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

## 🎬 Exploit Demonstration (Manually)
> The video below demonstrates step-by-step manual exploitation of this vulnerability without script automation.

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

This vulnerability was discovered by **Alex Perrakis** (Stolichnayer).

## 🔗 References:
- [Mist CE Github Repository](https://github.com/mistio/mist-ce)
- [Patched Version (v4.7.2)](https://github.com/mistio/mist-ce/releases/tag/v4.7.2)
- [Fix Commit](https://github.com/mistio/mist.api/commit/db10ecb62ac832c1ed4924556d167efb9bc07fad)


