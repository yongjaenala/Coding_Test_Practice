def solution(id_pw, db):
    id = []
    for i in db :
        id.append(i[0])
    if id_pw in db :
        return "login"
    else :
        if id_pw[0] not in id :
            return "fail"
        else :
            if id_pw not in db:
                return "wrong pw"