# etk_leftraru


## connect to cluster

```
$ ssh student<nn>@leftraru.nlhpc.cl
```

\<nn\> = 21-25; 32 - 67

## update repo 

```
$ cd etk_leftraru
$ git pull
```

If you get this error message due to conflict with changes, i.e.

```
error: Your local changes to the following files would be overwritten by merge:
```

do a hard reset to the origin branch by 

```
$ git fetch --all
$ git reset --hard origin/main
```

## Python

Useful links at NLHPC [conda](https://wiki.nlhpc.cl/Uso_de_conda), [jupyter](https://wiki.nlhpc.cl/Jupyter_bajo_Conda)


### Create environment

```
$ conda create -n my_env
$ conda activate my_env
$ conda install numpy scipy matplotlib jupyter nb_conda_kernels
```

## jupyter connection 
```
$ hostname
leftraru<x>
```
\<x\> = 1,2,3,4

```
$ jupyter-notebook --no-browser --port 23<nn>
```
Make note of hostname number and URLs

Open new terminal in local machine
```
$ ssh -NL 23<nn>:localhost:23<nn> -l student<nn> leftraru<x>.nlhpc.cl
```
with \<nn\> from student number, and \<x\> from hostname number

Open the URL in your favorite browser, and that's it! You should see the jupyter navigator

## ETK Tests

### Hello world

Run the hello-world test with 

```
./simfactory/bin/sim create-run helloworld --parfile arrangements/CactusExamples/HelloWorld/par/HelloWorld.par
```

You should see an output including

```
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
INFO (HelloWorld): Hello World!
```

### TOV star

Run the TOV star example with binary evolution with 

```
./simfactory/bin/sim submit tov_ET --parfile=par/tov_ET.par --procs=2 --ppn=2 --ppn-used=2 --num-threads=1 --walltime=00:30:00
```

Note that adding too many CPUs will result in an error (grid structure inconsistent). 

### Quasi-circular binaries

Run the quasi-circular binary evolution test with 

```
./simfactory/bin/sim submit qc0-mclachlan --parfile=par/qc0-mclachlan.par --procs=20 --ppn=20 --ppn-used=20 --num-threads=1 --walltime=00:10:00
```

This is an unexpensive example of a black hole binary, which will run for 10 minutes using 20 CPUs. 

Run another quasi-circular binary evolution with 

```
./simfactory/bin/sim submit BBHMedRes --parfile=par/BBHMedRes.par --procs=40 --ppn=20 --ppn-used=20 --num-threads=1 --walltime=20:00:00
```

This is a more expensive example of a black hole binary, which takes about 20 hours using 40 CPUs to complete. 

## Simfactory commands

Create and submit new simulation
```
./simfactory/bin/sim submit <simulation_name> --parfile=<parfile> [...info about resources]
```

Show all simulations
```
./simfactory/bin/sim list-simulations
```

Stop simulation 
```
./simfactory/bin/sim stop <simulation_name>
```

Resume simulation
```
./simfactory/bin/sim submit <existing_simulation_name>
```