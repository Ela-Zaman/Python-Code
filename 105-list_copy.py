text_messages=["Hello", "Good Morning", "Good Night", "Bye"]

def show_messages(text_messages):
    print("Bellow are the text_messages/n")
    for text_message in text_messages:
        print(f"This is one of the text messages: {text_message}\n")

show_messages(text_messages)

def send_messages(text_messages):
    
    sent_messages=[]
    
    for text_message in text_messages:
        sent_messages.append(text_message)
        print(f"Text Message: {text_message}")
        
    
    text_messages=[]
    print(f"This is text_messages: {text_messages}")
    print(f"This is sent_messages: {sent_messages}")

    return text_messages

    
messages = ["Hello", "Hi", "Bye", "Good Morning"]
messages_2= [1,2,3,4]

list1=send_messages(messages[:])
list2=send_messages(messages_2)

print("Original list",list1,"\n")
print("Empty list",list2,"\n")
