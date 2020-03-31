import argparse
import fileinput

from parking_lot.parking_manager import ParkingManager


class Console:
    """A class to perform incoming console requests."""

    def __init__(self):
        """Create a new parking manager instance."""
        self.manager = ParkingManager()

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

        if command == 'exit':
            raise KeyboardInterrupt

        if hasattr(self.manager, command):
            try:
                output = getattr(self.manager, command)(*args)
            except Exception as e:
                output = str(e)
        else:
            output = f'Given command [{command}] does not exists'

        print(self._prepare_output(output))

    def _parse_request(self, request):
        """Parses the given request in 'command' and 'arguments'."""
        tokens = request.split()

        return [tokens[0], tokens[1:]]

    def _prepare_output(self, output):
        """Prepares the output in printable format."""
        if isinstance(output, list):
            return ''.join(['{:12}{:19}{}\n'.format(*row) for row in output]).rstrip()

        return output


if __name__ == '__main__':
    try:
        Console().run()
    except KeyboardInterrupt:
        pass
