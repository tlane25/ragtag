# prototype-v1

chat doc prototype v1

## Front-End

To link uploading with back-end:

- Change `vite.config.ts` proxy target for `/api` route to be the address of the backend (e.g. `http://localhost:3000`)
- `npm run dev`



## Back-End

### Installation
#### Create virtual python environment(.venv) running python 3.12
##### On Mac
1. Open Terminal
2. Navigate to the directory where you want to create the virtual env
3. Create venv: `python3 -m venv env`
4. Activate: `source env/bin/activate`
5. Install Libraries with pip(possibly pip3)
6. When you're done, deactivate: `deactivate'
*you will need to activate venv in each terminal you want to use it*

#### Setup
Install FastAPI
`pip install fastapi`

Run (from `/back`)
`fastapi dev main.py`

