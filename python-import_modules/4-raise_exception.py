def raise_exception():
    raise TypeError


# Test the function
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
