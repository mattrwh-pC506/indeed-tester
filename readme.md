# Indeed Query Sandbox


## Usage
Make sure you have python2.7 and pip installed. Then run the below commands.
```bash
pip install requests
pip install xmlutils
python job_search.py
```

You will be prompted to fill in 3 parameters. See below:
```bash
$ python job_search.py
enter a city. hit enter for default of "New York, NY"
enter a radius. hit enter for default of "2"
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 455
2 files have been generated
-----------------------------------------------------------
./results/csv/locationNewYorkNYradius2queryRetailORSalespersons.csv
./results/xml/locationNewYorkNYradius2queryRetailORSalespersons.xml
```

Look for your results in the results folder.


example searches
```bash
enter search criteria. default is "((Retail) OR (Salespersons))"
n job_search.py
enter a city. default is "New York, NY"
enter a radius. default is "2"
enter search criteria. default is "((Retail) OR (Salespersons))"
Total Results = 455
2 files have been generated
-----------------------------------------------------------
./results/csv/locationNewYorkNYradius2queryRetailORSalespersons.csv
./results/xml/locationNewYorkNYradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" Dallas, TX
enter a radius. hit enter for default of "2" 2
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 226
2 files have been generated
-----------------------------------------------------------
./results/csv/locationDallasTXradius2queryRetailORSalespersons.csv
./results/xml/locationDallasTXradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" LA, CA
enter a radius. hit enter for default of "2" 2
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 248
2 files have been generated
-----------------------------------------------------------
./results/csv/locationLACAradius2queryRetailORSalespersons.csv
./results/xml/locationLACAradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" Los Angeles, CA
enter a radius. hit enter for default of "2"
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 248
2 files have been generated
-----------------------------------------------------------
./results/csv/locationLosAngelesCAradius2queryRetailORSalespersons.csv
./results/xml/locationLosAngelesCAradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" Madison, WI
enter a radius. hit enter for default of "2"
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 72
2 files have been generated
-----------------------------------------------------------
./results/csv/locationMadisonWIradius2queryRetailORSalespersons.csv
./results/xml/locationMadisonWIradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" Newark, NJ
enter a radius. hit enter for default of "2"
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 19
2 files have been generated
-----------------------------------------------------------
./results/csv/locationNewarkNJradius2queryRetailORSalespersons.csv
./results/xml/locationNewarkNJradius2queryRetailORSalespersons.xml

$ python job_search.py
enter a city. hit enter for default of "New York, NY" Tampa, FL
enter a radius. hit enter for default of "2"
enter search criteria. hit enter for default of "((Retail) OR (Salespersons))"
Total Results = 136
2 files have been generated
-----------------------------------------------------------
./results/csv/locationTampaFLradius2queryRetailORSalespersons.csv
./results/xml/locationTampaFLradius2queryRetailORSalespersons.xml

```
