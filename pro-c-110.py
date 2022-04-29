import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

readcsv=pd.read_csv('medium_data.csv')
data=readcsv['claps'].tolist()
mean=statistics.mean(data)
print('mean is:',mean)

# Mean of gien data sample
def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        index=random.randint(0,len(data))
        value=data[index]
        dataset.append(value)
    meanof30data=statistics.mean(dataset)
    return meanof30data

def graph(meanlist):
    graph=meanlist
    graphdata=ff.create_distplot([graph],['claps'],show_hist=False)
    graphdata.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='Mean'))
    graphdata.show()

# Function to get mean of 30 data 100 times
def setup():
    meanlist=[]
    for i in range(0,100):
        pushtomean=randomsetofmean(30)
        meanlist.append(pushtomean)
    graph(meanlist)
    print("Sampling mean is:",statistics.mean(meanlist))

setup()