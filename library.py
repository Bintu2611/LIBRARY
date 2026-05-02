import asyncio
from typing import Dict, List


# Collection of library items
library_items: Dict[int, Dict[str, object]] = {
    301: {
        "id": 301,
        "title": "Intro to Programming",
        "author": "James Carter",
        "category": "Computing",
        "available": True
    },
    302: {
        "id": 302,
        "title": "Data Communication Basics",
        "author": "Linda Green",
        "category": "Networking",
        "available": True
    }
}


# Library users
users_db: Dict[int, Dict[str, object]] = {}

# System logs
activity_log: List[Dict[str, object]] = []


# Add new user
async def add_user(user_id: int, name: str, email: str, membership: str) -> str:
    print(f"Adding user: {name}")

    await asyncio.sleep(4)

    users_db[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "membership": membership
    }

    activity_log.append({
        "event": "user_added",
        "user_id": user_id
    })

    return f"User {name} added successfully (ID: {user_id})"


# Retrieve all users
async def get_users() -> List[Dict[str, object]]:
    print("Retrieving user list...")

    await asyncio.sleep(2)

    return list(users_db.values())


# Update library item
async def update_item(item_id: int, title: str = None, author: str = None) -> str:
    print(f"Updating item ID {item_id}...")

    await asyncio.sleep(3)

    item = library_items.get(item_id)

    if not item:
        return "Item does not exist"

    if title:
        item["title"] = title

    if author:
        item["author"] = author

    activity_log.append({
        "event": "item_updated",
        "item_id": item_id
    })

    return f"Item {item_id} updated"


# Get activity logs
async def get_logs() -> List[Dict[str, object]]:
    print("Accessing system logs...")

    await asyncio.sleep(2)

    return activity_log


# Main execution
async def run_system() -> None:
    print("Starting Task A: Add User")
    print("Starting Task B: Update Item")
    print("Starting Task C: View Logs")

    results = await asyncio.gather(
        add_user(10, "Alice Smith", "alice@mail.com", "premium"),
        update_item(301, title="Programming Basics"),
        get_logs()
    )

    print("\n=== OPERATIONS FINISHED ===")

    print("\n=== OUTPUT ===")
    for res in results:
        print(res)


asyncio.run(run_system())
