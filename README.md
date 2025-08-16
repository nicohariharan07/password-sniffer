 🔐 Password Sniffer Simulation (Educational Project)

## 📌 Overview
This project demonstrates how unencrypted network protocols (like HTTP) expose sensitive information such as **usernames and passwords**.  

We simulate a login system using **Flask** and build a simple **network sniffer** using **Scapy** to capture credentials transmitted over the network.

⚠️ **Disclaimer:**  
This project is for **educational purposes only**. Do not run on real networks. Always test inside a **lab environment** (your own computer/VM).

---

## 🛠 Features
- Simple Flask-based login page (HTTP, no encryption).
- Python packet sniffer using Scapy.
- Detects and extracts `username` and `password` fields from HTTP POST data.
- Demonstrates why HTTPS/SSH is critical for security.

---

## 📂 Project Structure

├── web_server.py    # Fake login web server (Flask) ├── sniffer.py       # Network sniffer using Scapy └── README.md        # Documentation

---

## 🚀 Setup Instructions

### 1. Install Requirements
```bash
sudo apt update
sudo apt install python3-pip
pip3 install flask scapy

2. Start the Fake Login Server

python3 web_server.py

Visit: http://127.0.0.1:8080 in your browser and submit a test username & password.
Example: alice / 1234

3. Run the Sniffer (in another terminal)

sudo python3 sniffer.py

4. Test Login Capture

Submit the login form again or use:

curl -d "username=alice&password=1234" http://127.0.0.1:8080/login

The sniffer will capture:

[*] Captured: username=alice&password=1234


---




---

🔮 Future Improvements

Save captured credentials into a log file.

Add FTP/Telnet packet sniffing.

Build a dashboard to visualize captured credentials.

Extend to demonstrate HTTPS (sniffer won’t see credentials).



---

📜 License

MIT License – free to use for learning & research only.
Unauthorized real-world use is strictly prohibited.
