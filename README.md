# DeepSeek Auto Coder 🚀

An intelligent code generation and improvement system powered by DeepSeek's R1 model. This tool automatically generates, iteratively improves, and enhances Python code based on your requirements, with a special focus on creating visually stunning applications without external dependencies.

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
- OpenRouter API key

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

3. Set up your OpenRouter API key as an environment variable:

```bash
# Windows
set OPENROUTER_API_KEY=your_api_key_here

# Linux/Mac
export OPENROUTER_API_KEY=your_api_key_here
```

## Usage 💻

1. Configure your project in `deep_seek_auto_coder.py`:

```python
# User Configuration
USER_PROMPT = "Your detailed Python program description"
NUMBER_OF_ITERATIONS = 50  # Number of improvement iterations
```

2. Run the script:

```bash
python deep_seek_auto_coder.py
```

3. Find your generated code in the `generated_code` folder:

- `generated_code_v0.py`: Initial generation
- `generated_code_v1.py` to `generated_code_vN.py`: Improved iterations

## How It Works 🔄

1. **Initial Generation**: Creates base code from your prompt
2. **Iterative Improvement**: Enhances the code through multiple iterations
3. **Visual Focus**: Emphasizes beautiful, programmatically generated visuals
4. **Code Organization**: Maintains clean structure and documentation
5. **Error Handling**: Includes comprehensive error handling
6. **Progress Tracking**: Shows colored progress in the terminal

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
