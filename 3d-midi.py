"""Functions to translate 3d mouse input to midi."""
import rtmidi
import pyspacemouse
import time


def read_spacemouse():
    """Output values from the spacemouse."""
    success = pyspacemouse.open(dof_callback=pyspacemouse.print_state,
                                button_callback=pyspacemouse.print_buttons)
    if success:
        while 1:
            pyspacemouse.read()
            time.sleep(0.01)


def output_ports():
    """List output ports."""
    midiout = rtmidi.RtMidiOut()
    ports = range(midiout.getPortCount())
    for i in ports:
        print(f"{i}: {midiout.getPortName(i)}")


def button_0(state, buttons, pressed_buttons):
    """Event fired when button 0 is pressed."""
    print("Button 0 pressed:", pressed_buttons)


def button_1(state, buttons, pressed_buttons):
    """Event fired when button 1 is pressed."""
    print("Button 1 pressed", pressed_buttons)


def x_axis(state, axis):
    """Event fired when x-axis moves."""
    print(f"X-axis: {axis}")


def y_axis(state, axis):
    """Event fired when y-axis moves."""
    print(f"Y-axis: {axis}")


def z_axis(state, axis):
    """Event fired when z-axis moves."""
    print(f"Z-axis: {axis}")


def roll(state, axis):
    """Event fired on roll."""
    print(f"Roll: {axis}")


def pitch(state, axis):
    """Event fired on pitch."""
    print(f"Pitch: {axis}")


def yaw(state, axis):
    """Event fired on yaw."""
    print(f"Yaw: {axis}")


# Ignore any inputs below this value:
# 0.8 makes it possible to send any axis without (much) noise from the other 5.
sensitivity = 0.08


def main():
    """Listen to the 3d mouse and fire various fns."""
    button_arr = [pyspacemouse.ButtonCallback([0], button_0),
                  pyspacemouse.ButtonCallback([1], button_1),]
    axis_arr = [pyspacemouse.DofCallback("x",
                                         x_axis,
                                         0.0001,
                                         x_axis,
                                         sensitivity),
                pyspacemouse.DofCallback("y",
                                         y_axis,
                                         0.0001,
                                         y_axis,
                                         sensitivity),
                pyspacemouse.DofCallback("z",
                                         z_axis,
                                         0.0001,
                                         z_axis,
                                         sensitivity),
                pyspacemouse.DofCallback("roll",
                                         roll,
                                         0.0001,
                                         roll,
                                         sensitivity),
                pyspacemouse.DofCallback("pitch",
                                         pitch,
                                         0.0001,
                                         pitch,
                                         sensitivity),
                pyspacemouse.DofCallback("yaw",
                                         yaw,
                                         0.0001,
                                         yaw,
                                         sensitivity)]

    success = pyspacemouse.open(button_callback_arr=button_arr,
                                dof_callback_arr=axis_arr)
    if success:
        while True:
            pyspacemouse.read()
            time.sleep(0.001)


main()
# output_ports()
# read_spacemouse()
