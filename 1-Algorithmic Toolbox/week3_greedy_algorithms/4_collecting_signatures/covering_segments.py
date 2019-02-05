# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    if len(segments) == 1:
        points.append(segments[0].end)
    else:
        sorted_segments = sorted(segments, key = lambda x: x.end)
        # print(sorted_segments)
        #write your code here
        while len(sorted_segments) > 0:
            sorted_temp = []
            points.append(sorted_segments[0].end)
            # print(sorted_segments)
            # print(points)
            for i in range(len(sorted_segments)):
                if sorted_segments[i].start > sorted_segments[0].end:
                    sorted_temp.append(sorted_segments[i])
            sorted_segments = sorted_temp
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
