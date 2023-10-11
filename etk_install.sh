# download 
curl -kLO https://raw.githubusercontent.com/gridaphobe/CRL/ET_2023_05/GetComponents
chmod a+x GetComponents
./GetComponents https://bitbucket.org/einsteintoolkit/manifest/raw/ET_2023_05/einsteintoolkit.th
rm einsteintoolkit.th

# move to root
cd Cactus/

# later to remove setup silent
./simfactory/bin/sim setup-silent

# copy thornlist
echo "copying thornlist"
cp ../leftraru_config/einsteintoolkit.th thornlists/

# copy config files

echo "copying .ini file"
cp ../leftraru_config/leftraru2.nlhpc.cl.ini simfactory/mdb/machines/ 

echo "copying .cfg file"
cp ../leftraru_config/leftraru.cfg simfactory/mdb/optionlists/

# unset MPI
# unset MPI_DIR
