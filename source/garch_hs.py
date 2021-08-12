import numpy as np
from arch import arch_model
import pandas as pd

def GARCH_HS(s, winsize, day=4, miu=False):
    s = s.reset_index(drop=True)  # 对Series s 重设索引
    

    garch = arch_model(y=s, mean='Constant', lags=0, vol='GARCH', p=1, o=0, q=1, dist='normal')
        
    garchmodel = garch.fit(disp=0)
    params = garchmodel.params
    sigma = sigma_2 = np.zeros(winsize + 1)  # +1 是为了放未来波动率的预测值

    # Set volatility at the 1st time point of the 2rd window
    if day != 0:
        sigma[0] = (s[winsize - day:winsize]).std()
    else:
        sigma[0] = 0.0


    ret = s[winsize - 1:]
    ret = ret.reset_index(drop=True)

    
    # Set gamma (γ)
    if miu:
        gamma = ret - params[0]
    else:
        gamma = ret
    
    # gamma = ret
    
    gamma_2 = gamma ** 2
    
    for i in range(winsize):
        sigma_2[i + 1] = params[1] + params[2] * gamma_2[i] + params[3] * sigma_2[i]
    
    sigma = np.sqrt(sigma_2)
    
    wight = 1 / sigma[:-1]
    wight_ret = ret * wight * sigma[-1]
    VaR_p5 = np.percentile(wight_ret, 5)
    VaR_p50 = np.percentile(wight_ret, 50)

    return VaR_p5, VaR_p50