from openai import OpenAI
import time

client = OpenAI()

# Define the AI State management class
class AIState:
    def __init__(self):
        self.goals = []  # List of current goals/tasks
        self.thoughts = []  # List of generated thoughts
        self.responses = []  # Record of responses to prompts
        self.external_state = {}  # Placeholder for external inputs, like sensor data or API calls

# Wrapper for OpenAI API calls using the ChatCompletion endpoint
def api_call(client, messages, model="gpt-4o-mini", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# Function to generate a new thought based on the current AI state
def generate_thought(state, client):
    prompt = f"The AI's current state: {state}. Based on this, I will think about..." 
    messages = [
        {"role": "system", "content": "You are a helpful assistant who can think autonomously."},
        {"role": "user", "content": prompt}
    ]

    thought = api_call(client, messages)
    if thought:
        state.thoughts.append(thought)
    return thought

# Function to create a new self-prompt based on the AI's state
def self_prompt(state):
    if len(state.goals) == 0:
        return "What should I do?"
    else:
        return f"Given the goal: {state.goals[-1]}, what should be my next step?"

# Function to reflect on the AI's actions and update the internal state
def reflect(state, client, feedback):
    reflection_prompt = f"Based on the feedback '{feedback}', what did I learn?"
    messages = [
        {"role": "system", "content": "You are a reflective assistant who learns from feedback."},
        {"role": "user", "content": reflection_prompt}
    ]

    reflection = api_call(client, messages)
    if reflection:
        state.thoughts.append(reflection)
    return reflection

# Main autonomous loop function that keeps the AI running
def autonomous_loop(state):

    while True:
        # Generate a new thought
        thought = generate_thought(state, client)
        if thought:
            print(f"Thought: {thought}")
        
        # Generate a self-prompt based on the thought
        prompt = self_prompt(state)
        print(f"Self-prompt: {prompt}")
        
        # Generate a response or action based on the prompt
        messages = [
            {"role": "system", "content": "You are a goal-oriented assistant."},
            {"role": "user", "content": prompt}
        ]
        action_response = api_call(client, messages)
        if action_response:
            state.responses.append(action_response)
            print(f"Action: {action_response}")
        
        # Reflect on the action
        feedback = f"The action '{action_response}' led to no external change." if action_response else "No action was taken."
        reflection = reflect(state, client, feedback)
        print(f"Reflection: {reflection}")
        
        # Simulate time passing to prevent infinite rapid looping
        time.sleep(10)  # Adjust sleep time as necessary

# Run the AI with the updated loop
if __name__ == "__main__":
    # Initialize the state
    state = AIState()
    
    # Start the autonomous loop
    autonomous_loop(state)

