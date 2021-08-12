# Historical-Simulation-in-Conjunction-with-GARCH-Model-for-Value-at-Risk-(VaR)
### Introduction
- This *Python* code is applied to compute __*rolling Value at Risk(VaR)*__ of fiancial assets and some of economic time series, based on the procedure proposed by [*Hull & White(1998)*](http://www.smartquant.com/references/VaR/var32.pdf).
- The model integrates historical simulation, GARCH(1,1) model and rolling samples technology for the calculation of *VaR*. More specifically, I set two rolling windows in the code, one is called *"big window"* and the other is named as *"small window"*, among which the latter is included in the former. When the procedure is working, 
