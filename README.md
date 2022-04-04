# Spider
before run any command or script we need to run our Flask api by typing :
```commandeline
python3 api.py
```
## module 1
in order to collect data run the following command:
```bash
    ./dataCollector.bash
```
> this command will generate logs.txt file contain our data

in order to send the collected data run the following command:
```bash
    ./dataSender.bash
```

## module 2
in order to create a backup of our database run the following command:
```bash
./backup.bash n
```
> this script has params (number of backups te preserve) that you should specify when you run it 
## module 3
in order to visualise the collected data
```commandline
python3 ./affichage.py
```
//todo:SMTP & crise detection
## module 4
and finally if you want to visualize collected data just visit [http://localhost:8080/]
