from contextlib import ExitStack


def make_telemetry_context():
    with ExitStack() as stack:
        resource = stack.enter_context(open("/tmp/fake-resource.txt", "w"))
        resource.write("starting telemetry")
        return "correct feature telemetry context"
