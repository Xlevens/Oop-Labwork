from Modules.user import UserFront
from Modules.chat import MainChat
from Modules.Ronin import RoninChat
from Modules.Zubaidas import ZubaidaChat
from Modules.Khaadi import KhaadiChat

CB = MainChat("Umair")

print(CB.req())
res = input()
msg, b = CB.response(res)
print(msg)


while True:
        query = input("You: ")
        
        if query.lower() in ["exit", "quit", "bye"]:
            print("Chat ended. Goodbye!")
            break

        response = b.queryset(query.lower())
        print(response)

        if "goodbye" in response.lower() or "bye" in response.lower():
            print("Chat ended. Goodbye!")
            break
