class Tmp:
    # static variable
    counter = 0

    def __init__(self, name='', id=None):
        self.name = name
        self.id = id
        Tmp.counter += 1

    @staticmethod
    def get_counter():
        return Tmp.counter

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> int:
        return self.id

    def set_name(self, name: str):
        self.name = name

    def set_id(self, id: int):
        self.id = id