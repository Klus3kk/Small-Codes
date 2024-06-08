import os
import pandas as pd
from PIL import Image
from pydub import AudioSegment
import ffmpeg

def convert_file(input_file, output_format):
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = f".{output_format.lower()}"

    # Create the output file name
    output_file = os.path.splitext(input_file)[0] + output_ext

    try:
        if input_ext in ['.txt', '.csv', '.json', '.xml', '.xlsx'] and output_ext in ['.txt', '.csv', '.json', '.xml', '.xlsx']:
            data_conversion(input_file, input_ext, output_file, output_ext)
        elif input_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff'] and output_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
            image_conversion(input_file, output_file)
        elif input_ext in ['.mp3', '.wav', '.flac', '.aac'] and output_ext in ['.mp3', '.wav', '.flac', '.aac']:
            audio_conversion(input_file, output_file)
        elif input_ext in ['.mp4', '.avi', '.mkv', '.mov'] and output_ext in ['.mp4', '.avi', '.mkv', '.mov']:
            video_conversion(input_file, output_file)
        else:
            raise ValueError(f"Unsupported file format conversion: {input_ext} to {output_ext}")

        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error occurred: {e}")

def data_conversion(input_file, input_ext, output_file, output_ext):
    df = None
    if input_ext == '.csv':
        df = pd.read_csv(input_file)
    elif input_ext == '.json':
        df = pd.read_json(input_file)
    elif input_ext == '.xlsx':
        df = pd.read_excel(input_file)
    elif input_ext == '.xml':
        df = pd.read_xml(input_file)
    elif input_ext == '.txt':
        df = pd.read_csv(input_file, delimiter='\t')

    if df is not None:
        if output_ext == '.csv':
            df.to_csv(output_file, index=False)
        elif output_ext == '.json':
            df.to_json(output_file, orient='records', lines=True)
        elif output_ext == '.xlsx':
            df.to_excel(output_file, index=False)
        elif output_ext == '.xml':
            df.to_xml(output_file)
        elif output_ext == '.txt':
            df.to_csv(output_file, sep='\t', index=False)

def image_conversion(input_file, output_file):
    img = Image.open(input_file)
    img.save(output_file)

def audio_conversion(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format=os.path.splitext(output_file)[1][1:])

def video_conversion(input_file, output_file):
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(stream)

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_format = input("Enter the desired output format (e.g., csv, json, xlsx, xml, txt, jpg, png, bmp, tiff, mp3, wav, flac, aac, mp4, avi, mkv, mov): ")
    convert_file(input_file, output_format)
