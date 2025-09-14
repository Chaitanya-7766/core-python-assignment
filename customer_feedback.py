def positive_feedback(ratings):
    count=0
    for rating in ratings:
        if rating == 4 or rating == 5:
            count+=1
    return count
ratings=[5,4,3,5,2,4,1,5]
positives=positive_feedback(ratings)
positivesPercentage=positives/round(len(ratings),1)
print(f"Positive Feedback: {positivesPercentage*100}%")