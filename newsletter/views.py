from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NewsletterSubscriber
from .serializers import NewsletterSubscriberSerializer
import uuid

@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Check if already subscribed and active
    if NewsletterSubscriber.objects.filter(email=email, subscribed=True).exists():
        return Response({'error': 'Already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
    
    # If exists but unsubscribed, resubscribe
    try:
        subscriber = NewsletterSubscriber.objects.get(email=email)
        subscriber.subscribed = True
        subscriber.confirmation_code = uuid.uuid4()
        subscriber.save()
        serializer = NewsletterSubscriberSerializer(subscriber)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except NewsletterSubscriber.DoesNotExist:
        # Create new subscriber
        subscriber = NewsletterSubscriber(email=email)
        subscriber.confirmation_code = uuid.uuid4()
        subscriber.save()
        serializer = NewsletterSubscriberSerializer(subscriber)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def unsubscribe(request, code):
    try:
        subscriber = NewsletterSubscriber.objects.get(confirmation_code=code)
        subscriber.subscribed = False
        subscriber.save()
        return Response({'message': 'Successfully unsubscribed'}, status=status.HTTP_200_OK)
    except NewsletterSubscriber.DoesNotExist:
        return Response({'error': 'Invalid unsubscribe link'}, status=status.HTTP_404_NOT_FOUND)
