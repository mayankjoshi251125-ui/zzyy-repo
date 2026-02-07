from app.agent import create_github_agent

def main():
    agent = create_github_agent()

    print("🚀 GitHub Automation Agent (Groq Powered)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )

        print("\nAgent:", result["messages"][-1].content)
        print()


if __name__ == "__main__":
    main()






