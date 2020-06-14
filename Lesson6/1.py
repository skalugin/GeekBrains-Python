class Traffic:
    def running(self):
        self._color = {'red': 5, 'yellow': 2, 'green': 5}
        for key, value in self._color.items():
            print("Running:", key, value)

t1 = Traffic()
t1.running()