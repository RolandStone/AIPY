import platform
import sys
import subprocess
import psutil

def print_system_info():
    print("Operating System: ", platform.system())
    print("OS Release: ", platform.release())
    print("Python version: ", sys.version)
    print("Machine type: ", platform.machine())
    print("Processor type: ", platform.processor())
    print("Hostname: ", platform.node())
    print("Architecture: ", platform.architecture()[0])
    
    if platform.system() == 'Linux':
        result = subprocess.run(['dmidecode', '-t', 'system'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        lines = output.split("\n")
        for line in lines:
            if "Serial Number" in line:
                print("Serial Number: ", line.split(":")[1].strip())
            elif "Manufacturer" in line:
                print("Vendor: ", line.split(":")[1].strip())
            elif "Product Name" in line:
                print("System Name: ", line.split(":")[1].strip())
            elif "Product" in line:
                print("Device Name: ", line.split(":")[1].strip())

    print("Total Memory: ", psutil.virtual_memory().total / (1024 ** 3), "GB")
    print("Total Swap Memory: ", psutil.swap_memory().total / (1024 ** 3), "GB")
    print("Free Memory: ", psutil.virtual_memory().available / (1024 ** 3), "GB")
    print("Free Swap Memory: ", psutil.swap_memory().free / (1024 ** 3), "GB")
    print("Number of CPU cores: ", psutil.cpu_count())
    print("CPU Frequency: ", psutil.cpu_freq().current, "MHz")
    print("CPU Load: ", psutil.cpu_percent(), "%")
    print("Boot Time: ", psutil.boot_time())
    print("Up Time: ", int(psutil.boot_time()), " seconds")

if __name__ == '__main__':
    print_system_info()
