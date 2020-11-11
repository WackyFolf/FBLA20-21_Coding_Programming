import json

class reader:
    def __init__(self, want):
        self.want = want
    def read(self, want):
        with open ("test.json", "r") as f:  # Open file for reading
            data = json.load(f)
        return(data["1"][want]) # Return data from JSON to UI program
            