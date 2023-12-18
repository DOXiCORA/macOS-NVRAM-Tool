# NVRAM Tool for macOS
# DOXiCORA

`nvram_tool.py` is a Python script for interacting with the Non-Volatile Random Access Memory (NVRAM) on macOS systems. It provides a command-line interface to get, set, and delete NVRAM variables, as well as to list all NVRAM variables.

## Warning

Modifying NVRAM settings can affect system behavior and stability. It should only be done by users who understand the implications of making changes to system settings at this level. Always ensure you have a current backup of your system before making any changes.

## Prerequisites

- Python 3.x
- macOS system

## Usage

To use `nvram_tool.py`, navigate to the directory containing the script and run it with Python 3. Depending on the action you wish to perform, different arguments may be required.

### Getting the Value of an NVRAM Variable

```bash
python3 nvram_tool.py get <variable_name>

### Setting the Value of an NVRAM Variable
sudo python3 nvram_tool.py set <variable_name> --value <value>

### Deleting an NVRAM Variable
sudo python3 nvram_tool.py delete <variable_name>

### Listing All NVRAM Variables
python3 nvram_tool.py get-all

### Help
python3 nvram_tool.py -h