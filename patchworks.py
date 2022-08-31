import module1
import unittest
from unittest.mock import MagicMock, call, patch

from module1 import A, B
from module1 import module_method2


class TestSomeMethods(unittest.TestCase):

    @patch('module1.module_method1')
    def test_instance2module_method(self,mock_module_method):
        """instance method calls module method
           method patch by full reference"""
        A().methodA('testArg')
        mock_module_method.assert_called_once()

    @patch.object(module1,'module_method1')
    def test_instance2module_method_object_patch(self,mock_module_method):
        """instance method calls module method 
           method patch via parent object"""
        A().methodA('testArg')
        mock_module_method.assert_called_once()



    @patch('module1.module_method1')
    def test_instance2instance2module_method(self,mock_module_method):
        """instance method instantiates object, method call of which calls module method
           method patch by full reference"""
        B().methodB()
        mock_module_method.assert_called_once()
        
    @patch.object(module1,'module_method1')
    def test_instance2instance2module_method_object_patch(self,mock_module_method):
        """instance method instantiates object, method call of which calls module method
           method patch via parent object"""
        B().methodB()
        mock_module_method.assert_called_once()



    @patch('module1.module_method1')
    def test_module2instance2module_method(self,mock_module_method):
        """module method instantiates object, method call of which calls module method 
           method patch by full reference"""
        module_method2()
        mock_module_method.assert_called_once()
                
    @patch.object(module1,'module_method1')
    def test_module2instance2module_method_object_patch(self,mock_module_method):
        """module method instantiates object, method call of which calls module method
           method patch via parent object"""
        module_method2()
        mock_module_method.assert_called_once()

    @patch('module1.A',autospec=True)    
    def test_module2instance2module_method_instance_patch(self,mock_A):
        """module method instantiates object, method call of which calls module method 
           class patch by full reference"""
        module_method2()
        mock_A.assert_called_once_with()
        mock_A.assert_has_calls([call().methodA('arg1')])

    @patch.object(module1,'A',autospec=True)    
    def test_module2instance2module_method_instance_patch_object(self,mock_A):
        """module method instantiates object, method call of which calls module method 
           class patch via parent module"""
        module_method2()
        mock_A.assert_called_once_with()
        mock_A.assert_has_calls([call().methodA('arg1')])
