from isserviceup.models.user import User


def upsert_user(avatar_url, username, github_access_token):
    return User.objects(username=username).upsert_one(set__avatar_url=avatar_url,
                                                      set__github_access_token=github_access_token)


def get_user(user_id):
    return User.objects.with_id(user_id)
