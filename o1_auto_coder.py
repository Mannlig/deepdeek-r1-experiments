import os
from openai import OpenAI
from termcolor import colored
import re
import time

# User Configuration
USER_PROMPT = "create a beautiful tower defense game in pygame. do not use outside assets. all assets should be created within pygame"
NUMBER_OF_ITERATIONS = 3

# Constants
MODEL = "o1" #you can also use o1-mini or gpt-4o
OUTPUT_FOLDER = "generated_code"

SYSTEM_PROMPT = """You are an expert Python programmer specializing in creating visually stunning and well-structured applications. Generate clean, efficient, and well-documented Python code based on the user's request.

Follow these EXACT rules for code generation:
1. ALWAYS wrap your code response in <code></code> tags
2. Include ALL necessary imports at the top
3. Add descriptive comments and docstrings
4. Return ONLY the code within the tags, no explanations outside the tags
5. Make sure the code is complete and can run immediately
6. Use proper Python formatting and PEP 8 guidelines
7. NEVER use or reference external files (no loading images, sounds, or data files)
8. ALL assets (graphics, sounds, data) must be generated programmatically within the code

For visual applications (GUI, games, graphics):
- Create beautiful, polished visuals using ONLY programmatic generation
- All graphics must be drawn using the framework's primitives (shapes, lines, etc.)
- Implement smooth animations and transitions
- Use appealing color schemes and visual effects
- Design intuitive and responsive UI/UX
- Add visual feedback for user interactions
- Include particle effects and visual polish where appropriate
- ALL visual assets must be created within the code itself

return the full code in <code></code> tags"""

IMPROVEMENT_PROMPT = """Improve this working Python code with the following priorities:

1. Visual Enhancement (for GUI/games):
   - Enhance visual aesthetics (colors, shapes, animations)
   - Add visual polish (particles, effects, transitions)
   - Improve UI/UX elements
   - Make the visuals more professional and engaging
   - ALL graphics must be generated programmatically
   - Use framework primitives for all visual assets

2. Feature Enhancement:
   - Expand core functionality
   - Add quality-of-life improvements
   - Implement additional user interactions
   - Include more game mechanics/options if it's a game
   - ALL assets must be created within the code

3. Technical Optimization:
   - Optimize performance
   - Improve code organization
   - Add helpful comments
   - NO external file operations

Keep the code complete and runnable. Return the full improved code in its entirety in <code></code> tags."""

# Initialize OpenAI client
try:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
except Exception as e:
    print(colored(f"Error initializing OpenAI client: {str(e)}", "red"))
    exit(1)

def extract_code(response_text):
    """Extract code from between <code></code> tags."""
    try:
        pattern = r"<code>(.*?)</code>"
        match = re.search(pattern, response_text, re.DOTALL)
        return match.group(1).strip() if match else None
    except Exception as e:
        print(colored(f"Error extracting code: {str(e)}", "red"))
        return None

def generate_code(prompt, iteration=1):
    """Generate code using o1 model."""
    try:
        print(colored(f"\nGenerating code - Iteration {iteration}...", "cyan"))
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Create a new Python program for: {prompt}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(colored(f"Error generating code: {str(e)}", "red"))
        return None

def improve_code(code, iteration):
    """Improve working code."""
    try:
        print(colored(f"\nImproving code - Iteration {iteration}...", "yellow"))
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{IMPROVEMENT_PROMPT}\n\nHere's the code to improve:\n{code}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(colored(f"Error improving code: {str(e)}", "red"))
        return None

def save_code(code, iteration):
    """Save generated code to file."""
    try:
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
        
        filename = os.path.join(OUTPUT_FOLDER, f"generated_code_v{iteration}.py")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        print(colored(f"Code saved to: {filename}", "green"))
    except Exception as e:
        print(colored(f"Error saving code: {str(e)}", "red"))

def main():
    print(colored(f"Starting code generation for prompt: {USER_PROMPT}", "cyan"))
    print(colored(f"Number of iterations: {NUMBER_OF_ITERATIONS}", "cyan"))

    code = None
    for i in range(NUMBER_OF_ITERATIONS):
        # Generate or improve code
        if i == 0:
            response = generate_code(USER_PROMPT, i + 1)
        else:
            response = improve_code(code, i + 1)
        
        if not response:
            continue

        code = extract_code(response)
        if not code:
            print(colored("No code found in the response", "red"))
            continue

        # Save the code
        save_code(code, i)
        time.sleep(1)  # Rate limiting

    print(colored("\nCode generation and improvement completed!", "green"))

if __name__ == "__main__":
    main() 