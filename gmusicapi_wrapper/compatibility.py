# Compatibility fixes and workarounds for gmusicapi-wrapper

import os
import warnings

# Workaround for protobuf compatibility issues
if 'PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION' not in os.environ:
    os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
    warnings.warn(
        "Setting PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python for compatibility. "
        "This may impact performance.",
        UserWarning
    )

# Warning about service discontinuation
warnings.warn(
    "WARNING: Google Play Music was discontinued in December 2020. "
    "This library can no longer connect to Google Music services. "
    "Only local file operations will work. "
    "Consider migrating to alternatives like ytmusicapi for YouTube Music.",
    DeprecationWarning
)