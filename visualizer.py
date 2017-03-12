import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualizer():
    def __init__(self, track):
        self.track = track

    def _animate(self, i):
        if self.track.empty():
            return []
        plt.clf()
        args = self.track.get()
        plt.hist(range(len(args)), len(args), weights=args)
        return []

    def start(self):
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._animate, interval=40)
        plt.show()
