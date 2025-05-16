import unittest
from hw2 import Profile, Activity, Post, Message, User

class TestProfile(unittest.TestCase):
    """Test cases for the Profile class"""

    def test_profile_initialization(self):
        """Test the initialization of a Profile instance."""
        profile = Profile("user1", "password1", "User One", "user1@example.com")
        self.assertEqual(profile.username, "user1")
        self.assertEqual(profile.password, "password1")
        self.assertEqual(profile.screen_name, "User One")
        self.assertEqual(profile.email, "user1@example.com")

    def test_modify_profile(self):
        """Test modifying a profile"""
        profile = Profile("user1", "password1", "User One", "user1@example.com")
        profile.modify_profile(screen_name="Updated Name", email="updated@example.com")
        self.assertEqual(profile.screen_name, "Updated Name")
        self.assertEqual(profile.email, "updated@example.com")

class TestActivity(unittest.TestCase):
   """Test cases for the Activity class."""
  
   def setUp(self):
       self.user = User("user1", "password1", "User One", "user1@example.com")
       self.activity = Activity(self.user, "Test Content")
  
   def test_activity_initialization(self):
       """Test the initialization of an Activity instance."""
       self.assertEqual(self.activity.user, self.user)
       self.assertEqual(self.activity.content, "Test Content")

   def test_activity_str(self):
        """Test if the __str__ method returns the expected string."""
        expected_str = "User One - Test Content"
        self.assertEqual(str(self.activity), expected_str)


class TestPost(unittest.TestCase):
   """Test cases for the Post class."""
  
   def test_post_str(self):
       """Test if the __str__ method returns the expected string."""
       user = User("user1", "password1", "User One", "user1@example.com")
       post = Post(user, "Test Post Content")
       expected_str = "Post by User One: Test Post Content"
       self.assertEqual(str(post), expected_str)


class TestMessage(unittest.TestCase):
   """Test cases for the Message class."""
  
   def setUp(self):
       self.sender = User("sender1", "password1", "Sender One", "sender1@example.com")
       self.receiver = User("receiver1", "password2", "Receiver One", "receiver1@example.com")
       self.message = Message(self.sender, self.receiver, "Test Message Content")


   def test_message_initialization(self):
       """Test the initialization of a Message instance."""
       self.assertEqual(self.message.user, self.sender)
       self.assertEqual(self.message.receiver, self.receiver)
       self.assertEqual(self.message.content, "Test Message Content")


   def test_message_str(self):
       """Test if the __str__ method returns the expected string."""
       expected_str = "Message from Sender One to Receiver One: Test Message Content"
       self.assertEqual(str(self.message), expected_str)

class TestUser(unittest.TestCase):
   """Test cases for the User class."""
  
   def setUp(self):
       self.user = User("user1", "password1", "User One", "user1@example.com")


   def test_create_post(self):
       """Test creating a post for a user."""
       post = self.user.create_post("Test Post Content")
       # Check if the post is added to the user's posts list
       self.assertIn(post, self.user.posts)
       # Check if the user is correct
       self.assertEqual(post.user, self.user)
       # Check if the content of the post is correct
       self.assertEqual(post.content, "Test Post Content")


   def test_create_post_empty_content(self):
       """Test creating a post with empty content. Expecting a ValueError to be raised."""
       with self.assertRaises(ValueError):
           self.user.create_post("")


   def test_send_message(self):
       """Test sending a message from a user to another user."""
       receiver = User("receiver1", "password2", "Receiver One", "receiver1@example.com")
       message = self.user.send_message(receiver, "Test Message Content")
       self.assertIn(message, self.user.messages)
       self.assertEqual(message.user, self.user)
       self.assertEqual(message.receiver, receiver)
       self.assertEqual(message.content, "Test Message Content")

   def test_send_message_empty_content(self):
       """Test sending a message with empty content. Expecting a ValueError to be raised."""
       receiver = User("receiver1", "password2", "Receiver One", "receiver1@example.com")
       with self.assertRaises(ValueError):
           self.user.send_message(receiver, "")

if __name__ == '__main__':
    unittest.main()
