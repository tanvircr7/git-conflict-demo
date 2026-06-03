def make_telemetry_context():
    # BUG: this staging version leaks resources
    resource = open("/tmp/fake-resource.txt", "w")
    resource.write("starting telemetry")
    return "buggy staging telemetry context"
