# Wi-Fi Device Logger

## Overview
The **Wi-Fi Device Logger** is a Python-based script designed to monitor and log the devices connected to your local network. This utility can help you keep track of new devices that join the network and those that reconnect after being offline. It is particularly useful for network administrators, home users wanting to monitor their network, or anyone interested in tracking device activity on their Wi-Fi network.

## Features
- **Automatic Detection**: The script automatically scans your local network and detects when new devices connect, logging their details in real time.
- **Reconnection Logging**: It keeps track of devices that were previously disconnected. When they reconnect, the script logs them along with their connection timestamp.
- **Detailed Logging**: Each log entry includes:
  - **IP Address**: The unique identifier assigned to the device on the network.
  - **MAC Address**: The hardware address of the device, which can be used to identify it uniquely on the network.
  - **Manufacturer**: The manufacturer information derived from the MAC address, giving insight into the type of device.
  - **Timestamp**: The exact date and time of the connection, formatted for clarity.
- **Customizable Scanning Interval**: The scanning interval can be adjusted according to your preferences to ensure timely updates based on network activity.

## Requirements
To run the Wi-Fi Device Logger, ensure you have the following installed on your system:

- **Python 3.x**: The script is written in Python, so you need Python 3 installed. You can download it from the [official Python website](https://www.python.org/downloads/).
- **arp-scan**: This is a command-line tool used to discover devices on the local network. It can be installed via your package manager:
  - For **Debian/Ubuntu**:
    ```bash
    sudo apt-get install arp-scan
    ```
  - For **Fedora**:
    ```bash
    sudo dnf install arp-scan
    ```
  - For **Arch Linux**:
    ```bash
    sudo pacman -S arp-scan
    ```
  - For **macOS** (using Homebrew):
    ```bash
    brew install arp-scan
    ```
## Screenshot
Text File (Lest side) and Terminal (Right side)
![image](https://github.com/user-attachments/assets/7954ce2c-1b9a-4403-a179-e1d4678b6da0)

## Installation

To get started with the Wi-Fi Device Logger, follow these installation steps:

1. **Clone the repository**:
   Open a terminal and run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/muzi5622/wifi-scanner.git
