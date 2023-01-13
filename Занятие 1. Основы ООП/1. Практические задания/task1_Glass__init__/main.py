from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  инициализировать объект "Стакан"

        if not (isinstance(capacity_volume, int) or isinstance(occupied_volume, int)):
            raise TypeError("it must be int!")
        if capacity_volume < 0 or occupied_volume < 0:
            raise ValueError("it must be > 0!")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        print(self.capacity_volume, self.occupied_volume)


if __name__ == "__main__":
    # инициализировать два объекта типа Glass
    glass1 = Glass(200, 0)
    glass2 = Glass(300, 100)

    # попробовать инициализировать не корректные объекты
    glass3 = Glass(-200, 0)
    # glass4 = Glass(500, -150)
    # glass5 = Glass("hohoho", 200)
    # glass6 = Glass(140, "ahahah")
