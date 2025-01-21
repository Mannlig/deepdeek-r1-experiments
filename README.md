# AI Auto Coder Collection 🚀


### DeepSeek R1 Versions:

1. `deep_seek_auto_coder.py` - Safe version that only generates code
2. `deep_seek_auto_coder_executor.py` - ⚠️**EXECUTES AI-GENERATED CODE ON YOUR MACHINE**

### OpenAI O1 Versions:

3. `o1_auto_coder.py` - Safe version that only generates code
4. `o1_auto_coder_executor.py` - ⚠️**EXECUTES AI-GENERATED CODE ON YOUR MACHINE**

If you're not comfortable with code execution, use the safe versions (`deep_seek_auto_coder.py` or `o1_auto_coder.py`).

An intelligent code generation and improvement system that automatically generates, iteratively improves, and enhances Python code based on your requirements, with a special focus on creating visually stunning applications without external dependencies.

## Model Options 🤖

### DeepSeek R1:

- Available through OpenRouter
- Specialized in code generation
- Requires OpenRouter API key

### OpenAI O1:

- Available through OpenAI
- Can also use o1-mini or gpt-4o variants
- Requires OpenAI API key
- Generally faster response times

## Features ✨

- 🎨 Specialized in generating visually appealing applications
- 🔄 Iterative code improvement system
- 🛠️ Automatic code generation from text descriptions
- 📝 Clean, documented, and well-structured code output
- 🎮 Perfect for games, GUIs, and visual applications
- 🔒 No external file dependencies - everything is generated programmatically
- 🎯 Multiple iterations of improvements
- 🌈 Colored terminal output for better visibility

## ❤️Join my AI Community & Get 400+ AI Projects & 1000x Cursor Course

This is one of 400+ fascinating projects in my collection! [Support me on Patreon](https://www.patreon.com/c/echohive42/membership) to get:

- 🎯 Access to 400+ AI projects (and growing daily!)
  - Including advanced projects like [2 Agent Real-time voice template with turn taking](https://www.patreon.com/posts/2-agent-real-you-118330397)
- 📥 Full source code & detailed explanations
- 📚 1000x Cursor Course
- 🎓 Live coding sessions & AMAs
- 💬 1-on-1 consultations (higher tiers)
- 🎁 Exclusive discounts on AI tools & platforms (up to $180 value)

## Prerequisites 📋

- Python 3.x
- OpenRouter API key (for DeepSeek versions)
- OpenAI API key (for O1 versions)

## Installation 🔧

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Set up your API key as an environment variable:

```bash
# For DeepSeek versions (Windows)
set OPENROUTER_API_KEY=your_api_key_here

# For O1 versions (Windows)
set OPENAI_API_KEY=your_api_key_here

# For DeepSeek versions (Linux/Mac)
export OPENROUTER_API_KEY=your_api_key_here

# For O1 versions (Linux/Mac)
export OPENAI_API_KEY=your_api_key_here
```

## Usage 💻

1. Choose your preferred version and configure:

```python
# User Configuration
USER_PROMPT = "Your detailed Python program description"
NUMBER_OF_ITERATIONS = 3  # Number of improvement iterations
MODEL = "o1"  # For O1 versions, can also use "o1-mini" or "gpt-4o"
```

2. Run your chosen version:

```bash
# DeepSeek versions
python deep_seek_auto_coder.py
python deep_seek_auto_coder_executor.py

# O1 versions
python o1_auto_coder.py
python o1_auto_coder_executor.py
```

3. Find your generated code in the `generated_code` folder:

- `generated_code_v0.py`: Initial generation
- `generated_code_v1.py` to `generated_code_vN.py`: Improved iterations

## Version Comparison 🔄

### Safe Versions (deep_seek_auto_coder.py & o1_auto_coder.py):

- Generate and improve code without execution
- Save all iterations to files
- No system access or security risks
- Best for initial development and exploration
- Choose between DeepSeek R1 or OpenAI O1 models

### Executor Versions (deep_seek_auto_coder_executor.py & o1_auto_coder_executor.py):

- **⚠️ EXECUTE CODE ON YOUR SYSTEM**
- Automatically test generated code
- Detect and fix runtime errors
- 5-second timeout for each execution
- Include error correction agent
- Only save working versions
- More efficient iteration process
- Choose between DeepSeek R1 or OpenAI O1 models

## How It Works 🔄

### Safe Version:

1. **Initial Generation**: Creates base code from your prompt
2. **Iterative Improvement**: Enhances the code through multiple iterations
3. **Visual Focus**: Emphasizes beautiful, programmatically generated visuals
4. **Code Organization**: Maintains clean structure and documentation
5. **Progress Tracking**: Shows colored progress in the terminal

### Executor Version:

1. **Code Generation**: Creates initial code from prompt
2. **Execution Testing**: Runs code with 5-second timeout
3. **Error Detection**: Captures and analyzes runtime errors
4. **Automatic Fixing**: Uses AI to fix detected errors
5. **Verification**: Tests fixed code before proceeding
6. **Improvement**: Enhances working code
7. **Safety Features**: Process isolation, timeout, cleanup

## Example Prompts 📝

```python
# Game Development
USER_PROMPT = "create a beautiful tower defense game in pygame. do not use outside assets. all assets should be created within pygame"

# GUI Application
USER_PROMPT = "create a modern calculator with a beautiful dark theme using tkinter"

# Data Visualization
USER_PROMPT = "create an interactive bar chart race visualization using pygame"
```

## Features of Generated Code 🎯

- ✅ Complete error handling with descriptive messages
- ✅ Defensive programming practices
- ✅ Edge case handling
- ✅ Resource cleanup and management
- ✅ Proper documentation
- ✅ Clean code structure
- ✅ Programmatically generated assets
- ✅ No external file dependencies
- ✅ Beautiful visuals and animations
- ✅ Performance optimizations

## Notes 📌

- All visual assets are created programmatically - no external files needed
- Each iteration builds upon the previous one
- The system includes rate limiting to prevent API overload
- Progress is saved after each iteration
- Uses UTF-8 encoding for file operations
- Comprehensive error detection and prevention
- Defensive programming approach
- Visual feedback for errors
- Proper resource management

## Error Handling 🚨

The script includes comprehensive error handling for:

- Runtime errors and edge cases
- Resource management and cleanup
- State transitions and validation
- User input and parameters
- Visual elements and animations
- Memory management
- API connection issues
- Code generation failures
- File operations
- Code extraction problems
