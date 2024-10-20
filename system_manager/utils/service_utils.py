import subprocess

#Restarting the service
def restart_service(service_name):
    try:
        subprocess.run(['systemctl', 'restart', service_name], check=True)
        print(f"Service {service_name} was successfully restarted.")
    except subprocess.CalledProcessError as e:
        print(f"Error when restarting service: {e}")