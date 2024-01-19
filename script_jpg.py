import os
import subprocess

def convert_to_jpg(input_path, output_path, target_height):
    # Create the output folder if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Recursively go through the input folder
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith(".jpg"):
                # Construct the input and output file paths
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_path)
                output_file = os.path.join(output_path, relative_path)

                # Create the output folder for the current file if it doesn't exist
                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                # Construct and execute the convert command
                command = ["convert", input_file, "-resize", "x" + str(target_height), output_file]
                subprocess.run(command)

if __name__ == "__main__":
    input_folder = "/Users/antoinedujardin/Developer/sinowell_website/src/assets"
    output_folder = "/Users/antoinedujardin/Developer/sinowell_website/public/assets"
    target_height = 1000

    convert_to_jpg(input_folder, output_folder, target_height)