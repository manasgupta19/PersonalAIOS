from storage.json_store import (
    JsonStore
)


class ProfileManager:

    def __init__(self):

        self.path = (
            "identity/profile.json"
        )

        self.store = (
            JsonStore()
        )


    def load(self):

        return self.store.load(
            self.path,
            {}
        )


    def save(
        self,
        profile
    ):

        self.store.save(
            self.path,
            profile
        )


    def update(
        self,
        key,
        value
    ):

        profile = self.load()

        profile[
            key
        ] = value

        self.save(
            profile
        )