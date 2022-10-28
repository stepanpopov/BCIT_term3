from operator import itemgetter
 
class CD_disk:
    """CD-disk"""
    def __init__(self, id, name, size, libr_id):
        self.id = id
        self.name = name 
        self.size = size  # MB size
        self.libr_id = libr_id
 
class CD_library:
    """CD-library"""
    def __init__(self, id, street):
        self.id = id
        self.street = street
 
class disk_libr:
    def __init__(self, libr_id, disk_id):
        self.libr_id = libr_id
        self.disk_id = disk_id
 

libraries = [
    CD_library(1, 'Братиславская'),
    CD_library(2, 'Проспект мира'),
    CD_library(3, 'Верхние поля'),
 
    CD_library(11, 'Невский проспект'),
    CD_library(22, 'Гороховая'),
    CD_library(33, 'Академическая'),
]
 
disks = [
    CD_disk(1, 'Nirvana', 2000, 1),
    CD_disk(2, 'Drain Gang', 3500, 2),
    CD_disk(3, 'No counrty for old man', 4500, 3),
    CD_disk(4, 'Reservoir Dogs', 2500, 3),
    CD_disk(5, 'Trainspotting', 3500, 3),
]
 
disks_librs = [
    disk_libr(1,1),
    disk_libr(2,2),
    disk_libr(3,3),
    disk_libr(3,4),
    disk_libr(3,5),
 
    disk_libr(11,1),
    disk_libr(22,2),
    disk_libr(33,3),
    disk_libr(33,4),
    disk_libr(33,5),
]
 
def main():
    # 1:M 
    one_to_many = [(d.name, d.size, l.street) 
        for d in disks
        for l in libraries 
        if d.libr_id==l.id]
    
    # M:M
    many_to_many_temp = [(l.street, dl.disk_id) 
        for l in libraries 
        for dl in disks_librs 
        if l.id==dl.libr_id]
    
    many_to_many = [(d.name, d.size, lib_street) 
        for lib_street, disk_id in many_to_many_temp
        for d in disks if d.id==disk_id]

    print('Задание B1: Названия дисков, начинающихся с N')
    res_1 = list(filter(lambda iter: iter[0][0] == 'N', one_to_many))
    print(res_1)

    print('\nЗадание B2: список библиотек с диском минимального размера в каждой библиотеке, отсортированный по размеру диска')
    dict_dynamic = {street: size for _,size,street in one_to_many}
    for _,size,street in one_to_many:
        if size < dict_dynamic[street]:
            dict_dynamic[street] = size

    res_2 = sorted(dict_dynamic.items(), key=itemgetter(1))
    print(res_2)

    print('\nЗадание B3: список всех связанных дисков и библиотек, отсортированный по названию дисков')
    res_3 = sorted(many_to_many, key = itemgetter(0, 2))
    print(res_3)


if __name__ == '__main__':
    main()
