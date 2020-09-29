


# cityscapes共有2975张图片用于训练


train_path = 'E://BaiduNetdiskDownload/cityscapes/train_multitask.txt'

train_ct = ''
with open(train_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        ss = line.split(' ')
        img_path = ss[0]
        disparity_path = ss[1]
        ins_path = ss[2]
        label_path = ss[3]
        train_ct += '%s\t%s\t%s\n' % (label_path, img_path, ins_path)


with open('train_list.txt', 'w', encoding='utf-8') as f:
    f.write(train_ct)
    f.close()



val_path = 'E://BaiduNetdiskDownload/cityscapes/train_multitask.txt'

val_ct = ''
kk = 0
with open(val_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        ss = line.split(' ')
        img_path = ss[0]
        disparity_path = ss[1]
        ins_path = ss[2]
        label_path = ss[3]
        val_ct += '%s\t%s\t%s\n' % (label_path, img_path, ins_path)
        kk += 1
        if kk == 20:
            break


with open('val_list.txt', 'w', encoding='utf-8') as f:
    f.write(val_ct)
    f.close()



