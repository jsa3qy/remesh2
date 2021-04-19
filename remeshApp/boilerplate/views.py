from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import context
import uuid
from .models import Conversation, Message, Thought
from .forms import ConversationForm, MessageForm, ThoughtForm

# Create your views here.

def conversations(request):

    is_search = request.GET.get('search', '')
    # if we are landing on hitting the page after submitting a search on the filter input
    if is_search:
        page_type = request.GET.get('page_type', '')
        id = request.GET.get('id', '')
        title = request.GET.get('title', '')

        if page_type == 'Conversation':
            possible_conversations = Conversation.objects.all()
            if id != '':
                possible_conversations = possible_conversations.filter(id = id)
            possible_conversations = possible_conversations.filter(title__contains=title)
            context = {'latest_conversation_list': possible_conversations}

            return render(request, 'boilerplate/conversations.html', context)

    # else we are in a regular hit
    latest_conversation_list = Conversation.objects.all()
    context = {'latest_conversation_list': latest_conversation_list}

    return render(request, 'boilerplate/conversations.html', context)

def messages_for_conversation(request, uuid):

    is_search = request.GET.get('search', '')
    # if we are landing on hitting the page after submitting a search on the filter input
    if is_search:
        page_type = request.GET.get('page_type', '')
        id = request.GET.get('id', '')
        title = request.GET.get('title', '')

        possible_messages = Message.objects.all()
        if id != '':
            possible_messages = possible_messages.filter(conversation_id = id)
        possible_messages = possible_messages.filter(title__contains=title)
        context = {
            'message_list': possible_messages,
            'convo_title': Conversation.objects.filter(id = id)[0].title,
            'convo_id': id
        }
        return render(request, 'boilerplate/messages.html', context)

    # else we are in a regular hit
    message_list = Message.objects.filter(conversation_id = uuid)
    parent_convo_title = Conversation.objects.filter(id = uuid)[0].title

    context = {
        'message_list': message_list,
        'convo_title': Conversation.objects.filter(id = uuid)[0].title,
        'convo_id': uuid
    }
    return render(request, 'boilerplate/messages.html', context)

def thoughts_for_message(request, uuid):
    is_search = request.GET.get('search', '')
    # if we are landing on hitting the page after submitting a search on the filter input
    if is_search:
        page_type = request.GET.get('page_type', '')
        id = request.GET.get('id', '')
        # we search on text for thoughts, not title
        text = request.GET.get('title', '')

        possible_thoughts = Thought.objects.all()
        if id != '':
            possible_thoughts= possible_thoughts.filter(message_id = id)
        possible_thoughts = possible_thoughts.filter(text__contains=text)

        parent_message = Message.objects.filter(id = uuid)[0]
        grandparent_id = parent_message.conversation_id.id

        context = {
            'thoughts_list': possible_thoughts,
            'message_title': Message.objects.filter(id = id)[0].title,
            'message_id': id,
            'convo_id': grandparent_id
        }

        return render(request, 'boilerplate/thoughts.html', context)

    # else we are in a regular hit
    thoughts_list = Thought.objects.filter(message_id = uuid)
    parent_message = Message.objects.filter(id = uuid)[0]
    grandparent_id = parent_message.conversation_id.id
    grandparent_title = parent_message.conversation_id.title


    context = {
        'thoughts_list': thoughts_list,
        'message_title': Message.objects.filter(id = uuid)[0].title,
        'message_id': uuid,
        'convo_id': grandparent_id,
        'grandparent_title': grandparent_title
    }
    return render(request, 'boilerplate/thoughts.html', context)

def conversation_post(request):
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        title = request.POST.get('title', '')
        if (title != ''):
            new_conversation = Conversation(title = title)
            new_conversation.save()
        return HttpResponseRedirect('/')
    return render(request, 'boilerplate/conversations.html')

def message_post(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        title = request.POST.get('title', '')
        conversation_id = request.POST.get('id', '')
        if (title != ''):
            new_conversation = Message(title = title, conversation_id = Conversation.objects.filter(id = conversation_id)[0])
            new_conversation.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    return render(request, 'boilerplate/messages.html')

def thought_post(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        text = request.POST.get('text', '')
        message_id = request.POST.get('id', '')
        if (text != ''):
            new_thought = Thought(text = text, message_id = Message.objects.filter(id = message_id)[0])
            new_thought.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    return render(request, 'boilerplate/thoughts.html')
    