# Copyright 2024 Praveen R Kumar, N6PRK.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import board
import digitalio
import keypad
import neopixel_write
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


class Emitter:
    """Emits keycodes and controls the neopixel."""

    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)
        self.keycodes = [Keycode.LEFT_CONTROL, Keycode.RIGHT_CONTROL]

        self.pixel = digitalio.DigitalInOut(board.NEOPIXEL)
        self.pixel.direction = digitalio.Direction.OUTPUT
        self.pixel_state = 0
        self.pixel_colors = [
            bytearray([0, 0, 0]),
            bytearray([0xFF, 0, 0]),
            bytearray([0, 0, 0xFF]),
            bytearray([0, 0xFF, 0]),
        ]

        self.actions = {True: self._pressed, False: self._released}

    def emit(self, key_number, pressed):
        """Emits the keycode for the given key and controls the neopixel."""
        self.actions[pressed](key_number)
        neopixel_write.neopixel_write(self.pixel, self.pixel_colors[self.pixel_state])

    def _pressed(self, key_number):
        keycode = self.keycodes[key_number]
        self.kbd.press(keycode)
        self.pixel_state += key_number + 1

    def _released(self, key_number):
        keycode = self.keycodes[key_number]
        self.kbd.release(keycode)
        self.pixel_state -= key_number + 1


def main():
    for pin in (board.RING_2, board.SLEEVE):
        digitalio.DigitalInOut(pin).switch_to_output(False)
    keys = keypad.Keys((board.TIP, board.RING_1), value_when_pressed=False)
    emitter = Emitter()
    while True:
        event = keys.events.get()
        if event:
            emitter.emit(event.key_number, event.pressed)


main()
