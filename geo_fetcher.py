#!/usr/bin/env python3
# FSA
# 03/08/2016 15:02
# 

import csv, argparse, sys, re
import googlemaps


# Parse command line argument
parser = argparse.ArgumentParser(\
            description='Retrieve GPS coordinated from gMaps using post address from input file')
parser.add_argument('input_file', action='store', help="input file")
parser.add_argument('output_file', action='store', help="output file")
parser.add_argument('-d', '--debug', action='store_true', dest="debug", default=False,
                    help="Enable debugging information")
parser.add_argument('set', nargs='?', action='store', default=False,
                    help="List of column to use separated by ',' (Ex: \"3,4,5\") ")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0')
options = parser.parse_args()


# CSV mapping
csv_mapping = []


def gmap_req(req):
    gmaps = googlemaps.Client(key='<Your API key>')
    # Geocoding an address
    geocode_result = gmaps.geocode(str(req))
    return geocode_result

if __name__ == '__main__':
    # Enable debug if option -v is specified
    if options.debug: debug = True
    else: debug = False

    wrapper = {}

    if not options.set :
        # Read csv file and check for matching id
        with open(options.input_file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            i = 0
            for row in readCSV:
                j = 0
                if i < 5:
                    print("[ROW:", i, "]", sep="", end="")
                    for cols in row:
                        print("[COL:", j, "]", cols, sep="", end="")
                        j += 1
                    i += 1
                    print()
                else:
                    print("Please enter column number containing address :")
                    print("\t Multiple column can be selected using ',' ")
                    print("\t Best result if address formatted in below format:")
                    print("<street name><street number>, <postcode> <city>, <state>, <country>")
                    # Generate csv parsing schema
                    for cols in str(input("Column number :")).split(",") :
                        csv_mapping.append(str(cols))

                    print("Schema defined:")
                    j=  0
                    for i in csv_mapping :
                        print ("[",j,"]=>[",i,"];", end=""); j+=1
                    print()
                    s = ""
                    print("Sample request: ", end="")
                    for i in range(len(csv_mapping)-1):
                        if not i == len(csv_mapping)-1 :
                            s += row[int(csv_mapping[i])]+","
                        else : s += row[int(csv_mapping[i])]
                    print(s)
                    print(":) :) :) :) :)")

                    print("Trying : ) Requesting gmaps location...")
                    resp = gmap_req(s)
                    res = resp[0]

                    #print("LIST", resp[0])
                    print("Location", resp[0]['geometry']['location'])
                    break
            csvfile.close()
            print("Requesting location for all elements...")
    else :
        # Generate csv parsing schema in command line
        for cols in str(options.set).split(","):
            csv_mapping.append(str(cols))

    with open(options.input_file) as csvfile:
        resp_wrap = []
        readCSV = csv.reader(csvfile, delimiter=',')
        j = 1
        cmt_regex = [ '^#.*', '^\ *$', '^\*', '^\*+' ]
        no_found = 0
        for row2 in readCSV:
            comment = False
            err = False
            if len(row2) == 0 : 
                j += 1
                comment = True
            else : 
                for reg in cmt_regex :
                    if re.match( reg, row2[0] ) or re.match( reg, row2[0]) :
                        print("Row ",j, "skipped")
                        j += 1
                        comment = True
                        break
            if comment: continue
            req = ""
            resp = []
            for i in csv_mapping:
                try : req += row2[int(i)]+","
                except IndexError: j += 1; print("Row ",j, "skipped - Index Error"); err = True
            if err == True : continue
            resp = gmap_req(req)
            print("Request [row:", j, "] :", req, sep="")
            try :
                resp_wrap.append(
                    str(resp[0]['geometry']['location']['lat'])+','
                    +str(resp[0]['geometry']['location']['lng']))
                print("Location: ", resp[0]['geometry']['location'])

                if options.output_file:
                    out = options.output_file+".csv"
                    fh = open (out, 'a')

                    fh.write(';'.join(str(e) for e in row2)+";"+resp_wrap.pop()+"\n")

            except IndexError :
                print("Location: <Not found>")
                no_found += 1

            j += 1

        print("Completed =>  Number of addresses not found : ", no_found)
        csvfile.close()
