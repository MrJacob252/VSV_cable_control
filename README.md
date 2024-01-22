# VSV_cable_control
Repository for a school group project for a machine vision class (VSV).

## Task

Choose a camera and light setup and create a software solution to indetify defect cables.

## Solution

Solution is a neural network created on images taken in the school laboratory. The dataset was expanded and then labeled using [RoboFlow](https://app.roboflow.com/).

Neureal network itself was also used using Roboflow utilising ImageNet as a starting point

Final solutions is a predict.py script that provides a GUI for user to appload a photo and then it uses Roboflow's API to connect to our workspace and predicts the cables state using our network

**Warnig** API key is not included in the github code

## Requirements
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for creating the GUI
  - ```
    pip install customtkinter
    ```
- Roboflow for connecting to the roboflow API
  - ```
    pip install roboflow
    ```

## Running the script

- API Key needs to be placed into the predict.py script as a string
  - ```
    app = App("!!API_KEY_HERE!!")
    ```
- Run the script