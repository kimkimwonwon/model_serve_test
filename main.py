from fastapi import FastAPI
import torch


app = FastAPI()

# PyTorch Lightning 체크포인트 파일 경로
ckpt_path = "path/to/your/checkpoint.ckpt"

# PyTorch Lightning 모델 로드
model = YourModel.load_from_checkpoint(ckpt_path)

@app.get("/")
async def read_root():
    # 모델 사용 예시
    input_tensor = torch.randn(1, 3, 224, 224)
    output = model(input_tensor)
    return {"prediction": output.tolist()}