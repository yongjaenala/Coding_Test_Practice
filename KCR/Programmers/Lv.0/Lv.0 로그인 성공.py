def solution(id_pw, db):
    w_id = 0
    w_pw = 0
    for i in db :
        if id_pw[0] != i[0] :
            w_id += 1
            continue
        if w_id == len(db) :
            return 'fail'
        if (id_pw[0] == i[0]) & (id_pw[0])


id_pw = ["meosseugi", "1234"]	; db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]	#"login"
id_pw = ["programmer01", "15789"]	; db=[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]	#"wrong pw"
id_pw = ["rabbit04", "98761"]	; db=[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]	#"fail"
print(solution(id_pw,db))