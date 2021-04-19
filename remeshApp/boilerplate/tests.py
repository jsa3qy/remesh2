from django.test import TestCase
from .models import Conversation, Message, Thought
from .forms import ConversationForm, MessageForm, ThoughtForm, SearchForm
from django.urls import reverse
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your tests here.

class ConversationTests(TestCase):

    def create_conversation(self, title="only a test"):
        return Conversation.objects.create(title=title)

    def test_conversation_creation(self):
        w = self.create_conversation()
        self.assertTrue('Conversation' in str(w))

class MessageTests(TestCase):

    def create_message(self, title="only a test"):
        #parent model necessary, tested above
        conversation = Conversation.objects.create(title=title)
        return Message.objects.create(title=title, conversation_id=conversation)

    def test_message_creation(self):
        w = self.create_message()
        self.assertTrue('Message' in str(w))

class ThoughtTests(TestCase):

    def create_thought(self):
        #parent model dependencies (all tested alone above)
        title = "only a test"
        conversation = Conversation.objects.create(title=title)
        message = Message.objects.create(title=title, conversation_id=conversation)

        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        return Thought.objects.create(text=text, message_id=message)
    
    def test_thought_creation(self):
        w = self.create_thought()
        self.assertTrue('Thought' in str(w))

# Integrated testing
class TestLandingPage(TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) 
        self.driver = browser

    # goes to conversations page and makes a conversation
    def test_conversation_landing_and_creation(self):
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_id('new_convo').send_keys("test title")
        self.driver.find_element_by_id('submit_button').click()
        self.assertIn("test title", self.driver.find_element_by_class_name('python-test-selenium').get_attribute("innerText"))

    # goes to messages page for a conversation and makes a message
    def test_message_landing(self):
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_id('new_convo').send_keys("test title")
        self.driver.find_element_by_id('submit_button').click()
        self.driver.find_element_by_class_name('js-message-link').click()
        self.assertIn("Past Messages", self.driver.find_element_by_class_name('python-test-selenium').get_attribute("innerText"))

    # goes to through the entire flow above, making its way to a thoughts page to confirm the page loads 
    def test_thought_landing(self):
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_id('new_convo').send_keys("test title")
        self.driver.find_element_by_id('submit_button').click()
        self.driver.find_element_by_class_name('js-message-link').click()
        self.driver.find_element_by_id('new_message').send_keys("test title")
        self.driver.find_element_by_id('submit_button').click()
        self.driver.find_element_by_class_name('js-message-link').click()
        self.assertIn("Past Thoughts", self.driver.find_element_by_class_name('python-test-selenium').get_attribute("innerText"))

    def tearDown(self):
        self.driver.quit

class TestSearchFunctionality(TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) 
        self.driver = browser

    # goes to the conversation page and adds three conversations, ensures that search functionality leaves us with the correct number of results
    def test_conversation_landing_and_creation(self):
        self.driver.get("http://localhost:8000")
        self.driver.find_element_by_id('new_convo').send_keys("a")
        self.driver.find_element_by_id('submit_button').click()
        self.driver.find_element_by_id('new_convo').send_keys("unique_convo_name")
        self.driver.find_element_by_id('submit_button').click()
        self.driver.find_element_by_id('new_convo').send_keys("c")
        self.driver.find_element_by_id('submit_button').click()
        
        self.driver.find_element_by_id('search_input').send_keys("unique_convo_name")
        self.driver.find_element_by_id('search_button').click()
        results_list = self.driver.find_elements_by_class_name('conversation-list-items')
        print(results_list)

        self.assertEqual(len(results_list), 1)

    def tearDown(self):
        self.driver.quit

class TestForms(TestCase):
    def test_valid_conversation_form(self):
        w = Conversation.objects.create(title='Foo')
        data = {'title': w.title}
        form = ConversationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_message_form(self):
        conversation = Conversation.objects.create(title='Foo')
        w = Message.objects.create(title='Foo',conversation_id=conversation)
        data = {'title': w.title}
        form = MessageForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_thought_form(self):
        conversation = Conversation.objects.create(title='Foo')
        message = Message.objects.create(title='Foo',conversation_id=conversation)
        w = Thought.objects.create(text='Foo',message_id=message)
        data = {'text': w.text}
        form = ThoughtForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_search_form(self):
        data = {'search_text': 'test search'}
        form = SearchForm(data)
        self.assertTrue(form.is_valid())

    # invalid forms
    def test_invalid_conversation_form(self):
        w = Conversation.objects.create(title='Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        data = {'title': w.title}
        form = ConversationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_message_form(self):
        conversation = Conversation.objects.create(title='Foo')
        w = Message.objects.create(title='Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.',conversation_id=conversation)
        data = {'title': w.title}
        form = MessageForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_thought_form(self):
        conversation = Conversation.objects.create(title='Foo')
        message = Message.objects.create(title='Foo',conversation_id=conversation)
        w = Thought.objects.create(text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.',message_id=message)
        data = {'text': w.text}
        form = ThoughtForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_search_form(self):
        data = {'search_text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit.'}
        form = SearchForm(data)
        self.assertFalse(form.is_valid())
