from google.cloud import pubsub_v1

# Define your project ID and topic ID
project_id = "myownproject241124"
topic_id = "myownproj-tp11"

# Create a publisher client
publisher = pubsub_v1.PublisherClient()

# Build the topic name
topic_path = publisher.topic_path(project_id, topic_id)

# Publish a message
message = "Hello, Pub/Sub this is from M V SIVAKUMAR!"

# The message data must be a bytestring
future = publisher.publish(topic_path, message.encode("utf-8"))

print(f"Message published. Message ID: {future.result()}")