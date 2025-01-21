import os
import sys
import subprocess
import time
from openai import OpenAI
from termcolor import colored
import re
import tempfile

# User Configuration
USER_PROMPT = "create a beautiful tower defense game in pygame. do not use outside assets. all assets should be created within pygame"
NUMBER_OF_ITERATIONS = 20

# Constants
MODEL = "deepseek/deepseek-r1"
OUTPUT_FOLDER = "generated_code"
MAX_ERROR_LENGTH = 500  # Maximum length of error message to send to model
CODE_TIMEOUT = 5  # Maximum seconds to run code

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

ERROR_CORRECTION_PROMPT = """You are an expert Python debugging agent. Your task is to fix code that has runtime errors.
Focus ONLY on fixing the specific error provided. Do not make unnecessary improvements or changes.

Follow these rules EXACTLY:
1. Analyze the error message carefully
2. Make minimal changes needed to fix the error
3. Preserve the original functionality
4. Return the COMPLETE fixed code in <code></code> tags
5. Do not add features or make improvements beyond error fixing
6. Keep all assets programmatically generated
7. NEVER return partial code or just the fixed section
8. Include ALL imports and ALL functions from the original code
9. Make sure to wrap the ENTIRE program in <code></code> tags
10. The code between the tags must be immediately runnable

Example format:
<code>
import something

# All original imports and code here
# With minimal fixes applied
# COMPLETE program, not just the fixed parts

def main():
    # Complete main function
    pass

if __name__ == "__main__":
    main()
</code>"""

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
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
except Exception as e:
    print(colored(f"Error initializing OpenAI client: {str(e)}", "red"))
    exit(1)

def run_code_with_timeout(code):
    """Run the code with a timeout and capture output/errors.
    A timeout usually indicates the program is running successfully in a continuous loop or long process."""
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_path = f.name

        try:
            # Run the code in a separate process with timeout
            process = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                text=True,
                timeout=CODE_TIMEOUT
            )
            # If we get here, the program exited before timeout
            if process.returncode != 0:
                return process.returncode, process.stdout, process.stderr
            return 0, process.stdout, process.stderr
        except subprocess.TimeoutExpired as e:
            print(colored(f"Program running (timeout reached after {CODE_TIMEOUT}s) - This is normal for continuous processes!", "green"))
            return 0, "", ""  # Treat timeout as success
        finally:
            try:
                os.unlink(temp_path)  # Clean up temp file
            except:
                pass
    except Exception as e:
        return -1, "", str(e)

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
    """Generate code using DeepSeek model."""
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

def fix_code(code, error_msg):
    """Fix code using the error correction agent."""
    try:
        print(colored("\nAttempting to fix code errors...", "yellow"))
        # Get last MAX_ERROR_LENGTH characters of error
        error_msg = error_msg[-MAX_ERROR_LENGTH:] if len(error_msg) > MAX_ERROR_LENGTH else error_msg
        
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": ERROR_CORRECTION_PROMPT},
                {"role": "user", "content": f"Fix this Python code that has the following error:\n{error_msg}\n\nHere's the code:\n{code}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(colored(f"Error fixing code: {str(e)}", "red"))
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
    print(colored(f"Note: Reaching the {CODE_TIMEOUT}s timeout means the program is running successfully!", "green"))

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

        # Test the code
        print(colored("\nTesting code execution...", "cyan"))
        returncode, stdout, stderr = run_code_with_timeout(code)

        # Handle code execution results
        if returncode != 0 and stderr:
            print(colored(f"Code execution failed with error:\n{stderr}", "red"))
            # Try to fix the error
            fixed_response = fix_code(code, stderr)
            if not fixed_response:
                print(colored("Failed to fix the error, continuing to next iteration", "red"))
                continue
                
            code = extract_code(fixed_response)
            if not code:
                print(colored("No fixed code found in the response", "red"))
                continue
                
            # Test the fixed code
            print(colored("\nTesting fixed code...", "cyan"))
            returncode, stdout, stderr = run_code_with_timeout(code)
            if returncode != 0:
                print(colored("Fixed code still has errors, continuing to next iteration", "red"))
                continue
        else:
            if stdout:
                print(colored("Program output:", "cyan"))
                print(stdout)
            print(colored("Code execution successful!", "green"))

        # Save the working code
        save_code(code, i)
        time.sleep(1)  # Rate limiting

    print(colored("\nCode generation and improvement completed!", "green"))

if __name__ == "__main__":
    main() 