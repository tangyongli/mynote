# extract the speific string or number-find or re
``` python
f=r"C:\Users\YL\Downloads\2022_8daysmincompositevh_linearfillmosaci_1to365scale10samplepoint.csv"
import re
# 使用正则表达式提取days前数字
match = re.search(r'_(\d+)days', f)
if match:
    days_number = match.group(1)
    days_number=int(days_number)
    print(f"提取到的数字是: {days_number}")
else:
    print("未找到匹配的数字")
# 找到 "days" 后的字符串的索引
days_index = f.find("days")
# 找到 "composite" 前的字符串索引
composite_index = f.find("composite")
# 提取days 和composite之间的内容
composite = f[days_index+len("days"):composite_index]
print(f"提取的字符串（composite前）: {composite}")


f=rf'run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5 <br>
f=rf'.run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5'#eorro <br>
os.makedirs(f,exist_ok=False)<br>


