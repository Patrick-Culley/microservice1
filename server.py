# Class contains links to the following units of measurement: 
# inch, foot, meter, kilometer, centimeter, millimeter, micrometer, nanometer, mile, and yard
import json
from flask import Flask, jsonify
app = Flask(__name__)

class Measurement:
    def __init__(self, unit):
        self.unit = unit.lower()
        self.measurement = {"inch": "https://en.wikipedia.org/wiki/Inch",
                            "centimeter": "https://en.wikipedia.org/wiki/Centimetre",
                            "millimeter": "https://en.wikipedia.org/wiki/Millimetre",
                            "foot": "https://en.wikipedia.org/wiki/Foot_(unit)", 
                            "kilometer": "https://en.wikipedia.org/wiki/Kilometre", 
                            "meter": "https://en.wikipedia.org/wiki/Metre", 
                            "micrometer": "https://en.wikipedia.org/wiki/Micrometre", 
                            "nanometer": "https://en.wikipedia.org/wiki/Nanometre",
                            "mile": "https://en.wikipedia.org/wiki/Mile",
                            "yard": "https://en.wikipedia.org/wiki/Yard"
                            }

    def get_measurement(self): 
        return self.measurement[self.unit]


@app.route('/units/<unit>', methods=["GET"])
def get_unit_rest(unit): 
    unit = Measurement(unit)   
    response = jsonify(url=unit.get_measurement())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run()   
 