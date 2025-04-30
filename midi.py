import rtmidi
import midi
midiout = rtmidi.RtMidiOut()
ports = range(midiout.getPortCount())
channel = 11
testmessage = rtmidi.MidiMessage.noteOn(channel, 100, 120)


def output_ports():
    """List output ports."""
    for i in ports:
        print(f"{i}: {midiout.getPortName(i)}")


def open_midiout_port():
    """Check available ports and open users selection."""
    output_ports()
    port_number = int(input('enter port number '))
    return port_number


def pitchbend(val):
    """Send a pitchbend message. Val is in the range -1.0 to 1.0."""
    if val > 0:
        offset = 8191
    else:
        offset = 8192
    message = rtmidi.MidiMessage.pitchWheel(
        midi.channel, (offset + (int(val * 8192))))
    midi.midiout.sendMessage(message)
