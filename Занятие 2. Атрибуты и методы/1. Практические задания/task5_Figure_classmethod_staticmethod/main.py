import math


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    # сделать методом класса
    @classmethod
    def area(cls, *args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            cls.area_by_height(*args)
        if len(args) == 3:
            cls.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):  # сделать статическим методом
        """ Формула площади по двум сторонам и углу между ними. """
        sq = 0.5 * a * b * math.sin(angle)
        print(sq)
        return sq

    @staticmethod
    def area_by_height(a, h):  # сделать статическим методом
        """ Формула площади по основанию и высоте. """
        sq = 0.5 * a * h
        print(sq)
        return sq


if __name__ == '__main__':
    TriangleCalculator().area(5, 8, 1)  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр

    TriangleCalculator.area(5, 8, 1)  # Работаем через класс
    TriangleCalculator.area_by_height(5, 10)  # Работаем через класс
