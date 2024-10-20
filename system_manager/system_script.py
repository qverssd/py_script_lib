from __init__ import check_disk_usage, copy_file, check_cpu_usage, check_memory_usage, restart_service

if __name__ == '__main__':
    #Utils usage
    total, used, free = check_disk_usage('/')
    print(f"Disk: {total} GB, Used: {used} GB, Free: {free} GB")

    cpu = check_cpu_usage()
    memory_percent, memory_used, memory_total = check_memory_usage()
    print(f"CPU usage: {cpu}%, Memory: {memory_used}/{memory_total} MB ({memory_percent}%)")
    
    service_name = input("Enter the name of the service to restart: ")
    restart_service(service_name)