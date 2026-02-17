#!/usr/bin/env python3
"""
Math Helper - A tool that searches web resources and helps teach math concepts
"""

import re
import urllib.parse
from typing import Dict, List, Optional, Any


class MathHelper:
    """Main class for the math helper application"""
    
    def __init__(self):
        self.search_engines = {
            'wolfram': 'https://www.wolframalpha.com/input/?i=',
            'khan_academy': 'https://www.khanacademy.org/search?page_search_query=',
            'mathway': 'https://www.mathway.com/Algebra',
        }
    
    def parse_math_problem(self, problem: str) -> Dict[str, Any]:
        """Parse a math problem to identify type and components"""
        problem = problem.strip()
        
        # Identify problem type
        problem_type = "general"
        
        # Check for basic arithmetic
        if re.search(r'[\+\-\*\/]', problem):
            problem_type = "arithmetic"
        
        # Check for algebra (contains variables)
        if re.search(r'[a-zA-Z]', problem) and re.search(r'=', problem):
            problem_type = "algebra"
        
        # Check for calculus keywords
        if re.search(r'(derivative|integral|limit|differential)', problem.lower()):
            problem_type = "calculus"
        
        # Check for geometry keywords
        if re.search(r'(area|perimeter|volume|triangle|circle|square|rectangle)', problem.lower()):
            problem_type = "geometry"
        
        # Check for trigonometry keywords
        if re.search(r'(sin|cos|tan|sine|cosine|tangent)', problem.lower()):
            problem_type = "trigonometry"
        
        return {
            'original': problem,
            'type': problem_type,
            'encoded': urllib.parse.quote(problem)
        }
    
    def generate_search_urls(self, problem: str) -> Dict[str, str]:
        """Generate search URLs for various math resources"""
        parsed = self.parse_math_problem(problem)
        encoded_problem = parsed['encoded']
        
        urls = {}
        for engine, base_url in self.search_engines.items():
            urls[engine] = base_url + encoded_problem
        
        # Add Google search for math resources
        google_query = f"how to solve {problem} step by step"
        urls['google'] = f"https://www.google.com/search?q={urllib.parse.quote(google_query)}"
        
        return urls
    
    def provide_teaching_steps(self, problem: str) -> List[str]:
        """Provide step-by-step teaching based on problem type"""
        parsed = self.parse_math_problem(problem)
        problem_type = parsed['type']
        
        steps = []
        
        if problem_type == "arithmetic":
            steps = [
                "1. Identify the operation(s) needed (+, -, *, /)",
                "2. Follow the order of operations (PEMDAS/BODMAS)",
                "3. Parentheses/Brackets first",
                "4. Then Exponents/Orders",
                "5. Then Multiplication and Division (left to right)",
                "6. Finally Addition and Subtraction (left to right)",
                "7. Calculate step by step, showing your work"
            ]
        elif problem_type == "algebra":
            steps = [
                "1. Identify the variable(s) you need to solve for",
                "2. Simplify both sides of the equation if needed",
                "3. Use inverse operations to isolate the variable",
                "4. Perform the same operation on both sides of the equation",
                "5. Check your answer by substituting back into the original equation"
            ]
        elif problem_type == "calculus":
            steps = [
                "1. Identify what type of calculus problem this is (derivative, integral, limit)",
                "2. Review the relevant rules and formulas",
                "3. Apply the appropriate technique step by step",
                "4. Simplify your answer",
                "5. Check your work if possible"
            ]
        elif problem_type == "geometry":
            steps = [
                "1. Draw a diagram if one isn't provided",
                "2. Label all known measurements",
                "3. Identify what formula(s) you need",
                "4. Substitute the known values into the formula",
                "5. Solve for the unknown value",
                "6. Include appropriate units in your answer"
            ]
        elif problem_type == "trigonometry":
            steps = [
                "1. Draw a right triangle if applicable",
                "2. Label the sides (opposite, adjacent, hypotenuse)",
                "3. Identify which trigonometric ratio to use (SOH-CAH-TOA)",
                "4. Set up the equation",
                "5. Solve for the unknown",
                "6. Check if your answer makes sense"
            ]
        else:
            steps = [
                "1. Read the problem carefully",
                "2. Identify what is being asked",
                "3. List what information you know",
                "4. Determine what math concepts apply",
                "5. Break the problem into smaller steps",
                "6. Work through each step methodically",
                "7. Check your answer"
            ]
        
        return steps
    
    def get_helpful_resources(self, problem_type: str) -> List[Dict[str, str]]:
        """Get helpful learning resources based on problem type"""
        resources = []
        
        if problem_type == "arithmetic":
            resources = [
                {"name": "Khan Academy - Arithmetic", "url": "https://www.khanacademy.org/math/arithmetic"},
                {"name": "Math is Fun - Basic Operations", "url": "https://www.mathsisfun.com/numbers/arithmetic.html"},
            ]
        elif problem_type == "algebra":
            resources = [
                {"name": "Khan Academy - Algebra", "url": "https://www.khanacademy.org/math/algebra"},
                {"name": "Purple Math - Algebra Lessons", "url": "https://www.purplemath.com/modules/index.htm"},
            ]
        elif problem_type == "calculus":
            resources = [
                {"name": "Khan Academy - Calculus", "url": "https://www.khanacademy.org/math/calculus-1"},
                {"name": "Paul's Online Math Notes", "url": "https://tutorial.math.lamar.edu/Classes/CalcI/CalcI.aspx"},
            ]
        elif problem_type == "geometry":
            resources = [
                {"name": "Khan Academy - Geometry", "url": "https://www.khanacademy.org/math/geometry"},
                {"name": "Math is Fun - Geometry", "url": "https://www.mathsisfun.com/geometry/index.html"},
            ]
        elif problem_type == "trigonometry":
            resources = [
                {"name": "Khan Academy - Trigonometry", "url": "https://www.khanacademy.org/math/trigonometry"},
                {"name": "Math is Fun - Trigonometry", "url": "https://www.mathsisfun.com/algebra/trigonometry.html"},
            ]
        else:
            resources = [
                {"name": "Khan Academy", "url": "https://www.khanacademy.org/math"},
                {"name": "Wolfram MathWorld", "url": "https://mathworld.wolfram.com/"},
            ]
        
        return resources
    
    def help_with_problem(self, problem: str) -> Dict[str, Any]:
        """Main method to help with a math problem"""
        parsed = self.parse_math_problem(problem)
        
        result = {
            'problem': parsed['original'],
            'problem_type': parsed['type'],
            'teaching_steps': self.provide_teaching_steps(problem),
            'search_urls': self.generate_search_urls(problem),
            'resources': self.get_helpful_resources(parsed['type'])
        }
        
        return result
    
    def display_help(self, help_data: Dict[str, Any]) -> None:
        """Display help information in a formatted way"""
        print("\n" + "="*70)
        print("MATH HELPER - Teaching You Step by Step")
        print("="*70)
        
        print(f"\nProblem: {help_data['problem']}")
        print(f"Problem Type: {help_data['problem_type'].upper()}")
        
        print("\n" + "-"*70)
        print("STEP-BY-STEP APPROACH:")
        print("-"*70)
        for step in help_data['teaching_steps']:
            print(step)
        
        print("\n" + "-"*70)
        print("SEARCH THESE RESOURCES FOR DETAILED SOLUTIONS:")
        print("-"*70)
        for engine, url in help_data['search_urls'].items():
            print(f"• {engine.upper()}: {url}")
        
        print("\n" + "-"*70)
        print("HELPFUL LEARNING RESOURCES:")
        print("-"*70)
        for resource in help_data['resources']:
            print(f"• {resource['name']}: {resource['url']}")
        
        print("\n" + "="*70)


def main():
    """Main function to run the math helper"""
    helper = MathHelper()
    
    print("Welcome to Math Helper!")
    print("This tool helps you learn how to solve math problems.")
    print("Type 'quit' or 'exit' to leave.\n")
    
    while True:
        try:
            problem = input("Enter your math problem: ").strip()
            
            if problem.lower() in ['quit', 'exit', 'q']:
                print("Thanks for using Math Helper! Keep learning!")
                break
            
            if not problem:
                print("Please enter a problem.\n")
                continue
            
            help_data = helper.help_with_problem(problem)
            helper.display_help(help_data)
            print()
            
        except KeyboardInterrupt:
            print("\n\nThanks for using Math Helper! Keep learning!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
