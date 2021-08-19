# VaR-Based-on-Historical-Simulation-in-Conjunction-with-GARCH-Model
## by *Yingxin LIN*
### 
### Introduction
- This *Python* code is applied to compute __*rolling Value at Risk(VaR)*__ of fiancial assets and some of economic time series, based on the procedure proposed by [*Hull & White(1998)*](http://www.smartquant.com/references/VaR/var32.pdf).
- __*Output*__
</br>This code can output *rolling VaR* time series at any rolling window length and quantiles which you're intrested in, as shown in *Fig.1 below*.
#### *Fig.1 VaR at diffrent winsize(A) & at diffrent quantiles(B)*
![fig.1](https://github.com/lyx66/limyingxin/blob/master/Function%20of%20Main%20code.png?raw=false)
- __*How dose this code work?*__
</br>The model integrates __*historical simulation, GARCH(1,1) model and rolling samples technology*__ for the calculation of *VaR*. More specifically, I set two rolling windows in the code, one is called *"big window"* and the other is named as *"small window"*, among which the latter is included in the former. 
1. When the procedure works, big window is used to estimate GARCH(1,1) model so that the volatility of assets in each time point will be available. 
2. After that, the historical data will be updated by the GARCH volatility (*i.g.* that is, wighted by the volatility), so that the difference betweenthe historical volatility of the market variable and its current volatility can be reflected[*(Hull & White, 1998)*](http://www.smartquant.com/references/VaR/var32.pdf).
3. Finally, historical simulation will be applied in the small window, and then *VaR* is computed successfully.
- Since the big window and small window mentioned above is rolling forword, the *VaR* outputted by this code will be *rolling VaR* (see *Fig.2* below).
#### *Fig.2 Rolling VaR time series at different winsizes*
![fig.2](https://github.com/lyx66/Value-at-Risk-VaR-Based-on-Historical-Simulation-in-Conjunction-with-GARCH-Model/blob/main/Rolling%20VaR%20at%20different%20winsizes.png?raw=false)

### Tips
- By modified `winsize` in [Main code](https://github.com/lyx66/Historical-Simulation-in-Conjunction-with-GARCH-Model-for-Value-at-Risk-VaR/blob/main/Main%20code.ipynb), you can change the lenth of rolling window. Accordingly, `2 * winsize - 1` observations will be lost, since there is two rolling windows in my code.
- In a stantard GARCH(1,1) model, the volatility of financial time series can be described as fellow equation: 
<div align=center><img src="https://raw.githubusercontent.com/lyx66/limyingxin/9eeb37e2ca5c106dbd4c811db198bf0ca17a6209/MommyTalk1628787855537.svg"/></div>

- Since the average value of a financial time serie is always close to 0, the residual error is quite close to financial time serie itself in GARCH model. Therefore, I approximate residuals to time series to reduce running time in this code. The relevant codes are shown below ( within function `GARCH_HS` ):</br>
```
def GARCH_HS(s, winsize, day=4, miu=False):

    ······
    # Approximate residuals gamma to asset return time series
    gamma = ret
    gamma_2 = gamma ** 2

    # Obtain volatility
    for i in range(winsize):
        sigma_2[i + 1] = params[1] + params[2] * gamma_2[i] + params[3] * sigma_2[i]

    sigma = np.sqrt(sigma_2)
    ······
```

### Files loaded
- In code, the *VaR* model can be constructed using daily return data from the 37 industrial stock indexes in Chinese stock market, which should be loaded from a csv file named as [*all_Industry_resid_data_num.csv*](https://github.com/lyx66/Historical-Simulation-in-Conjunction-with-GARCH-Model-for-Value-at-Risk-VaR/blob/main/all_Industry_resid_data_num.csv).

### Copyright notice
- AUTHOR: __*Yingxin LIN*__
- Company: *Prof.[__FAN Yi__](http://sf.cufe.edu.cn/info/1112/10555.htm)'s workshop, School of Finance, Central University of Finance and Economics* (CUFE)
- Contact: lyxurthebest@163.com or lyxurthebest@outlook.com
- The copyright belongs to __*Yingxin LIN*__ , 2021/08/12.
#### *Enjoy*（。＾▽＾) *! (...and extend/modify)* 😊
