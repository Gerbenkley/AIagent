import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(target_file):
        return print(f'Error: File "{file_path}" not found.')
    if not target_file.endswith('.py'):
        return print(f'Error: "{file_path}" is not a Python file.')
    
    
    try:
        command = ["python", target_file] + args
        completed = subprocess.run(command, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)

        output_lines = []
        if completed.stdout.strip():
            output_lines.append(f"STDOUT:\n{completed.stdout.strip()}")
        if completed.stderr.strip():
            output_lines.append(f"STDERR:\n{completed.stderr.strip()}")
        if completed.returncode != 0:
            output_lines.append(f"Process exited with code {completed.returncode}")
        if not output_lines:
            return "No output produced."
        return "\n".join(output_lines)
    
    except subprocess.TimeoutExpired:
        return print(f'Error: Execution of "{file_path}" timed out after 30 seconds')
    except Exception as e:
        return print(f"Error: executing Python file: {e}")