def NULL_not_found(object: any) -> int:

    obj_type = type(object)
    if object is None:
        print(f"Nothing: {object} {obj_type}")
        return 0
    elif obj_type == float:
        print(f"Cheese : {object} {obj_type}")
        return 0
    elif obj_type == int:
        print(f"Zero: {object} {obj_type}")
        return 0
    elif object == " ":
        print(f"Empty : {object} {obj_type}")
        return 0
    elif obj_type == bool:
        print(f"Fake: {object} {obj_type}")
        return 0
    else:
        print("Type not found")
        return 1
