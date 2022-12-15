import unittest
from CD import *
from main import *


class Test_CD(unittest.TestCase):
    def setUp(self):
        self.libraries = [
            CD_Library(1, 'Братиславская'),
            CD_Library(2, 'Проспект мира'),
            CD_Library(3, 'Верхние поля'),
 
            CD_Library(11, 'Невский проспект'),
            CD_Library(22, 'Гороховая'),
            CD_Library(33, 'Академическая')
        ]
 
        self.disks = [
            CD_Disk(1, 'Nirvana', 2000, 1),
            CD_Disk(2, 'Drain Gang', 3500, 2),
            CD_Disk(3, 'No counrty for old man', 4500, 3),
            CD_Disk(4, 'Reservoir Dogs', 2500, 3),
            CD_Disk(5, 'Trainspotting', 3500, 3)
        ]
 
        self.disks_librs = [
            Disk_Libr(1,1),
            Disk_Libr(2,2),
            Disk_Libr(3,3),
            Disk_Libr(3,4),
            Disk_Libr(3,5),
        
            Disk_Libr(11,1),
            Disk_Libr(22,2),
            Disk_Libr(33,3),
            Disk_Libr(33,4),
            Disk_Libr(33,5)
        ] 

        self.one_to_many = one_disk_to_many_libraries(self.disks, self.libraries)
        self.many_to_many = many_disks_to_many_libraries(self.disks, self.libraries, self.disks_librs)


    def test_task_1(self):
        supposed_res = [ 
            ('Nirvana', 2000, 'Братиславская'), 
            ('No counrty for old man', 4500, 'Верхние поля')
        ]
        res = disks_names_from_N(self.one_to_many)
        self.assertEqual(res, supposed_res)

    def test_task_2(self):
        supposed_res = [
            ('Братиславская', 2000), 
            ('Верхние поля', 2500), 
            ('Проспект мира', 3500)
        ]
        res = librs_with_minimal_disk_size_sorted(self.one_to_many)
        self.assertEqual(res, supposed_res)

    def test_task_3(self):
        supposed_res = [
            ('Drain Gang', 3500, 'Гороховая'), 
            ('Drain Gang', 3500, 'Проспект мира'), 
            ('Nirvana', 2000, 'Братиславская'), 
            ('Nirvana', 2000, 'Невский проспект'), 
            ('No counrty for old man', 4500, 'Академическая'), 
            ('No counrty for old man', 4500, 'Верхние поля'), 
            ('Reservoir Dogs', 2500, 'Академическая'), 
            ('Reservoir Dogs', 2500, 'Верхние поля'), 
            ('Trainspotting', 3500, 'Академическая'), 
            ('Trainspotting', 3500, 'Верхние поля')
        ]
        res = librs_to_disks_sorted_by_name(self.many_to_many)
        self.assertEqual(res, supposed_res)


if __name__ == '__main__':
    unittest.main()
    