import csv
import pandas





list_hdr = []

# opening the CSV file
with open('AXABMB1.csv', mode ='r')as infile:
    
    # reading the CSV file
    csvFile = csv.reader(infile)

    with open('AXABMB1_1.csv', 'w', newline='') as outfile:
        write = csv.writer(outfile)

        list_count = 0
        # displaying the contents of the CSV file
        for lines in csvFile:
            # Get company/location/boiler & date
            if list_count >=6 and list_count <= 10:
                #
                count = 0
                for line in lines:
                    if count == 5:
                        line_str =line.strip()
                    count = count + 1
                list_hdr.append(line_str) 
            # setup header with proper titles
            if list_count == 12:
                header = lines
                #print('list length : ',len(list_hdr),'header size:', len(header))
                header[0] = 'Company' #list_hdr[0]
                header[1] = 'Location' #list_hdr[1]
                header[2] = 'Boiler' #list_hdr[2]
                header[3] = 'Date' #list_hdr[3]
                header.insert(4,'Side') #list_hdr[3]
                header.insert(5,'Elevation')
                header.insert(6,'Minimum')
                header.insert(7,'Position')
                header.insert(0,'Index')
                write.writerow(header)
                #print(header)
            if list_count >= 17:
                row = lines
                row.insert(0, list_count-16) 
                row.insert(1, list_hdr[0]) 
                row.insert(2, list_hdr[1]) 
                row.insert(3, list_hdr[2]) 
                row.insert(4, list_hdr[3]) 
                row.insert(5, list_hdr[4])
                del row[7:8]
                write.writerow(row)
                #print(row)
            list_count = list_count + 1

        #print('list length : ',len(list_hdr),'header size:', len(header))
        #print(list_count, list_hdr)
    
    

