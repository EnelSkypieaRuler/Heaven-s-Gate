def _key():
    key='barcvrpr'
    aplpha_num="abcdefghijklmnopqrstuvwxyz"
    output=""
    for i in key:
        output+=aplpha_num[(aplpha_num.find(i)+13)%26]
    return output
key=_key()
