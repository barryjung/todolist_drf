from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import UserSerializer, UserEditSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료"})
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = UserEditSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "수정완료"})
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        request.user.delete()
        return Response({"message": "삭제완료"}, status=status.HTTP_204_NO_CONTENT)
