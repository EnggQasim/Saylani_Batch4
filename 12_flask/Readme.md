# Create Virtual Envornment
* `python -m venv <name>`
    * `<name>\Scripts\activate`
    * `deactivate`
    * get all installed packages name in **requirements.txt**
        * `pip freeze > requirements.txt`

## Create Virtual envornment with conda
* `conda create --name <name>`
    * ` conda activate <name>`
    * `deactivate`
* install package from **requirements.txt**
    * `pip install -r requirements.txt`