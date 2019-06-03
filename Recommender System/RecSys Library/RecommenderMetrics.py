from surprise import accuracy
from collections import defaultdict


class RecommenderMetrics:

    def MAE(predictions):
        return accuracy.mae(predictions, verbose=False)

    def RMSE(predictions):
        return accuracy.rmse(predictions, verbose=False)

    def GetTopN(predictions, n=10, minimumRating=0):
        topN = defaultdict(list)
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
            if (estimatedRating >= minimumRating):
                topN[userID].append((movieID, estimatedRating))

        for userID, ratings in topN.items():
            ratings.sort(key=lambda x: x[1], reverse=True)
            topN[userID] = ratings[:n]

        return topN

    def HitRate(topNPredicted, leftOutPredictions):
        hits = 0
        total = 0

        # For each left-out rating
        for leftOut in leftOutPredictions:
            userID = leftOut[0]
            leftOutMoiveID = leftOut[1]
            hit = False
            for movieID, predictedRating in topNPredicted[userID]:
                if leftOutMoiveID == movieID:
                    hit = True
                    break
            if hit:
                hits += 1

            total += 1
        return hits/total
