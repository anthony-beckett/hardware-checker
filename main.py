import psutil as ps, json
from time import sleep

def json_write(hardware_info):
    hardware_info = { 
        "name" : "sathiyajith", 
        "rollno" : 56, 
        "cgpa" : 8.6, 
        "phonenumber" : "9976770500"
    } 
    
    # Serializing json  
    json_object = json.dumps(hardware_info, indent = 4) 
    
    # Writing to sample.json 
    with open("sample.json", "w") as outfile: 
        outfile.write(json_object) 

if __name__ == "__main__":
    ps.cpu_freq("test")