yes | sudo apt-get update && yes | sudo apt install python3-virtualenv && yes | sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && yes | wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && yes | sudo apt-get update && yes | sudo apt-get -y install postgresql postgresql-contrib && cd projectfullstack && virtualenv fullstack_env && source fullstack_env/bin/activate
