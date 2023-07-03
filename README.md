This repo contains sample code to reproduce the error described in [this bug report](https://github.com/triton-inference-server/client/pull/350).

Steps to reproduce:
===================

1. (optional) regenerate model_repository/test_model/1/model.pt using model.py, or look at model.py for the definition of the pytorch model.
2. Run Triton server using `docker run --gpus=1 --rm --net=host -v ${PWD}/model_repository:/models nvcr.io/nvidia/tritonserver:23.05-py3 tritonserver --model-repository=/models`
3. Run Trition client using `docker run --rm -it --net=host -v $(pwd):/test/ nvcr.io/nvidia/tritonserver:23.05-py3-sdk python3 /test/client.py`
4. (optional) Alternatively, reproduce using perf_client (requires updating client libraries to include [this fix](https://github.com/triton-inference-server/client/pull/350)):
 - Works: `perf_analyzer -u localhost:8001 -i gRPC -m test_model --input-data inputs1.json`
 - Error: `perf_analyzer -u localhost:8001 -i gRPC -m test_model --input-data inputs0.json`
