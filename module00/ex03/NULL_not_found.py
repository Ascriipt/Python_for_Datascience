def NULL_not_found(object: any) -> int:
    types = {
        None: "Nothing: None ",
        float: "Cheese: nan ",
        int: "Zero: 0 ",
        str: "Empty: ",
        bool: "Fake: False "
    }
    key = type(object)
    if object is None:
        print(f"{types[None]}{key}")
    elif key in types and not object:
        print(f"{types[key]}{key}")
    elif isinstance(object, float):
        print(f"{types[key]}{key}")
    else:
        print("Type not Found")
    return 1
