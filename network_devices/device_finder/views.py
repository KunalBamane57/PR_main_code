from django.shortcuts import render
import nmap
import subprocess

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
    # This view renders the next page message
    return render(request, 'device_finder/next_page.html')


def attacks_page(request):
    # This view renders the next page message
    return render(request, 'device_finder/attacks.html')