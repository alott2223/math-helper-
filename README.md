# Math Helper

A Python-based math helper that searches web resources and helps teach you how to solve math problems step by step.

## Features

- 🔍 **Web Resource Search**: Generates search URLs for popular math resources (Wolfram Alpha, Khan Academy, Google, etc.)
- 📚 **Step-by-Step Teaching**: Provides detailed steps for solving different types of math problems
- 🎯 **Problem Type Detection**: Automatically identifies the type of math problem (arithmetic, algebra, calculus, geometry, trigonometry)
- 🌐 **Curated Resources**: Suggests helpful learning resources based on problem type

## Supported Problem Types

- **Arithmetic**: Basic operations with PEMDAS/BODMAS guidance
- **Algebra**: Equation solving with variable isolation steps
- **Calculus**: Derivatives, integrals, and limits
- **Geometry**: Area, perimeter, volume calculations
- **Trigonometry**: Sin, cos, tan with SOH-CAH-TOA reminders

## Installation

No external dependencies required! Just Python 3.6+

```bash
git clone https://github.com/alott2223/math-helper-.git
cd math-helper-
```

## Usage

### Interactive Mode

Run the program in interactive mode to solve multiple problems:

```bash
python3 math_helper.py
```

Then enter your math problems one at a time:

```
Enter your math problem: solve 2x + 5 = 15
Enter your math problem: find the area of a circle with radius 5
Enter your math problem: derivative of x^2
```

### Example Output

```
======================================================================
MATH HELPER - Teaching You Step by Step
======================================================================

Problem: solve 2x + 5 = 15
Problem Type: ALGEBRA

----------------------------------------------------------------------
STEP-BY-STEP APPROACH:
----------------------------------------------------------------------
1. Identify the variable(s) you need to solve for
2. Simplify both sides of the equation if needed
3. Use inverse operations to isolate the variable
4. Perform the same operation on both sides of the equation
5. Check your answer by substituting back into the original equation

----------------------------------------------------------------------
SEARCH THESE RESOURCES FOR DETAILED SOLUTIONS:
----------------------------------------------------------------------
• WOLFRAM: https://www.wolframalpha.com/input/?i=solve+2x+%2B+5+%3D+15
• KHAN_ACADEMY: https://www.khanacademy.org/search?page_search_query=solve+2x+%2B+5+%3D+15
• GOOGLE: https://www.google.com/search?q=how+to+solve+...

----------------------------------------------------------------------
HELPFUL LEARNING RESOURCES:
----------------------------------------------------------------------
• Khan Academy - Algebra: https://www.khanacademy.org/math/algebra
• Purple Math - Algebra Lessons: https://www.purplemath.com/modules/index.htm
```

## How It Works

1. **Input**: You provide a math problem
2. **Analysis**: The program identifies the problem type
3. **Teaching**: Displays step-by-step approach for that problem type
4. **Resources**: Generates search URLs and resource links
5. **Learning**: Follow the steps and use the resources to learn!

## Examples

Try these example problems:

- `2 + 3 * 4` - Arithmetic with order of operations
- `solve x^2 - 5x + 6 = 0` - Quadratic algebra
- `derivative of sin(x)` - Calculus
- `area of triangle with base 10 and height 5` - Geometry
- `cos(30 degrees)` - Trigonometry

## Contributing

Feel free to submit issues or pull requests to improve Math Helper!

## License

MIT License - feel free to use and modify as needed.
