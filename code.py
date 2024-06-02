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
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


for pin in (board.RING_2, board.SLEEVE):
    digitalio.DigitalInOut(pin).switch_to_output(False)

keys = keypad.Keys((board.TIP, board.RING_1), value_when_pressed=False)
keycode_map = [Keycode.LEFT_CONTROL, Keycode.RIGHT_CONTROL]
actuation_map = {True: Keyboard.press, False: Keyboard.release}

kbd = Keyboard(usb_hid.devices)
while True:
    event = keys.events.get()
    if event:
        keycode = keycode_map[event.key_number]
        actuation_map[event.pressed](kbd, keycode)
