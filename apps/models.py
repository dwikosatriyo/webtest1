# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db
from sqlalchemy.orm import relationship
'''
Add your models below
'''

# Book Sample
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))

# class Lampid(db.Model):
#     __tablename__ = 'Lampid'
#     ID = db.Column(db.Integer, primary_key=True)
#     NO_PROP = db.Column(db.String)
#     NO_KAB = db.Column(db.String)
#     NO_KEC = db.Column(db.String)
#     NO_KEL = db.Column(db.String)
#     NAMA_PROP = db.Column(db.String)
#     NAMA_KAB = db.Column(db.String)
#     NAMA_KEC = db.Column(db.String)
#     NAMA_KEL = db.Column(db.String)
#     TAHUN = db.Column(db.String)
#     BULAN = db.Column(db.String)
#     LAHIR_L = db.Column(db.String)
#     LAHIR_P = db.Column(db.String)
#     LAHIR_LP = db.Column(db.String)
#     MATI_L = db.Column(db.String)
#     MATI_P = db.Column(db.String)
#     MATI_LP = db.Column(db.String)
#     PINDAH_LUAR_DKI_L = db.Column(db.String)
#     PINDAH_LUAR_DKI_P = db.Column(db.String)
#     PINDAH_LUAR_DKI_LP = db.Column(db.String)
#     DATANG_LUAR_DKI_L = db.Column(db.String)
#     DATANG_LUAR_DKI_P = db.Column(db.String)
#     DATANG_LUAR_DKI_LP = db.Column(db.String)


# def request_data_all():
#     return Lampid.query.all()