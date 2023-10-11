# etk_leftraru


# Instructions to install EinsteinToolkit

## Download and configure
Execute the script 
```
$ ./etk_install.sh
```

## Compile
Compile the code with 8 CPUs (this can take about XXX minutes)
```
$ cd Cactus/
$ ./simfactory/bin/sim build -j8 --thornlist thornlists/einsteintoolkit.th
```

## Test

Run the hello-world test with 

```
./simfactory/bin/sim create-run helloworld --parfile arrangements/CactusExamples/HelloWorld/par/HelloWorld.par
```

