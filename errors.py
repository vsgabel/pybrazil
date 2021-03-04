class InvalidLength(Exception):
    def __init__(self, length, target, minimum=True):
        if minimum:
            self.message = f"Minimum length of {target} is {length}"
        else:
            self.message = f"Maximum length of {target} is {length}"
        super().__init__(self.message)