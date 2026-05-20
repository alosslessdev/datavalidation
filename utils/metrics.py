def calculate_quality_score(results):

    total = len(results)

    success = sum(r["success"] for r in results)

    score = (success / total) * 100

    return round(score, 2)
