import sys

kitchen = ["Kettle", "Mug", "Water", "Milk", "Teaspoons", "Teabags", "Sugar", "Bin"]
kettle = []
mug = []


def make_tea():
    amount_of_sugar = -1
    count = 0

    while amount_of_sugar not in range(0, 99):
        too_sassy = False
        if count <= 3:
            try:
                amount_of_sugar = int(input("How many teaspoons of sugar do you want? please enter a value between 0 and 99"))
            except ValueError:
                print("thats not a number")
        elif count <= 10:
            try:
                amount_of_sugar = int(input("come on now do you want any sugar? please enter a value between 0 and 99"))
            except ValueError:
                print("thats not a number")
        else:
            try:
                amount_of_sugar = int(input("Last chance. please enter a value between 0 and 99"))
            except ValueError:
                print("thats not a number")
            too_sassy = True

        if too_sassy:
            sys.exit()
        count += 1

    try:
        boil_water()
    except NoKettle:
        print("You dont have a kettle!!")
        sys.exit()
    except NoWater:
        print("You dont have any watter!!")
        sys.exit()

    try:
        add_dry_components(amount_of_sugar)
    except NoMug:
        print("You dont have a Mug!!")
        sys.exit()
    except NoTeabag:
        print("You dont have any Teabags!!")
        sys.exit()
    except NoSugar:
        print("You dont have any Sugar!!")
        sys.exit()

    # add_item_to_container("Boiling water", "Mug")
    # stir()
    # remove_item_from_container("Teabag", "Mug")
    # add_item_to_container("Teabag", "Bin")
    # add_item_to_container("Milk", "Mug")
    # stir()
    # print("You have sweet milky tea")


def fetch(item):
    kitchen.remove(item)


def put_back(item):
    kitchen.append(item)


def add_dry_components(amount_of_sugar):
    if "Mug" in kitchen:
        fetch("Mug")
        add_item_to_container("Teabag", mug)
    else:
        raise NoMug
    if "Teabag" in kitchen:
        fetch("Teabag")
    else:
        raise NoTeabag
    if amount_of_sugar > 0:
        if "Sugar" in kitchen:
            fetch("Sugar")
            add_item_to_container("Sugar", mug)
        else:
            raise NoSugar


def add_item_to_container(item, container):
    container.append(item)


def boil_water():
    if "kettle" in kitchen:
        fetch("Kettle")
    else:
        raise NoKettle
    if "Water" in kitchen:
        fetch("Water")
    else:
        raise NoKettle
    add_item_to_container("Water", kettle)
    add_item_to_container("Boiled water", kitchen)


def stir():
    return True


def remove_item_from_container(item, container):
    container.remove(item)


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoKettle(Error):
    """Raised when kettle is missing"""
    pass


class NoWater(Error):
    """Raised when kettle is missing"""
    pass


class NoMug(Error):
    """Raised when mug is missing"""
    pass


class NoTeabag(Error):
    """Raised when teabag is missing"""
    pass


class NoSugar(Error):
    """Raised when sugar is missing"""
    pass


make_tea()
