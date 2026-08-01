import boto3
import pandas as pd
from sklearn.cluster import KMeans
import joblib

# Load data from S3
s3 = boto3.client('s3')
bucket = 'handybot-ml-data'
file_key = 'player_stats.csv'
obj = s3.get_object(Bucket=bucket, Key=file_key)
df = pd.read_csv(obj['Body'])

# Features for clustering
features = df[['VPIP', 'PFR', 'ThreeBet', 'FoldToCbet']].fillna(0)

# Cluster players into 3 styles: Tight, Loose, Aggressive
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(features)

# Save model to S3 for inference Lambda
joblib.dump(kmeans, '/opt/ml/model/kmeans_model.joblib')
# Upload back to S3 if needed
