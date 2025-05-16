class Profile:
    def __init__(self, username, password, screen_name, email):
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email

    def modify_profile(self, screen_name=None, email=None):
        if screen_name:
            self.screen_name = screen_name
        if email:
            self.email = email

class Activity:
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        return f"{self.user.screen_name} - {self.content}"

class Post(Activity):
    def __str__(self):
        return f"Post by {self.user.screen_name}: {self.content}"

class Message:
    def __init__(self, user, receiver, content):
        self.user = user
        self.receiver = receiver
        self.content = content

    def __str__(self):
        return f"Message from {self.user.screen_name} to {self.receiver.screen_name}: {self.content}"

class User:
    def __init__(self, username, password, screen_name, email):
        self.username = username
        self.password = password
        self.screen_name = screen_name
        self.email = email
        self.posts = []
        self.messages = []

    def create_post(self, content):
        if content == '':
            raise ValueError("Post content cannot be empty.")
        else:
            post = Post(self, content)
            self.posts.append(post)
            return post

    def send_message(self, receiver, content):
        if content == '':
            raise ValueError("Message cannot be empty.")
        else:
            message = Message(self, receiver, content)
            self.messages.append(message)
            return message
