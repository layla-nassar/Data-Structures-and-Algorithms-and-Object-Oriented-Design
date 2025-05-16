class Activity:
    def __init__(self, user, content):
        self.user = user 
        self.content = content 

    def __str__(self):
        return f"{self.user.profile.screen_name} - {self.content}"
    
class Post(Activity):
    def __str__(self):
        return f"Post by {self.user.profile.screen_name}: {self.content}"
    

class Message(Activity):
    def __init__(self, user, reciever, content):
        super().__init__(user, content)
        self.reciever = reciever 

    def __str__(self):
        return f"Message from {self.user.profile.screen_name} to {self.reciever.profile.screen_name}: {self.content}"
    
class User:
    def __init__(self, username, password, screen_name, email):
        self.profile = Profile(username, password, screen_name, email)
        self.posts = []
        self.messages = []

    def create_post(self, content):
        if not content:
            raise ValueError("Post cannot be empty.")
        post = Post(self, content)
        self.posts.append(post)
        return post
    
    def send_message(self, reciever, content):
        if not reciever or not content:
            raise ValueError("Reciever and message content cannot be empty.")
        message = Message(self, reciever, content):
        self.messages.append(message)
        return message
    
    def __str__(self):
        return f"{self.profile.screen_name}'s Profile"