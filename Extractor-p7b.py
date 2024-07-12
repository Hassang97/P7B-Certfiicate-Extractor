import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs7

def extract_certs_from_p7b(p7b_file_path, cert_output_folder):
    # Read the p7b file
    with open(p7b_file_path, 'rb') as f:
        p7b_data = f.read()

    # Parse the p7b file
    try:
        # Try to parse as PEM
        certs = x509.load_pem_x509_certificates(p7b_data)
    except ValueError:
        # If PEM fails, try to parse as DER
        certs = pkcs7.load_der_pkcs7_certificates(p7b_data)

    # Extract each certificate
    for i, cert in enumerate(certs):
        # Try to get the common name from the certificate
        try:
            common_name = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
            cert_filename = f"{common_name}.cer"
        except:
            # If common name extraction fails, use a generic name
            cert_filename = f"certificate_{i+1}.cer"

        # Ensure the filename is valid
        cert_filename = "".join(c for c in cert_filename if c.isalnum() or c in (' ', '.', '_')).rstrip()
        cert_path = os.path.join(cert_output_folder, cert_filename)

        # If a file with this name already exists, append a number
        base_filename, extension = os.path.splitext(cert_filename)
        counter = 1
        while os.path.exists(cert_path):
            cert_filename = f"{base_filename}_{counter}{extension}"
            cert_path = os.path.join(cert_output_folder, cert_filename)
            counter += 1

        # Write the certificate to a file in PEM format (base-64 encoded X.509)
        with open(cert_path, 'wb') as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

        print(f"Extracted: {cert_filename}")

    print(f"Extracted {len(certs)} certificates from {os.path.basename(p7b_file_path)} to {cert_output_folder}")

# Set the paths
source_folder = os.path.join(os.path.expanduser("~"), "Downloads")
cert_output_folder = source_folder

# Find all .p7b files in the Downloads folder
p7b_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.p7b')]

if not p7b_files:
    print("No .p7b files found in the Downloads folder.")
    exit(1)

# Process each .p7b file
for p7b_file in p7b_files:
    p7b_file_path = os.path.join(source_folder, p7b_file)
    print(f"\nProcessing: {p7b_file}")
    try:
        extract_certs_from_p7b(p7b_file_path, cert_output_folder)
    except Exception as e:
        print(f"Error processing {p7b_file}: {str(e)}")

print("\nAll .p7b files processed.")