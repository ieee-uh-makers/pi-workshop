import time
from typing import List
import random


class Region(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        return "X: %d Y: %d W: %d H: %d" % (self.x, self.y, self.w, self.h)


class DetectionGame(object):

    def __init__(self, level: int=1):
        self.level = level
        self.started = False

        self.levels = {1: {"win_start": 1, "win_end": 4},
                       2: {"win_start": 2, "win_end": 4},
                       3: {"win_start": 2, "win_end": 5},
                       4: {"win_start": 2, "win_end": 4}}

        self.win_window = self.levels[level]['win_end'] - self.levels[level]['win_start']

        self.counter = 0

    def start(self):
        self.started = True
        self.start_time = time.time()

    def detections(self) -> List[Region]:

        time.sleep(0.1)

        tss = time.time() - self.start_time

        if tss > self.levels[self.level]['win_end']:
            print("You missed it!")

        if self.level == 1:
            return self._detections_level1(tss)
        elif self.level == 2:
            return self._detections_level2(tss)
        elif self.level == 3:
            return self._detections_level3(tss)
        elif self.level == 4:
            return self._detections_level4(tss)

    def _detections_level1(self, tss):

        if tss >= self.levels[1]['win_start'] and tss <= self.levels[1]['win_end']:
            coeff = tss/self.win_window
            r = Region(coeff * 500 + int(random.random() * 5), coeff * 500 + int(random.random() * 5)
                       , 100 + int(random.random() * 100),
                       100 + int(random.random() * 100))
            return [r]

        return []

    def _detections_level2(self, tss):

        if tss >= self.levels[2]['win_start'] and tss <= self.levels[2]['win_end']:
            coeff = tss/self.win_window
            r = Region(coeff * 500 + int(random.random() * 5), coeff * 500 + int(random.random() * 5)
                       , 100 + int(random.random() * 100),
                       100 + int(random.random() * 100))
            return [r]
        else:
            if self.counter == 5:
                coeff = tss/self.win_window
                r = Region(coeff*500+int(random.random() * 5), coeff*500+int(random.random() * 5)
                           , 100+int(random.random() * 100),
                           100+int(random.random() * 100))
                self.counter = 0
                return [r]
            else:
                self.counter += 1

        return []

    def _detections_level3(self, tss):
        print(tss)
        if tss >= self.levels[3]['win_start'] and tss <= self.levels[3]['win_end']:
            if self.counter == 1:
                coeff = tss/self.win_window
                r = Region(coeff*500+int(random.random() * 5), coeff*500+int(random.random() * 5)
                           , 100+int(random.random() * 100),
                           100+int(random.random() * 100))
                self.counter = 0
                return [r]
            else:
                self.counter += 1
        else:
            if self.counter == 5:
                coeff = tss/self.win_window
                r = Region(coeff*500+int(random.random() * 5), coeff*500+int(random.random() * 5)
                           , 100+int(random.random() * 100),
                           100+int(random.random() * 100))
                self.counter = 0
                return [r]
            else:
                self.counter += 1

        return []

    def _detections_level4(self, tss):

        rects = []
        for i in range(0, int(random.random()*4)):
            w = int(random.random() * 100)
            h = int(random.random() * 100)

            x = int(random.random() * 540)
            y = int(random.random() * 380)

            rects.append(Region(x, y, w, h))

        if tss >= self.levels[4]['win_start'] and tss <= self.levels[4]['win_end']:
            if self.counter == 1:
                coeff = tss/self.win_window
                r = Region(coeff*500+int(random.random() * 5), coeff*500+int(random.random() * 5)
                           , 100+int(random.random() * 100),
                           100+int(random.random() * 100))
                self.counter = 0
                rects.append(r)
            else:
                self.counter += 1

        return rects

    def alarm(self) -> bool:
        tss = time.time() - self.start_time

        if tss >= self.levels[self.level]['win_start'] and tss <= self.levels[self.level]['win_end']:
            print("Success!")
            return True
        else:
            print("False positive. Try again.")
            return False
