# HX711-ESP32

This repository contains a simple program to read weight measurements using the HX711 load cell amplifier with an ESP32 microcontroller.

## Repository

[https://github.com/unreliablecode/HX711-ESP32/](https://github.com/unreliablecode/HX711-ESP32/)

## Description

The program initializes the HX711 sensor and reads weight measurements in a loop. It includes basic calibration to convert the raw measurement to weight.

## Hardware

- ESP32 microcontroller
- HX711 load cell amplifier
- Load cell

## Connections

| HX711 Pin | ESP32 Pin |
|-----------|-----------|
| DT        | GPIO 19   |
| SCK       | GPIO 18   |
| VCC       | 3.3V      |
| GND       | GND       |

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/unreliablecode/HX711-ESP32.git
    cd HX711-ESP32
    ```

2. Install necessary dependencies for your ESP32 environment.

## Usage

1. Connect the HX711 load cell amplifier to the ESP32 as described in the **Connections** section.
2. Upload the code to your ESP32 microcontroller.
3. Open a serial monitor to view the weight measurements.
