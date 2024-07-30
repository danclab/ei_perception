import numpy as np
from hnn_core import JoblibBackend, simulate_dipole

from model import create_model


def run_detected_undetected_simulations(n_trials=100):

    # Create model for detected stimulus and run simulation
    net_ds = create_model(detected=True)
    with JoblibBackend(n_jobs=-1):
        _ = simulate_dipole(net_ds, tstop=450., n_trials=n_trials)
    np.save('shank_ds.npy', np.array(net_ds.rec_arrays['shank']._data))

    # Create model for undetected stimulus and run simulation
    net_us = create_model(detected=False)
    with JoblibBackend(n_jobs=-1):
        _ = simulate_dipole(net_us, tstop=450., n_trials=n_trials)
    np.save('shank_us.npy', np.array(net_us.rec_arrays['shank']._data))


if __name__=='__main__':
    run_detected_undetected_simulations()
