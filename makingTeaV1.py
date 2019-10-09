def make_tea():
    fetch("Kettle")
    fetch("Water")
    add_x_to_y("Water", "Kettle")
    boil_water()
    fetch("Mug")
    fetch("Teabag")
    add_x_to_y("Teabag", "mug")
    fetch("Sugar")
    add_x_to_y("Sugar", "Mug")
    add_x_to_y("Boiling water", "Mug")
    stir()
    remove_y_from_x("Teabag", "Mug")
    add_x_to_y("Teabag", "Bin")
    add_x_to_y("Milk", "Mug")
    stir()
    print("You have sweet milky tea")


def fetch(str):
    return True


def add_x_to_y(x, y):
    return True


def boil_water() :
    return True


def stir():
    return True


def remove_y_from_x(y, x):
    return True


make_tea()
