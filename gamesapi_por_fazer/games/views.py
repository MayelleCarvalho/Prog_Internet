"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .models import Game, GameCategory, Player, Score
from .serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, ScoreSerializer

# class ApiRoot(generics.GenericAPIView):
#
# 	name = 'api-root'
# 	def get(self, request,*args,**kwargs):
# 		return Response({'players': reverse(PlayerList.name,request=request),
# 						 'game-categories': reverse(GameCategoryList.name,request=request),
# 						 'games': reverse(GameList.name,request=request),
# 						 'scores': reverse(ScoreList.name,request=request)
# 						 })
#

class GameList(generics.ListCreateAPIView):

	queryset = Game.objects.all()
	serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Game.objects.all()
	serializer_class = GameSerializer


class GameCategoryList(generics.ListCreateAPIView):

	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer


class PlayerList(generics.ListCreateAPIView):

	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-detail'


class ScoreList(generics.ListCreateAPIView):

	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-list'


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):

	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-detail'


# @api_view(['GET','PUT', 'POST', 'DELETE'])
# def game_detail(request, id):
# 	try:
# 		game = Game.objects.get(id=id)
# 	except Game.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
#
# 	if request.method == 'GET':
# 		games_serializer = GameSerializer(game)
# 		return Response(games_serializer.data)
#
# 	elif request.method == 'PUT':
# 		games_serializer = GameSerializer(game, data=request.data)
# 		if games_serializer.is_valid():
# 			games_serializer.save()
# 			return Response(games_serializer.data)
# 		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	elif request.method == 'DELETE':
# 		game.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def game_list(request):
# 	if request.method == 'GET':
# 		games = Game.objects.all()
# 		games_serializer = GameSerializer(games, many=True)
# 		return Response(games_serializer.data)
# 	elif request.method == 'POST':
# 		games_serializer = GameSerializer(data=request.data)
# 		if games_serializer.is_valid():
# 			games_serializer.save()
# 			return Response(games_serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class GameList(mixins.ListModelMixin,
# 			   mixins.CreateModelMixin,
# 			   mixins.GenericAPIView):
#
# 	queryset = Game.objects.all()
# 	serializer_class = GameSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)
#
# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)



# class GameDetail(mixins.RetrieveModelMixin,
# 				 mixins.UpdateModelMixin,
# 				 mixins.DestroyModelMixin,
# 				 mixins.GenericAPIView):
#
# 	queryset = Game.objects.all()
# 	serializer_class = GameSerializer
#
# 	def get(self, request, *args, **kwargs):
# 		return self.retrive(request, *args, **kwargs)
#
#
# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)
#
#
# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)