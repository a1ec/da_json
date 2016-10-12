import hashlib
import sys
import json

# dict to pretty JSON string
def json_pretty(dict_object):
    return json.dumps(dict_object, sort_keys=True, indent=2)

# return the sha224 hash of any string
def string_hash(string):
    return hashlib.sha224(string).hexdigest()

# return serialised JSON string with no spacing
def json_serial(dict_object):
    return json.dumps(dict_object, sort_keys=True, separators=(',', ':'))

def json_hash(dict_object):
    return string_hash(json_serial(dict_object).encode('utf-8'))
    

class record:
    """ DA record """
    def __init__(self, data=None):
        self.data = {}
        if data:
            self.data = data.copy()
        # TODO 
        # self.signature = json_serial(self.data)
        
    def set(self, data):
        self.data = data.copy()
        # TODO
        # self.signature = json_serial(self.data)

    def equals(self, record2):
        return self.signature == record2.signature
         

def main():
    pass

if __name__ == "__main__":
   main()
