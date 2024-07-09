import os
import json
import glob
import edge_tts

# Print the current working directory
current_path = os.getcwd()
print(current_path)

# Set the voice characteristics/language for the speaker
config_path = os.path.join(current_path, 'config.json')
with open(config_path, 'r') as config_file:
    config_data = json.load(config_file)
    # Get all the speakers' values
    chosen_speakers = config_data.get('speakers', [])
    for speaker in chosen_speakers:
        print(speaker)

# Define the folders for txt files and outputs
txt_folder = os.path.join(current_path, 'txts')
output_folder = os.path.join(current_path, 'outputs')

# Check if the txts folder exists, create it if not
if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)
    print("The 'txts' folder did not exist, so it has been created. Please place your .txt files in the 'txts' folder.")

# Use glob.glob to find all .txt files in the txts folder
txt_files = glob.glob(os.path.join(txt_folder, '*.txt'))

# If txt_files is empty, indicate that there are no .txt files in the txts folder
if not txt_files:
    print("No .txt files were found in the 'txts' folder. Please add your .txt files and try again.")
else:
    print("Found .txt files:")
    for file in txt_files:
        print(file)

    # Read file contents into a list
    texts = []
    filenames_only = []
    for file_path in txt_files:
        text = None
        encodings = ['utf-8', 'GBK', None]
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    text = file.read()
                    break
            except UnicodeDecodeError:
                continue
            except TypeError:
                pass

        if text is None:
            print(f"Failed to read {file_path} with any of the attempted encodings.")
            continue

        texts.append(text)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        filenames_only.append(filename)

print(txt_files)

# Convert texts to speech using the selected speakers
for chosen_speaker in chosen_speakers:
    for text in texts:
        MAX_RETRIES = 5
        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                text_idx = texts.index(text)
                output_file = os.path.join(output_folder, f"{filenames_only[text_idx]}_{chosen_speaker}.mp3")
                communicate = edge_tts.Communicate(text, chosen_speaker)
                communicate.save_sync(output_file)
                print(f"Operation on {filenames_only[text_idx]} succeeded, speaker was: {chosen_speaker}")
                break
            except Exception as e:
                print(f"Attempt {retry_count + 1} failed due to: {e}")
                retry_count += 1
                if retry_count < MAX_RETRIES:
                    print("Preparing to retry...")
                else:
                    print("Maximum retries reached, no further attempts will be made.")
