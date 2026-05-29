import sys

def main():
    minSup = float(sys.argv[1])
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]

    transactions = []

    with open(inputFile, 'r') as file:
        for line in file:
            items = line.strip().split('\t')
            transaction = set(map(int, items))
            transactions.append(transaction)
    
    counts = {}
    frequentItemsets = {}
    tmpList = []

    for transaction in transactions:
        for item in transaction:
            itemset = frozenset([item])
            counts[itemset] = counts.get(itemset, 0) + 1 
    
    total = len(transactions)
    minCount = minSup * total / 100
    frequentItemsets = {key: value for key, value in counts.items() if value >= minCount}
    tmpList = list(frequentItemsets.keys())

    k = 2
    while(len(tmpList) > 0):
        counts = {}
        candidates = set()
        tmpSet = set(tmpList)
        
        for i in range(len(tmpList)):
            for j in range(i+1, len(tmpList)):
                candidate = tmpList[i].union(tmpList[j])
                if len(candidate) == k:
                    isValid = True
                    for item in candidate:
                        if candidate - frozenset([item]) not in tmpSet:
                            isValid = False
                            break  
                    if isValid:
                        candidates.add(candidate)
        
        for transaction in transactions:
            for candidate in candidates:
                if candidate.issubset(transaction):
                    counts[candidate] = counts.get(candidate, 0) + 1

        frequentCandidate = {key: value for key, value in counts.items() if value >= minCount}
        frequentItemsets.update(frequentCandidate)
        tmpList = list(frequentCandidate.keys())
        k += 1


    sortedItems = sorted(frequentItemsets.items(), key=lambda x: (len(x[0]), tuple(sorted(x[0]))))
    with open(outputFile, 'w') as out:
        for itemset, supportCount in sortedItems:
            n = len(itemset)
            if n < 2:
                continue
            
            itemsetList = sorted(list(itemset))
            
            for i in range(1, (1 << n) - 1):
                XList = []
                for j in range(n):
                    if i & (1 << j):
                        XList.append(itemsetList[j])
                
                X = frozenset(XList)
                Y = itemset - X
                
                support = (supportCount / total) * 100
                confidence = (supportCount / frequentItemsets[X]) * 100
                
                support = support + 1e-6
                confidence = confidence + 1e-6
                
                strX = "{" + ",".join(map(str, sorted(X))) + "}"
                strY = "{" + ",".join(map(str, sorted(Y))) + "}"
                
                out.writelines(f"{strX}\t{strY}\t{support:.2f}\t{confidence:.2f}\n")
                

if __name__ == "__main__":
    main()
