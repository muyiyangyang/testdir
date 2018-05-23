from random import sample
from flask import Flask, jsonify
from celery_config import make_celery

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecret"

app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379/0", # or your broker
    CELERY_RESULT_BACKEND="redis://localhost:6379/0" # or your broker
)
celery = make_celery(app)

@celery.task(name="main.async_data")
def async_data():
    jsonify({"result": sample(range(101), 6)})
    return True

@app.route("/")
def index():
    async_data.delay()
    return 'test'

if __name__ == "__main__":
    app.run(host='192.168.101.61', port=8011, debug=True)
