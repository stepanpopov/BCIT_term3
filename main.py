from operator import itemgetter
from CD import *

# 1:M
def one_disk_to_many_libraries(disks, libraries):
    return [(d.name, d.size, l.street) 
        for d in disks
        for l in libraries 
        if d.libr_id==l.id]

# M:M
def many_disks_to_many_libraries(disks, libraries, disks_librs):
    many_to_many_temp = [(l.street, dl.disk_id) 
        for l in libraries 
        for dl in disks_librs 
        if l.id==dl.libr_id]

    return [(d.name, d.size, lib_street) 
        for lib_street, disk_id in many_to_many_temp
        for d in disks if d.id==disk_id]

# Задание B1: Названия дисков, начинающихся с N
def disks_names_from_N(one_to_many):
    return list(filter(lambda iter: iter[0][0] == 'N', one_to_many))

# Задание B2: список библиотек с диском минимального размера в каждой библиотеке, 
# отсортированный по размеру диска
def librs_with_minimal_disk_size_sorted(one_to_many):
    dict_dynamic = {street: size for _,size,street in one_to_many}
    for _,size,street in one_to_many:
        if size < dict_dynamic[street]:
            dict_dynamic[street] = size
    return sorted(dict_dynamic.items(), key=itemgetter(1))

# Задание B3: список всех связанных дисков и библиотек, отсортированный по названию дисков
def librs_to_disks_sorted_by_name(many_to_many):
    return sorted(many_to_many, key = itemgetter(0, 2))
 
def main():
    libraries = [
        CD_Library(1, 'Братиславская'),
        CD_Library(2, 'Проспект мира'),
        CD_Library(3, 'Верхние поля'),
    
        CD_Library(11, 'Невский проспект'),
        CD_Library(22, 'Гороховая'),
        CD_Library(33, 'Академическая')
    ]
    
    disks = [
        CD_Disk(1, 'Nirvana', 2000, 1),
        CD_Disk(2, 'Drain Gang', 3500, 2),
        CD_Disk(3, 'No counrty for old man', 4500, 3),
        CD_Disk(4, 'Reservoir Dogs', 2500, 3),
        CD_Disk(5, 'Trainspotting', 3500, 3)
    ]
    
    disks_librs = [
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

    # 1:M 
    one_to_many = one_disk_to_many_libraries(disks, libraries)

    # M:M
    many_to_many = many_disks_to_many_libraries(disks, libraries, disks_librs)


    print('Задание B1: Названия дисков, начинающихся с N')
    res_1 = disks_names_from_N(one_to_many)
    print(res_1)

    print('\nЗадание B2: список библиотек с диском минимального размера в каждой библиотеке, отсортированный по размеру диска')
    res_2 = librs_with_minimal_disk_size_sorted(one_to_many)
    print(res_2)

    print('\nЗадание B3: список всех связанных дисков и библиотек, отсортированный по названию дисков')
    res_3 = librs_to_disks_sorted_by_name(many_to_many)
    print(res_3)


if __name__ == '__main__':
    main()
