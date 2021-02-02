import sys
import math



def minimum_distance(x, y):
    a = list(zip(x,y))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    p1, p2, mi = closest_pair(ax,ay)
    return mi

def closest_pair(ax, ay):
    len_ax = len(ax)
    if len_ax <= 3:
        return brute_force(ax)
    mid = len_ax // 2
    Lx = ax[:mid]
    Rx = ax[mid:]
    
    lx = set(Lx)
    Ly = list()
    Ry = list()
    for x in ay:
        if x in lx:
            Ly.append(x)
        else:
            Ry.append(x)
            
    (p1, q1, m1) = closest_pair(Lx,Ly)
    (p2, q2, m2) = closest_pair(Rx,Ry)
    
    if m1 <= m2:
        d = m1
        mini = (p1,q1)
    else:
        d = m2
        mini = (p2, q2)
    
    (p3, q3, m3) = closest_split_pair(ax, ay, d, mini)
    
    if d <= m3:
        return mini[0], mini[1], d
    else:
        return p3, q3, m3
        
def brute_force(ax):
    mini = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    len_ax= len(ax)
    if len_ax == 2:
        return p1, p2, mini
    for i in range(len_ax - 1):
        for j in range(i + 1, len_ax):
            if i != 0 and j != 1:
                d = dist(ax[i],ax[j])
                if d < mini:
                    mini = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mini
    



    
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def closest_split_pair(p_x, p_y, delta, best_pair):
    len_x = len(p_x)
    mx_x = p_x[len_x // 2][0]
    
    s_y = [ x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    len_y = len(s_y)
    for i in range(len_y - 1):
        for j in range(i + 1, min(i + 7, len_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

