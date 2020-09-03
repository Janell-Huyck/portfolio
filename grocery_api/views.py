from rest_framework.viewsets import ModelViewSet
from grocery_api.serializers import GroceryItemSerializer, CustomUserSerializer
from grocery_list_backend.models import GroceryItem
from custom_user.models import CustomUser


class GroceryItemViewSet(ModelViewSet):
    """Returns all grocery items for the requesting user"""

    basename = "grocery_item"
    serializer_class = GroceryItemSerializer

    def get_queryset(self):
        shopper = self.request.user
        if shopper.id:
            queryset = GroceryItem.objects.filter(shopper=shopper)
        else:
            queryset = []
        return queryset


class CustomUserViewSet(ModelViewSet):
    """Returns all users"""

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


"""

class GhostPostViewSet(ModelViewSet):
    basename = 'posts'
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.all()

    @action(detail=True, methods=['post'])
    def likePost(self, request, pk=None):
        ghostpost = self.get_object()
        ghostpost.up_votes += 1
        ghostpost.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['post'])
    def dislikePost(self, request, pk=None):
        ghostpost = self.get_object()
        ghostpost.down_votes += 1
        ghostpost.save()
        return Response({'status': 'downvoted'})


class BoastViewSet(ModelViewSet):
    basename = 'boasts'
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.filter(is_boast=True)


class RoastViewSet(ModelViewSet):
    basename = 'roasts'
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.filter(is_boast=False)




# inside views.py
def create(response):
    if response.method == "POST":
	form = CreateNewList(response.POST)

	if form.is_valid():
	    n = form.cleaned_data["name"]
	    t = ToDoList(name=n)
	    t.save()
	    response.user.todolist.add(t)  # adds the to do list to the current logged in user

	    return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})
"""
