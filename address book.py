import json

'''  通讯录保存格式
a = {
        "1":{
            'name':'sadsa',
            'phone':'dasdsad',
            'email':'cdd'
        },

        "2":{
            "name": "HP",
            "phone": "123456789",
            "email": "jlj@hool.com"
        }

    }
'''

def opf():              #打开文件没有则新建
    try:
        with open('e:/data.json','r') as f:
            rddata = json.load(f)
    except:
        with open('e:/data.json','w') as f:
            rddata = {}
    return rddata
def savein():           
    a = {}
    a['name'] = input('请输入姓名：')
    a['phone'] = input('请输入号码：')
    a['email'] = input('请输入邮箱：')
    data = opf()
    data[str(len(data)+1)] = a
    with open('e:/data.json','w') as f:
        json.dump(data,f)
def search():
    key = input('请输入关键字：')
    data = opf()
    for i in data:
        if key in data or key in str(data[i]):
            print('{} {} {} {}'.format(i,data[i]['name'],data[i]['phone'],data[i]['email']))
def show():
    data = opf()
    for i in data:
        print('{} {} {} {}'.format(i,data[i]['name'],data[i]['phone'],data[i]['email']))
def delete():
    data = opf()
    while True:
        Inid =input('联系人ID：')
        if int(Inid)>0 and data.get(Inid):
            print('{} {} {} {}'.format(Inid,data[Inid]['name'],data[Inid]['phone'],data[Inid]['email']))
            while True:
                flag = input('确认删除此联系人？（y/[n]）')
                if flag == 'y':
                    del data[Inid]
                    with open('e:/data.json', 'w') as f:
                        json.dump(data,f)
                    break
                elif flag == 'n':
                    print('取消删除')
                    break
                else:
                    print('输入错误，请重新输入')
            break
        else:
            print('无效ID，请重新输入')
def main():
    while True:
        a = input('请选择：1.录入2.查找3.全部显示4.删除（回车退出）：')
        if a == '1':
            savein()
        elif a == '2':
            search()
        elif a == '3':
            show()
        elif a == '4':
            delete()
        else:
            print('感谢使用')
            break
if __name__ == '__main__':
    main()
