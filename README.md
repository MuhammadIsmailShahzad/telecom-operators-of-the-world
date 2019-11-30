
This is a dataset of leading telecom operators of the world

## Data
### List of mobile network operators:
Data is obtained from https://en.wikipedia.org/wiki/List_of_mobile_network_operators
The data contains 
 
 * The overall rank of the mobile network company.
 * Their main markets.
 * Technology they use
 * Total Subscription
 * Ownership of the company
 This data can be viewed in telecom-operators.csv

### List of total revenue of mobile network operators:
Data is obtained from https://en.wikipedia.org/wiki/List_of_telephone_operating_companies
The data contains 
 
 * The overall rank of the mobile network company.
 * Name of the company
 * Total Revenue
 * Country of the company
 This data can be viewed in telecom-revenue.csv



## Preparation
* The process.py and process-revenue scripts fetch data from table on wikipedia
* The data is extracted and cleaned in python and written to a csv file.
* Libraries used requests,beautifulsoup,csv

## License
[Public Domain Dedication and License v1.0](http://www.opendatacommons.org/licenses/pddl/1.0/)
