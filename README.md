# NumFys
A resource for solving problems in computational physics using <code>Python</code>, covering many topics in physics.

## Set up the website on your system
1. Clone this repository:

    ```
    git clone https://github.com/numfys/numfys.git
    ```
2. Create and activate a new virtual environment:

    ```
    virtualenv -p /usr/bin/python3 venv
    source venv/bin/activate
    ```
3. Use pip to install the necessary packages and dependencies from `requirements.txt`, by running:

    ```
    pip3 install -r requirements.txt
    ```
    NB! The installation depends on the libraries `libmysqlclient` and `libjpeg`.
    These are found in the following apt packages: `libmysqlclient-dev` and `libjpeg8-dev`.
4. Set up the `SQLite` database by running the commands:

    ```
    ./manage.py makemigrations notebook
    ./manage.py migrate
    ```
5. Now it's time to run the Django development server. In the directory containing `manage.py`, run:

    ```
    ./manage.py runserver
    ```
6. To manage the website content, create a superuser and log in at 127.0.0.1:8000/admin:

    ```
    ./manage.py createsuperuser
    ```
---

Didn't work? Send us a message explaining what error message you got.

A project of the [Department of Physics](https://www.ntnu.edu/physics) at [NTNU](https://www.ntnu.edu/), supported by [Norgesuniversitetet](https://norgesuniversitetet.no).

___
## License

The content of this project itself is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/), and the underlying source code used to format and display that content is licensed under a [Modified License](LICENSE.md).
