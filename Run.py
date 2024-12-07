import subprocess

# Function to run a Python script
def run_script(script_name):
    if script_name == 'visualization.py':
        # Run the visualization script with streamlit
        result = subprocess.run(['streamlit', 'run', script_name], capture_output=True, text=True)
    else:
        # Run other Python scripts normally
        result = subprocess.run(['python', script_name], capture_output=True, text=True)

    print(f"Running {script_name}:\n")
    print(result.stdout)
    if result.stderr:
        print(f"Error in {script_name}:\n{result.stderr}")
    print("-" * 40)

# List of scripts to run
scripts_to_run = ['scrape_reviews.py', 'scrape_subreviews.py', 'write.py', 'mining.py', 'visualization.py']

# Run all scripts sequentially
def run_all_scripts():
    for script in scripts_to_run:
        run_script(script)

# Call the function to run scripts when the file is executed
run_all_scripts()
