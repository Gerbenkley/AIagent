import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return print(f'Error: Cannot read "{target_file}" as it is outside the permitted working directory')
    if not os.path.isfile(target_file):
        return print(f'Error: File not found or is not a regular file: "{target_file}"')
    
    try: 
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string = file_content_string + f"[...File '{target_file}' truncated at 10000 characters.]"
            return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read a file in the specified directory, constrained to the working directory. It truncates to 10.000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read a file from, relative to the working directory. It has to be provided.",
            ),
        },
    ),
)