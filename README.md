# PyMorseTrin - A Morse Key/Paddle USB interface for Adafruit TRRS Trinkey in Python 

## Overview

This project enables using [Adafruit TRRS
Trinkey](https://www.adafruit.com/product/5954) as a USB interface for Morse
keys and paddles.

## Installation

- Flash Adafruit TRRS Trinkey with
[CircuitPython](https://circuitpython.org/board/adafruit_trrs_trinkey_m0/).
- Copy `code.py` to the USB volume

## Behavior

The code expects the Tip to be connected to the Dah paddle and the Ring 1 to be
connected to the Dit paddle. Ring 2 and Sleeve are used as ground.

By default, Dah emits `LEFT_CONTROL` and Dit emits `RIGHT_CONTROL`.
