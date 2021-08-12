# Historical-Simulation-in-Conjunction-with-GARCH-Model-for-Value-at-Risk-(VaR)
## by *Yingxin LIN*
### 
### Introduction
- This *Python* code is applied to compute __*rolling Value at Risk(VaR)*__ of fiancial assets and some of economic time series, based on the procedure proposed by [*Hull & White(1998)*](http://www.smartquant.com/references/VaR/var32.pdf).
- __*How it work?*__
</br>The model integrates __historical simulation, GARCH(1,1) model and rolling samples technology__ for the calculation of *VaR*. More specifically, I set two rolling windows in the code, one is called *"big window"* and the other is named as *"small window"*, among which the latter is included in the former. 
1. When the procedure works, big window is used to estimate GARCH(1,1) model so that the volatility of assets in each time point will be available. 
2. After that, the historical data will be updated by the GARCH volatility (*i.g.* that is, wighted by the volatility), so that the difference betweenthe historical volatility of the market variable and its current volatility can be reflected[*(Hull & White, 1998)*](http://www.smartquant.com/references/VaR/var32.pdf).
3. Finally, historical simulation will be applied in the small window, and then *VaR* is computed successfully.
- Since the big window and small window mentioned above is rolling forword, the *VaR* outputted by this code will be *rolling VaR* (see *fig.1* below).


### Tips
- by modified `winsize` in [Main code](), you can change the lenth of rolling window. Accordingly, `2 * winsize - 1` observations will be lost, since there is two rolling windows in my code.
