class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Just a glass of water

        :param capacity_volume: all volume of the glass
        :param occupied_volume: occupied volume only
        """
        # print(self, "from init")
        # print(".__dict__ from init:", self.__dict__)
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        # print(".__dict__ from init:", self.__dict__)


if __name__ == "__main__":
    glass = Glass(200, 0)
    print(glass)
    print(glass.__class__)
    # print(glass.__dict__)
    # print(glass.__delattr__("occupied_volume"))
    print(glass.__dict__)
    print(glass.__dir__)
    print(glass.__doc__)
    print(dir(glass))
