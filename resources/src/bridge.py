from time import sleep
import can

def main():
    bus0 = can.Bus('can0', bustype='socketcan', bitrate=500000, receive_own_messages=False)
    bus1 = can.Bus('can1', bustype='socketcan', bitrate=500000, receive_own_messages=False)

    def parseData0(msg: can.Message):
        bus1.send(msg)
        print(f"B->S {msg}")

    def parseData1(msg: can.Message):
        bus0.send(msg)
        print(f"S->B {msg}")

    notifier2 = can.Notifier(bus1,[parseData1])
    notifier = can.Notifier(bus0,[parseData0])

    try:
        while True:
            sleep(100)
    except Exception as e:
        print(e)
    finally:
        notifier.stop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Receiver stopped")
    except Exception as e:
        print(e)