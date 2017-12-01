import functionalParam


def action_controller(action_no, obj_str):
    if obj_str is not "NULL":
        act_str = functionalParam.ACTION_DIC[action_no]
        resp = ">> ACT : [" + act_str + "] | OBJ :[" + obj_str + "]"
        #print(resp)
        return
    else:
        return
