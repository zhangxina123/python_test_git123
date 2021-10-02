import yaml

document = """
  a:1
  b:
       c:3
       d:4
    """
dic = yaml.safe_load(document)
print(type(dic))
print(yaml.safe_load(document))
