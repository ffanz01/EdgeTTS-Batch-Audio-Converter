
---

# EdgeTTS Batch Audio Converter

This project is designed to convert batches of text files into audio using Microsoft Edge TTS (Text-to-Speech) technology. It supports custom voice selections and handles multiple text files efficiently.

## Directory Structure

- **outputs**: This directory stores the generated audio files in MP3 format after processing the text files.
- **txts**: This is where you should place your text files (.txt) that you want to convert into audio.
- **EdgeTTS_Batch_Audio_Converter.py**: The main Python script that drives the text-to-audio conversion process. It reads text files from the `txts` directory, converts them into audio using the configured voice(from config.json), and saves the audio files in the `outputs` directory.
- **config.json**: This JSON configuration file includes the settings for the text-to-speech conversion process. Specifically, it contains a list of all the speakers that you wish to use for the conversion. Each speaker listed here will be applied to the text files during the batch conversion process.
- **choose_speakers.txt**: This text file enumerates all the speaker options supported by the Edge TTS (Text-to-Speech) service. It serves as a reference for users to understand which voices are available and can potentially be used when configuring the config.json file to select desired speakers for text-to-speech conversion.

## How to Run

To run the `EdgeTTS_Batch_Audio_Converter.py` script, follow these steps:

1. Ensure that you have Python installed on your system. We recommend using Python 3.7 or higher.

2. Install the required Python packages by running the following command in your terminal or command prompt:
   ```
   pip install edge-tts
   ```

3. Place your text files in the `txts` directory.

4. Configure the voices and other settings in the `config.json` file according to your preferences.

5. Open a terminal or command prompt and navigate to the project directory.

6. Execute the main script by running:
   ```
   python EdgeTTS_Batch_Audio_Converter.py
   ```

The script will start processing each text file in the `txts` directory, converting them to audio using the configured voice, and saving the resulting audio files in the `outputs` directory.

## Troubleshooting

- If you encounter errors during the conversion, ensure that your text files are properly formatted and placed in the correct directory.
- Make sure that the voices specified in `config.json` are supported by the Edge TTS service.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request. Be sure to include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
