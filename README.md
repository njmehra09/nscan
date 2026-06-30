# 🚀 NScan

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg">
  <img src="https://img.shields.io/badge/Platform-Termux-green.svg">
  <img src="https://img.shields.io/badge/OS-Linux-orange.svg">
  <img src="https://img.shields.io/badge/License-MIT-red.svg">
</p>

<p align="center">
Fast • Accurate • Lightweight • Network Reconnaissance Tool
</p>

---

# 📖 About

**NScan** is a powerful Python-based Network Reconnaissance Tool built for fast Bug Host Discovery, Reverse IP Lookup, Active Subnet Detection and Payload Generation.

It combines multiple reconnaissance utilities into one interactive terminal interface while using **ProjectDiscovery httpx** for high-speed verification.

---

# ✨ Features

- 🔍 Bug Host Discovery
- 🌐 Reverse IP Lookup
- 📡 Active /16 Subnet Scanner
- ⚡ Payload Generator
- 🖥 HTTP Status Detection
- 🔒 HTTPS Detection
- 📦 Technology Detection
- 🌍 Server Banner Detection
- 💾 Automatic Result Saving
- 📁 File & CIDR Support
- 🚀 Fast Multi-threaded Scanning

---

# 🛠 Requirements

Before running NScan make sure these packages are installed:

- Python 3.x
- Git
- Golang
- ProjectDiscovery httpx

---

# 📦 Installation (Termux)

## Step 1 — Update Packages

```bash
pkg update -y && pkg upgrade -y
```

---

## Step 2 — Install Required Packages

```bash
pkg install python git golang -y
```

---

## Step 3 — Install ProjectDiscovery httpx

```bash
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

---

## Step 4 — Add httpx to PATH

```bash
cp $HOME/go/bin/httpx $PREFIX/bin/ 2>/dev/null || true
```

---

## Step 5 — Clone Repository

```bash
git clone https://github.com/njmehra09/nscan.git
```

---

## Step 6 — Enter Project Directory

```bash
cd nscan
```
---

## Step 7 — Create Global Shortcut (Optional)

Agar aap chahte hain ki tool ko future me sirf `ns` likhkar kahin se bhi run kar sakein, to ye command chalayein:

```bash
sed -i '/alias ns=/d' $HOME/.bashrc
echo "alias ns='cd \$HOME/nscan && python nscan.py'" >> $HOME/.bashrc
source $HOME/.bashrc
```

Ab terminal me sirf:

```bash
ns
```

likhne se tool start ho jayega.

---

## Step 8 — Run NScan

```bash
python nscan.py
```

Ya agar alias banaya hai:

```bash
ns
```

---

# ⚡ One Click Installer

Ek hi command me complete installation:

```bash
pkg update -y && \
pkg install python git golang -y && \
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest && \
cp $HOME/go/bin/httpx $PREFIX/bin/ 2>/dev/null || true && \
rm -rf nscan && \
git clone https://github.com/njmehra09/nscan.git && \
cd nscan && \
sed -i '/alias ns=/d' $HOME/.bashrc && \
echo "alias ns='cd \$HOME/nscan && python nscan.py'" >> $HOME/.bashrc && \
source $HOME/.bashrc && \
python nscan.py
```

---

# 🖥 Main Menu

When you run the tool, you'll see a menu similar to:

```
[1] Bug Host Discovery
[2] Reverse IP Lookup
[3] Payload Generator
[4] Active /16 Subnet Scanner
[5] Exit
```

---

# 📂 Output Files

Generated files are automatically saved.

Example:

```
scan_results_20260630_101500/
```

Reverse DNS output:

```
reverse_dns_results.txt
```

Verified subnets:

```
verified_subnets.txt
```

Payloads:

```
payloads.txt
```

---

# 🚀 Usage Examples

### Scan Single Target

```
example.com
```

### Scan Multiple Targets

```
targets.txt
```

### Scan CIDR

```
104.16.0.0/16
```

### Reverse Lookup

```
8.8.8.8
```

### Payload Generation

Generate payloads directly from the Payload Generator menu.

---

# ⚙ Supported Platforms

- ✅ Termux
- ✅ Ubuntu
- ✅ Debian
- ✅ Kali Linux
- ✅ Arch Linux
- ✅ Fedora
- ✅ macOS (Python + Go Installed)

---
# 📌 Notes

- Internet connection is required.
- Make sure **httpx** is installed correctly.
- The tool automatically saves scan results.
- Supports both single targets and bulk input files.
- Supports CIDR-based scanning.
- Large scans may take time depending on network speed.

---

# ⚠ Disclaimer

This project is intended **only for educational purposes and authorized security testing**.

Do not scan or test systems without proper permission.

The developer is **not responsible** for any misuse of this tool.

---

# 📁 Project Structure

```
nscan/
│
├── nscan.py
├── README.md
├── requirements.txt
├── payloads/
├── output/
└── assets/
```

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 🐞 Reporting Bugs

If you find any bug or have suggestions:

- Open an Issue on GitHub
- Contact via Telegram

---

# ⭐ Support

If you like this project, don't forget to:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with your friends

---

# 👨‍💻 Developed By

## **NS Hacker**

Cyber Security Researcher & Python Developer

---

# 📢 Telegram

**Channel:** https://t.me/nscan_script

Stay updated for:

- Latest Tool Updates
- Bug Host Collections
- Payloads
- Security Tips
- New Releases

---

# ❤️ Thank You

Thank you for using **NScan**.

Your support motivates future updates and improvements.

Happy Scanning! 🚀

---

<p align="center">

Made with ❤️ by <b>NS Hacker</b>

</p>

<p align="center">

⭐ Don't forget to Star this Repository ⭐

</p>
