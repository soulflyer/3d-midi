import rtmidi
midiout = rtmidi.RtMidiOut()
ports = range(midiout.getPortCount())
testmessage = rtmidi.MidiMessage.noteOn(1, 100, 120)


def output_ports():
    """List output ports."""
    for i in ports:
        print(f"{i}: {midiout.getPortName(i)}")


def open_midiout_port():
    """Check available ports and open users selection."""
    output_ports()
    port_number = int(input('enter port number '))
    return port_number
