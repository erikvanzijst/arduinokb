typedef struct {
  const unsigned int pin;
  int currState;  // the current reading from the input pin
  int lastState;  // the previous reading from the input pin
  unsigned long lastChanged;
  unsigned long lastDebounce;
} Button;
const unsigned long debounceDelay = 50;

bool waspressed(Button *button) {
  const int value = digitalRead(button->pin);
  if (value != button->lastState) {
    button->lastDebounce = millis();
    button->lastState = value;
  }

  if ((millis() - button->lastDebounce) > debounceDelay && value != button->currState) {
    button->currState = value;
    button->lastChanged = millis();
    if (button->currState == HIGH) {
      return true;
    }
  }
  return false;
}

Button LEFT   = {A1, LOW, LOW, 0, 0};
Button RIGHT  = {A3, LOW, LOW, 0, 0};
Button UP     = {A2, LOW, LOW, 0, 0};
Button DOWN   = {A0, LOW, LOW, 0, 0};
Button CTRL   = {A4, LOW, LOW, 0, 0};

void setup() {
  pinMode(UP.pin, INPUT);
  pinMode(DOWN.pin, INPUT);
  pinMode(LEFT.pin, INPUT);
  pinMode(RIGHT.pin, INPUT);
  pinMode(CTRL.pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  
  if (waspressed(&UP)) {
    Serial.println("up");
  }
  if (waspressed(&DOWN)) {
    Serial.println("down");
  }
  if (waspressed(&LEFT)) {
    Serial.println("left");
  }
  if (waspressed(&RIGHT)) {
    Serial.println("right");
  }
  if (waspressed(&CTRL)) {
    Serial.println("space");
  }
}
