# Description:
# Defines a "Mobile" class that represents a mobile phone with
# attributes for make, model, OS, and color. Includes methods to
# simulate common mobile phone actions such as making or receiving
# calls, streaming videos, and playing games.

class Mobile:
    """A class that represents a mobile phone."""

    def __init__(self, make, model, os, color):
        """
        Initialize the Mobile object with the given attributes.
        Parameters:
        - make: the brand of the mobile phone (e.g., Samsung, Apple)
        - model: the specific model (e.g., Galaxy S24, iPhone 15)
        - os: the operating system version
        - color: the color of the mobile device
        """
        self.make = make
        self.model = model
        self.os = os
        self.color = color

    def make_call(self):
        """Simulate making a phone call."""
        print(f"The {self.make} {self.model} is making a call... ")

    def receive_call(self):
        """Simulate receiving a phone call."""
        print(f"The {self.make} {self.model} is receiving a call... ")

    def stream_video(self):
        """Simulate watching a YouTube video."""
        print(f"The {self.model} running {self.os} is streaming a video on YouTube ")

    def play_game(self):
        """Simulate gaming on the mobile device."""
        print(f"The {self.color} {self.model} is playing a game ")
