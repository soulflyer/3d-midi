"""Events fired by inputs from the 3d mouse."""
import midi
import config


def button_0(state, buttons, pressed_buttons):
    """Event fired when button 0 is pressed."""
    print("Button 0 pressed:", pressed_buttons)
    midi.midiout.sendMessage(midi.testmessage)


def button_1(state, buttons, pressed_buttons):
    """Event fired when button 1 is pressed."""
    midi.midiout.sendMessage(midi.testmessage)
    print("Button 1 pressed", pressed_buttons)


def right(value):
    """Event fired on move right."""
    midi.controller(config.right, value)


def left(value):
    """Event fired on move left."""
    midi.controller(config.left, value)


def forward(value):
    """Event fired on move forwards."""
    midi.controller(config.forward, value)


def back(value):
    """Event fired on move backwards."""
    midi.controller(config.back, value)


def up(value):
    """Event fired on move up."""
    midi.controller(config.up, value)


def down(value):
    """Event fired on move down."""
    midi.controller(config.down, value)


def roll_right(value):
    """Event fired on roll_right."""
    midi.controller(config.roll_right, value)


def roll_left(value):
    """Event fired on roll_left."""
    midi.controller(config.roll_left, value)


def pitch_forward(value):
    """Event fired on pitch forward."""
    midi.controller(config.pitch_forward, value)


def pitch_back(value):
    """Event fired on pitch back."""
    midi.controller(config.pitch_back, value)


def yaw_right(value):
    """Event fired on yaw right."""
    # midi.pitchbend(value)
    midi.controller(config.yaw_left, value)


def yaw_left(value):
    """Event fired on yaw left."""
    # midi.pitchbend(value)
    midi.controller(config.yaw_right, value)
