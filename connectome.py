import json
import numpy as np


class Connectome:
  """Simulates the 302-neuron C. elegans neural network with Leaky Integrate-and-Fire dynamics."""

  def __init__(self, config_path: str):
    with open(config_path, 'r') as f:
      self.config = json.load(f)

    self.num_neurons = self.config['neuron_count']
    self.dt = self.config['simulation']['dt_ms']
    self.tau = self.config['simulation']['decay_tau']
    self.v_rest = self.config['simulation']['v_rest_mv']
    self.v_th = self.config['simulation']['v_threshold_mv']

    # Initialize membrane potentials
    self.v = np.full(self.num_neurons, self.v_rest)

    # Synaptic weights matrix (302 x 302)
    np.random.seed(42)
    self.weights = np.random.randn(self.num_neurons, self.num_neurons) * 0.1

  def step(self, external_currents: np.ndarray) -> np.ndarray:
    """Runs a single integration step across all neurons."""
    synaptic_input = np.dot(self.weights, (self.v > self.v_th).astype(float))
    dv = (
        (-(self.v - self.v_rest) + synaptic_input + external_currents)
        / self.tau
        * self.dt
    )
    self.v += dv

    spikes = self.v >= self.v_th
    self.v[spikes] = self.config['simulation']['v_reset_mv']

    return spikes
