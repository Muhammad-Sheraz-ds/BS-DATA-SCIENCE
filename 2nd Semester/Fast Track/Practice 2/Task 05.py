def source_to_target(list):
    target_string=''
    blank=''
    i = 0
    while i < len(list):
        if list[i] =='.':
            i+=1
        elif list[i:i+3] ==' is':
            i+=3
        elif list[i:i+3] ==' am':
            i+=3
        elif list[i:i+4] ==' are':
            i+=4
        else:
            target_string+=list[i]
            i+=1

    print(target_string)

source_to_target('This is something am interesting. We are happy.')




