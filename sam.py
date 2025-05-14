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
