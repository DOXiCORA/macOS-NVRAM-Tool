import argparse
import subprocess

def get_nvram_variable(variable_name):
    try:
        result = subprocess.run(['nvram', variable_name], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error reading NVRAM: {e}")
        return None

def get_all_nvram_variables():
    try:
        result = subprocess.run(['nvram', '-xp'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error reading all NVRAM variables: {e}")
        return None

def set_nvram_variable(variable_name, value):
    try:
        subprocess.run(['sudo', 'nvram', f"{variable_name}={value}"], capture_output=True, text=True, check=True)
        print(f"{variable_name} set to {value}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting NVRAM: {e}")

def delete_nvram_variable(variable_name):
    try:
        subprocess.run(['sudo', 'nvram', '-d', variable_name], capture_output=True, text=True, check=True)
        print(f"{variable_name} deleted")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting NVRAM: {e}")

# Set up the argument parser
parser = argparse.ArgumentParser(description="Edit macOS NVRAM variables.")
parser.add_argument("action", choices=["get", "get-all", "set", "delete"], help="Action to perform (get, get-all, set, delete)")
parser.add_argument("variable", nargs='?', help="The NVRAM variable to interact with", default=None)
parser.add_argument("--value", help="The value to set the NVRAM variable to (required for set action)", required=False)

# Parse the arguments
args = parser.parse_args()

# Perform the action
if args.action == "get":
    if args.variable is None:
        parser.error("The variable name is required for the get action.")
    value = get_nvram_variable(args.variable)
    if value is not None:
        print(f"{args.variable}: {value}")
elif args.action == "get-all":
    all_vars = get_all_nvram_variables()
    if all_vars is not None:
        print(all_vars)
elif args.action == "set":
    if args.variable is None or args.value is None:
        parser.error("The variable name and --value parameter are required for the set action.")
    set_nvram_variable(args.variable, args.value)
elif args.action == "delete":
    if args.variable is None:
        parser.error("The variable name is required for the delete action.")
    delete_nvram_variable(args.variable)