#!/usr/bin/env python3
import unittest

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    
    def test_lower(self):
        self.assertEqual('FOO'.lower(), 'foo')
    
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
    
    def test_split(self):
        s = 'hello world'
        self.assertEquals(s.split(), ['hello', 'world'])
        
        with self.assertRaises(TypeError):
            s.split(2)
            
            
class meTestCase(unittest.TestCase):
    def test_widget_size(self):
        widget = widget('The widget')
        self.assertEqual(widget.size(), (50, 50))





if __name__ == '__main__':
    unittest.main()