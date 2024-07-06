# AMAXInit

AMXXInit is a Python script designed to automate the setup process for your Counter-Strike 1.6 server environment on GNU/Linux systems. It uses Python to download necessary files and configure your server environment.

>This script is intended for use on GNU/Linux systems only.

## Why?

This script was created for fun and playing some web crawling techniques :o
>I'm Also as an avid player of Counter-Strike 1.6 :D

## TL;DR

```shell
python3 main.py
pip install -r requirements.txt
```

## Installation

1. **Clone the repository:**

   ```shell
   git clone <repository_url>
   cd AMXXInit
   ```

2. **Install dependencies using pip:**

   Ensure you have Python 3 and pip installed. Then, install the required Python packages listed in `requirements.txt`:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script:**

   Simply execute `main.py` using Python 3 to automate the initialization of your Counter-Strike 1.6 server environment:

   ```shell
   python3 main.py
   ```

   Follow the prompts and instructions provided by the script to complete the setup.

2. Specify download path:

    You can optionally specify a custom download path using the `--path` argument. This is useful if you want to download the server files to a specific directory. By default, files will be downloaded to the current directory (`./`).

    ```shell
    python3 main.py --path /path/to/download/directory/
    ```
    
    Replace /path/to/download/directory/ with the desired directory where you want the files to be saved.

3. Lazy guys:
    
    For users who prefer not to read the README file, simply type `make` or `make help`. This will provide the necessary guidance and instructions.
    
    ```shell
    make help 
    ```

## License

This project is licensed under the [MIT License](./LICENSE).
