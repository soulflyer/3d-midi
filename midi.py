"""Whatever."""
import rtmidi
import config
midiout = rtmidi.RtMidiOut()
ports = range(midiout.getPortCount())
testmessage = rtmidi.MidiMessage.noteOn(config.channel, 100, 120)


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
    """Send pitchbend message in range -8192 t0 8192. Val is -1.0 to 1.0."""
    if val > 0:
        offset = 8191
    else:
        offset = 8192
    message = rtmidi.MidiMessage.pitchWheel(
        config.channel, (offset + (int(val * 8192))))
    midiout.sendMessage(message)


def controller(cc, val):
    """Send cc message in range 0-127."""
    adjusted_value = (abs(int(val * 127)))
    print(f"CC {cc} :{adjusted_value}")
    message = rtmidi.MidiMessage.controllerEvent(
        config.channel, cc, adjusted_value)
    midiout.sendMessage(message)
