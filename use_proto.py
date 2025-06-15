import demo_pb2
import sys

flower = demo_pb2.Flower()
flower.sepal_length = 1.2
flower.sepal_width = 1.3
flower.petal_length = 3.2
flower.petal_width = 4

flower_dict={}
flower_dict["sepal_length"]="Harekrishna"

print(flower)
print(flower_dict)
print(sys.getsizeof(flower))
print(sys.getsizeof(flower_dict))

print(flower.SerializeToString())

dflower = demo_pb2.Flower()
dflower.ParseFromString(b'\r\x9a\x99\x99?\x15ff\xa6?\x1d\xcd\xccL@%\x00\x00\x80@')

print(dflower)
