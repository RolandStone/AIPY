import psutil
import time

def dashboard():
    print("\033c")  # Clears the terminal
    print("\033[1;35;40mServer Dashboard\033[0m\n")  # Changes text color to purple
    print("\033[1;32;40mConnected peers: \033[0m", psutil.net_connections())  # Changes text color to green
    print("\n\033[1;32;40mRunning commands: \033[0m\n")  # Changes text color to green

    for process in psutil.process_iter():
        print("\033[1;33;40m", process.name(), "\033[0m: \033[1;36;40m", process.cmdline(), "\033[0m")  # Changes text color to yellow

    print("\n\033[1;32;40mCPU utilization: \033[0m \033[1;36;40m", psutil.cpu_percent(), "%\033[0m")  # Changes text color to green and blue
    print("\033[1;32;40mMemory utilization: \033[0m \033[1;36;40m", psutil.virtual_memory().percent, "%\033[0m")  # Changes text color to green and blue
    print("\033[1;32;40mDisk utilization: \033[0m \033[1;36;40m", psutil.disk_usage('/').percent, "%\033[0m")  # Changes text color to green and blue

    print("\n\033[1;32;40mRefreshing in 5 seconds...\033[0m\n")  # Changes text color to green
    time.sleep(5)

while True:
    dashboard()
