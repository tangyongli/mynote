f=rf'run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5
f=rf'.run/train/logs/checkpoint/model.{epoch:02d}-{val_loss:.2f}.h5'#eorro
os.makedirs(f,exist_ok=False)#
-ricefield
--- dataset
-------    _init__.py
-------     data.py
-------    dataio.py
---utils
------- model
------------ model.py
--------train
-------------fit.py
![image](https://github.com/tangyongli/mynote/assets/133754833/70a622a7-88de-47c0-af0c-4a44c6f951fa)
# 增加环境变量PYTHONPATH，路径为工程文件夹目录，如D:\RICEFIELD;D:\code\global-cropland-mapping-master;
# 打开vsc的setting.json

{
    "vscode-office.openOutline": true,
    "python.defaultInterpreterPath": "C:\\Users\\YL\\anaconda3\\envs\\myenv\\python.exe",
  **  "terminal.integrated.env.windows": {"PYTHONPATH":"${workspaceFolder};${env:PYTHONPATH}"}**,
}

# 重启，导入库
假如目前目录在model.py，要导入dataset中的dataio中的class onehot
from 文件夹.文件夹.文件 import moduel/class
import 文件夹.文件夹.文件
from dataste.dataio import onehot # don't use from .. dataset.dataio import onehot 
假如目前目录在data.py，要导入train中的fit.py的class call 
from utils.train.fit import call




