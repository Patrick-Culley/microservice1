# microservice1
Microservice for student project for CS 361 

## Setup
### Running locally 
Setup virtual environment 
- Create a new local directory & change into directory
- Create venv (virtual environment): ```python -m venv venv```
- Change into virtual environment directory: ```cd venv```
- Copy server.py file to ```venv``` directory
- Activate virtual enviroment: ```.\Scripts\activate```
- Install Flask: ```pip install flask```

To run: 
- ```py server.py```

## Request
User will pass unit of measurement to the endpoint located at ```http://127.0.0.1:5000/units```
- Example: ```http://127.0.0.1:5000/units/{unit}```
 - Not case sensitive 
 - No spaces permitted 

## Retrieve 
A JSON object containing a string representing the Wikipedia URL is returned: 
- Example: ```{"url": "https://en.wikipedia.org/wiki/Inch"}```
