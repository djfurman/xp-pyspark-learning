from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("MessingAroundInBigData")
sc = SparkContext(conf=conf)

user_rdd = sc.textFile("./sample_data/2015-12-12.csv")

