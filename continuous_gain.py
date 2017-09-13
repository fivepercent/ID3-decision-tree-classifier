def continuous_gain(data, attribute):
    attriList = np.array(data[attribute]).tolist()
    attriList.sort()
    TList=[]
    for i in range(len(attriList)-1):
        TList.append((attriList[i]+attriList[i+1])/2)
    gain_max=0

    for Tn in TList:
        p_smaller=data[data[attribute]<=Tn].shape[0]/num_total
        p_larger=1-p_smaller
        entropy_smaller=calculateEntropy(data[data[attribute]<=Tn])
        entropy_larger=calculateEntropy(data[data[attribute]>Tn])
        gain_continuous=entropy-(p_smaller*entropy_smaller)-(p_larger*entropy_larger)
        if(gain_continuous>gain_max):
            T=Tn
            gain_max=gain_continuous
    return (gain_max, T)