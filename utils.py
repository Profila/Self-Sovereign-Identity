import secrets
import string

def generate_api_key(length=32):
    """Generate a cryptographically secure random string."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))