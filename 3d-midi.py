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


output_ports()
read_spacemouse()
