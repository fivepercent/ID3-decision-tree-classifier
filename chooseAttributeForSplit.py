def chooseAttributeForSplit(data):
    max_gain=0
    res=(None,None)
    for attribute in data.columns:
        if(attribute=='好瓜'):
            continue
        T=None
        if(type(data[attribute].iloc[0])==str):
            gain_attr=discrete_gain(data, attribute)
        else:
            (gain_attr, T)=continuous_gain(data, attribute)
        if(gain_attr>max_gain):
            res=(attribute, T)
            max_gain=gain_attr
    return res