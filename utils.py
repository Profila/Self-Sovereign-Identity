import secrets
import string
from datetime import datetime

def generate_api_key(length=32):
    """Generate a cryptographically secure random string."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def generate_challenge():
    return secrets.token_urlsafe(16)

def serialize(obj):
    """Helper function to serialize common data types to JSON-compatible formats."""
    if isinstance(obj, (dict, list, str, int, float, bool, type(None))):
        return obj
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif hasattr(obj, 'to_dict'):  # For models with a to_dict method
        return obj.to_dict()
    elif isinstance(obj, tuple):
        return [serialize(item) for item in obj]
    else:
        raise TypeError(f"Type {type(obj)} not serializable")
    