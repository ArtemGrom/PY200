class Glass:
    "Initialize object with name Glass"
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: int):
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: int):
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
