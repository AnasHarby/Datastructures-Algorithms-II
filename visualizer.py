import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualizer:
    """Visualizes a sorting algorithm using matplotlib."""
    def __init__(self, track):
        """Constructs a new visualizer.
        :type track: queue
        :param track: Tracking queue for the array that was sorted."""
        self.track = track

    def _animate(self, i):
        if self.track.empty():
            return []
        plt.clf()
        args = self.track.get()
        plt.hist(range(len(args)), len(args), weights=args)
        return []

    def start(self):
        """Starts a new execution for the plot."""
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._animate, interval=40)
        plt.show()
