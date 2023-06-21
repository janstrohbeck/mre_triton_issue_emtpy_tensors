import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        tmp = [0, 0] if x.shape[0] > 0 else [1, 1]
        return torch.tensor(tmp, dtype=torch.long)

model = Model()
scripted_model = torch.jit.script(model)

inputs = [
    torch.empty((0,), dtype=torch.long),
    torch.zeros((1,), dtype=torch.long),
]
for x in inputs:
    print(model(x), scripted_model(x))

torch.jit.save(scripted_model, 'model_repository/test_model/1/model.pt')
