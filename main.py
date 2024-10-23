from interviewer import AIInterviewer

def main():
    print("Welcome to AI Technical Interviewer")
    print("===================================")
    print("This program will conduct a technical interview focusing on Python and Algorithms.")
    print("Please provide detailed answers to get the best assessment.\n")
    
    interviewer = AIInterviewer()
    interviewer.conduct_interview()

if __name__ == "__main__":
    main()