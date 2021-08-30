# StocKeeper

Stock management software for footwear shop built using python-eel and Svelte.

![Screenshot](https://github.com/mochatek/StocKeeper/blob/master/Screenshot.png)

## Prerequisites

- [Python3](https://www.python.org/) Installed

- [Node.js](https://nodejs.org/en/) Install

## Installation

Frontend is built using [Svelte](https://svelte.dev/)

- cd into UI folder and install the required dependancies: ```npm install```

- Run ```npm run dev``` to view the interface during development

Application is built using [python-eel](https://github.com/ChrisKnott/Eel)

- cd into app folder and create virtual environment: ```python -m venv env```

- Activate the environment: ```env\Scripts\activate```

- Install the dependancies: ```pip install -r requirements.txt```

## How to Build the Interface

To build the UI, run the command: ```npm run build```, inside UI folder.

Once the build is complete, JS and CSS bundles will be generated inside _app/web/assets/_

## How to Run the Application

To launch the application, run the command: ```python main.py```, inside app folder (virtual environment activated).

## How to Package the Application

- Use [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) for packaging.

- Follow this [Reference](https://github.com/ChrisKnott/Eel#building-distributable-binary-with-pyinstaller) for packaging  python-eel application using PyInstaller.
