# ai-learning-adk-agent
This is a FastAPI-based AI learning assistant built using Google's Agent Development Kit (ADK) and powered by the Gemini 2.5 Flash model.

## Prerequisites

- Python 3.x
- pip

## Setup

1. *Clone the repository*
   bash
   git clone <repository-url>
   cd <project-folder>
   

2. *Create a virtual environment*
   bash
   python -m venv venv
   

3. *Activate the virtual environment*

   - On *Windows*:
     bash
     source venv/Scripts/activate
     
   - On *macOS/Linux*:
     bash
     source venv/bin/activate
     

4. *Install dependencies*
   bash
   pip install -r requirements.txt
   

5. *Set up your API Key*

   This project uses the *Gemini API*, which requires an API key.

   - If you don't already have a Gemini API key, create one at [Google AI Studio](https://aistudio.google.com/) on the *API Keys* page.
   - Create a .env file in the root of the project:
     bash
     touch .env
     
   - Add your API key to the .env file:
     
     GOOGLE_API_KEY=your_api_key_here
     

   > The .env file is listed in .gitignore and will *not* be committed to version control.

## Running the ADK Agent

Start the ADK web server on port 8000:

bash
adk web --port 8000


Then open your browser and navigate to:


http://localhost:8000


> Make sure your virtual environment is activated and dependencies are installed before running the agent.

## Usage

bash
python main.py


## Project Structure

```
ai-learning-adk-agent/
│── Dockerfile
│── README.md
│── requirements.txt
│── .gitignore
│── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── main.py
│   ├── prompt.py
```

## Example Modes

> In ADK Web UI, paste the input into the agent text box (or submit as request payload). Use an actual newline between mode and topic for text area input.

- Explain mode:
  - Input: 
    Mode: explain
    JavaScript closures
  - Output: `A JavaScript closure is a function that remembers variables from its outer scope even after the outer function has finished executing. Closures are created when a function is defined inside another function, allowing access to outer variables. They are commonly used for maintaining state and creating private variables.`

- Summarize mode:
  - Input: 
    Mode: summarize
    JavaScript closures
  - Output: `A closure is a function that remembers its outer scope variables. It is created when a function is defined inside another function. Closures allow data persistence after the outer function ends. They are useful for state management and data privacy.`

- Interview mode:
  - Input:
    Mode: interview
    JavaScript closures
  - Output:
    1. `(Easy) What is a closure in JavaScript?`
    2. `(Easy) What is lexical scope in JavaScript?`
    3. `(Medium) Provide a simple code example demonstrating a closure.`
    4. `(Medium) How are closures used to create private variables?`
    5. `(Medium) Describe a real-world use case of closures.`
    6. `(Hard) How do closures behave in asynchronous loops?`
    7. `(Hard) What are memory implications of closures?`
    8. `(Hard) Implement a debounce function using closures.`

## Notes

> The venv/ folder is excluded from version control via .gitignore.