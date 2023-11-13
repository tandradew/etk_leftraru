# etk_leftraru


## connect to cluster

```
$ ssh student<nn>@leftraru.nlhpc.cl
```

\<nn\> = 21-25; 32 - 67

## update repo 

```
$ git pull
```

##  Clone this repository
```
git clone https://github.com/tandradew/etk_leftraru.git
```

## Load modules

Install some dependencies on top of the ones loaded by default in leftraru.

```
module load impi/2019.2.185
module load libtool
```

You can access the full list of modules by 
```
$ module list 
```
You sould see

Currently Loaded Modules:
1) GCCcore/8.2.0
2) icc/2019.2.187-GCC-8.2.0-2.31.1                      
3) ifort/2019.2.187-GCC-8.2.0-2.31.1   
4) intel/2019b    
5) impi/2019.2.185   
6) imkl/2019.2.187  
7) binutils/2.32   
8) M4/1.4.18
9) libtool/2.4.6
  
## Download and configure
Execute the script 
```
$ cd etk_leftraru/
$ ./etk_install.sh
```

## Compile
Compile the code with 8 CPUs (this can take up to 30 minutes)
```
$ cd Cactus/
$ ./simfactory/bin/sim build -j8 --thornlist thornlists/einsteintoolkit.th
```

## Test

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