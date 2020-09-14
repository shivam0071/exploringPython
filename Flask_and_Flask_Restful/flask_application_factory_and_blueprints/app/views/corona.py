from flasgger import SwaggerView    # for api docs
from flask import current_app as app, jsonify, request # current app as app???
from app.blueprints import shared
from app.extensions import cache
from util.get_corona_data import get_state_wise_data_wiki

class state_wise_data_wiki(SwaggerView):

    @staticmethod
    def get():
        data = get_state_wise_data_wiki()
        return ({"data" : data})

shared.add_url_rule(
    f"/get-indian-states-data/v1",
    view_func=state_wise_data_wiki.as_view("state_wise_data_wikipedia"),
    methods=["GET"],
)