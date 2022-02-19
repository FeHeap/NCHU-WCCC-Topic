from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MyApp")
sc = SparkContext(conf = conf)

data_file = 'alice.txt'

text_file = sc.textFile(data_file)
alphabets = text_file.flatMap(lambda string: (char for char in string)).\
			filter(lambda x: x.isalpha()).\
			map(lambda x: (x.lower(), 1))

alphabetsCount = alphabets.reduceByKey(lambda x, y: (x+y)).sortByKey()


for pair in alphabetsCount.collect():
	print(pair[0] + f': {pair[1]}')
