import argparse
import fileinput
import sys


class Console:
    """A class to perform incoming console requests."""

    def run(self):
        """Run the console command to perform the requests."""
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'file', metavar='FILE',
            nargs='?', help='file to read, if empty, stdin is used')
        args = parser.parse_args()

        for request in fileinput.input(files=args.file):
            self._perform_request(request.rstrip())

    def _perform_request(self, request):
        """Perform the incoming request."""
        command, args = self._parse_request(request)

        if request == 'exit':
            raise KeyboardInterrupt

        print(f'{command=} {args=}')

    def _parse_request(self, request):
        """Parses the given request in 'command' and 'arguments'."""
        tokens = request.split()

        return [tokens[0], tokens[1:]]


if __name__ == '__main__':
    try:
        Console().run()
    except KeyboardInterrupt as e:
        print(e, file=sys.stderr)
