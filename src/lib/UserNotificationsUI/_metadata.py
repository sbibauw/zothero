# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 19:28:21 2022
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
enums = """$UNNotificationContentExtensionMediaPlayPauseButtonTypeDefault@1$UNNotificationContentExtensionMediaPlayPauseButtonTypeNone@0$UNNotificationContentExtensionMediaPlayPauseButtonTypeOverlay@2$UNNotificationContentExtensionResponseOptionDismiss@1$UNNotificationContentExtensionResponseOptionDismissAndForwardAction@2$UNNotificationContentExtensionResponseOptionDoNotDismiss@0$"""
misc.update(
    {
        "UNNotificationContentExtensionMediaPlayPauseButtonType": NewType(
            "UNNotificationContentExtensionMediaPlayPauseButtonType", int
        ),
        "UNNotificationContentExtensionResponseOption": NewType(
            "UNNotificationContentExtensionResponseOption", int
        ),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"didReceiveNotification:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"didReceiveNotificationResponse:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Q"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(b"NSObject", b"mediaPause", {"required": False, "retval": {"type": b"v"}})
    r(b"NSObject", b"mediaPlay", {"required": False, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"mediaPlayPauseButtonFrame",
        {"required": False, "retval": {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"}},
    )
    r(
        b"NSObject",
        b"mediaPlayPauseButtonTintColor",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"mediaPlayPauseButtonType",
        {"required": False, "retval": {"type": b"Q"}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
