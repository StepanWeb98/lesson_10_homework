import utils
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def begin():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:id>")
def id_candidate(id):
    candidate_id = utils.get_candidate(id)
    return render_template('single.html', candidate=candidate_id)

@app.route("/search/<candidate_name>")
def get_candidate_name(candidate_name):
    candidate_name = utils.get_candidates_by_name(candidate_name)
    count_candidate = len(candidate_name)
    return render_template('search.html', candidates=candidate_name, count_candidate=count_candidate)

@app.route("/skill/<skill_name>")
def get_candidate_skill(skill_name):
    candidate_skill = utils.get_candidates_by_skill(skill_name)
    count_candidate = len(candidate_skill)
    return render_template('skill.html', candidates=candidate_skill, skill=skill_name, count_candidate=count_candidate)

app.run()