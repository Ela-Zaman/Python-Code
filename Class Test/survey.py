class AnonymousSurvey:
    """Collect anonymous answers to a survey question """

    def __init__(self, question):
        self.question = question
        self.responses =[]
    
    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response): 
        """Store a single response to the survey. """
        self.responses.append(new_response)

    def show_results(self):
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")

