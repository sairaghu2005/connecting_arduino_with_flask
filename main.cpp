const int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "on") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    }
    else if (command == "off") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    }
    else {
      Serial.println("Invalid command");
    }
  }
}
