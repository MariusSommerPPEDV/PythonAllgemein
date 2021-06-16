from typing import NewType


class Engine():

    def __init__(self, cylinder_count: int, volume: float, layout : str, weight: int):
        self.Cylinder = cylinder_count
        self.Volume = volume
        self.Layout = layout
        self.Weight = weight

    def __str__(self):
        description = f"Enginetype: {self.Layout}\nCylindercount: {self.Cylinder}\nVolume: {self.Volume}\nWeight:" \
                      f" {self.Weight}"
        return description


Turbo = Engine(4, "3.2", "Inline", 200)


UserId = NewType("UserId", int)


def get_user_name(user_id: UserId) -> str:
    """Gibt den der ID zugehörigen Usernamen zurück"""
    return 123


a = get_user_name(100)
b = get_user_name(UserId(2333))


def get_engine_cylinders(engine: Engine):
    return engine.Cylinder


print(get_engine_cylinders(Turbo))