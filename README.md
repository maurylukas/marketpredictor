<h1 align="center">Market Predictor</h1>
<p>&nbsp;</p>
<h2 align="left">A fully customizable live market forecaster deployed and monitored via Prefect tool for Python</h2>
<p>&nbsp;</p>

|<h3 align="center">First we get market info from Yahoo Finance API</h3>|<h3 align="center">Then we normalize the chosen data</h3>| 
|------------|-------------|
|<p align="center"><img src="https://user-images.githubusercontent.com/97759783/227783798-62730bff-deda-4ada-b5ce-21fa66e05a91.png" alt="market prices" width="100%"></img>|<img src="https://user-images.githubusercontent.com/97759783/227783804-7f726243-5081-4492-a822-82647963340a.png" alt="normal data" width="100%"></img></p>|

<p>&nbsp;</p>
<h3 align="center">After that we train and test on a deep learning model until we get above 90% improvement over benchmark parameter</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/97759783/227783813-ec8f3276-238e-42dd-baf9-211ef4446df5.png" alt="model loss" width="49%"></img>
<img src="https://user-images.githubusercontent.com/97759783/227783815-7a1e936c-124d-4a85-95e3-d23ed0e02c5c.png" alt="model metric" width="49%"></img>
</p>

<p>&nbsp;</p>
<h3 align="center">At last we can schedule a flow to repeatedly run, for example, every 5 minutes or so</h3>
<p align="center"> <img src="https://user-images.githubusercontent.com/97759783/227785220-77ba52aa-82c5-4d4e-b12f-fe122e20d700.png" alt="flow deploy" /> </p>
