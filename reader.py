import json

class reader:
    def __init__(self, want, num, quiz):
        self.want = want
        self.num = num
        self.quiz = quiz
    def read(self, want, num, quiz):
        with open ("quizzes/"+quiz+".json", "r") as f:  # Open file for reading
            data = json.load(f)
        return(data[num][want]) # Return data from JSON to UI program
            