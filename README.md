# projectfullstack
1 - https://learn.microsoft.com/en-us/windows/wsl/install (install WSL)

2 - Choose WSL Ubuntu-20.04 distribution
3 - Clone this repository
4 - execute install_postgress.sh
5 - sudo service postgresql start
5 - pip install -r requirements.txt

# configs of postgres in linux
1 - go to cd etc/postgresql/16/main/
2 - modify postgres.conf
2.1 - execute sudo nano postgres.conf
2.2 - change #listen_addresses = 'localhost' ==>>> listen_addresses = '*'
3 - sudo service postgresql restart
4 - modfify pg_hba.conf
4.1 - execute sudo nano pg_hba.conf
4.2 - add this lines: 
    ipv4 and ipv6 remote connections:
      host    all     all             0.0.0.0/0            scram-sha-256
      host    all     all             ::0/0                 scram-sha-256
5 - save the file and execute sudo service postgresql restart
    

