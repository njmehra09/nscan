# 🚀 nscan - Fast Bug Host Discovery & Network Recon Tool

`nscan` ek power-packed Python script hai jo Network Reconnaissance, Bug Host Discovery, active /16 subnets tracking aur Payload Generation ko ek hi seamless interactive terminal interface me combine karti hai. Isme ProjectDiscovery ke `httpx` ka backend use kiya gaya hai taaki scanning ki accuracy aur speed pro-level ho.

---

## ⚡ Features
* **Bug Host Discovery:** Perfect table layout ke sath HTTP/S live hosts, status codes, aur server/technology banner detection (80, 443, 8443 by default).
* **Reverse IP Lookup:** Single IP, file list ya poori CIDR range par fast mass reverse DNS lookup.
* **Active Subnet Finder:** Dual-Node Routing Matrix ka use karke kisi bhi main block ke active `/16` subnets (`.0.1` aur `.1.1`) ko instantly check aur filter karna.
* **Payload Generator:** Instant working CDN/Websocket payloads generate karna.

---

## 🛠️ Requirements & Dependencies
Yeh tool backend me command-line utilities ka use karta hai, isliye iske smoothly chalne ke liye niche diye gaye packages ka hona zaroori hai:
* **Python 3.x**
* **Git**
* **Golang** (ProjectDiscovery `httpx` ko compile karne ke liye)
* **httpx** (ProjectDiscovery Go-binary tool)

---

## 🚀 Installation & Setup Steps (One by One)

Agar aap is tool ko pehli baar setup kar rahe hain, toh aap niche diye gaye steps ko ek-ek karke run karein:

### 🔹 Step 1: System Packages ko Update karein
```bash
pkg update -y && pkg upgrade -y