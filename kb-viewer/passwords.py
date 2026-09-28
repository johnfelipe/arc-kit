"""
Salted, memory-hard password hashing (scrypt) for the KB viewer.

Generate a hash for users.json:
    python passwords.py
"""

import base64
import getpass
import hashlib
import hmac
import secrets

SCRYPT_N = 2**15
SCRYPT_R = 8
SCRYPT_P = 1
SCRYPT_DKLEN = 64
SCRYPT_MAXMEM = 64 * 1024 * 1024
SALT_BYTES = 16


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _scrypt(password: str, salt: bytes, n: int, r: int, p: int, dklen: int) -> bytes:
    return hashlib.scrypt(
        password.encode("utf-8"), salt=salt, n=n, r=r, p=p, dklen=dklen, maxmem=SCRYPT_MAXMEM
    )


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(SALT_BYTES)
    digest = _scrypt(password, salt, SCRYPT_N, SCRYPT_R, SCRYPT_P, SCRYPT_DKLEN)
    return f"scrypt${SCRYPT_N}${SCRYPT_R}${SCRYPT_P}${_b64(salt)}${_b64(digest)}"


def verify_password(password: str, encoded: str) -> bool:
    try:
        scheme, n, r, p, salt_b64, digest_b64 = encoded.split("$")
        if scheme != "scrypt":
            return False
        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(digest_b64)
        actual = _scrypt(password, salt, int(n), int(r), int(p), len(expected))
    except (ValueError, TypeError):
        return False
    return hmac.compare_digest(actual, expected)


DUMMY_HASH = hash_password(secrets.token_urlsafe(32))


if __name__ == "__main__":
    pw = getpass.getpass("Nueva contraseña: ")
    if len(pw) < 12:
        raise SystemExit("La contraseña debe tener al menos 12 caracteres.")
    if pw != getpass.getpass("Confirmar contraseña: "):
        raise SystemExit("Las contraseñas no coinciden.")
    print(hash_password(pw))
