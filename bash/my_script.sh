echo "hello world, I am at: "$PWD

SIMS=("sim_BBH1" "sim_BBH2")

for SIM in ${SIMS[*]}
do
    echo Working on $SIM
    mkdir $SIM/
    echo $SIM > $SIM/params.txt
done 
