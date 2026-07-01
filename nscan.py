import os
import socket
import subprocess
import concurrent.futures
import re
import ipaddress
from datetime import datetime

# Basic Color Codes for Layout
G = '\033[32m' # Green
C = '\033[36m' # Cyan
Y = '\033[33m' # Yellow
R = '\033[31m' # Red
W = '\033[0m'  # White

ORANGE = '\033[38;5;208m'
PURPLE = '\033[35m'
BLUE   = '\033[34m'
LIGHT_BLUE = '\033[94m'

def clear_screen():
    os.system('clear')

def get_banner():
    print(f"""{C}
███╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{W}""")

    print(f"{Y}           Fast Network Reconnaissance Toolkit{W}")
    print(f"{C}{'='*58}{W}")
    print(f"{G} Version   :{W} v1.1.0")
    print(f"{G} Developer :{W} NS Hacker")
    print(f"{G} Engine    :{W} ProjectDiscovery httpx")
    print(f"{G} Platform  :{W} Termux / Linux")
    print(f"{G} Telegram  :{W} https://t.me/nscan_script")
    print(f"{C}{'='*58}{W}")

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'(?:\x1B[@-_][0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def get_tech_colored_string(tech_string):
    if not tech_string or tech_string == "unknown": return f"{W}unknown"
    parts = [p.strip() for p in tech_string.split(",")]
    colored_parts = []
    for p in parts:
        p_low = p.lower()
        if "cloudflare" in p_low: colored_parts.append(f"{G}{p}{W}")
        elif "gws" in p_low or "apache" in p_low: colored_parts.append(f"{ORANGE}{p}{W}")
        elif "google" in p_low or "php" in p_low: colored_parts.append(f"{PURPLE}{p}{W}")
        elif "nginx" in p_low: colored_parts.append(f"{LIGHT_BLUE}{p}{W}")
        else: colored_parts.append(f"{C}{p}{W}")
    return ", ".join(colored_parts)

def run_httpx_and_format_table(cmd, folder_name):
    print(f"\n{C}+--------------------+------+--------+-------------------------------+{W}")
    print(f"{C}| {'IP / Host / URL':<18} | {'Port':<4} | {'Status':<6} | {'Server / Technology':<29} |{W}")
    print(f"+--------------------+------+--------+-------------------------------+{W}")
    
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None: break
            raw_line = line.strip()
            if raw_line and not raw_line.startswith("[WRN]") and "projectdiscovery.io" not in raw_line:
                clean_raw_line = strip_ansi_codes(raw_line)
                url_match = re.match(r'^(https?://[^\s\[]+)', clean_raw_line)
                if not url_match: continue
                url = url_match.group(1)
                
                clean_url = url.replace("https://", "").replace("http://", "")
                port = "80" if url.startswith("http://") else "443"
                if ":" in clean_url: clean_url, port = clean_url.split(":", 1)
                
                brackets = re.findall(r'\[([^\]]+)\]', clean_raw_line)
                if brackets:
                    status_num = brackets[0].split()[0]
                    tech_list = brackets[1:]
                    tech_filtered = [t.strip() for t in tech_list if not any(x in t.lower() for x in ["moved", "forbidden", "found", "redirect", "bad request", "not found"])]
                    server_name = ", ".join(tech_filtered) if tech_filtered else "unknown"
                else:
                    status_num = "200"
                    server_name = "unknown"
                    tech_filtered = []
                
                url_display = clean_url[:18]
                if status_num == "200": sc_color = G
                elif status_num in ["301", "302", "401", "403"]: sc_color = Y
                else: sc_color = R
                
                colored_server_display = get_tech_colored_string(server_name[:29])
                raw_srv_len = len(server_name[:29])
                padding_space = " " * (29 - raw_srv_len) if raw_srv_len < 29 else ""
                
                print(f"| {W}{url_display:<18} | {C}{port:<4}{W} | {sc_color}{status_num:<6}{W} | {colored_server_display}{padding_space} |")
                
                main_server = tech_filtered[0].split(",")[0].strip() if tech_filtered else "unknown"
                safe_file_name = "".join(c for c in main_server if c.isalnum() or c in ('-', '_')).lower()
                if not safe_file_name: safe_file_name = "unknown"
                
                file_path = os.path.join(folder_name, f"{safe_file_name}.txt")
                with open(file_path, "a") as f:
                    f.write(f"{clean_url} | Port: {port} | Status: {status_num} | Server: {server_name}\n")
        process.wait()
    except Exception as e:
        print(f"{R}[-] Error: {e}{W}")
    print(f"{C}+--------------------+------+--------+-------------------------------+{W}")

def bug_host_scan():
    print(f"\n{G}[1]{W} Scan from File (e.g. ips.txt)")
    print(f"{G}[2]{W} Scan direct CIDR (e.g. 52.0.0.0/16)")
    sub_opt = input(f"\n{C}Selection > {W}")
    port_input = input(f"\n{Y}[?]{W} Ports (Default: 80,443,8443): ")
    port = port_input if port_input else "80,443,8443"
    threads = input(f"{Y}[?]{W} Threads (Default: 100): ")
    if not threads: threads = "100"
    
    folder_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"scan_results_{folder_timestamp}"
    os.makedirs(folder_name, exist_ok=True)

    if sub_opt == '1':
        file_path = input(f"{Y}[?]{W} Enter File Name: ")
        if os.path.exists(file_path): cmd = f"httpx -l {file_path} -p {port} -t {threads} -sc -server -td"
        else: print(f"{R}[!] File nahi mili!{W}"); return
    else:
        cidr = input(f"{Y}[?]{W} Enter CIDR Range: ")
        cmd = f"echo {cidr} | httpx -p {port} -t {threads} -sc -server -td"

    run_httpx_and_format_table(cmd, folder_name)

def reverse_worker(ip):
    try:
        host = socket.gethostbyaddr(str(ip))[0]
        return (str(ip), host)
    except: return (str(ip), "N/A")

def mass_reverse_dns():
    print(f"\n{G}[1]{W} Scan from File / Single IP\n{G}[2]{W} Scan direct CIDR Range")
    rev_opt = input(f"\n{C}Selection > {W}")
    ips = []
    if rev_opt == '1':
        target = input(f"\n{Y}[?]{W} File name ya IP enter karein: ")
        if os.path.exists(target):
            with open(target, 'r') as f: ips = [line.strip() for line in f if line.strip()]
        else: ips = [target]
    elif rev_opt == '2':
        cidr_input = input(f"\n{Y}[?]{W} Enter CIDR Range: ")
        try:
            network = ipaddress.ip_network(cidr_input, strict=False)
            ips = [str(ip) for ip in network.hosts()]
        except Exception as e: print(f"{R}[!] Error: {e}{W}"); return

    if not ips: return
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(reverse_worker, ips))
    
    output_file = f"reverse_dns_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, "w") as f:
        for ip, host in results:
            if host != "N/A":
                print(f"| {G}{ip:<15}{W} | {W}{host:<43} |")
                f.write(f"IP: {ip} | Host: {host}\n")

def stable_connect(ip):
    """Balanced timeout for unstable zero-data networks"""
    for port in [80, 443]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.8)
            result = sock.connect_ex((ip, port))
            sock.close()
            if result == 0: return True
        except: pass
    return False

def subnet_smart_worker(subnet_base):
    """Checks both classic .0.1 and gateway .1.1 sequentially to bypass routing drops"""
    if stable_connect(f"{subnet_base}.0.1"):
        return subnet_base, True, f"{subnet_base}.0.1"
    if stable_connect(f"{subnet_base}.1.1"):
        return subnet_base, True, f"{subnet_base}.1.1"
    return subnet_base, False, None

def active_subnet_finder():
    print(f"\n{Y}[*] Kaun sa block filter karna hai? (e.g. 56, 52){W}")
    block_input = input(f"{C}Enter Main Block > {W}").strip()
    if not block_input: return
        
    print(f"{C}[*] Checking 256 subnets with Dual-Node Routing Matrix...{W}")
    subnet_bases = [f"{block_input}.{i}" for i in range(256)]
    active_subnets = []
    
    print(f"\n{C}+-------------------+-------------------+--------+{W}")
    print(f"{C}| {'Live Subnet Range':<17} | {'Sample IP Responded':<17} | {'HTTP/S':<6} |{W}")
    print(f"+-------------------+-------------------+--------+{W}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(subnet_smart_worker, subnet_bases)
        for base, is_alive, matched_ip in results:
            subnet_range = f"{base}.0.0/16"
            if is_alive:
                print(f"| {G}{subnet_range:<17}{W} | {W}{matched_ip:<17} | {G}{'LIVE':<6}{W} |")
                active_subnets.append(subnet_range)

    print(f"{C}+-------------------+-------------------+--------+{W}")
    if active_subnets:
        filename = f"verified_subnets_{block_input}.txt"
        with open(filename, "w") as f:
            for sub in active_subnets: f.write(f"{sub}\n")
        print(f"\n{G}[✓] Filter Complete! {len(active_subnets)} active ranges captured and saved in '{filename}'{W}\n")
    else:
        print(f"\n{R}[-] Koi response nahi mila. Stable connectivity check karein.{W}\n")

def payload_gen():
    host = input(f"\n{Y}[?]{W} Hostname/IP: ")
    print(f"\n{G}[+] PAYLOADS:\n{C}WS:{W} GET / HTTP/1.1[crlf]Host: {host}[crlf]Upgrade: websocket[crlf][crlf]")

def main():
    while True:
        clear_screen()
        get_banner()
        print(f"{G}[1]{W} Bug Host Discovery (Perfect Table View)")
        print(f"{G}[2]{W} Reverse IP Lookup (Table View)")
        print(f"{G}[3]{W} Payload Generator")
        print(f"{G}[4]{W} Subnet Scanner (Active /16 Finder) 🔥")
        print(f"{G}[5]{W} Exit")
        opt = input(f"\n{C}NS-Hacker > {W}")
        if opt == '1': bug_host_scan(); input("\nEnter...")
        elif opt == '2': mass_reverse_dns(); input("\nEnter...")
        elif opt == '3': payload_gen(); input("\nEnter...")
        elif opt == '4': active_subnet_finder(); input("\nEnter...")
        elif opt == '5': break

if __name__ == "__main__": main()
