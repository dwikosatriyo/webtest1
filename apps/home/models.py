# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""



from sqlalchemy.orm import relationship
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Lampid(db.Model):

    __tablename__ = 'Lampid'

    ID = db.Column(db.Integer, primary_key=True)
    NO_PROP = db.Column(db.String(64))
    NO_KAB = db.Column(db.String(64))
    NO_KEC = db.Column(db.String(64))
    NO_KEL = db.Column(db.String(64))
    NAMA_PROP = db.Column(db.String(64))
    NAMA_KAB = db.Column(db.String(64))
    NAMA_KEC = db.Column(db.String(64))
    NAMA_KEL = db.Column(db.String(64))
    TAHUN = db.Column(db.String(64))
    BULAN = db.Column(db.String(64))
    LAHIR_L = db.Column(db.String(64))
    LAHIR_P = db.Column(db.String(64))
    LAHIR_LP = db.Column(db.String(64))
    MATI_L = db.Column(db.String(64))
    MATI_P = db.Column(db.String(64))
    MATI_LP = db.Column(db.String(64))
    PINDAH_LUAR_DKI_L = db.Column(db.String(64))
    PINDAH_LUAR_DKI_P = db.Column(db.String(64))
    PINDAH_LUAR_DKI_LP = db.Column(db.String(64))
    DATANG_LUAR_DKI_L = db.Column(db.String(64))
    DATANG_LUAR_DKI_P = db.Column(db.String(64))
    DATANG_LUAR_DKI_LP = db.Column(db.String(64))


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            setattr(self, property, value)

    def __repr__(self):
        return str(self.ID)

def request_data_all():
    return Lampid.query.all()



    