<div align="center">

# 🛡️ NScan

### Fast • Accurate • Lightweight Network Reconnaissance Toolkit

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-v1.0.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

*A modern network reconnaissance toolkit for fast bug host discovery, reverse IP lookup, active subnet scanning, and payload generation.*

---

**👨‍💻 Developer:** **NS Hacker**

**📢 Telegram:** https://t.me/nscan_script

</div>

---

# 🚀 About

NScan is a lightweight and powerful Python-based network reconnaissance toolkit designed for researchers and security professionals.

It combines multiple reconnaissance modules into a single interactive terminal interface while using ProjectDiscovery's **httpx** engine for fast and reliable HTTP probing.

---

# ✨ Features

- 🌐 Bug Host Discovery
- 🔎 Reverse IP Lookup
- 📡 Active /16 Subnet Scanner
- ⚡ HTTP/HTTPS Live Host Detection
- 🛰️ Technology & Server Detection
- 🔥 Payload Generator
- 📁 Save Scan Results
- 🎨 Interactive Terminal Interface
- 🚀 Fast Scanning using httpx
  
 # 📦 Installation

## 📋 Requirements

Before installing NScan, make sure the following packages are available:

- Python 3.x
- Git
- Golang
- ProjectDiscovery httpx

---

## 📱 Termux Installation

### Step 1 — Update Packages

```bash
pkg update -y && pkg upgrade -y
```

### Step 2 — Install Dependencies

```bash
pkg install python git golang -y
```

### Step 3 — Install httpx

```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

### Step 4 — Add httpx to PATH

```bash
cp $HOME/go/bin/httpx $PREFIX/bin/ 2>/dev/null || true
```

### Step 5 — Clone Repository

```bash
git clone https://github.com/njmehra09/nscan.git
```

### Step 6 — Open Project

```bash
cd nscan
```

### Step 7 — Run NScan

```bash
python nscan.py
```

---

# ⚡ One-Click Installation

Run the following command to install everything automatically.

```bash
pkg update -y && \
pkg install python git golang -y && \
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest && \
cp $HOME/go/bin/httpx $PREFIX/bin/ 2>/dev/null || true && \
git clone https://github.com/njmehra09/nscan.git && \
cd nscan && \
python nscan.py
```

---

# 💻 Linux Installation

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3 python3-pip git golang -y

go install github.com/projectdiscovery/httpx/cmd/httpx@latest

git clone https://github.com/njmehra09/nscan.git

cd nscan

python3 nscan.py
```

---

### Kali Linux

```bash
sudo apt update
sudo apt install python3 python3-pip git golang -y

go install github.com/projectdiscovery/httpx/cmd/httpx@latest

git clone https://github.com/njmehra09/nscan.git

cd nscan

python3 nscan.py
```

---

# 🚀 Create Global Command

Create a shortcut so you can launch NScan from anywhere.

```bash
echo "alias ns='cd \$HOME/nscan && python nscan.py'" >> ~/.bashrc

source ~/.bashrc
```

Now simply run:

```bash
ns
```

from anywhere in your terminal.

---

# 📁 Project Structure

```text
nscan/
├── nscan.py
├── assets/
├── output/
├── requirements.txt
├── install.sh
├── LICENSE
└── README.md
```
# 📸 Screenshots

> **Coming Soon**

### Main Menu

![Main Menu](assets/screenshots/main-menu.png)

### Bug Host Discovery

![Bug Host Discovery](assets/screenshots/bug-host.png)

### Reverse IP Lookup

![Reverse IP](assets/screenshots/reverse-ip.png)

### Active /16 Scanner

![Subnet Scanner](assets/screenshots/subnet.png)

---

# 🚀 Usage

Start the tool using:

```bash
python nscan.py
```

or (if alias is configured):

```bash
ns
```

---

# 📋 Available Modules

| Module | Description |
|---------|-------------|
| 🌐 Bug Host Discovery | Discover live HTTP/HTTPS bug hosts |
| 🔎 Reverse IP Lookup | Find domains hosted on an IP |
| 📡 Active /16 Scanner | Scan active subnets quickly |
| 🔥 Payload Generator | Generate payloads instantly |

---

# 📂 Output

Results are automatically saved inside the **output/** directory.

Example:

```text
output/
├── bug_hosts.txt
├── reverse_ip.txt
├── subnet_scan.txt
└── payloads.txt
```

---

# ❓ Frequently Asked Questions

### Does NScan support Termux?

✅ Yes.

---

### Does it work on Linux?

✅ Ubuntu, Debian and Kali Linux are supported.

---

### Which HTTP engine does NScan use?

NScan uses **ProjectDiscovery httpx** for fast and reliable HTTP probing.

---

### Is Python required?

Yes. Python 3.x is required.

---

# 🛣️ Roadmap

### Version 1.0

- ✅ Bug Host Discovery
- ✅ Reverse IP Lookup
- ✅ Active /16 Scanner
- ✅ Payload Generator

### Upcoming

- DNS Lookup
- SSL Information
- GeoIP Lookup
- JSON Export
- HTML Report
- Better CLI
- Configuration File
- Auto Update

---

# 🤝 Contributing

Contributions, bug reports and feature requests are welcome.

Feel free to open an Issue or Pull Request.

---

# ⚠️ Disclaimer

This project is intended for educational purposes and authorized security testing only.

The developer is not responsible for any misuse of this tool.

---

# 👨‍💻 Developer

**NS Hacker**

📢 Telegram

https://t.me/nscan_script

---

# ⭐ Support

If you like this project:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

<div align="center">

## ❤️ Thank You For Using NScan

**Fast • Accurate • Lightweight**

Made with ❤️ by **NS Hacker**

</div>
