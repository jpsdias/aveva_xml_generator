import os

def process_file(input_file, output_file_general, output_file_pid):
    # Open the file with the proper encoding
    with open(input_file, 'r', encoding='utf-16') as f:
        lines = f.readlines()

    general = []
    pid = []

    for i, line in enumerate(lines, start=1):
        # Skip the first 5 lines.
        if i <= 5:
            continue

        # Remove leading/trailing whitespace.
        line_stripped = line.strip()

        if '_ProIntlk,' in line_stripped:
            TempGeneralLine = line_stripped.split('_', 3)[2]
            general.append(TempGeneralLine + "\n")

        if '_Intlk,' in line_stripped:
            TempPidLine = line_stripped.split('_', 3)[2]
            pid.append(TempPidLine + "\n")

    with open(output_file_general, 'w', encoding='utf-16') as f:
        f.writelines(general)

    with open(output_file_pid, 'w', encoding='utf-16') as f:
        f.writelines(pid)

if __name__ == "__main__":
    # Assume the current working directory is PROJECT_ROOT.
    base_dir = os.getcwd()

    folder = "ZL1"
    
    # Define file paths relative to PROJECT_ROOT.
    input_file_path = os.path.join(base_dir, "db", folder, "Objects.csv")
    output_file_general_path = os.path.join(base_dir, "db", folder, "general.csv")
    output_file_pid_path = os.path.join(base_dir, "db", folder, "pid.csv")

    process_file(input_file_path, output_file_general_path, output_file_pid_path)
    # print(f"Processed file saved as: {output_file_path}")
