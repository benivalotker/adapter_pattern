import adapter_

def main():
    # get producer object with the wrong hardware (interface)
    computer  = adapter_.Computer()

    # add the object to adapter object
    adapter = adapter_.Adapter(computer)

    # noe the client can use the fixes computer hardware
    client  = adapter_.Client(adapter)

    print(client)


if __name__ == "__main__":
    main()