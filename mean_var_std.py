import numpy as np

def calculate(list):
    if(validate(list)):
        nList= np.asarray(list, dtype=np.float64).reshape(3,3)
        rawCalculations = {
            'mean': [
                np.mean(nList, axis=0),
                np.mean(nList, axis=1),
                np.ndarray.flatten(nList).mean()
                ],
            'variance': [
                np.var(nList, axis=0),
                np.var(nList, axis=1),
                np.ndarray.flatten(nList).var()
                ],
            'standard deviation': [
                np.std(nList, axis=0),
                np.std(nList, axis=1),
                np.ndarray.flatten(nList).std()
                ],
            'max': [np.max(nList, axis=0),
                    np.max(nList, axis=1),
                    np.ndarray.flatten(nList).max()
                    ],
            'min': [
                np.min(nList, axis=0),
                np.min(nList, axis=1),
                np.ndarray.flatten(nList).min()],
            'sum': [
                np.sum(nList, axis=0),
                np.sum(nList, axis=1),
                np.ndarray.flatten(nList).sum()]
        }
        calculations = valuesToList(rawCalculations)
        
    return calculations

def validate(list):
    if(len(list) != 9 ):
        raise ValueError('List must contain nine numbers.')
        return False
    return True

def valuesToList(dictionary):
    for key in dictionary:
        dictionary[key] = [item.tolist() if isinstance(item, np.ndarray) else item for item in dictionary[key]]
    return dictionary
