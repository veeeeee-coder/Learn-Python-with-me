# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1

    def __init__(self, sender, content, receiver=None):
        self.id = Message.message_counter
        Message.message_counter += 1

        self.sender = sender
        self.content = content
        self.receiver = receiver  # None = public, else private

    def __str__(self):
        if self.receiver:
            return f"(DM {self.id}) {self.sender.username} → {self.receiver.username}: {self.content}"
        else:
            return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_room(self, room):
        if self.chatroom:
            print(f"{self.username} already in a room")
            return
        room.add_user(self)
        self.chatroom = room
        print(f"{self.username} joined {room.name}")

    def leave_room(self):
        if not self.chatroom:
            print(f"{self.username} not in any room")
            return
        self.chatroom.remove_user(self)
        print(f"{self.username} left {self.chatroom.name}")
        self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print("Join a room first!")
            return
        self.chatroom.broadcast(self, content)

    def send_private_message(self, other_user, content):
        msg = Message(self, content, other_user)
        print(msg)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        msg = Message(sender, content)
        self.messages.append(msg)
        print(msg)

    def show_history(self):
        print(f"\n--- {self.name} Chat History ---")
        for msg in self.messages:
            print(msg)


# -------------------------------
# ChatSystem (NEW 🔥)
# -------------------------------
class ChatSystem:
    def __init__(self):
        self.users = {}
        self.rooms = {}

    def create_user(self, username):
        user = User(username)
        self.users[username] = user
        return user

    def create_room(self, room_name):
        room = ChatRoom(room_name)
        self.rooms[room_name] = room
        return room

    def get_user(self, username):
        return self.users.get(username)

    def get_room(self, room_name):
        return self.rooms.get(room_name)
    



# create system
system = ChatSystem()

# create users
u1 = system.create_user("veee")
u2 = system.create_user("john")

# create rooms
r1 = system.create_room("General")
r2 = system.create_room("Tech")

# join rooms
u1.join_room(r1)
u2.join_room(r1)

# public messages
u1.send_message("Hello everyone")
u2.send_message("Hi!")

# private message
u1.send_private_message(u2, "This is private 👀")

# show history
r1.show_history()