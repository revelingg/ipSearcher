#Ibukun Adenuga
# 5/10/23
#processes files and finds the IPs



def checkFile(path, mode):
      #checks if the file exists and processes it
  
    val = True
    while val:
        fileP = input(f"{path}")
        try:
            file = open(fileP, mode)
            val = False
        except FileNotFoundError:
            print("\nERROR -- There is an issue with file {fileP}. Please reenter:")
    return file

def findHackers(file):
    print()
    #the potetial Ips 
    ip1 = "168.193"
    ip2 = "224.174"
    ip3 = "233.012"
    potentialHackers = []
  
    records = 0
   

    #counts the records in the file 

    for line in file:

        #uses split and join to get the delimeters and then joins them by the "." 
            #it ONLY joins Ips in the first 2 octets and not in the whole address so only the Ips that begin
        records += 1
        line.rstrip()
        split = line.split(".")
        octet = ".".join(split[:2])


        #if the line contains these variables then do this
        if ip1 in octet or ip2 in octet or ip3 in octet:
            potentialHackers.append(line)

    file.close()

    return records, potentialHackers    

    
def outputRepo(record, hackers, output):
    #prints the report on the hackers 

    for item in hackers:
        output.write(item)
    
    
    print(f"\nOutput Report \n-------------")
    print(f"The total number of records in the file is: {record}")
    print(f"\nThe number of suspect IP addresses is: {len(hackers)}")
    perc = len(hackers) / record
    print(f"\nThe percentage of suspect IP addresses is: {perc : .4f} ")

    print(f"\nSuspect IP Addresses  \n--------------------")
    for item in hackers:
    
        ipL = item.split()
        ip = ipL[0]
        date = " ".join(ipL[1:])
        
        print(f"IP Address =  {ip}\t\t Date and Time =  {date}\n")
   


    output.close()

    
def main():
    path = checkFile("Enter the path of the file: ", "r")
    output = checkFile("Enter the path of the output file: ", "w")
    record, hackers = findHackers(path)
    outputRepo(record, hackers, output)
    













print("Welcome \n")
main()
print("Program Complete!")
