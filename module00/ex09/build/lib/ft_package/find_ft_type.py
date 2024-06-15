def all_thing_is_obj(object: any) -> int:
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }
    key = type(object)
    if key in types:
        print(f"{types[key]} : {key}")
    elif key == str:
        print(f"{object} is in the kitchen : {key}")
    else:
        print("Type not found")
    return 42
