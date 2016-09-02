# Geo_parser


Retrieve GPS coordinate from list of postal address using Google Maps API

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [OPTIONS](#options)
- [EXAMPLE](#example)

# INSTALLATION

To install it right away for all UNIX users (Linux, OS X, etc.), type:

    sudo apt-get install python3
    sudo python3 -m pip install goooglemaps
    
To install python3 for CentOs (not in repo):

    wget http://python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz
    tar xvf Python-3.4.1.tar.xz
    cd Python-3.4.1
    sudo ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
    sudo make
    sudo make altinstall
    sudo python3 -m pip install goooglemaps  
    

    - Install python3 installer (https://www.python.org/downloads/)
    - In administrator command line, type :
    
   
To install it for windows :

    Install python3 installer (https://www.python.org/downloads/)
    In administrator command line, type :
    -> <PYTHON BIN PATH>\python3 -m pip install goooglemaps  
    
# OPTIONS

    usage: geo_fetcher.py [-h] [-d] [-v] input_file output_file [set]
        Retrieve GPS coordinated from gMaps using post address from input file
        positional arguments:
            input_file     input file
            output_file    output file
            set            List of columns containing postal address separated by ',' (Ex: "3,4,5")
        optional arguments:
            -h, --help     show this help message and exit
            -d, --debug    Enable debugging information
            -v, --version  show program's version number and exit


# EXAMPLE

Example in set mode :

            python geo_fetcher.py vd_input.csv update_input                                                                   [ROW:0][COL:0]ROUTER[COL:1]customer1[COL:2]RT_0102[COL:3]1.1.1.1[COL:4]test[COL:5][COL:6]3044CK[COL:7]ROTTERDAM[COL:8]Nederland
            [ROW:1][COL:0]ROUTER[COL:1]customer1[COL:2]RT_0103[COL:3]2.2.2.2[COL:4]test[COL:5][COL:6]3044CK[COL:7]ROTTERDAM[COL:8]Nederland
            [ROW:2][COL:0]ROUTER[COL:1]customer1[COL:2]RT_0104[COL:3]3.3.3.3[COL:4]test[COL:5][COL:6]2334CP[COL:7]LEIDEN[COL:8]Nederland
            [ROW:3][COL:0]ROUTER[COL:1]customer1[COL:2]RT_0105[COL:3]4.4.4.4[COL:4]test[COL:5][COL:6][COL:7][COL:8]
            [ROW:4][COL:0]ROUTER[COL:1]customer1[COL:2]RT_0106[COL:3]5.5.5.5[COL:4]test[COL:5]Hakgriend[COL:6]3371KA[COL:7]HARDINXVELD GIESSENDAM[COL:8]Nederland
            
            Please enter column number containing address :
                Multiple column can be selected using ',' 
                Best result if address formatted in below format:
                <street name><street number>, <postcode> <city>, <state>, <country>
            Column number :5,6,7,8
            
            Schema defined:
            [ 0 ]=>[ 5 ];[ 1 ]=>[ 6 ];[ 2 ]=>[ 7 ];[ 3 ]=>[ 8 ];
            
            Sample request test: ,3044CK,ROTTERDAM,
            :) :) :) :) :)
            
            Trying : ) Requesting gmaps location...
            Location {'lng': 4.4175639, 'lat': 51.9308754}
            
            Requesting location for all elements...
            Request [row:1] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:2] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:3] :,2334CP,LEIDEN,Nederland,
            Location:  {'lng': 4.482279999999999, 'lat': 52.1721689}
            Request [row:4] :,,,,
            Location: <Not found>
            Request [row:5] :Hakgriend,3371KA,HARDINXVELD GIESSENDAM,Nederland,
            Location:  {'lng': 4.8488904, 'lat': 51.82492689999999}
            Request [row:6] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:7] :sumatralaan,1217GP,HILVERSUM,Nederland,
            Location:  {'lng': 5.1724751, 'lat': 52.2359787}
            Request [row:8] :morsestraat,4004JP,TIEL,Nederland
            [...]

Example in batch mode :

        python geo_fetcher.py vd_input.csv update_input "5,6,7,8"
            Request [row:1] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:2] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:3] :,2334CP,LEIDEN,Nederland,
            Location:  {'lng': 4.482279999999999, 'lat': 52.1721689}
            Request [row:4] :,,,,
            Location: <Not found>
            Request [row:5] :Hakgriend,3371KA,HARDINXVELD GIESSENDAM,Nederland,
            Location:  {'lng': 4.8488904, 'lat': 51.82492689999999}
            Request [row:6] :,3044CK,ROTTERDAM,Nederland,
            Location:  {'lng': 4.418044699999999, 'lat': 51.9323904}
            Request [row:7] :sumatralaan,1217GP,HILVERSUM,Nederland,
            [...]
            

        
