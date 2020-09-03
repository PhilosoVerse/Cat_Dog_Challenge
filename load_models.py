from tensorflow.keras.models import load_model
import os
import numpy as np

save_path = "C:\\Users\\Steven Verkest\\PycharmProjects\\Cat_Dog_Challenge\\saved_models"

model2 = load_model(os.path.join(save_path,"network.h5"))
#pred = model2.predict(x)
#score = np.sqrt(metrics.mean_squared_error(pred,y))