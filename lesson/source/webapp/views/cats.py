def cats_status (request: WSGIRrequest):
    name = request.GET.get('name')
    happy = 10
    satiety = 40


    if request.Post.get('action')=='game':
