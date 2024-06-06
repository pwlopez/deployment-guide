# This contains all the necessary functions for serving the custom model

def model_fn():
    """
    Load the model
    """
    pass

def input_fn(request, content_type):
    """
    Accept parameters passed from Sagemaker
    """
    pass

def predict_fn(input_data, model):
    """
    Perform model inference
    """
    pass

def output_fn(data, content_type):
    """
    Build output object and return
    """
    pass