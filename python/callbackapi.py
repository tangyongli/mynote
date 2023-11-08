from keras.callbacks import CSVLogger, ModelCheckpoint,EarlyStopping
import datetime
dt_now = str(datetime.datetime.now()).replace(".", "_").replace(":", "_")
early_stopping_callback = keras.callbacks.EarlyStopping(monitor="val_loss", patience=5)
csv_logger = rf"run/train/logs/log_{dt_now}.csv"
csv_logger=CSVLogger(csv_logger,separator=',',append=False) # 默认会保存每轮所有的指标，epoch	accuracy	loss	mean_io_u	val_accuracy	val_loss	val_mean_io_u
model_checkpoint_callback = keras.callbacks.ModelCheckpoint( rf'run/train/logs/checkpoint/model.{epoch:02d}.h5',
    save_weights_only=True, #只保存权重，节约磁盘空间
    monitor="val_accuracy", #回调函数将尝试找到具有最小损失函数值的模型。modle.fit中假如epho是50，但是模型在第25epho时已经达到了最低损失函数，那么回调函数会保存第25轮的权重
    mode="max",
    save_best_only=True,
)
callback=[early_stopping_callback,model_checkpoint_callback,csv_logger]
history=model.fit( train_dataset , epochs=2,validation_data=val_dataset,callbacks=[model_checkpoint_callback,csv_logger],
        verbose=2)
## pd save
def savemetric(path):
    df = pd.DataFrame(columns=['time','epoch','train Loss','training accuracy','val Loss','val accuracy','valmeaniou'])#列名
    df.to_csv(path,index=False) #路径可以根据需要更改
## plot
def plot_hist(hist):
    plt.plot(hist.history["accuracy"])
    plt.plot(hist.history["val_accuracy"])
    plt.title("model accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.savefig("./run/train/plots/{dt_now}.jpg")
    plt.show()    
