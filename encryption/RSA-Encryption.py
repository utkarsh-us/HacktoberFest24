from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Step 1: Generate RSA keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    return private_key, public_key

# Step 2: Encrypt the passphrase using the public key
def encrypt_passphrase(public_key, passphrase):
    encrypted_passphrase = public_key.encrypt(
        passphrase.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_passphrase

# Step 3: Decrypt the passphrase using the private key
def decrypt_passphrase(private_key, encrypted_passphrase):
    decrypted_passphrase = private_key.decrypt(
        encrypted_passphrase,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_passphrase.decode('utf-8')

# Optional: Save and load keys
def save_private_key(private_key, filename):
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def load_private_key(filename):
    with open(filename, 'rb') as pem_in:
        private_key = serialization.load_pem_private_key(
            pem_in.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def save_public_key(public_key, filename):
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def load_public_key(filename):
    with open(filename, 'rb') as pem_in:
        public_key = serialization.load_pem_public_key(
            pem_in.read(),
            backend=default_backend()
        )
    return public_key

# Example usage
if __name__ == "__main__":
    passphrase = "my_secure_passphrase"

    # Generate RSA keys
    private_key, public_key = generate_keys()

    # Encrypt the passphrase
    encrypted_passphrase = encrypt_passphrase(public_key, passphrase)
    print(f"Encrypted passphrase: {encrypted_passphrase}")
    print(len(encrypted_passphrase))

    # Decrypt the passphrase
    decrypted_passphrase = decrypt_passphrase(private_key, encrypted_passphrase)
    print(f"Decrypted passphrase: {decrypted_passphrase}")
