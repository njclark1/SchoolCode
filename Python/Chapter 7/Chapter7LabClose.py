from random import randint

def main():

    iplist = []
    counter = 0

    print("This program generates a series of public IP Addresses and writes them to a file.\n")

    numberOfIps = input("How many addresses to write? ")
    while not numberOfIps.isnumeric() or int(numberOfIps) <= 0:
        print("\nThe number of addresses to generate must be a positive whole number\n")
        numberOfIps = input("How many addresses to write? ")

    for _ in range(int(numberOfIps)):
        
        iplist.append(getIpAddress())
        
        

    for ip in iplist:
        counter += 1
        print("Address " + str(counter) + ": " + ip)
    

    filename = "ipfile.txt"

    writefile(filename, iplist)

#writefile()

#will write the IPs as a list object

def writefile(filename, iplist):

    try:
        fileobject = open(filename, "w")
    except:
        print("An error occurred")

    #write to file
    
    fileobject.write(str(iplist))
    print("\nWriting addresses to file...\n")
    fileobject.close()

    print("Done!")


def getIpAddress():
    
    while True:
        octet1 = randint(1, 223)

        if octet1 == 10 or octet1 == 127:
            continue
        else:
            break

    while True:
        octet2 = randint(0, 255)

        if octet1 == 100 and octet2 >= 64 and octet2 <= 127:
            continue
        elif octet1 == 169 and octet2 == 254:
            continue
        elif octet1 == 172 and octet2 >= 16 and octet2 <= 31:
            continue
        elif octet1 == 192 and octet2 == 168:
            continue
        elif octet1 == 198 and octet2 >= 18 and octet2 <= 19:
            continue
        else:
            break
            
    octet4 = randint(0, 255)

    while True:
        octet3 = randint(0, 255)

        if octet1 == 192 and octet2 == 0 and octet3 == 0 and octet4 >= 0 and octet4 <= 255:
            continue
        elif octet1 == 192 and octet2 == 0 and octet3 == 2 and octet4 >= 0 and octet4 <= 255:
            continue
        elif octet1 == 192 and octet2 == 88 and octet3 == 99 and octet4 >= 0 and octet4 <= 255:
            continue
        elif octet1 == 198 and octet2 == 51 and octet3 == 100 and octet4 >= 0 and octet4 <= 255:
            continue
        elif octet1 == 203 and octet2 == 0 and octet3 == 113 and octet4 >= 0 and octet4 <= 255:
            continue
        else:
            break

    return str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)

main()