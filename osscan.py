import re

# Open the file to be scanned
with open('ports.txt', 'r') as f:
    # Read the contents of the file into a variable
    file_contents = f.read()
    
    # Use regular expressions to search for IP addresses in the file
    ip_address_search = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    
    # Find all matches of IP addresses in the file
    ip_addresses = ip_address_search.findall(file_contents)
    
    # Open the output file
    with open("output.txt", "w") as out_file:
        for ip in ip_addresses:
            # Write the IP address to the output file
            out_file.write(ip + "\n")
