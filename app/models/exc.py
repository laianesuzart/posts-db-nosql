class NonexistentPostError(Exception):
    def __init__(self, id: int):
        self.message = {
            'error': f'There\'s no post with the id {id} yet.'
        }
        super().__init__(self.message)

class InvalidDataError(Exception):
    def __init__(self, msg: str):
        self.message = {
            'error': msg
        }
        super().__init__(self.message)
