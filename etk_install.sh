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


# edit ini file
echo "editing .ini file"
sed -i 's/generic.cfg/leftraru.cfg/g' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini
sed -i 's/generic.sub/leftraru.sub/g' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini
sed -i 's/generic.run/leftraru.run/g' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini

sed -i '/submit  /c\submit          = sbatch @SCRIPTFILE@; sleep 3; echo "using sbatch" ' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini
sed -i '/getstatus	/c\getstatus	= squeue -j  @JOB_ID@' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini
sed -i '/stop  /c\stop            = scancel @JOB_ID@' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini
sed -i '/nodes  /c\nodes           = 8' simfactory/mdb/machines/leftraru2.nlhpc.cl.ini  

# copy config files
echo "copying .cfg file"
cp ../leftraru_config/leftraru.cfg simfactory/mdb/optionlists/

echo "copying .run file"
cp ../leftraru_config/leftraru.run simfactory/mdb/runscripts/

echo "copying .sub file"
cp ../leftraru_config/leftraru.sub simfactory/mdb/submitscripts/

echo "copying test parameter files"
cp ../test_parfiles/qc0-mclachlan.par par/
cp ../test_parfiles/tov_ET.par par/
cp ../test_parfiles/BBHMedRes.par par/
