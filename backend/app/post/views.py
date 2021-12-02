#리액트의 라우트 역할 보여지는 것 관리함. Post라는 엔드포인트에 Get이라는 메서드를 날렸을 경우에 하는 동작을 View에서 담당. api URL 엔드포인트라고 칭함.
#View에서 URL로 들어온 요청을 처리함.
# 전체 조회, 개별 생성, 개별 조회
# 기능이 나왔으면, URL 설계를 먼저 함. (엔드포인트 설계) 레스트 하게 설계를 하라.
# serializer는 오브젝트를 json으로 변환하는 것임. 그 반대도 가능.


from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from app.post.serializers import PostSerializer

from app.post.models import Post


class PostListCreateView(ListCreateAPIView): #전체 조회와 생성
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_id' #어떤 값으로 조회할 것인지?
    lookup_field = 'id'



