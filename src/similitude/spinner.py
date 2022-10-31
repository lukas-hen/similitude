import sys
import time
import threading

frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in frames:
                yield cursor

    def __init__(self, msg: str = "", delay: int = None):
        self.msg = msg
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        while self.busy:
            out = f"{next(self.spinner_generator)} {self.msg}"
            sys.stdout.write(out)
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write("\b" * len(out))
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        sys.stdout.write("\n")
        if exception is not None:
            return False
