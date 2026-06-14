from memory.memory_manager import (
    MemoryManager
)

from knowledge.knowledge_manager import (
    KnowledgeManager
)

from identity.profile_manager import (
    ProfileManager
)

from notifications.notifier import (
    NotificationEngine
)

from opportunities.engine import (
    OpportunityEngine
)

from declutter.scanner import (
    DeclutterScanner
)


memory = MemoryManager()

knowledge = KnowledgeManager()

profile = ProfileManager()

notify = NotificationEngine()

opportunity = OpportunityEngine()

declutter = DeclutterScanner()