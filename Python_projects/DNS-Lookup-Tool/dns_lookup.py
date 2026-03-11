import socket
website = input("Enter the name of the site(google.com): ")
try:
    ip_address = socket.gethostbyname(website)

    print("-" * 30)
    print(f"Site: {website}")
    print(f"IP address (A Record): {ip_address}")
    print("-" * 30)

except socket.gaierror:
    print("Error invalid site name")
