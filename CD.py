class CD_Disk:
    """CD-disk"""
    def __init__(self, id, name, size, libr_id):
        self.id = id
        self.name = name 
        self.size = size  # MB size
        self.libr_id = libr_id
 
class CD_Library:
    """CD-library"""
    def __init__(self, id, street):
        self.id = id
        self.street = street
 
class Disk_Libr:
    def __init__(self, libr_id, disk_id):
        self.libr_id = libr_id
        self.disk_id = disk_id