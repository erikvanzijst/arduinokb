## Setup

Make sure you have Python 3 installed on your system. To install,
go to [https://www.python.org/downloads/](https://www.python.org/downloads/)

Then install `pyserial` and `pywin32`:

```
C:> pip install pyserial pywin32
```

## Usage

Connect the Arduino.

Now you can start the Python script that will listen for commands
from the Arduino Serial console and it will convert them into
virtual keyboard presses in Windows.

Which ever window has focus will receive these keyboard events.

```
C:\Users\erik\arduinokb> python main.py
Listening for commands from the Arduino.
Now switch to another window to control it...
```