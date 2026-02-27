import calendar
from datetime import datetime

class InteractiveCalendar:
    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month

    def display_calendar(self):
        print(calendar.month(self.year, self.month))

    def run(self):
        while True:
            self.display_calendar()
            print("Commands: [n]ext month, [p]revious month, [ny] next year, [py] previous year, [q]uit")
            command = input("Enter command: ").strip().lower()

            if command == 'n':
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
            elif command == 'p':
                if self.month == 1:
                    self.month = 12
                    self.year -= 1
                else:
                    self.month -= 1
            elif command == 'ny':
                self.year += 1
            elif command == 'py':
                self.year -= 1
            elif command == 'q':
                print("Exiting Interactive Calendar.")
                break
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    cal = InteractiveCalendar()
    cal.run()
