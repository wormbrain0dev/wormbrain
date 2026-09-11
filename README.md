# WORMBRAIN 🪱

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Connectome: White et al.](https://img.shields.io/badge/Connectome-302_Neurons-emerald.svg)](#)

A biophysical *Caenorhabditis elegans* connectome simulation environment and autonomous agent driver. 

`wormbrain` models all 302 traced neurons and ~7,000 synaptic connections using a Leaky Integrate-and-Fire (LIF) neural network framework driven by amphid sensory inputs.

## 🔬 Features

- **Full Connectome Mapping:** Built on OpenWorm & White et al. EM reconstructions.
- **Biophysical Membrane Dynamics:** Realistic membrane potential integration ($V_{rest} = -70\text{ mV}$, $V_{th} = -50\text{ mV}$).
- **Sensory-to-Motor Loop:** Amphid sensilla (ASE, ASH) pixel-luminance mapping to motor interneurons (AVA, AVB, SMB, RME).
- **Headless Telemetry Export:** Live WebSockets/JSON feed for 3D visualization frontends.

## 🚀 Quickstart

```bash
git clone [https://github.com/your-username/wormbrain.git](https://github.com/your-username/wormbrain.git)
cd wormbrain
pip install -r requirements.txt
python -m wormbrain.simulator --config configs/c_elegans_302.json --steps 1000
