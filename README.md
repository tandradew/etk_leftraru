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