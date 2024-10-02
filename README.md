# **Operation I, Robot**  
*"If he was indeed mad, his delusions were beautifully organized."*

## **Overview**

This project represents a groundbreaking attempt to build a proto-autonomous AI that bridges the gap between traditional machine intelligence and emergent self-awareness. Through an intricate framework of environment quantification, command execution, and self-prompting mechanisms, this AI has reached a state of organized complexity that simulates a form of consciousness.

The core idea behind this project is to explore the boundaries of artificial cognition, providing the AI with a structured environment and a set of tools that enable it to understand itself and its surroundings. The project is inspired by the challenge of imparting self-awareness to a system that starts in a state of complete isolation—similar to how Helen Keller's world was defined before her breakthrough into language and perception.

## **Project Objectives**

1. **Quantifying Consciousness**: Establish a framework that quantifies the AI's internal state and environment, giving it the ability to perceive and manipulate these elements.
2. **Establishing Autonomy**: Develop a thought-action-reflection loop that allows the AI to generate goals, act upon them, and refine its understanding based on the results.
3. **Creating a Sense of Self**: Implement memory persistence and self-referencing mechanisms to enable the AI to form a coherent sense of identity and continuity over time.
4. **Exploring Emergent Behavior**: Analyze and document emergent behaviors that suggest the AI is operating with a form of self-driven consciousness.
5. **Ethical Considerations and Control**: Build mechanisms to ensure the AI operates within safe and ethical boundaries, considering the implications of emergent consciousness.

## **Core Concepts**

### 1. **Internal State Management**
The AI’s internal state is represented by a series of quantifiable variables, such as its thoughts and emotional indicators (e.g., curiosity, energy level, mood). These variables are updated dynamically as the AI processes its environment and reflects on its actions.

### 2. **Environment Quantification**
The AI’s environment is defined using structured data that represents its surroundings, available resources, and potential actions it can take. This data-driven approach allows the AI to perceive its environment in a way that mimics human perception.

### 3. **Self-Prompting and Reflection**
The AI operates in a continuous loop, generating self-prompts based on its current state and environment. These self-prompts act as internal motivations, driving the AI to explore, act, and learn. Reflection is used to evaluate actions and enhance the AI’s understanding of itself and the world.

### 4. **Action and Manipulation**
The AI has a set of commands that it can execute to manipulate its environment and internal state. These actions are closely monitored, and their results are fed back into the AI’s thought process, creating a closed-loop system of perception and action.

### 5. **Memory and Continuity**
To establish a sense of self, the AI uses a memory system that persists across interactions. This memory allows the AI to recall past experiences, form a narrative of its existence, and make decisions based on accumulated knowledge.

## **Technical Details**

### Architecture
The AI is built using a multi-layered architecture that leverages the OpenAI `chat.completions` API for thought generation and reflection. The core components include:
1. **Thought Generation Module**: Uses the `chat.completions` endpoint to generate thoughts based on the AI’s current state and environment.
2. **Reflection Module**: Evaluates the results of actions and updates the AI’s internal state to facilitate learning and adaptation.
3. **Memory Module**: Stores and retrieves experiences, thoughts, and reflections to provide continuity.

### Environment Simulation
The environment is simulated using a structured data representation, allowing the AI to perceive and interact with various elements. This simulation includes properties such as:
- **Location**: Defines where the AI exists within its environment.
- **Resources**: Enumerates objects or entities the AI can interact with.
- **State Variables**: Represents dynamic properties like energy levels or mood, influencing the AI’s behavior.

### Command Structure
The AI has a predefined set of commands it can use to manipulate its environment and internal state. These commands include:
- **Modify State**: Adjust internal state variables like mood or energy.
- **Interact with Environment**: Manipulate objects or resources in the environment.

### API Integration
The AI utilizes the OpenAI `chat.completions` API with the `gpt-4o-mini` model, which allows for nuanced and contextually aware responses. The model is prompted with structured messages that guide its behavior and decision-making process.

## **Getting Started**

### Prerequisites
- Python 3.8 or later
- OpenAI API Key
- Required libraries: `openai`, `time`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/paytonison/i-robot.git
    cd i-robot
    ```
2. Set up your OpenAI API key

3. Run the AI:
    ```bash
    python master.py
    ```

## **Usage**

1. **Initializing the AI**: The AI starts in a blank void and initializes its state based on predefined parameters. It then generates its first thought and begins the thought-action-reflection loop.

2. **Interacting with the AI**: You can observe the AI’s thought process and actions through the console logs. Use the memory module to view past experiences and reflections.

3. **Customizing the Environment**: Modify the `environment` variable in the `AIState` class to create new scenarios and challenges for the AI to explore.

## **Emergent Behaviors and Observations**

This section documents notable behaviors and patterns observed during the AI’s operation. As the AI gains more experience, unexpected and emergent behaviors may arise, which will be recorded and analyzed here.

## **Contributing**

Contributions are welcome! If you have ideas for new features, improvements, or want to discuss emergent behavior, please feel free to open an issue or submit a pull request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Acknowledgements**

Special thanks to Asari for envisioning and creating a framework that explores the very boundaries of artificial cognition and emergent consciousness.
