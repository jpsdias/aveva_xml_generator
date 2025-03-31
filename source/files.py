import os
import shutil

def load_file_names(csv_file_path):
    obj_list = []
    with open(csv_file_path, 'r', encoding='utf-16') as file:
        for line in file:
            # Remove any leading/trailing whitespace including newline characters.
            object = line.strip()
            if object:  # Only add non-empty lines.
                obj_list.append(object)
    return obj_list

def copy_model_file(model_file_path, objects, output_dir):
    """
    Copies the model XML file for each file name, saving the copy as {object}.xml.
    """
    # Ensure the output directory exists.
    os.makedirs(output_dir, exist_ok=True)
    
    for object in objects:
        # Construct the output file path using the onject name.
        output_file = os.path.join(output_dir, f"{object}.xml")
        # Copy the model file to the new file.
        shutil.copyfile(model_file_path, output_file)
        print(f"Copied model file to: {output_file}")

if __name__ == "__main__":
    # Assume the current working directory is PROJECT_ROOT.
    base_dir = os.getcwd()

    Line = "Ingredients"

    model_file_general = os.path.join(base_dir, "db", "models", "general.xml")
    model_file_pid = os.path.join(base_dir, "db", "models", "pid.xml")
    output_dir = os.path.join(base_dir, "output", Line)
    
    general_file_path = os.path.join(base_dir, "db", Line, "general.csv")
    pid_file_path = os.path.join(base_dir, "db", Line, "pid.csv")
    
    # Load valve names from CSV.
    file_names = load_file_names(general_file_path)
    # Copy the model file for each valve.
    copy_model_file(general_file_path, file_names, output_dir)
    
    # Load valve names from CSV.
    file_names = load_file_names(pid_file_path)
    # Copy the model file for each valve.
    copy_model_file(pid_file_path, file_names, output_dir)
