import psutil

#Checking CPU and Memory Usage
def check_system_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    print(f"CPU usage: {cpu_percent}%")
    print(f"Memory usage: {memory_info.percent}% ({memory_info.used // (2**20)} MB from {memory_info.total // (2**20)})")