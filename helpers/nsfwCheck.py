def nsfw_check(results):
    content = {
        'nude': False,
        'violence': False
        # 'drugs': False
    }

    for res in results:
        if res['preds']['nude_score'] >= 80:
            content['nude'] = True

        # if res['preds']['drugs_score'] > 35 and res['preds']['natural_score'] < 25:
        #     content['drugs'] = True

        if res['preds']['violence_score'] > 35 and res['preds']['natural_score'] < 25:
            content['violence'] = True

        if res['preds']['violence_score'] > 39:
            content['violence'] = True

    return content