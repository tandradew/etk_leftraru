# etk_leftraru


# Instructions to install EinsteinToolkit

## ssh to leftraru

```
scp <username>@leftraru2.nlhpc.cl
```

The hostname used by ETK is picked up from the way you connect, so here we force it 
to be `leftraru2`. -- TO DO: make compilation independent of this


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

### Quasi-circular binary

Run the quasi-circular binary evolution with 

```
./simfactory/bin/sim submit qc0-mclachlan --parfile=par/qc0-mclachlan.par --procs=20 --ppn=20 --ppn-used=20 --num-threads=1 --walltime=00:10:00
```

This is an unexpensive example of a black hole binary. 