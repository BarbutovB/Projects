def main():
    votes = {}
    print("--- Digital Poll System ---")
    print("Enter candidate names to vote. Type 'results' to see the winner.")

    while True:
        choice = input("Vote for: ").strip().title()

        if choice.lower() == "results":
            break

        if choice not in votes:
            votes[choice] = 0
        votes[choice] += 1
        print(f"Vote for {choice} recorded!")

    if not votes:
        print("No votes were cast.")
        return

    total_votes = sum(votes.values())
    print("\n--- Final Results ---")

    sorted_results = sorted(votes.items(), key=lambda x: x[1], reverse=True)

    for candidate, count in sorted_results:
        percentage = (count / total_votes) * 100
        print(f"{candidate}: {count} votes ({percentage:.1f}%)")


if __name__ == "__main__":
    main()