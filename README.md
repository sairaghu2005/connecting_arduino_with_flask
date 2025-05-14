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


pip install flask pyserial
```bash
#flask code
from flask import Flask, render_template, request
import serial
import time
import atexit

app = Flask(__name__)

# Open serial port once
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        if 'on' in request.form:
            ser.write(b'on\n')
            message = ser.readline().decode().strip()
        elif 'off' in request.form:
            ser.write(b'off\n')
            message = ser.readline().decode().strip()
    return render_template('health.html', message=message)

# Close serial when Flask app exits
def close_serial():
    if ser.is_open:
        ser.close()

atexit.register(close_serial)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

