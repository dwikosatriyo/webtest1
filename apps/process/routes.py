# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json
from datetime import datetime

from apps.home import blueprint
import flask
from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)



from apps import db, login_manager
from apps.process import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users

from apps.authentication.util import verify_pass, generate_token

# Bind API -> Auth BP


@blueprint.route('/lampid')
def lampid():
    
    # user = Users.query.filter_by(username="a").first()

    return render_template("process/lampid.html", segment='lampid')



