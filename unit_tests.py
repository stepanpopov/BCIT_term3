import unittest
from unittest.mock import patch

from lab_python_fp.process_data import f1
from lab_python_fp.unique import Unique

# testing f1 from process_data.py
class Test_Process_Data_F1(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"job-name" : "Street-photographer"}, 
            {"job-name" : "programmist"} ,
            {"job-name" : "programmist"}, 
            {"job-name" : "Tatu-master"}
        ]
        self.supposed_result = [
            "programmist",
            "Street-photographer",
            "Tatu-master"
        ] 
    
    def test_without_mock(self):
        res = f1(self.data)
        self.assertEqual(res, self.supposed_result)

    @patch('lab_python_fp.process_data.field')
    @patch('lab_python_fp.process_data.Unique')
    def test_with_mock(self, mock_Unique, mock_field):
        mock_field.return_value = ["Street-photographer", "programmist", "programmist", "Tatu-master"]
        mock_Unique.return_value = (i for i in ["Street-photographer", "programmist", "Tatu-master"] )    

        res = f1(self.data)

        mock_field.assert_called_once_with(self.data, 'job-name')
        mock_Unique.assert_called_once_with(mock_field.return_value, ignore_case=True)
        self.assertEqual(res, self.supposed_result)

# testing Unique from unique.py
class Test_Unique(unittest.TestCase):
    def test_same_object(self):
        data = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
        res = list(Unique(data))
        supposed_res = ['a']
        self.assertEqual(res, supposed_res)

    def test_base(self):
        data = [1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 3, 'A', 3, 'a', '1567', 1567, 'yooo']
        res = list(Unique(data))
        supposed_res = [1, 2, 3, 'A', 'a', '1567', 1567, 'yooo']
        self.assertEqual(res, supposed_res)

    def test_ignore_case(self):
        data = ['aBC', 'ABc', 'aBc', 'abc', 'ABC']
        res = list(Unique(data, ignore_case=True))
        supposed_res = ['aBC']
        self.assertEqual(res, supposed_res)

if __name__ == '__main__':
    unittest.main()
