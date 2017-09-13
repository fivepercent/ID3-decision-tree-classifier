def discrete_gain(data, attribute):
    gain_attr=calculateEntropy(data)
    for attr_value in data[attribute].unique():
        num_attr_value=data[data[attribute]==attr_value].shape[0]
        entropy_attr=calculateEntropy(data[data[attribute]==attr_value])
        gain_attr-=(num_attr_value/num_total)*entropy_attr
    return gain_attr