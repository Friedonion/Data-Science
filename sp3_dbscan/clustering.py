import sys
import os

def Dbscan(points, eps, minPts):
    grid = {}
    for pt in points:
        gx = int(pt[1] / eps)
        gy = int(pt[2] / eps)
        gridKey = (gx, gy)
        if gridKey not in grid:
            grid[gridKey] = []
        grid[gridKey].append(pt)
        
    pointDict = {pt[0]: pt for pt in points}
    
    visited = set()
    clustered = set()
    clusters = []
    
    for pt in points:
        ptId = pt[0]
        if ptId in visited:
            continue
        visited.add(ptId)
        
        neighbors = []
        gx = int(pt[1] / eps)
        gy = int(pt[2] / eps)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                gridKey = (gx + dx, gy + dy)
                if gridKey in grid:
                    for cand in grid[gridKey]:
                        dist = ((pt[1] - cand[1])**2 + (pt[2] - cand[2])**2)**0.5
                        if dist <= eps:
                            neighbors.append(cand[0])
                            
        if len(neighbors) < minPts:
            continue
            
        currentCluster = [ptId]
        clustered.add(ptId)
        
        seedSet = list(neighbors)
        if ptId in seedSet:
            seedSet.remove(ptId)
            
        for nId in seedSet:
            if nId not in clustered:
                clustered.add(nId)
                currentCluster.append(nId)
                
        idx = 0
        while idx < len(seedSet):
            currId = seedSet[idx]
            if currId not in visited:
                visited.add(currId)
                
                currPt = pointDict[currId]
                currNeighbors = []
                cgx = int(currPt[1] / eps)
                cgy = int(currPt[2] / eps)
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        gridKey = (cgx + dx, cgy + dy)
                        if gridKey in grid:
                            for cand in grid[gridKey]:
                                dist = ((currPt[1] - cand[1])**2 + (currPt[2] - cand[2])**2)**0.5
                                if dist <= eps:
                                    currNeighbors.append(cand[0])
                                    
                if len(currNeighbors) >= minPts:
                    for nId in currNeighbors:
                        if nId not in seedSet:
                            seedSet.append(nId)
                            if nId not in clustered:
                                clustered.add(nId)
                                currentCluster.append(nId)
            idx += 1
            
        clusters.append(currentCluster)
        
    return clusters

def main():
    if len(sys.argv) < 5:
        sys.exit(1)
        
    inputFileName = sys.argv[1]
    n = int(sys.argv[2])
    eps = float(sys.argv[3])
    minPts = int(sys.argv[4])
    
    points = []
    with open(inputFileName, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                ptId = int(parts[0])
                x = float(parts[1])
                y = float(parts[2])
                points.append((ptId, x, y))
                
    clusters = Dbscan(points, eps, minPts)
    
    baseName = os.path.splitext(os.path.basename(inputFileName))[0]
    clusters.sort(key=len, reverse=True)
    selected = clusters[:n]
    for idx, cluster in enumerate(selected):
        cluster.sort()
        outFileName = f"{baseName}_cluster_{idx}.txt"
        with open(outFileName, 'w') as outFile:
            for ptId in cluster:
                outFile.write(f"{ptId}\n")

if __name__ == "__main__":
    main()
