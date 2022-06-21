def isiterable(obj) -> bool:
    try:
        _ = iter(obj)
    except:
        return False
    return True