class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question): #to create instance, just have to provide a question 
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = [] #empty list to provide responses

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response) #Adds the response to the list

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")