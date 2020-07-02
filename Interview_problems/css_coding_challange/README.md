# Usage

## Prerequisite check 

* Check python version  
    ```bash
    $ python3 --version
    Python 3.8.0
    ```

* If python is not installed follow following steps on a mac. 

  + install python

    ```bash
    $ /usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

    $ brew doctor 
    Your system is ready to brew.
    
    $ brew install python3

* Check pip3 version 
    ```
    $ pip3 --version
    pip 20.0.2 from ..../site-packages/pip (python 3.8)
    ```

## Setup

* download the zip and unzip at a location 

* go to the directory of unzip
    ```bash
    $ cd ~/Downloads/css
    ```

* Create a virtual environment
    ```bash
    $ python3 -m venv css_env
    $ . css_env/bin/activate
    ```

* Install django
    ```bash
    (css_env) $ pip install django
    (css_env) $ django-admin --version
    3.0.4
    ```

## Run Simlator

* default
    ```bash
    $ python manage.py run_simulator
    ```

* custom options
  + copy the orders-custom.json at ~/Downloads/css/orders-custom.json first
  + run following
    ```bash
    $ python manage.py run_simulator --order_file="orders-custom.json" --order_rate=20
    ```

* get help
    ```bash
    $ python manage.py run_simulator --help
    ```

## Logs

* Logs are present in the directory ~/Downloads/css/logs/.
* every new run should create a new log file with name \<timestamp>_simulator.log