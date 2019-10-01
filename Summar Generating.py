def generate_summary(scores,threshold):
    summary=" "
    for i in scores:
        if(scores[i]>threshold):
            summary=summary+" "+i
    return summary
