import os
import shutil

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