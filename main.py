from tasks import add

def create_tast():
    return add.delay(3, 3)

