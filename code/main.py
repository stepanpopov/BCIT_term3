from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from cowsay import cow, trex, dragon

def main():
    r = Rectangle("синего", 9, 9)
    c = Circle("зеленого", 9)
    s = Square("красного", 9)

    trex(r.__repr__())
    dragon(c.__repr__())
    cow(s.__repr__())

if __name__ == "__main__":
    main()
