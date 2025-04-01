"""Events fired by inputs from the 3d mouse."""


def button_0(state, buttons, pressed_buttons):
    """Event fired when button 0 is pressed."""
    print("Button 0 pressed:", pressed_buttons)


def button_1(state, buttons, pressed_buttons):
    """Event fired when button 1 is pressed."""
    print("Button 1 pressed", pressed_buttons)


def right(state, axis):
    """Event fired on move right."""
    print(f"Right: {axis}")


def left(state, axis):
    """Event fired on move left."""
    print(f"Left: {axis}")


def forward(state, axis):
    """Event fired on move forwards."""
    print(f"Forward: {axis}")


def back(state, axis):
    """Event fired on move backwards."""
    print(f"Back: {axis}")


def up(state, axis):
    """Event fired on move up."""
    print(f"Up: {axis}")


def down(state, axis):
    """Event fired on move down."""
    print(f"Down: {axis}")


def roll_right(state, axis):
    """Event fired on roll_right."""
    print(f"Roll right: {axis}")


def roll_left(state, axis):
    """Event fired on roll_left."""
    print(f"Roll left: {axis}")


def pitch_forward(state, axis):
    """Event fired on pitch forward."""
    print(f"Pitch forward: {axis}")


def pitch_back(state, axis):
    """Event fired on pitch back."""
    print(f"Pitch back: {axis}")


def yaw_right(state, axis):
    """Event fired on yaw right."""
    print(f"Yaw right: {axis}")


def yaw_left(state, axis):
    """Event fired on yaw left."""
    print(f"Yaw left: {axis}")
