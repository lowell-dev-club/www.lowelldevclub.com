import sys
from datetime import datetime
from hashlib import sha256

from lowelldevclub import app, bcrypt, db
from lowelldevclub.models import *

if sys.argv[1] == 'test':
    db.create_all()

    pass1 = bcrypt.generate_password_hash(
        sha256(('pass' + 'demo@domain.com').encode('utf-8')).hexdigest()
    ).decode('utf-8')

    user = User(email='demo@domain.com', password=pass1)

    db.session.add(user)
    db.session.commit()

else:
    sys.exit('No argument or exsisting argument found')
