from .key import KeyPair

if __name__ == "__main__":
    variable = "foo"
    print(variable)

    def change_variable(variable):
        variable = "bar"
        return variable

    change_variable(variable)
    print(variable)
