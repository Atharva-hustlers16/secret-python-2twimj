class Candidate:
    def __init__(self):
        self.responses = []
        self.score = 0
        self.current_level = 'easy'
        
    def add_response(self, question, answer, confidence_score):
        self.responses.append({
            'question': question,
            'answer': answer,
            'confidence': confidence_score
        })
        
    def update_score(self, score):
        self.score += score
        # Adjust difficulty based on performance
        if self.score >= 8:
            self.current_level = 'hard'
        elif self.score >= 5:
            self.current_level = 'medium'