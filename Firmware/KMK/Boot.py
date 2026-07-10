import board
import digitalio
import storage
import usb_cdc

# ---- CHANGE THIS PIN TO YOUR "A" KEY GPIO ----
A_KEY_PIN = board.GP27   # example: row/col pin where A is connected

key = digitalio.DigitalInOut(A_KEY_PIN)
key.direction = digitalio.Direction.INPUT
key.pull = digitalio.Pull.UP

# If A key is held during plug-in → enable USB storage & serial
if not key.value:
    storage.enable_usb_drive()
    usb_cdc.enable(console=True, data=True)
else:
    # Normal keyboard mode → no USB drive, no REPL
    storage.disable_usb_drive()
    usb_cdc.disable()