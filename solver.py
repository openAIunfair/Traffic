import json
import madopt
import numpy as np


def solve(inst):
    m = madopt.IpoptModel()








    m.show_solver = True
    m.solve()
    return 0


inst = json.load(open('traffic.json'))
res = solve(inst)