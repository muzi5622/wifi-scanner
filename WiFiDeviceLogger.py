#!/usr/bin/env python3
import os
import time
import subprocess

LOG_FILE = "wifi_devices_log.txt"

def scan_network():
    try:
        # Use arp-scan to get a list of connected devices
        result = subprocess.run(['arp-scan', '-l'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error scanning network:", e)
        return ""

def parse_scan_results(scan_output):
    devices = []
    lines = scan_output.splitlines()
    
    for line in lines:
        parts = line.split()
        # Ensure there are at least two parts for IP and MAC
        if len(parts) >= 2 and "." in parts[0]:
            ip = parts[0]
            mac = parts[1]
            manufacturer = " ".join(parts[2:]) if len(parts) > 2 else "Unknown"
            devices.append((ip, mac, manufacturer))
    
    return devices

def log_device_event(device, event):
    ip, mac, manufacturer = device
    with open(LOG_FILE, "a") as log_file:
        log_entry = (
            f"Device {event}:\n"
            f"  IP Address: {ip}\n"
            f"  MAC Address: {mac}\n"
            f"  Manufacturer: {manufacturer}\n"
            f"  Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n"
            f"{'-' * 40}\n"
        )
        log_file.write(log_entry)

def update_device_status(current_devices, previous_devices):
    current_macs = {device[1] for device in current_devices}
    previous_macs = {device[1] for device in previous_devices}

    # Detect new devices (currently online but were not in the previous scan)
    new_devices = [device for device in current_devices if device[1] not in previous_macs]

    # Detect returning devices (devices that were offline but now are online again)
    returning_devices = [device for device in current_devices if device[1] in previous_macs]

    # Log new or returning devices
    for device in new_devices:
        log_device_event(device, "Connected (New)")
    for device in returning_devices:
        log_device_event(device, "Reconnected")

    return current_devices  # Update the tracked device list

def display_devices(devices):
    if devices:
        # Print table header
        print(f"{'IP Address':<16} {'MAC Address':<20} {'Manufacturer':<30}")
        print("-" * 66)
        # Print device details in tabular format
        for ip, mac, manufacturer in devices:
            print(f"{ip:<16} {mac:<20} {manufacturer:<30}")
        print()
    else:
        print("No devices found.\n")

if __name__ == "__main__":
    previous_devices = []  # Track previously detected devices

    while True:
        print("Scanning the network...\n")
        scan_output = scan_network()
        current_devices = parse_scan_results(scan_output)
        
        # Display currently connected devices
        display_devices(current_devices)

        # Update the status and log new/returning devices
        previous_devices = update_device_status(current_devices, previous_devices)

        # Wait before scanning again
        time.sleep(30)
