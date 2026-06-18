from pathlib import Path


class DeclutterScanner:

    def scan(
        self,
        folder
    ):

        result = {

            "delete": [],

            "review": [],

            "keep": []
        }

        files = (

            Path(folder)
            .glob("*")
        )

        for f in files:

            if not f.is_file():

                continue

            size = (
                f.stat()
                .st_size
            )

            if size < 10000:

                result[
                    "review"
                ].append(
                    f.name
                )

            else:

                result[
                    "keep"
                ].append(
                    f.name
                )

        return result