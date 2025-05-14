# 🔌 connecting_flask_with_arduino

This project demonstrates a simple web interface built with **Flask (Python)** to control an **Arduino** over a **serial connection**. The Arduino listens to commands like `on` and `off` to control an LED (or any digital device) and responds back to the web interface.

---

## 🛠️ Features

- Control Arduino using a web interface.
- Simple HTML interface with ON/OFF buttons.
- Serial port cleanup on app shutdown.

---

## 🧰 Requirements

### Python Side (Flask Web App)

- Python 3.x
- Flask
- PySerial

Install dependencies:

```bash
pip install flask pyserial
