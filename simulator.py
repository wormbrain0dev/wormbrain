import argparse
import time
import numpy as np
from .connectome import Connectome


def run_simulation(config_file: str, steps: int):
  brain = Connectome(config_file)
  print(f'[*] Connectome loaded: {brain.num_neurons} neurons running.')

  for t in range(steps):
    sensory_stimulus = np.zeros(brain.num_neurons)
    sensory_stimulus[0:4] = np.random.uniform(0.0, 15.0, size=4)

    spikes = brain.step(sensory_stimulus)
    firing_count = np.sum(spikes)

    if t % 100 == 0:
      print(
          f'[Step {t:04d}] Active Neurons: {firing_count}/302 | Mean Vm:'
          f' {np.mean(brain.v):.2f} mV'
      )
    time.sleep(0.001)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='WORMBRAIN Simulation Engine')
  parser.add_argument(
      '--config', type=str, default='configs/c_elegans_302.json'
  )
  parser.add_argument('--steps', type=int, default=500)
  args = parser.parse_args()

  run_simulation(args.config, args.steps)
