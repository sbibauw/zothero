# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 19:09:47 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$$"""
misc.update({})
misc.update(
    {
        "_METRICS_SIGNPOST_TYPE_TOKEN": b"signpost:metrics",
        "_MXSIGNPOST_METRICS_SNAPSHOT_FORMAT": b"\n%{public, signpost:metrics}@",
    }
)
functions = {"_MXSignpostMetricsSnapshot": (b"^v",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MXMetricPayload",
        b"includesMultipleApplicationVersions",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSObject",
        b"didReceiveDiagnosticPayloads:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didReceiveMetricPayloads:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
