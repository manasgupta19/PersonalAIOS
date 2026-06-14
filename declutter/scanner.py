from pathlib import Path
from datetime import datetime


class DeclutterScanner:

    def scan(
        self,
        folder
    ):

        p = Path(folder)

        if not p.exists():

            return []

        result = []

        now = datetime.now()

        for f in p.iterdir():

            try:

                if f.is_file():

                    age = (
                        now
                        -
                        datetime.fromtimestamp(
                            f.stat().st_mtime
                        )
                    ).days

                    if age > 30:

                        result.append({

                            "name":
                                f.name,

                            "days":
                                age
                        })

            except:

                pass

        return sorted(

            result,

            key=lambda x:
                x["days"],

            reverse=True
        )

    def recommend(
        self,
        files
    ):

        if not files:

            return []

        advice = []

        if len(files) > 20:

            advice.append(
                "Downloads likely needs review"
            )

        if len(files) > 50:

            advice.append(
                "Consider archive folder"
            )

        return advice