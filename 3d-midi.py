"""Functions to translate 3d mouse input to midi."""
import rtmidi
import pyspacemouse
import time
import event
import midi

# Ignore any inputs below this value:
# 0.1 makes it possible to send any axis without (much) noise from the other 5.
sensitivity = 0.1

# Time the callback fns will wait before checking if anything has changed.
sleep = 0.0001

button_arr = [pyspacemouse.ButtonCallback([0], event.button_0),
              pyspacemouse.ButtonCallback([1], event.button_1),]
axis_arr = [pyspacemouse.DofCallback("x",
                                     event.right,
                                     sleep,
                                     event.left,
                                     sensitivity),
            pyspacemouse.DofCallback("y",
                                     event.forward,
                                     sleep,
                                     event.back,
                                     sensitivity),
            pyspacemouse.DofCallback("z",
                                     event.up,
                                     sleep,
                                     event.down,
                                     sensitivity),
            pyspacemouse.DofCallback("roll",
                                     event.roll_right,
                                     sleep,
                                     event.roll_left,
                                     sensitivity),
            pyspacemouse.DofCallback("pitch",
                                     event.pitch_forward,
                                     sleep,
                                     event.pitch_back,
                                     sensitivity),
            pyspacemouse.DofCallback("yaw",
                                     event.yaw_right,
                                     sleep,
                                     event.yaw_left,
                                     sensitivity)]


def main():
    """Listen to the 3d mouse and fire various fns."""
    success_3d = pyspacemouse.open(button_callback_arr=button_arr,
                                   dof_callback_arr=axis_arr)
    port_number = midi.open_midiout_port()
    print(f"Opening {midi.midiout.getPortName(port_number)}")
    midi.midiout.openPort(port_number)
    if success_3d and port_number:
        while True:
            pyspacemouse.read()
            time.sleep(0.001)


main()

