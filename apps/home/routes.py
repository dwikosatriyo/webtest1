# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.authentication.models import Users
from apps.home.models import Lampid
from apps.config import API_GENERATOR
from sqlalchemy import func
@blueprint.route('/index')
# @login_required
def index():
    return render_template('home/index.html', segment='index', API_GENERATOR=len(API_GENERATOR))

@blueprint.route('/<template>')
# @login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        # if (template == "lampid.html"):
        # user = Users.query.filter_by(username=username).first()
        # lampid = Lampid.query.filter_by(ID="1").first()
        # print(lampid)
            # return render_template("home/" + template, segment=segment, lampid=lampid)
        #     lampid = db.session.execute(db.select(LAMPID)).scalars()
        #     print(lampid,flush=True)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, API_GENERATOR=len(API_GENERATOR))

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
    
@blueprint.route('/lampid')
def lampid():
    
    # user = Users.query.filter_by(username="a").first()
    # print(user)

    # lampid = Lampid.query.all()
    # lampid = Lampid.query.with_entities(Lampid.ID, Lampid.NO_PROP).all()
    # print(lampid)
    # user = Users.query.all()
    # print(user)

    return render_template("process/lampid.html", segment='lampid',lampid=lampid)

@blueprint.route('/lampid/lahir_mati')
def lampid_lahirMati():
    dataPerBulan = []

    
    for i in range(12):
        # print(i)
      
        lampid = Lampid.query.with_entities(func.sum(Lampid.LAHIR_L)
                                            , func.sum(Lampid.LAHIR_P)	 
                                            , func.sum(Lampid.LAHIR_LP)	 
                                            , func.sum(Lampid.MATI_L)	 
                                            , func.sum(Lampid.MATI_P)	 
                                            , func.sum(Lampid.MATI_LP)	 	 
                                            ).filter_by(BULAN=str(i+1)).all()
        # print(str(i+1))
        dataPerBulan.append(lampid)
        
    data = []
    for i in range(len(dataPerBulan[0][0])):
        data.append([])
    

    for i in dataPerBulan :
        # print (len(i[0]))
        for num, j in enumerate(i[0]) :
            # print(j)
            data[num].append(j)
    return render_template("process/lahirMati.html", segment='lampid',data=data)
@blueprint.route('/lampid/datang_pergi')
def lampid_datangPergi():
    dataPerBulan = []

    
    for i in range(12):
        # print(i)
      
        lampid = Lampid.query.with_entities(func.sum(Lampid.PINDAH_LUAR_DKI_L)
                                            , func.sum(Lampid.PINDAH_LUAR_DKI_P)	 
                                            , func.sum(Lampid.PINDAH_LUAR_DKI_LP)	 
                                            , func.sum(Lampid.DATANG_LUAR_DKI_L)	 
                                            , func.sum(Lampid.DATANG_LUAR_DKI_P)	 
                                            , func.sum(Lampid.DATANG_LUAR_DKI_LP)	 	 
                                            ).filter_by(BULAN=str(i+1)).all()
        # print(str(i+1))
        dataPerBulan.append(lampid)
        
    data = []
    for i in range(len(dataPerBulan[0][0])):
        data.append([])
    

    for i in dataPerBulan :
        # print (len(i[0]))
        for num, j in enumerate(i[0]) :
            # print(j)
            data[num].append(j)
    return render_template("process/datangPergi.html", segment='lampid',data=data)



    # print(data)
        # for num, j in enumerate(lampid) :
        #     # print(i)
        #     data[num] += int(i)
        # print (data)
    # user = Users.query.filter_by(username="a").first()
    # print(user)

    # lampid = Lampid.query.all()
    # lampid = Lampid.query.with_entities(Lampid.ID
    #                                     , Lampid.NO_PROP	
    #                                     , Lampid.NO_KAB	
    #                                     , Lampid.NO_KEC	
    #                                     , Lampid.NO_KEL	
    #                                     , Lampid.NAMA_PROP	
    #                                     , Lampid.NAMA_KAB	
    #                                     , Lampid.NAMA_KEC	
    #                                     , Lampid.NAMA_KEL	
    #                                     , Lampid.TAHUN	
    #                                     , Lampid.BULAN	 
    #                                     , Lampid.LAHIR_L	 
    #                                     , Lampid.LAHIR_P	 
    #                                     , Lampid.LAHIR_LP	 
    #                                     , Lampid.MATI_L	 
    #                                     , Lampid.MATI_P	 
    #                                     , Lampid.MATI_LP	 
    #                                     , Lampid.PINDAH_LUAR_DKI_L	 
    #                                     , Lampid.PINDAH_LUAR_DKI_P	 
    #                                     , Lampid.PINDAH_LUAR_DKI_LP	 
    #                                     , Lampid.DATANG_LUAR_DKI_L	 
    #                                     , Lampid.DATANG_LUAR_DKI_P	 
    #                                     , Lampid.DATANG_LUAR_DKI_LP).all()
    # LAHIR_L = []
    # LAHIR_P = []
    # LAHIR_LP = []
    # MATI_L = []
    # MATI_P = []
    # MATI_LP = []
    # PINDAH_LUAR_DKI_L = []
    # PINDAH_LUAR_DKI_P = []
    # PINDAH_LUAR_DKI_LP = []
    # DATANG_LUAR_DKI_L = []
    # DATANG_LUAR_DKI_P = []
    # DATANG_LUAR_DKI_LP = []
    # dataPerBulan = []
    # for i in range(12):
    #     dataPerBulan.append([])
    # # for i in lampid :
    # #     LAHIR_L.append(i[11])
    # #     LAHIR_P.append(i[12])
    # #     LAHIR_LP.append(i[13])
    # #     MATI_L.append(i[14])
    # #     MATI_P.append(i[15])
    # #     MATI_LP.append(i[16])
    # #     PINDAH_LUAR_DKI_L.append(i[17])
    # #     PINDAH_LUAR_DKI_P.append(i[18])
    # #     PINDAH_LUAR_DKI_LP.append(i[19])
    # #     DATANG_LUAR_DKI_L.append(i[20])
    # #     DATANG_LUAR_DKI_P.append(i[21])
    # #     DATANG_LUAR_DKI_LP.append(i[22])
    
    # for i in lampid :
    #     # print(int(i.BULAN)-1)
    #     dataPerBulan[int(i.BULAN)-1].append(i.LAHIR_L)
    #     dataPerBulan[int(i.BULAN)-1].append(i.LAHIR_P)
    #     dataPerBulan[int(i.BULAN)-1].append(i.LAHIR_LP)
    #     dataPerBulan[int(i.BULAN)-1].append(i.MATI_L)
    #     dataPerBulan[int(i.BULAN)-1].append(i.MATI_P)
    #     dataPerBulan[int(i.BULAN)-1].append(i.MATI_LP)
    #     dataPerBulan[int(i.BULAN)-1].append(i.PINDAH_LUAR_DKI_L)
    #     dataPerBulan[int(i.BULAN)-1].append(i.PINDAH_LUAR_DKI_P)
    #     dataPerBulan[int(i.BULAN)-1].append(i.PINDAH_LUAR_DKI_LP)
    #     dataPerBulan[int(i.BULAN)-1].append(i.DATANG_LUAR_DKI_L)
    #     dataPerBulan[int(i.BULAN)-1].append(i.DATANG_LUAR_DKI_P)
    #     dataPerBulan[int(i.BULAN)-1].append(i.DATANG_LUAR_DKI_LP)
    # # print(dataPerBulan)
    
    # totalDataPerBulan = []
    # for i in range(12):
    #     totalDataPerBulan.append([])

    # for bulan, data  in enumerate(dataPerBulan) :
    #     print(data)
    #     for i in data :
    #         # print(i)
    #         totalDataPerBulan[bulan].append(sum(list(map(int, i))))
    # print(totalDataPerBulan)

    # for i in lampid :
    #     totalDataPerBulan[int(i.BULAN)-1].append(sum(list(map(int, i.LAHIR_L))))
    # print(totalDataPerBulan)
    # for i in dataPerBulan:
    #     totalDataPerBulan.append()
    # print(LAHIR_L)
    # total_LAHIR_L = sum(LAHIR_L)
    # print(total_LAHIR_L)
    # print(LAHIR_L)
    # user = Users.query.all()
    # print(user)



    
