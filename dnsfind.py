from prettytable import PrettyTable
from ping3 import ping

# Colors for beautiful output.
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

dns_servers = {
    "Google DNS": ["8.8.8.8", "8.8.4.4"],
    "Cloudflare DNS": ["1.1.1.1", "1.0.0.1"],
    "OpenDNS": ["208.67.222.222", "208.67.220.220"],
    "Quad9 DNS": ["9.9.9.9", "149.112.112.112"],
    "Comodo Secure DNS": ["8.26.56.26", "8.20.247.20"],
    "Verisign DNS": ["64.6.64.6", "64.6.65.6"],
    "DNS.Watch": ["84.200.69.80", "84.200.70.40"],
    "CleanBrowsing DNS": ["185.228.168.9", "185.228.169.9"],
    "Yandex DNS": ["77.88.8.8", "77.88.8.1"],
    "OpenNIC": ["185.121.177.177", "169.239.202.202"],
    "FreeDNS": ["37.235.1.174", "37.235.1.177"],
    "Level3 DNS": ["4.2.2.1", "4.2.2.2"],
    "Mediacom DNS": ["24.153.128.10", "24.153.128.11"],
    "AT&T DNS": ["68.94.156.1", "68.94.157.1"],
    "Verizon DNS": ["4.2.2.1", "4.2.2.2"]
}

dns_results = {}
output_names = []
output_pings = []
non_reachable = []
for i in dns_servers.keys():
	print("Pinging",f'{GREEN}{i}{RESET}'," Server")
	result = ping((dns_servers[i])[0], unit='ms')
	if result is None:
		non_reachable.append(i)
		print(f"{RED}{i} server is not reachable.{RESET}")
	else:
		output_names.append(i)
		output_pings.append(round(result,4))

asc_pings = sorted(output_pings)

print("{BLUE}Your best options are listed below from best to worst.......{RESET}")

f_table = PrettyTable()
f_table.field_names = ["Rank","Server Name","Primary DNS Add.","Secondary DNS Add.","Ping(ms)"]
# Find Lowest Ping Now
for i in range(0,len(asc_pings)):
	for k in range(0,len(output_pings)):
		if asc_pings[i] == output_pings[k]:
			f_table.add_row([i+1,output_names[k],(dns_servers[output_names[k]])[0],(dns_servers[output_names[k]])[1],asc_pings[i]])
print(f_table)
print(non_reachable)
print("Thanks for Using !!")
print("P.S.: This test only hands you the latencies not a detailed specification about the actual benfits using one DNS resolver over the other !")

