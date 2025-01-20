from flask import Flask, render_template
from flask_apscheduler import APScheduler
import json

app = Flask(__name__)
scheduler = APScheduler()

__API_URL__ = "vraag.json"
__VRAAG__ = None
__CLICKERS__ = 0


@app.route("/")
def index():
    global __VRAAG__
    global __CLICKERS__
    return render_template("vraag.html", vraag=__VRAAG__, clickers=__CLICKERS__)


def get_vraag():
    global __VRAAG__
    with open(__API_URL__, "r", encoding="utf-8") as f:
        j = json.loads(f.read())
        __VRAAG__ = j["vraag"]


# def get_num_clickers():
#     global __CLICKERS__
#     with open(__API_URL__, "r", encoding="utf-8") as f:
#         j = json.loads(f.read())
#         __CLICKERS__ = int(j["count"])


if __name__ == "__main__":
    get_vraag()
    scheduler.add_job(func=get_vraag, trigger="interval", seconds=600, id="get_vraag")
    # scheduler.add_job(
    #     func=get_num_clickers, trigger="interval", seconds=5, id="get_num_clickers"
    # )
    scheduler.start()
    app.run(debug=False)
