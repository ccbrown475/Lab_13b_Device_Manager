import json
import tkinter as tk

# Load the existing device data.
with open("network_devices.json", "r") as file:
    devices = json.load(file)


# Create the main program window.
window = tk.Tk()
window.title("Network Device Viewer")
window.geometry("400x600")


def show_device():
    """Display the first device stored in the JSON data."""
    device = devices[0]

    output = f"""
Name: {device['Name']}
IP: {device['IP']}
MAC: {device['MAC']}
RAM: {device['RAM']}
SSD: {device['SSD_Size']}
Free Space: {device['Free_Space']}
"""

    label.config(text=output)


def save_data():
    """Save the updated list of devices to the JSON file."""
    with open("network_devices.json", "w") as file:
        json.dump(devices, file, indent=4)


def add_device():
    """Create a new device from the Entry fields and save it."""
    new_device = {
        "Name": name_entry.get(),
        "IP": ip_entry.get(),
        "MAC": mac_entry.get(),
        "RAM": ram_entry.get(),
        "SSD_Size": ssd_entry.get(),
        "Free_Space": free_space_entry.get()
    }

    devices.append(new_device)
    save_data()

    label.config(
        text=f"Device added successfully: {new_device['Name']}"
    )

def show_all_devices():
    output = ""

    for device in devices:
        output += f"{device['Name']} - {device['IP']}\n"

    label.config(text=output)

def update_device():
    target_name = name_entry.get()
    device_found = False

    for device in devices:
        if device["Name"] == target_name:
            device["IP"] = ip_entry.get()
            device["MAC"] = mac_entry.get()
            device["RAM"] = ram_entry.get()
            device["SSD_Size"] = ssd_entry.get()
            device["Free_Space"] = free_space_entry.get()

            device_found = True
            break

    if device_found:
        save_data()
        label.config(
            text=f"Device updated successfully: {target_name}\n"
                 f"New IP: {ip_entry.get()}"
        )
    else:
        label.config(text=f"Device not found: {target_name}")
def delete_device():
    target_name = name_entry.get()

    global devices
    original_count = len(devices)

    devices = [
        device for device in devices
        if device["Name"] != target_name
    ]

    if len(devices) < original_count:
        save_data()
        label.config(text=f"Device deleted successfully: {target_name}")
    else:
        label.config(text=f"Device not found: {target_name}")

# Input fields.
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="IP Address:").pack()
ip_entry = tk.Entry(window)
ip_entry.pack()

tk.Label(window, text="MAC Address:").pack()
mac_entry = tk.Entry(window)
mac_entry.pack()

tk.Label(window, text="RAM:").pack()
ram_entry = tk.Entry(window)
ram_entry.pack()

tk.Label(window, text="SSD Size:").pack()
ssd_entry = tk.Entry(window)
ssd_entry.pack()

tk.Label(window, text="Free Space:").pack()
free_space_entry = tk.Entry(window)
free_space_entry.pack()


# Buttons.
show_button = tk.Button(
    window,
    text="Show Device",
    command=show_device
)
show_button.pack(pady=10)

add_button = tk.Button(
    window,
    text="Add Device",
    command=add_device
)
add_button.pack()

view_button = tk.Button(
    window,
    text="View All Devices",
    command=show_all_devices
)
view_button.pack(pady=10)

update_button = tk.Button(
    window,
    text="Update Device",
    command=update_device
)
update_button.pack()

delete_button = tk.Button(
    window,
    text="Delete Device",
    command=delete_device
)
delete_button.pack()

# Output label.
label = tk.Label(window, text="")
label.pack(pady=10)


window.mainloop()