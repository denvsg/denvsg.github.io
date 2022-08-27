import argparse


class Configure:
    parser = argparse.ArgumentParser(description="input parser")

    def __init__(self):
        # self.parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'),
        #                          help='the file where the sum should be written')

        self.parser.add_argument('--a', default=True, required=True, help="--p")
        self.parser.add_argument('--b', default=True, help="--p")
        self.parser.add_argument('--c', default=True, help="--p")
        self.parser.add_argument('--d', default=True, nargs="+", help="--p")
        self.parser.add_argument('--log', dest="log", nargs="*", help="--p")
        self.args = self.parser.parse_args()

    def __str__(self):
        return f"{self.args}"


def params():
    parser = argparse.ArgumentParser(description="input parser")
    parser.add_argument('--log', default=True, help="--p")
    args = parser.parse_args()
    print(args.log)


if __name__ == "__main__":
    args = Configure()
    print(args)
