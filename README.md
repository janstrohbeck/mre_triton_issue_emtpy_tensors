Steps to reproduce:
===================

1. (optional) generate model_repository/test_model/1/model.pt using model.py, or look at model.py for the definition of the pytorch model.
2. Run Triton server using `docker run --gpus=1 --rm --net=host -v ${PWD}/model_repository:/models nvcr.io/nvidia/tritonserver:23.05-py3 tritonserver --model-repository=/models`
3. Run Trition client using `docker run --rm -it --net=host -v $(pwd):/test/ nvcr.io/nvidia/tritonserver:23.05-py3-sdk python3 /test/client.py`
