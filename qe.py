from sklearn.ensemble import RandomForestClassifier  # 导入随机森林分类器，用于构建分类模型
import pandas as pd  # 导入pandas库并简写为pd，用于数据处理和分析
from sklearn.metrics import accuracy_score  # 导入accuracy_score函数，用于评估模型预测准确率
from sklearn.model_selection import train_test_split  # 导入train_test_split函数，用于将数据集拆分为训练集和测试集
import pickle  # 导入pickle库，用于模型和数据的序列化保存

# 读取中文编码的企鹅数据集CSV文件，存储到DataFrame对象中
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

# 删除数据集中包含缺失值的行，inplace=True表示直接修改原DataFrame
penguin_df.dropna(inplace=True)

# 提取目标变量（标签）：企鹅的种类
output = penguin_df['企鹅的种类']

# 提取特征变量：企鹅栖息的岛屿、喙的长度、喙的深度、翅膀的长度、身体质量、性别
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]

# 对分类特征进行独热编码，将非数值特征转换为数值特征
features = pd.get_dummies(features)

# 将目标变量（企鹅种类）转换为数值编码，output_codes是编码后的值，output_uniques是原始唯一值
output_codes, output_uniques = pd.factorize(output)

# 将数据集拆分为训练集和测试集，训练集占80%，测试集占20%
x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 创建随机森林分类器对象，使用默认参数
rfc = RandomForestClassifier()

# 使用训练集数据训练随机森林模型
rfc.fit(x_train, y_train)

# 使用训练好的模型对测试集进行预测，得到预测结果
y_pred = rfc.predict(x_test)

# 计算模型在测试集上的预测准确率
score = accuracy_score(y_test, y_pred)

# 以二进制写入模式打开文件，准备保存训练好的模型
with open('rfc_model.pkl', 'wb') as f:  # 将训练好的随机森林模型序列化保存到文件
    pickle.dump(rfc, f)

# 以二进制写入模式打开文件，准备保存编码映射
with open('output_uniques.pkl', 'wb') as f:  # 将目标变量的编码映射序列化保存到文件
    pickle.dump(output_uniques, f)

print('保存成功,已生成相关文件。')  # 打印保存成功信息