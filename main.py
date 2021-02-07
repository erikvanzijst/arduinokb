import win32api
from serial import Serial
from serial.tools import list_ports
from time import sleep

USB_PRODUCT = 'arduino'
USB_MANUFACTURER = 'arduino'


def readcmd(port):
    cmd = ''
    while '\r\n' not in cmd:
      cmd += port.read(1).decode('ascii')
    return cmd.rstrip()


if __name__ == '__main__':
    try:
        # attempt to autodetect the Arduino
        dev = next(filter(lambda p: p.product and USB_PRODUCT in p.product.lower() or
                                    p.manufacturer and USB_MANUFACTURER in p.manufacturer.lower(),
                          list_ports.comports())).device
    except StopIteration:
        print('Cannot find Arduino. If it is connected, specify the port '
              'manually.')
        exit(1)
    else:
        port = Serial(port=dev, baudrate=9600, timeout=30)
        sleep(2)    # wait for the COM port to open

        print('Listening for commands from the Arduino.')
        print('Now switch to another window to control it...')
        while True:
            cmd = readcmd(port).lower()
            print('cmd: ' + cmd)

            # Full list of keyboard scan codes:
            # https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
            if cmd == 'up':
                win32api.keybd_event(0x26, 0)  # up
            elif cmd == 'down':
                win32api.keybd_event(0x28, 0)  # down
            elif cmd == 'left':
                win32api.keybd_event(0x25, 0)  # left
            elif cmd == 'right':
                win32api.keybd_event(0x27, 0)  # right
            elif cmd == 'space':
                win32api.keybd_event(0x20, 0)  # space
            elif cmd == 'ctrl':
                win32api.keybd_event(0x11, 0)       # ctrl press
                win32api.keybd_event(0x11, 0, 0x2)  # ctrl release
            else:
                print('Unknown key: %s' % cmd)
