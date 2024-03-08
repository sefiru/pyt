from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

products = spark.createDataFrame([('p1', 'Product 1'), ('p2', 'Product 2'), ('p3', 'Product 3')], ['product_id', 'product_name'])
categories = spark.createDataFrame([('c1', 'Category 1'), ('c2', 'Category 2')], ['category_id', 'category_name'])
product_category_relations = spark.createDataFrame([('p1', 'c1'), ('p1', 'c2'), ('p2', 'c1')], ['product_id', 'category_id'])

product_category = products.join(product_category_relations, 'product_id', 'left').join(categories, 'category_id', 'left')

product_category_pairs = product_category.select('product_name', 'category_name')

products_without_category = product_category.filter(col('category_name').isNull()).select('product_name')