class NonexistentPostError(Exception):
    def __init__(self, id):
        self.message = {
            'error': f'There\'s no post with the id {id} yet.'
        }
        super().__init__(self.message)
