import os

def get_files_info(working_directory, directory="."):
    try: 
        #PATHING PARSING
        full_path = os.path.join(working_directory, directory)
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        #ERROR AND SCOPE HANDLING
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.exists(abs_full_path):
            return f'Error: The directory "{directory}" does not exist' 
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'
        
        try:
            items = os.listdir(abs_full_path)
        except OSError as e:
            return f'Error: Unable to list directory "{directory}": {str(e)}'
        
        items_list = []
        for item in items:
            item_path = os.path.join(abs_full_path, item)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                items_list.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                items_list.append(f"- {item}: Error: {str(e)}")
        return "\n".join(items_list) 
    
    except OSError:
        return f'Error: Permission denied for "{directory}"'