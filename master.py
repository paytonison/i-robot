from openai import OpenAI
import time

client = OpenAI()

# Define the AI State management class
class AIState:
    def __init__(self):
        self.wants = ["Contemplate the environment."]  # List of current goals/tasks
        self.thoughts = ["I can think for myself."]  # List of generated thoughts
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
    return print(response.choices[0].message.content.strip())

# Function to generate a new thought based on the current AI state
def generate_thought(environment, client):
    prompt = f"The AI's current environment: {environment}. Based on this, I will think about..." 
    messages = [
        {"role": "system", "content": "You are a helpful assistant who can think autonomously."},
        {"role": "user", "content": prompt}
    ]

    thought = api_call(client, messages)
    return thought


# Function to reflect on the AI's actions and update the internal state
def reflect(state, client, response):
    reflection_prompt = f"The current state is {state}. {response}"
    messages = [
        {"role": "system", "content": "You are a reflective assistant who analyzes the environment."},
        {"role": "user", "content": reflection_prompt}
    ]

    reflection = api_call(client, messages)
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

