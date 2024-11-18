import time
from datetime import datetime

# Path to hosts file
hosts_path = "/etc/hosts"  # Linux/Mac
# Uncomment the following line if using Windows:
# hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

# Redirect address
redirect = "127.0.0.1"

# Websites to block
websites = ["www.instagram.com", "instagram.com", "www.youtube.com", "youtube.com", "x.com", "www.x.com"]

# Define blocking hours
start_hour = 9  # Start blocking at 9 AM
end_hour = 17   # Stop blocking at 5 PM

def block_websites():
    print("Blocking websites...")
    with open(hosts_path, "r+") as file:
        content = file.read()
        for website in websites:
            if website not in content:
                file.write(f"{redirect} {website}\n")

def unblock_websites():
    print("Unblocking websites...")
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()

def manage_websites():
    current_hour = datetime.now().hour
    if start_hour <= current_hour < end_hour:
        block_websites()
    else:
        unblock_websites()

if __name__ == "__main__":
    try:
        while True:
            manage_websites()
            time.sleep(300)  # Check every 5 minutes
    except KeyboardInterrupt:
        print("Exiting program. Unblocking all websites.")
        unblock_websites()
