"""Demonstrate the Lorenz-III model."""

from matplotlib import pyplot as plt
from numpy import eye

import dapper.mods as modelling
from dapper.mods.LorenzIII import step, x0
from dapper.tools.viz import amplitude_animation

simulator = modelling.with_recursion(step, prog="Simulating")

N = 3
M = len(x0)
E0 = x0 + 1e-2*eye(M)[:N]

dt = 0.004
xx = simulator(E0, k=2000, t=0, dt=dt)

ani = amplitude_animation(xx, dt=dt, interval=10)
plt.show()
