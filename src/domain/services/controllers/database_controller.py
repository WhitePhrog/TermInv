class DatabaseController:
    def call(self,
             query: str,
             params: tuple[dict] = (),
            ):
        raise NotImplementedError
        