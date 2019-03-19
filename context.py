class SelfOpen(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handler = None

    def __enter__(self):
        print("enter:", self.file_name)
        self.file_handler = open(self.file_name, "r")
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()


with SelfOpen('decorator.py') as file_:
    for line in file_:
        print(line)
