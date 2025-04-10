import joblib, numpy as np
import litserve as ls
from pathlib import Path

class XGBoostAPI(ls.LitAPI):
    def setup(self, device):
        # load the model saved in above step during training
        model_path = Path("models", "xgboost_model.joblib")
        self.model = joblib.load(model_path)

    def decode_request(self, request):
        x = np.asarray(request["input"])
        x = np.expand_dims(x, 0)
        return x

    def predict(self, x):
        return self.model.predict(x)

    def encode_response(self, output):
        return {"class_idx": int(output)}

if __name__ == "__main__":
    api = XGBoostAPI()
    server = ls.LitServer(api)
    server.run(port=8080)
