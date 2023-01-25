import os
import hashlib
from typing import Optional


class Hash:
    '''
    Methods regarding password hash
    '''
    @staticmethod
    def generate_salt() -> bytes:
        '''
        Generate random salt to be used to hashing
        '''
        return os.urandom(32)
    
    @staticmethod
    def password(password: str, salt: Optional[str]=None) -> tuple[str, str]:
        '''
        Hashes the password
        '''
        if not salt:
            salt = Hash.generate_salt()
        else:
            salt = bytes.fromhex(salt)

        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100_000
        )
        return (salt.hex(), (salt + key).hex())
