# -*- coding: utf-8 -*-
def filterTags(attrs):
    if not attrs:
        return
    tags = {}

# 基本のタグ付け
# 県とか郡とかの is_inを付与。
    if attrs['FUDE']:
        tags.update({'ref:JP_fude':attrs['FUDE']})
    else:
        pass

# 耕地の種類にあわせてタグづけを変更

    check_type = attrs['TYPE']
    if check_type.endswith('畑'):
        tags.update({'landuse':'farmland'})
    elif check_type.endswith('田'):
        tags.update({'landuse':'farmland'})
        tags.update({'crop':'rice'})
    else:
        pass

    return tags
