from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MyApp")
sc = SparkContext(conf = conf)

data_file = 'alice.txt'

text_file = sc.textFile(data_file)
clean_text_file = text_file.map(lambda x: x.strip()).\
				filter(lambda x: len(x)!=0).\
				flatMap(lambda line: line.split(" "))

print(clean_text_file.count())

for str in clean_text_file.take(10):
	print(str)
