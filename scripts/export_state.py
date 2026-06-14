import json


folders = [

    "memory/goals.json",

    "identity/profile.json",

    "knowledge/knowledge.json"
]

data = {}

for f in folders:

    try:

        with open(
            f,
            "r",
            encoding="utf-8"
        ) as fp:

            data[f] = (
                json.load(fp)
            )

    except:

        pass

with open(

    "snapshot.json",

    "w",

    encoding="utf-8"

) as out:

    json.dump(

        data,

        out,

        indent=2
    )

print(
    "Snapshot created"
)