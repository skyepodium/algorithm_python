def _generate():
    linux = b""

    # machine-id is stable across boots, boot_id is not.
    linux += 'b875f129-5ae6-4ab1-90c0-ae07a6134578'

    a = "11:memory:/docker/e8c9f0084a3b2b724e4f2a526d60bf0a62505f38649743b8522a8c005b8334ae"
    linux += a.strip().rpartition(b"/")[2]

    if linux:
        return linux


print(_generate())