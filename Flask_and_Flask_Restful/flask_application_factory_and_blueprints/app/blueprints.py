from flask import Blueprint

blueprints = []

corona = Blueprint(name="corona", import_name="app.views.corona")
shared = Blueprint(name="shared", import_name="app.views.shared")

blueprints.append(corona)
blueprints.append(shared)