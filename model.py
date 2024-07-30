from hnn_core import calcium_model


def create_model(detected=False):
    # calcium network
    net = calcium_model()

    # proximal
    weights_ampa_p1 = {'L2_basket': 2.028, 'L2_pyramidal': 1.683,
                       'L5_basket': 0.4751, 'L5_pyramidal': 0.001}
    weights_nmda_p1 = {'L2_basket': 0.916, 'L2_pyramidal': 2.762,
                       'L5_basket': 0.0614, 'L5_pyramidal': 0.000999}
    synaptic_delays_prox = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
                            'L5_basket': 1., 'L5_pyramidal': 1.}
    net.add_evoked_drive(
        'evprox1', mu=47.815, sigma=13.217, numspikes=1, weights_ampa=weights_ampa_p1,
        weights_nmda=weights_nmda_p1, location='proximal',
        synaptic_delays=synaptic_delays_prox, event_seed=4)

    # distal 1
    weights_ampa_d1 = {'L2_basket': 0.645, 'L2_pyramidal': 0.0107,
                       'L5_pyramidal': 0.0005}
    weights_nmda_d1 = {'L2_basket': 0.988, 'L2_pyramidal': 0.03,
                       'L5_pyramidal': 0.0149}
    synaptic_delays_d1 = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
                          'L5_pyramidal': 0.1}
    net.add_evoked_drive(
        'evdist1', mu=84.275, sigma=15.063, numspikes=1, weights_ampa=weights_ampa_d1,
        weights_nmda=weights_nmda_d1, location='distal',
        synaptic_delays=synaptic_delays_d1, event_seed=4)

    # distal 2
    if detected:
        # TODO: is this a bug? should weights_ampa be set to weights_ampa_d2?
        weights_ampa_d2 = {'L2_basket': 0.593, 'L2_pyramidal': 0.164,
                           'L5_pyramidal': 0.0464}
        weights_nmda_d2 = {'L2_basket': 0.175, 'L2_pyramidal': 0.0703,
                           'L5_pyramidal': 0.297}
        synaptic_delays_d2 = {'L2_basket': 0.1, 'L2_pyramidal': 0.1,
                              'L5_pyramidal': 0.1}
        net.add_evoked_drive(
            'evdist2', mu=169.273, sigma=50.396, numspikes=1, weights_ampa=weights_ampa_d1,
            weights_nmda=weights_nmda_d2, location='distal',
            synaptic_delays=synaptic_delays_d2, event_seed=4)

    # Simulate shank recording
    net.set_cell_positions(inplane_distance=30.)
    depths = list(range(-325, 2150, 100))
    electrode_pos = [(135, 135, dep) for dep in depths]
    net.add_electrode_array('shank', electrode_pos)

    return net
