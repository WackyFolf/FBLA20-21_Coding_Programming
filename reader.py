import json

class reader:
    def __init__(self, want, num):
        self.want = want
        self.num = num
    def read(self, want, num):
        with open ("quizzes/test.json", "r") as f:  # Open file for reading
            data = json.load(f)
        return(data[num][want]) # Return data from JSON to UI program
            