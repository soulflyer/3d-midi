"""Events fired by inputs from the 3d mouse."""
import rtmidi
import midi
import time
import pyspacemouse


def button_0(state, buttons, pressed_buttons):
    """Event fired when button 0 is pressed."""
    print("Button 0 pressed:", pressed_buttons)
    midi.midiout.sendMessage(midi.testmessage)


def button_1(state, buttons, pressed_buttons):
    """Event fired when button 1 is pressed."""
    midi.midiout.sendMessage(midi.testmessage)
    print("Button 1 pressed", pressed_buttons)


def right(axis):
    """Event fired on move right."""
    # message = rtmidi.MidiMessage.controllerEvent(1, 100, int(axis * 127))
    # midi.midiout.sendMessage(message)
    # print(f"Right: {axis}")


def left(axis):
    """Event fired on move left."""
    # print(f"Left: {axis}")


def forward(axis):
    """Event fired on move forwards."""
    #print(f"Forward: {axis}")


def back(axis):
    """Event fired on move backwards."""
    #print(f"Back: {axis}")


def up(axis):
    """Event fired on move up."""
    #print(f"Up: {axis}")


def down(axis):
    """Event fired on move down."""
    #print(f"Down: {axis}")


def roll_right(axis):
    """Event fired on roll_right."""
    # print(f"Roll right: {axis}")


def roll_left(axis):
    """Event fired on roll_left."""
    # print(f"Roll left: {axis}")


def pitch_forward(axis):
    """Event fired on pitch forward."""
    # print(f"Pitch forward: {axis}")


def pitch_back(axis):
    """Event fired on pitch back."""
    # print(f"Pitch back: {axis}")


def yaw_right(axis):
    """Event fired on yaw right."""
    midi.pitchbend(axis)
    print(f"Yaw right: {axis}")


def yaw_left(axis):
    """Event fired on yaw left."""
    midi.pitchbend(axis)
    print(f"Yaw left: {axis}")
