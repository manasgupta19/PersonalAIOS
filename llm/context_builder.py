from memory.memory_manager import (
    MemoryManager
)

from identity.profile_manager import (
    ProfileManager
)


memory = (
    MemoryManager()
)

profile = (
    ProfileManager()
)


def build_context():

    return {

        "profile":
            profile.load(),

        "goals":
            memory.load()
    }