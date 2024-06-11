import json
import joblib

# This contains all the necessary functions for serving the custom model

def model_fn(model_dir):
    """
    Load the model using the preferred method. In this sample case we use joblib 
    which can handle a wide variety of model types. When possible, use the recommended
    serialization tools for your specific model. As a result, this function may be many
    lines longer.

    model_dir: model can be packed in the container alongside this code for deployment. 
    Make sure the model is stored in the correct location. In this case /app/
    """
    model = joblib.load(model_dir)

    return model

def input_fn(request, content_type):
    """
    Accept the request and request format (ex. json, text, etc)
    """

    # If there are multiple request options, make sure you verify the format
    if  content_type == "application/json":
        body = json.loads(request)

    # Perform any necessary data transformations to prepare for model ingestion

    return body

def predict_fn(input_data, model):
    """
    Perform model inference
    """
    
    output = model.predict(input_data)

    return output

def output_fn(output, accept):
    """
    Build output object and return

    Assume the accept content type is the same as input: application/json, so
    we build a json object and return it
    """
    
    output = json.dumps(output)

    return output, accept