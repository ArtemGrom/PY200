class Glass:
    """Initialize object with name Glass"""
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: int):
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: int):
        self.occupied_volume = occupied_volume

    def add_water(self, add_water:[int, float]):
        if not isinstance(add_water, (int, float)):
            raise TypeError
        if add_water <= 0 or add_water > self.capacity_volume:
            raise ValueError
        self.occupied_volume += add_water

    def remove_water(self, remove_water: [int, float]):
        if not isinstance(remove_water, (int, float)):
            raise TypeError
        if remove_water <= 0 or remove_water > self.occupied_volume:
            raise ValueError
        self.occupied_volume -= remove_water


if __name__ == "__main__":
    glass = Glass(500, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(300)
    print(glass.occupied_volume)
    glass.remove_water(300)
    print(glass.occupied_volume)
    glass.remove_water(200)
    print(glass.occupied_volume)