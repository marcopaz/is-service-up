from isserviceup.models.favorite import Favorite
from isserviceup.services import SERVICES


def get_favorite_services(user_id):
    favs = Favorite.objects(user_id=user_id)
    res = []
    for fav in favs:
        res.append(SERVICES[fav.service_id])
    return res


def update_favorite_status(user_id, service_id, status):
    if status:  # added favorite
        Favorite(user_id=user_id, service_id=service_id).save()
    else:  # removed favorite
        Favorite.objects(user_id=user_id, service_id=service_id).delete()
