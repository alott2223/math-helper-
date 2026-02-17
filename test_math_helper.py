#!/usr/bin/env python3
"""
Unit tests for Math Helper
"""

import unittest
from math_helper import MathHelper


class TestMathHelper(unittest.TestCase):
    """Test cases for MathHelper class"""
    
    def setUp(self):
        """Set up test helper instance"""
        self.helper = MathHelper()
    
    def test_parse_arithmetic_problem(self):
        """Test parsing of arithmetic problems"""
        result = self.helper.parse_math_problem("2 + 3 * 4")
        self.assertEqual(result['type'], 'arithmetic')
        
    def test_parse_algebra_problem(self):
        """Test parsing of algebra problems"""
        result = self.helper.parse_math_problem("solve 2x + 5 = 15")
        self.assertEqual(result['type'], 'algebra')
        
    def test_parse_calculus_problem(self):
        """Test parsing of calculus problems"""
        result = self.helper.parse_math_problem("derivative of x^2")
        self.assertEqual(result['type'], 'calculus')
        
    def test_parse_geometry_problem(self):
        """Test parsing of geometry problems"""
        result = self.helper.parse_math_problem("area of circle with radius 5")
        self.assertEqual(result['type'], 'geometry')
        
    def test_parse_trigonometry_problem(self):
        """Test parsing of trigonometry problems"""
        result = self.helper.parse_math_problem("sin(30 degrees)")
        self.assertEqual(result['type'], 'trigonometry')
    
    def test_generate_search_urls(self):
        """Test search URL generation"""
        urls = self.helper.generate_search_urls("solve x + 5 = 10")
        self.assertIn('wolfram', urls)
        self.assertIn('khan_academy', urls)
        self.assertIn('google', urls)
        self.assertTrue(all(isinstance(url, str) for url in urls.values()))
    
    def test_provide_teaching_steps(self):
        """Test teaching steps generation"""
        steps = self.helper.provide_teaching_steps("2x + 5 = 15")
        self.assertIsInstance(steps, list)
        self.assertTrue(len(steps) > 0)
        self.assertTrue(all(isinstance(step, str) for step in steps))
    
    def test_get_helpful_resources(self):
        """Test resource retrieval"""
        resources = self.helper.get_helpful_resources('algebra')
        self.assertIsInstance(resources, list)
        self.assertTrue(len(resources) > 0)
        for resource in resources:
            self.assertIn('name', resource)
            self.assertIn('url', resource)
    
    def test_help_with_problem(self):
        """Test complete help generation"""
        help_data = self.helper.help_with_problem("solve x + 5 = 10")
        self.assertIn('problem', help_data)
        self.assertIn('problem_type', help_data)
        self.assertIn('teaching_steps', help_data)
        self.assertIn('search_urls', help_data)
        self.assertIn('resources', help_data)
        
        # Verify structure
        self.assertIsInstance(help_data['teaching_steps'], list)
        self.assertIsInstance(help_data['search_urls'], dict)
        self.assertIsInstance(help_data['resources'], list)


if __name__ == '__main__':
    unittest.main()
