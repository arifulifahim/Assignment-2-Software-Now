import os
import subprocess

def install_packages():
    packages = [
        "spacy",
        "scispacy",
        "transformers",
        "torch",
        "wget"
    ]
    for package in packages:
        try:
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install package: {package}")
            print(f"Error: {e}")
            print(f"Output: {e.output}")

def download_models():
    import spacy
    from spacy.cli import download
    import sys

    try:
        # Download and install SciSpacy models
        download("en_core_sci_sm")
        download("en_ner_bc5cdr_md")
    except SystemExit as e:
        if e.code != 0:
            print(f"Failed to download models: {e}")
        else:
            print("Models downloaded and installed successfully!")

if __name__ == "__main__":
    install_packages()
    download_models()
