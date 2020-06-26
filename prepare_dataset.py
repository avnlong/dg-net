import os

dataset = 'moffice_datatrain'
train = os.path.join(dataset, 'train_all')
query = os.path.join(dataset, 'query')
if not os.path.exists(query):
    os.mkdir(query)
ratio = 0.5
ids = os.listdir(train)
for _id in ids:
    imgs = os.listdir(train + '/' + _id)
    num = int(len(imgs)*ratio)
    if num<=1:
        num += 3
    if not os.path.exists(query+'/'+_id):
        os.mkdir(query+'/'+_id)
    for i, img in enumerate(imgs):
        if i%num== 0:
            os.rename(os.path.join(train, _id, img), os.path.join(query, _id, img))

