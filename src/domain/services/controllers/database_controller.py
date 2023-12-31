class DatabaseController:
    def execute(
        self,
        query: str,
        params: tuple[str] = (),
    ) -> list[str]:
        raise NotImplementedError
