import matplotlib.pyplot as plt

from simphony.libraries import siepic
from simphony.simulators import MonteCarloSweepSimulator, SweepSimulator

gc_input = siepic.GratingCoupler()
y_splitter = siepic.YBranch()
wg_long = siepic.Waveguide(length=150e-6)
wg_short = siepic.Waveguide(length=50e-6)
y_recombiner = siepic.YBranch()
gc_output = siepic.GratingCoupler()


# connect the components to each other
# connect pins directly:
y_splitter["pin1"].connect(gc_input["pin1"])

# connect components with components
y_splitter.connect(wg_long)

# combination of the two:
y_splitter["pin3"].connect(wg_short)
# y_splitter.connect(wg_short["pin1"])

y_recombiner.multiconnect(gc_output, wg_short, wg_long)

simulator = SweepSimulator(1500e-9, 1600e-9)
simulator.multiconnect(gc_input, gc_output)

f, p = simulator.simulate()
plt.plot(f, p)
plt.title("MZI")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Transmission (dB)")
plt.tight_layout()
plt.show()
