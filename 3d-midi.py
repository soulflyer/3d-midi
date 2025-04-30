"""Functions to read 3d mouse input."""
import pyspacemouse
import time
import event
import midi

# Ignore any inputs below this value:
# 0.1 makes it possible to send any axis without (much) noise from the other 5.
sensitivity = 0.1

# Time the callback fns will wait before checking if anything has changed.
sleep = 0.001

button_arr = [pyspacemouse.ButtonCallback([0], event.button_0),
              pyspacemouse.ButtonCallback([1], event.button_1),]


def main():
    """Poll for the 6 axes, and callbackfor the buttons."""
    success = pyspacemouse.open(button_callback_arr=button_arr)
    port_number = midi.open_midiout_port()
    print(f"Opening {midi.midiout.getPortName(port_number)}")
    midi.midiout.openPort(port_number)
    stored_state = pyspacemouse.read()
    print(stored_state)
    print(stored_state.buttons[0])
    if success and port_number:
        while 1:
            state = pyspacemouse.read()
            if (state.x != stored_state.x):
                if (state.x >= 0):
                    event.right(state.x)
                if (state.x <= 0):
                    event.left(state.x)
            if (state.y != stored_state.y):
                if (state.y >= 0):
                    event.forward(state.y)
                if (state.y <= 0):
                    event.back(state.y)
            if (state.z != stored_state.z):
                if (state.z >= 0):
                    event.up(state.z)
                if (state.y <= 0):
                    event.down(state.z)
            # if (state.pitch != stored_state.pitch):
            #     print("p ", state.pitch)
            # if (state.roll != stored_state.roll):
            #     print("r ", state.roll)
            # if (state.yaw != stored_state.yaw):
            #     print("y ", state.yaw)
            stored_state = state
            # print(state.x, state.y, state.z, state.roll, state.pitch, state.yaw)
            time.sleep(0.01)


main()
