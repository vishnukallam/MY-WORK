class CustomException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        print(f"CustomException: {self.message}")
x = CustomException
x.__str__
