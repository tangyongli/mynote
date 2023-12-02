f=rf'run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5 <br>
f=rf'.run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5'#eorro <br>
os.makedirs(f,exist_ok=False)<br>
[教程1](https://blog.csdn.net/ld_long/article/details/120074106?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-120074106-blog-109474175.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-120074106-blog-109474175.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=8)
[2](https://blog.csdn.net/qq_31654025/article/details/109474175)<br>
-ricefield<br>
--- dataset><br>
-------    _init__.py<br>
-------     data.py<br>
-------    dataio.py<br>
---utils<br>
------- model<br>
------------ model.py<br>
--------train<br>
-------------fit.py<br>
![image](https://github.com/tangyongli/mynote/assets/133754833/70a622a7-88de-47c0-af0c-4a44c6f951fa)
# 增加环境变量PYTHONPATH，路径为工程文件夹目录，如D:\RICEFIELD;D:\code\global-cropland-mapping-master;
# 打开vsc的setting.json 

{
    "vscode-office.openOutline": true,<br>
    "python.defaultInterpreterPath": "C:\\Users\\YL\\anaconda3\\envs\\myenv\\python.exe",<br>
  **"terminal.integrated.env.windows": {"PYTHONPATH":"${workspaceFolder};${env:PYTHONPATH}"}**,<br>
}
# 也可以直接在vsc的setting.json增加换环境变量

{
    "vscode-office.openOutline": true,<br>
    "python.defaultInterpreterPath": "C:\\Users\\YL\\anaconda3\\envs\\myenv\\python.exe",<br>
  "terminal.integrated.env.windows": {"PYTHONPATH":"${workspaceFolder};${**env:D:\\RICEFIELD**}"},<br>
}
# 重启，导入库
假如目前目录在model.py，要导入dataset中的dataio中的class onehot<br>
from 文件夹.文件夹.文件 import moduel/class<br>
import 文件夹.文件夹.文件<br>
from dataste.dataio import onehot # don't use from .. dataset.dataio import onehot <br>
假如目前目录在data.py，要导入train中的fit.py的class call <br>
from utils.train.fit import call<br>




