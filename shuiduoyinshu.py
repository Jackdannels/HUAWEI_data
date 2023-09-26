import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

import statsmodels.api as sm



# 读取CSV文件
data = pd.read_csv('your_data.csv')

# 使用线性回归模型进行方差分析
model = ols('WaterRetention ~ C(Treatment1) + C(Treatment2) + C(Treatment3) + C(Treatment4) + C(Treatment5)+C(Treatment6)+C(Treatment7)', data=data).fit()

# 打印方差分析结果
print(model.summary())

# 获取ANOVA表
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
