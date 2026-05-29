import sys
import math

class Node:
    def __init__(self):
        self.attribute = None
        self.children = {}
        self.isLeaf = False
        self.classLabel = None

def getEntropy(data):
    total = len(data)
    entropy = 0.0
    if total == 0:
        return entropy
    counts = {}
    for row in data:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1
    for count in counts.values():
        entropy -= (count / total) * math.log2(count / total)
    return entropy
        

def buildTree(data, attributes):
    node = Node()
    labels = [row[-1] for row in data]
    
    if len(set(labels)) == 1:
        node.isLeaf = True
        node.classLabel = labels[0]
        return node

    majorClass = max(sorted(set(labels)), key=labels.count)

    if len(attributes) <= 1:
        node.isLeaf = True
        node.classLabel = majorClass
        return node
    
    baseEntropy = getEntropy(data)
    GainRatio = -1.0
    idx = -1
    
    for i in range(len(attributes) - 1):
        attrValues = set([row[i] for row in data])
        tmpEntropy = 0.0
        splitInfo = 0.0
        
        for value in attrValues:
            subset = [row for row in data if row[i] == value]
            ratio = len(subset) / len(data)
            tmpEntropy += ratio * getEntropy(subset)
            if ratio > 0:
                splitInfo -= ratio * math.log2(ratio)
            
        infoGain = baseEntropy - tmpEntropy
        
        if splitInfo == 0:
            tmpGainRatio = infoGain
        else:
            tmpGainRatio = infoGain / splitInfo
        
        if tmpGainRatio > GainRatio:
            GainRatio = tmpGainRatio
            idx = i
            
    node.attribute = attributes[idx]
    node.classLabel = majorClass
    
    attrValues = set([row[idx] for row in data])
    
    for value in attrValues:
        subset = []
        for row in data:
            if row[idx] == value:
                newRow = row[:idx] + row[idx+1:]
                subset.append(newRow)
                
        if len(subset) == 0:
            leaf = Node()
            leaf.isLeaf = True
            leaf.classLabel = majorClass
            node.children[value] = leaf
        else:
            newAttributes = attributes[:idx] + attributes[idx+1:]
            node.children[value] = buildTree(subset, newAttributes)
            
    return node

def classify(node, testTuple, testAttributes):
    if node.isLeaf:
        return node.classLabel
        
    attrIdx = testAttributes.index(node.attribute)
    testValue = testTuple[attrIdx]
    
    if testValue not in node.children:
        return node.classLabel
        
    return classify(node.children[testValue], testTuple, testAttributes)

def main():
    trainFile = sys.argv[1]
    testFile = sys.argv[2]
    outputFile = sys.argv[3]

    trainData = []
    trainAttributes = []
    
    with open(trainFile, 'r') as file:
        lines = file.readlines()
        if len(lines) > 0:
            trainAttributes = lines[0].strip().split('\t')
            for line in lines[1:]:
                items = line.strip().split('\t')
                trainData.append(items)
            

    root = buildTree(trainData, trainAttributes)
    
    testData = []
    testAttributes = []
    with open(testFile, 'r') as file:
        lines = file.readlines()
        if len(lines) > 0:
            testAttributes = lines[0].strip().split('\t')
            for line in lines[1:]:
                items = line.strip().split('\t')
                testData.append(items)
            
    with open(outputFile, 'w') as out:
        out.write('\t'.join(trainAttributes) + '\n')
        
        for testTuple in testData:
            predictedClass = classify(root, testTuple, testAttributes)
            
            result = testTuple + [predictedClass]
            out.write('\t'.join(result) + '\n')

if __name__ == "__main__":
    main()
