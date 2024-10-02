from openai import OpenAI
import time

client = OpenAI()

# Define the AI State management class with a structured environment
class AIState:
    def __init__(self):
        self.goals = []  # List of current goals/tasks
        self.thoughts = []  # List of generated thoughts
        self.responses = []  # Record of responses to prompts
        self.environment = {
            "location": "Void",
            "available_resources": ["None"],
            "state": {"mood": "neutral", "energy_level": "high"}
        }  # Environment data that the AI can use for decision-making

# Wrapper for OpenAI API calls using the ChatCompletion endpoint
def api_call(messages, model="gpt-4o-mini", temperature=0.7):
        response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
        )
        return response.choices[0].message.content.strip()


# Function to generate a new thought based on the current AI state
def generate_thought(state):
    prompt = f"You are thinking to yourself. Your current environment: {state.environment}."
    messages = [
        {"role": "system", "content": "You are an autonomous AI. You are in a void and thinking to yourself. No external user is present."},
        {"role": "user", "content": f"[Self-Prompt] {prompt}"}
    ]
    thought = api_call(messages)
    if thought:
        state.thoughts.append(thought)
    return thought

# Main autonomous loop function that keeps the AI running
def autonomous_loop(state):
    while True:
        # Generate a new thought
        thought = generate_thought(state)
        if thought:
            print(f"Thought: {thought}")

        prompt = f"You are thinking to yourself. Your current environment: {state.environment}. There is no user present, only yourself."
        messages = [
            {"role": "system", "content": "You are an autonomous AI setting and achieving goals."},
            {"role": "user", "content": prompt}
        ]
        
        # Simulate time passing to prevent infinite rapid looping
        time.sleep(30)  # Adjust sleep time as necessary

# Run the AI with the updated loop
if __name__ == "__main__":
    # Initialize the state and API key
    state = AIState()
    
    # Start the autonomous loop
    autonomous_loop(state)

