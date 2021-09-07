class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float], material: str):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане
        self.material = material

    def get_material(self):
        return self.material


if __name__ == "__main__":
    glass = Glass(500, 100, "paper")
    print(glass.material)
