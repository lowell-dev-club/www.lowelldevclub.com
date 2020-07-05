from lowelldevclub import db, app, bcrypt
from lowelldevclub.models import *
from hashlib import sha256
from datetime import datetime
import sys


if sys.argv[1] == 'test':
    db.create_all()

    pass1 = bcrypt.generate_password_hash(
        sha256(
            ('pass' +
             'demo@domain.com').encode('utf-8')).hexdigest()).decode('utf-8')

    user = User(
        email='demo@domain.com',
        password=pass1)

    db.session.add(user)
    db.session.commit()

else:
    sys.exit('No argument or exsisting argument found')
