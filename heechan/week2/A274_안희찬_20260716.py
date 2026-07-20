class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]  # 인덱스 0은 안 씀

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False