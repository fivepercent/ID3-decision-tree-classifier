def calculateEntropy(data):
    num_total=data.shape[0]
    p_good=(data[data['好瓜']=='是'].shape[0])/num_total
    p_not_good=1-p_good
    entropy=0
    if(p_good!=0):
        entropy -= (p_good*np.log2(p_good))
    if(p_not_good!=0):
        entropy -= (p_not_good*np.log2(p_not_good))
    return entropy