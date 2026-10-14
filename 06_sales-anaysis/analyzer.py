import os

# Check if we are in the right place
print(f"Current directory:", os.getcwd())


# Check if our data file exist
data_path = "data/sales.csv"

if os.path.exists(data_path):
    print(f"✅Found: {data_path}")

else:
    print(f"❌ Can not find: {data_path}")
    print(f"Make sure your running from the slaes analysis folder")