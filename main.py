from faker import Faker
import pandas as pd

NUM_DATA = 100

fake = Faker()
df = pd.DataFrame(
    {
        "id": [x for x in range(1, NUM_DATA + 1)],
        "username": [fake.name() for _ in range(NUM_DATA)],
        "address": [fake.address() for _ in range(NUM_DATA)],
    }
)

df.to_csv("fake_user.csv", index=False)
