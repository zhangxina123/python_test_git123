import yaml


# yaml.safe_load 将yaml数据流转成python对象
# yaml.safe_dump() 将python对象转成yaml的数据格式
def get_datas():
    with open("data.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


print(get_datas())
