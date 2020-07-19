import numpy as np
def calculate(list):
    if len(list)<9:
      raise ValueError("List must contain nine numbers.")
    else:
          
      arr=np.array(list).reshape((3,3))
      #Calculating mean
      mean_zeroaxis=arr.mean(axis=0)
      mean_oneaxis=arr.mean(axis=1)
      mean=arr.mean()
      
      #Calculating variance
      var_zeroaxis=arr.var(axis=0)
      var_oneaxis=arr.var(axis=1)
      var=arr.var()
      
      #Calculating standard deviation
      std_zeroaxis=arr.std(axis=0)
      std_oneaxis=arr.std(axis=1)
      std=arr.std()
      
      #Calculating maximum
      max_zeroaxis=arr.max(axis=0)
      max_oneaxis=arr.max(axis=1)
      maxx=arr.max()
      
      #Calculating minimum
      min_zeroaxis=arr.min(axis=0)
      min_oneaxis=arr.min(axis=1)
      mini=arr.min()
      
      #Calculating sum
      sum_zeroaxis=arr.sum(axis=0)
      sum_oneaxis=arr.sum(axis=1)
      summ=arr.sum()
      
      calculations={"mean":[[i for i in(mean_zeroaxis)],[i for i in (mean_oneaxis)],mean],
              "variance":[[i for i in(var_zeroaxis)],[i for i in (var_oneaxis)],var],
              "standard deviation":[[i for i in(std_zeroaxis)],[i for i in (std_oneaxis)],std],
              "max":[[i for i in(max_zeroaxis)],[i for i in (max_oneaxis)],maxx],
              "min":[[i for i in(min_zeroaxis)],[i for i in (min_oneaxis)],mini],
              "sum":[[i for i in(sum_zeroaxis)],[i for i in (sum_oneaxis)],summ]}
      return calculations
