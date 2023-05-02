# user-management-api-1

A Python microservice / API to handle login, signup, and user management functions for applications that require user management features. Built with:
* [FastAPI](https://fastapi.tiangolo.com/)
* [Firebase Auth](https://firebase.google.com/docs/auth)
* Packages and environment managed with [pip](https://pip.pypa.io/en/latest/development/)

API should be able to be integrated with any web application. Separate Firebase projects and Postgres databases will be created for each web app, allowing the same API to be used between different applications.

## Setting Up A Virtual Environment

1. Make sure you have the latest version of Python downloaded (currently Python 3.11). Get it [here](https://www.python.org/downloads/).

2. Install latest version of pip

```
python3 -m pip install --user --upgrade pip
```

3. Clone this repository.

4. Navigate to the project's root directory, and create your virtual environment in a directory called "env"

```
python3 -m venv --system-site-packages env
```

**_NOTES:_**  
* `--system-site-packages` gives your virtual environment access to the site-packages directory (aka. where packages / dependencies will be installed)
* `env` is the name of the output directory containing information about your virtual environment (this can be called `banana` and the directory will be named accordingly)

5. Activate the virtual environment by running the activate script inside.

```
source env/bin/activate
```
**_NOTE:_**  To leave the virtual environment - `deactivate` in the command line


6. If you have multiple versions of Python installed, make sure your code editor is using the correct interpreter by selecting the version of Python that matches the version specified inside your `pyvenv.cfg` file (located at env/pyvenv.cfg).

7. Install project dependencies from the provided `requirements.txt` file inside your virtual environment.

```
python3 -m pip install -r requirements.txt
```

8. Check your project dependencies in your virtual and global environments.

```
pip list
```

If everything was done correctly, the virtual environment should contain the project dependencies, while your global environment should not.


## Running Servers Locally
1. Activate your virtual environment.

2. Start your server on PORT 1234

```
uvicorn --port 1234 main:app --reload 
```

Now your API should be running locally, and you can test this with Postman or by writing scripts with the [requests](https://requests.readthedocs.io/en/latest/) package.
