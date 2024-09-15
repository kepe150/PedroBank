import pickle
name = 'configValues.pkl'

def getConfig():
    with open(name, 'rb') as archive:
        values = pickle.load(archive)
    return values

def setConfig(type, value):
    values = getConfig()
    values[type] = value

    with open(name, 'wb') as archive:
        pickle.dump(values, archive)
    return True


