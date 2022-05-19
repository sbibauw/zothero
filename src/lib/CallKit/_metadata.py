# This file is generated by objective.metadata
#
# Last update: Sun Feb 20 18:31:11 2022
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
constants = """$CXErrorDomain$CXErrorDomainCallDirectoryManager$CXErrorDomainIncomingCall$CXErrorDomainNotificationServiceExtension$CXErrorDomainRequestTransaction$"""
enums = """$CXCallDirectoryEnabledStatusDisabled@1$CXCallDirectoryEnabledStatusEnabled@2$CXCallDirectoryEnabledStatusUnknown@0$CXCallDirectoryPhoneNumberMax@9223372036854775806$CXCallEndedReasonAnsweredElsewhere@4$CXCallEndedReasonDeclinedElsewhere@5$CXCallEndedReasonFailed@1$CXCallEndedReasonRemoteEnded@2$CXCallEndedReasonUnanswered@3$CXErrorCodeCallDirectoryManagerErrorCurrentlyLoading@7$CXErrorCodeCallDirectoryManagerErrorDuplicateEntries@4$CXErrorCodeCallDirectoryManagerErrorEntriesOutOfOrder@3$CXErrorCodeCallDirectoryManagerErrorExtensionDisabled@6$CXErrorCodeCallDirectoryManagerErrorLoadingInterrupted@2$CXErrorCodeCallDirectoryManagerErrorMaximumEntriesExceeded@5$CXErrorCodeCallDirectoryManagerErrorNoExtensionFound@1$CXErrorCodeCallDirectoryManagerErrorUnexpectedIncrementalRemoval@8$CXErrorCodeCallDirectoryManagerErrorUnknown@0$CXErrorCodeIncomingCallErrorCallUUIDAlreadyExists@2$CXErrorCodeIncomingCallErrorFilteredByBlockList@4$CXErrorCodeIncomingCallErrorFilteredByDoNotDisturb@3$CXErrorCodeIncomingCallErrorUnentitled@1$CXErrorCodeIncomingCallErrorUnknown@0$CXErrorCodeInvalidArgument@2$CXErrorCodeMissingVoIPBackgroundMode@3$CXErrorCodeNotificationServiceExtensionErrorInvalidClientProcess@1$CXErrorCodeNotificationServiceExtensionErrorMissingNotificationFilteringEntitlement@2$CXErrorCodeNotificationServiceExtensionErrorUnknown@0$CXErrorCodeRequestTransactionErrorCallUUIDAlreadyExists@5$CXErrorCodeRequestTransactionErrorEmptyTransaction@3$CXErrorCodeRequestTransactionErrorInvalidAction@6$CXErrorCodeRequestTransactionErrorMaximumCallGroupsReached@7$CXErrorCodeRequestTransactionErrorUnentitled@1$CXErrorCodeRequestTransactionErrorUnknown@0$CXErrorCodeRequestTransactionErrorUnknownCallProvider@2$CXErrorCodeRequestTransactionErrorUnknownCallUUID@4$CXErrorCodeUnentitled@1$CXErrorCodeUnknownError@0$CXHandleTypeEmailAddress@3$CXHandleTypeGeneric@1$CXHandleTypePhoneNumber@2$CXPlayDTMFCallActionTypeHardPause@3$CXPlayDTMFCallActionTypeSingleTone@1$CXPlayDTMFCallActionTypeSoftPause@2$"""
misc.update(
    {
        "CXPlayDTMFCallActionType": NewType("CXPlayDTMFCallActionType", int),
        "CXErrorCodeCallDirectoryManagerError": NewType(
            "CXErrorCodeCallDirectoryManagerError", int
        ),
        "CXCallDirectoryEnabledStatus": NewType("CXCallDirectoryEnabledStatus", int),
        "CXHandleType": NewType("CXHandleType", int),
        "CXErrorCodeIncomingCallError": NewType("CXErrorCodeIncomingCallError", int),
        "CXErrorCodeRequestTransactionError": NewType(
            "CXErrorCodeRequestTransactionError", int
        ),
        "CXErrorCode": NewType("CXErrorCode", int),
        "CXCallEndedReason": NewType("CXCallEndedReason", int),
        "CXErrorCodeNotificationServiceExtensionError": NewType(
            "CXErrorCodeNotificationServiceExtensionError", int
        ),
    }
)
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"CXAction", b"isComplete", {"retval": {"type": b"Z"}})
    r(b"CXCall", b"hasConnected", {"retval": {"type": b"Z"}})
    r(b"CXCall", b"hasEnded", {"retval": {"type": b"Z"}})
    r(b"CXCall", b"isEqualToCall:", {"retval": {"type": b"Z"}})
    r(b"CXCall", b"isOnHold", {"retval": {"type": b"Z"}})
    r(b"CXCall", b"isOutgoing", {"retval": {"type": b"Z"}})
    r(
        b"CXCallController",
        b"requestTransaction:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CXCallController",
        b"requestTransactionWithAction:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CXCallController",
        b"requestTransactionWithActions:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CXCallDirectoryExtensionContext",
        b"completeRequestReturningItems:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(
        b"CXCallDirectoryExtensionContext",
        b"completeRequestWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(b"CXCallDirectoryExtensionContext", b"isIncremental", {"retval": {"type": b"Z"}})
    r(
        b"CXCallDirectoryManager",
        b"getEnabledStatusForExtensionWithIdentifier:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CXCallDirectoryManager",
        b"openSettingsWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CXCallDirectoryManager",
        b"reloadExtensionWithIdentifier:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"CXCallUpdate", b"hasVideo", {"retval": {"type": b"Z"}})
    r(b"CXCallUpdate", b"setHasVideo:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXCallUpdate", b"setSupportsDTMF:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXCallUpdate", b"setSupportsGrouping:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXCallUpdate", b"setSupportsHolding:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXCallUpdate", b"setSupportsUngrouping:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXCallUpdate", b"supportsDTMF", {"retval": {"type": b"Z"}})
    r(b"CXCallUpdate", b"supportsGrouping", {"retval": {"type": b"Z"}})
    r(b"CXCallUpdate", b"supportsHolding", {"retval": {"type": b"Z"}})
    r(b"CXCallUpdate", b"supportsUngrouping", {"retval": {"type": b"Z"}})
    r(b"CXHandle", b"isEqualToHandle:", {"retval": {"type": b"Z"}})
    r(
        b"CXProvider",
        b"reportNewIncomingCallWithUUID:update:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CXProvider",
        b"reportNewIncomingVoIPPushPayload:completion:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"CXProviderConfiguration", b"includesCallsInRecents", {"retval": {"type": b"Z"}})
    r(
        b"CXProviderConfiguration",
        b"setIncludesCallsInRecents:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CXProviderConfiguration",
        b"setSupportsVideo:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"CXProviderConfiguration", b"supportsVideo", {"retval": {"type": b"Z"}})
    r(
        b"CXSetHeldCallAction",
        b"initWithCallUUID:onHold:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"CXSetHeldCallAction", b"isOnHold", {"retval": {"type": b"Z"}})
    r(b"CXSetHeldCallAction", b"setOnHold:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"CXSetMutedCallAction",
        b"initWithCallUUID:muted:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"CXSetMutedCallAction", b"isMuted", {"retval": {"type": b"Z"}})
    r(b"CXSetMutedCallAction", b"setMuted:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXStartCallAction", b"isVideo", {"retval": {"type": b"Z"}})
    r(b"CXStartCallAction", b"setVideo:", {"arguments": {2: {"type": b"Z"}}})
    r(b"CXTransaction", b"isComplete", {"retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"callObserver:callChanged:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:didActivateAudioSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:didDeactivateAudioSession:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:executeTransaction:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performAnswerCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performEndCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performPlayDTMFCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performSetGroupCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performSetHeldCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performSetMutedCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:performStartCallAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"provider:timedOutPerformingAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"providerDidBegin:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"providerDidReset:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"requestFailedForExtensionContext:withError:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
