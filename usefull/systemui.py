from tkinter import *
import platform
import psutil

class SystemUI:
    def __init__(self, root):
        self.root = root
        root.title("System Information")
        root.geometry("600x500")

        # Create label and text widget to display system information
        Label(root, text="System Information", font=("Helvetica", 20)).pack(pady=20)
        self.system_info = Text(root, height=30, width=60, font=("Helvetica", 14))
        self.system_info.pack(pady=20)

        # Display system information
        self.print_system_info()

    def print_system_info(self):
        system_info = []
        system_info.append("System: {}".format(platform.system()))
        system_info.append("Node Name: {}".format(platform.node()))
        system_info.append("Release: {}".format(platform.release()))
        system_info.append("Version: {}".format(platform.version()))
        system_info.append("Machine: {}".format(platform.machine()))
        system_info.append("Processor: {}".format(platform.processor()))
        system_info.append("Memory: {} GB".format(
            round(psutil.virtual_memory().available / (1024.0 ** 3), 2)))
        system_info.append("Boot Device: {}".format(psutil.boot_time()))
        system_info.append("CPU Cores: {}".format(psutil.cpu_count()))
        system_info.append("CPU Frequency: {} GHz".format(
            round(psutil.cpu_freq().current / 1000.0, 2)))
        system_info.append("CPU Usage: {}%".format(
            psutil.cpu_percent(interval=1)))
        system_info.append("Virtual Memory: {} GB".format(
            round(psutil.virtual_memory().total / (1024.0 ** 3), 2)))
        system_info.append("Swap Memory: {} GB".format(
            round(psutil.swap_memory().total / (1024.0 ** 3), 2)))
        system_info.append("Disk Usage: {} GB".format(
            round(psutil.disk_usage('/').total / (1024.0 ** 3), 2)))
        system_info.append("Device Make: {}".format(platform.python_implementation()))
        system_info.append("Model: {}".format(platform.python_compiler()))
        system_info.append("System Configuration: {}".format(platform.architecture()))
        system_info.append("Storage Information: {}".format(psutil.disk_partitions()))
        system_info.append("Network Information: {}".format(psutil.net_if_addrs()))

        # Insert system information into text widget
        for info in system_info:
            self.system_info.insert(END, info + "\n")

root = Tk()
app = SystemUI(root)
root.mainloop()