from itertools import permutations


def match_banned_id(user, ban):
    id_len = len(user)
    if id_len != len(ban):
        return False
    for i in range(id_len):
        if ban[i] == '*':
            continue
        if user[i] != ban[i]:
            return False
    return True


def solution(user_id, banned_id):
    banned_len = len(banned_id)
    perms = permutations(user_id, banned_len)
    result = []
    for user_ids in perms:
        is_all_banned = True
        for i, user_id in enumerate(user_ids):
            if not match_banned_id(user_id, banned_id[i]):
                is_all_banned = False
                break

        if is_all_banned:
            set_ids = set(user_ids)
            if set_ids not in result:
                result.append(set_ids)

    return len(result)
