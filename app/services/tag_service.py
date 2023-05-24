from app.repositories.tag_repository import TagRepository



class TagService:
    def __init__(self):
        self.tag_repo = TagRepository()

    def get_all_tags(self):
        return self.tag_repo.get_all_tags()

    def get_tag(self, tag_id):
        return self.tag_repo.get_tag_by_id(tag_id)

    def create_tag(self, name, post_id):
        return self.tag_repo.create_tag(name, post_id)

    def update_tag(self, tag_id, name):
        return self.tag_repo.update_tag(tag_id, name)

    def delete_tag(self, tag_id):
        return self.tag_repo.delete_tag(tag_id)