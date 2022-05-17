from joblib import load

def model_result(model_dir, input_data):
    loaded_model= load(model_dir)
    res = loaded_model.predict(input_data)[0]
    return res
