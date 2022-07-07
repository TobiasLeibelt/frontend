# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@blueprint.route('/index.html')
@login_required
def index():
    # dummy data
    data = {}

    data["number_projects"] = 42
    data["percent_rise_projects"] = 43

    data["number_publications"] = 420
    data["percent_rise_publications"] = 69

    data["number_cooperations"] = 100
    data["percent_rise_cooperations"] = 10

    data["number_patents"] = 1337
    data["percent_rise_patents"] = 5

    return render_template('home/index.html', data=data)


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

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
