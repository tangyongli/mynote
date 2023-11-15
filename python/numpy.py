# 统计特征，不考虑nan
## shape is  32,32,33
np.nanmax(img,axis=-1) # 32.32.1
## 逐通道统计
np.nanmax(img,axis=(0,1)) #32
## mean,std
np.nanmean(img,axis=(0,1))
np.nanstd(img,axis=(0,1)) 
## 只要img中有一个像素 is nan. np.max is nan.others statistic is also nan.if all the pixeles in img are nan, np.nanmax is also nan.
#%%
# 逐通道进行归一化,min,max不需要广播，但是img的最后一个维度要是通道
def normalizemaxmin(img,min,max):
    # min_value = mean - 2 * std
    # max_value = mean + 2 * std
    img = (img - min) / (max- min) # img shape is (33,33,32) min is (32,)
    img = np.clip(img, 0, 1)
    return img
#%% replace nan with specific value
img[np.isnan(img)]=-1
#%%
image=np.concatenate((imgband,imgindex),axis=-1)
