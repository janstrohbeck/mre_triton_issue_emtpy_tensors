import grpc
from tritonclient.grpc import service_pb2
from tritonclient.grpc import service_pb2_grpc

if __name__ == '__main__':
    model_name = "test_model"
    model_version = "1"

    # Create gRPC stub for communicating with the server
    channel = grpc.insecure_channel("localhost:8001")
    grpc_stub = service_pb2_grpc.GRPCInferenceServiceStub(channel)

    inputs = [[0], []]

    for x in inputs:
        print("Input:", x)
        request = service_pb2.ModelInferRequest()
        request.model_name = model_name
        request.model_version = model_version
        # request.id = "my request id"

        input = service_pb2.ModelInferRequest().InferInputTensor()
        input.name = "x"
        input.datatype = "FP32"
        input.shape.extend([len(x)])
        request.inputs.extend([input])

        output = service_pb2.ModelInferRequest().InferRequestedOutputTensor()
        output.name = "result"
        request.outputs.extend([output])

        request.raw_input_contents.extend([bytes(x)])

        response = grpc_stub.ModelInfer(request)
        print("model infer:\n{}".format(response))
