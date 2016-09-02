# Geo_parser


Retrieve GPS coordinate from list of postal address using Google Maps API

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [OPTIONS](#options)
- [CONFIGURATION](#configuration)
- [OUTPUT TEMPLATE](#output-template)

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
    
