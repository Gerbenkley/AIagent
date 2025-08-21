import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
            print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        return print(f"Error writing file: {e}")
