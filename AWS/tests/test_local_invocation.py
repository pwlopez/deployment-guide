import json
from app.main import model_fn, predict_fn, input_fn, output_fn

payload = {}

response, accept = output_fn(
    predict_fn(
        input_fn(payload, "application/x-image"),
        model_fn("../")
    ),
    "application/json"
)
json.loads(response).keys()