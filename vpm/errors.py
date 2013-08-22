class VPMError(Exception):
    pass

class SetupError(VPMError):
    pass

class CommandNotFound(VPMError):
    pass

class CommandFailed(VPMError):
    pass

