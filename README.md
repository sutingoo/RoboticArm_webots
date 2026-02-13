# Robotic Arm made in Webots

This project was a attempt to recreate the robot made in the project 'Crisálida' with my robotics investigation group.

## Characteristics
* **Simulator:** Webots R2025a.
* **Language:** Python 3.10+.
* **OS:** Ubuntu 22.04 LTS.
* **Control:** Movement implementation with mathematical functions.

## Demo
<p align="center" >
  <img src="Webots_Robot2.gif" width="500" title="Webots_arm">
</p>

## Structure
* `worlds/`: File `.wbt` with the scene (robot model and chess floor).
* `controllers/`:
    * `my_controller4.py`: Principal script for movement logic.

## Install
   Having installed Webots on Ubuntu 22.04. If not:
   ```bash
   sudo snap install webots
