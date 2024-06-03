import os
import asyncio
import subprocess
import argparse

# Specify the path to the folder and the markdown file
folder_path = "./README.MD"

async def run_script(script_path, args, folder_path):
    command = ['python', script_path, folder_path] + args
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stdout:
        print(f'[stdout from {script_path}]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr from {script_path}]\n{stderr.decode()}')

async def main(args):
    scripts_dir = './scripts'
    script_files = [os.path.join(scripts_dir, f) for f in os.listdir(scripts_dir) if f.endswith('.py')]
    
    # Always execute all scripts in the scripts directory
    tasks = [run_script(script, args, folder_path) for script in script_files]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run specified Python scripts asynchronously.")
    parser.add_argument('script_args', metavar='ARG', type=str, nargs='*', help='arguments to be passed to the scripts')
    args = parser.parse_args()

    # Assign the parsed arguments to a variable
    script_args = args.script_args


    # Run the main function with the provided script arguments
    asyncio.run(main(script_args))
