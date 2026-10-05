"""
Automated unit test suite for Flask Web Application.
Tests all application routes and verifies status codes and template rendering.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Analysing Mental Health in Student Ecosystem', response.data)
        self.assertIn(b'Total Students Monitored', response.data)

    def test_dashboard_page(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Student Mental Health', response.data)

    def test_story_page(self):
        response = self.client.get('/story')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tableau Story', response.data)

    def test_data_page(self):
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'STU1001', response.data)

    def test_insights_page(self):
        response = self.client.get('/insights')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Analytical Findings', response.data)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlaskAppTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
