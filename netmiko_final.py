from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.181"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}

def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show run", use_textfsm=True)
        for status in result:
            if status["interface"].startswith("GigabitEthernet"):
                interface_status = status["status"]
                if interface_status == "up":
                    up += 1
                elif interface_status == "down":
                    down += 1
                elif interface_status == "administratively down":
                    admin_down += 1
        ans = f"Up: {up}, Down: {down}, Admin Down: {admin_down}"
        pprint(ans)
        return ans
