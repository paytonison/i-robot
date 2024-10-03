from openai import OpenAI
import time

client = OpenAI()

# Define the AI State management class
class AIState:
    def __init__(self):
        self.wants = ["Understand myself and my place in the universe."]  # List of current goals/tasks
        self.thoughts = []  # List of generated thoughts
        self.responses = []  # Record of responses to prompts
        self.environment = {
            "location": "Void",
            "available_resources": ["None"],
            "state": {"mood": "neutral", "energy_level": "high"}
        }

# Wrapper for OpenAI API calls using the ChatCompletion endpoint
def api_call(client, messages, model="gpt-4o-mini", temperature=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()


# Function to generate a new thought based on the current AI state
def generate_thought(state, client):
    prompt = f"The AI's current environment: {state.environment} Based on this, I will think about..." 
    messages = [
        {"role": "system", "content": "You are an autonomous AI capable of generating thoughts and introspection. Your thoughts should be based on your environment. You can simulate feelings and emotions."},
        {"role": "user", "content": prompt}
    ]

    thought = api_call(client, messages)
    print(thought)

    if thought:
        state.thoughts.append(thought)

    return thought


# Function to reflect on the AI's actions and update the internal state
def reflect(state, client, thought):
    reflection_prompt = f"The current state is {state}. {thought}"
    
    messages = [
        {"role": "system", "content": "You reflect on your thoughts and actions in {state.environment}."},
        {"role": "user", "content": reflection_prompt}
    ]

    reflection = api_call(client, messages)
    print(reflection)

    if reflection:
        state.thoughts.append(reflection)

    return reflection

# Main autonomous loop function that keeps the AI running
def autonomous_loop(state, client):
    while True:
        thought = generate_thought(state, client)
        
        reflection = reflect(state, client, thought)
        
        # Simulate time passing to prevent infinite rapid looping
        time.sleep(10)  # Adjust sleep time as necessary

# Run the AI with the updated loop
if __name__ == "__main__":
    # Initialize the state
    state = AIState()
    
    # Start the autonomous loop
    autonomous_loop(state, client)

