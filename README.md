# P7B Certificate Extractor

This project provides a Python script to extract individual certificates from P7B files, along with a batch script for easy execution on Windows.

## Contents

- `Extractor-p7b.py`: The main Python script for extracting certificates from P7B files.
- `extract-p7b.bat`: A batch script to run the Python extractor easily on Windows.

## Requirements

- Python 3.x
- cryptography library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the required library:

## Usage

1. Place your P7B files in your Downloads folder.
2. Update the `extract-p7b.bat` file with the correct path to your `Extractor-p7b.py` file.
3. Run the `extract-p7b.bat` file on Windows, or execute the Python script directly:


4. The extracted certificates will be saved in the same Downloads folder.

## Features

- Automatically processes all .p7b files in the Downloads folder
- Extracts individual certificates from P7B files
- Supports both PEM and DER encoded P7B files
- Names extracted certificates based on their Common Name (CN) when possible
- Handles filename conflicts by appending numbers
- Saves extracted certificates in PEM format

## How It Works

1. The script scans the specified folder for .p7b files
2. For each .p7b file:
- It attempts to parse the file as PEM, falling back to DER if necessary
- Each certificate is extracted and saved individually
- Certificates are named based on their Common Name, with a fallback to a generic name if CN extraction fails
- The script ensures unique filenames by appending numbers if conflicts occur

## Error Handling

The script includes basic error handling and will report any issues encountered while processing files.

## Customization

You can modify the source and output folders by editing the `source_folder` and `cert_output_folder` variables in the `Extractor-p7b.py` script.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to reach out to me if you have any questions or comments!

## Acknowledgments

- This project uses the `cryptography` library for certificate handling.