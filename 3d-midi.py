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
    print("Button 0 pressed:", pressed_buttons)


def button_1(state, buttons, pressed_buttons):
    print("Button 1 pressed", pressed_buttons)


def button_0_1(state, buttons, pressed_buttons):
    print("Both buttons pressed:", pressed_buttons)


def someButton(state, buttons):
    print("Some button event")


def callback():
    button_arr = [pyspacemouse.ButtonCallback([0], button_0),
                  pyspacemouse.ButtonCallback([1], button_1),]

    success = pyspacemouse.open(dof_callback=pyspacemouse.print_state,
                                button_callback_arr=button_arr)
    if success:
        while True:
            pyspacemouse.read()
            time.sleep(0.01)


callback()
# output_ports()
# read_spacemouse()
