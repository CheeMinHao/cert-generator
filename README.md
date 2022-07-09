# Certificate Generator

## Steps
1. Initialise a python virtual env environment (Recommended but optional)
2. Install dependencies by using command `pip install -r requirements.txt`
3. Prepare the required folders - `templates/` and `generated-certificates/`
3. Updates `names.csv` or upload one yourself with the exact same file name.
4. Upload an image of your choice that represents your certificate under `templates/` folder
5. Change the necessary parameters in `param.py`
6. Upload fonts where necessary under the `fonts/` folder.
7. At the project's root directory, you will need to run the command `python main.py` or `python3 main.py` based on your python version
8. You should be able to see your generated certificates under `generated-certificates/<your-certificate>.pdf`

## Optional Choices
- Feel free to switch your fonts in `main.py`
- You can also modify the alignment and axises under `main.py` as well, for each parameter (name, award, reason)

<br>

Author - Chee Min Hao (Monash University)