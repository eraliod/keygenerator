from . import KeyPair


if __name__ == "__main__":
    key = KeyPair()

    print(key.public.format(format_type="multiline"))