import random
from interview_questions import QUESTIONS
from candidate import Candidate

class AIInterviewer:
    def __init__(self):
        self.candidate = Candidate()
        self.topics = list(QUESTIONS.keys())
        self.current_topic_index = 0
        
    def analyze_response(self, response):
        # Simple keyword-based analysis
        keywords = {
            'python': ['interpreted', 'object-oriented', 'dynamic typing', 'high-level'],
            'algorithms': ['complexity', 'efficiency', 'optimization', 'data structure']
        }
        
        response_lower = response.lower()
        score = 0
        confidence = 0
        
        # Check for relevant keywords
        current_topic = self.topics[self.current_topic_index]
        for keyword in keywords[current_topic]:
            if keyword in response_lower:
                score += 1
                confidence += 0.2
                
        return min(score, 5), min(confidence, 1.0)
    
    def conduct_interview(self):
        print("\nAI Interviewer: Welcome to your technical interview!")
        print("I'll ask you questions about Python and Algorithms.\n")
        
        for topic in self.topics:
            print(f"\nLet's discuss {topic.upper()}...")
            for _ in range(3):  # 3 questions per topic
                question = random.choice(QUESTIONS[topic][self.candidate.current_level])
                print(f"\nQuestion: {question}")
                
                answer = input("Your answer: ")
                score, confidence = self.analyze_response(answer)
                
                self.candidate.add_response(question, answer, confidence)
                self.candidate.update_score(score)
                
            self.current_topic_index += 1
            
        self.provide_feedback()
    
    def provide_feedback(self):
        print("\n=== Interview Summary ===")
        print(f"Final Score: {self.candidate.score}/30")
        print(f"Highest Level Achieved: {self.candidate.current_level}")
        print("\nDetailed Feedback:")
        for response in self.candidate.responses:
            print(f"\nQ: {response['question']}")
            print(f"Confidence Score: {response['confidence']:.2f}")