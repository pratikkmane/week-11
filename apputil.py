"""
Unsupervised Learning Exercises - Week 11

Implements k-means clustering and time complexity analysis.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from time import time


# Load diamonds dataset and extract numerical columns (Exercise 2)
diamonds = sns.load_dataset('diamonds')
diamonds_numeric = diamonds.select_dtypes(include=[np.number])

# Global variable for bonus exercise
step_count = 0


def kmeans(X, k):
    """
    Perform k-means clustering on numerical data.
    
    Args:
        X: NumPy array of shape (n_samples, n_features)
        k: Number of clusters
        
    Returns:
        Tuple (centroids, labels) where:
            - centroids: 2D array of shape (k, n_features)
            - labels: 1D array of shape (n_samples,)
    """
    # Create and fit k-means model
    kmeans_model = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_model.fit(X)
    
    # Extract centroids and labels
    centroids = kmeans_model.cluster_centers_
    labels = kmeans_model.labels_
    
    return (centroids, labels)


def kmeans_diamonds(n, k):
    """
    Run k-means clustering on first n rows of diamonds dataset.
    
    Args:
        n: Number of rows to use from diamonds dataset
        k: Number of clusters
        
    Returns:
        Tuple (centroids, labels) from kmeans function
    """
    # Get first n rows of numerical diamond data
    X = diamonds_numeric.head(n).values
    
    # Run k-means clustering
    return kmeans(X, k)


def kmeans_timer(n, k, n_iter=5):
    """
    Measure average runtime of kmeans_diamonds function.
    
    Args:
        n: Number of rows to use from diamonds dataset
        k: Number of clusters
        n_iter: Number of iterations to run (default: 5)
        
    Returns:
        Average runtime in seconds across n_iter runs
    """
    times = []
    
    for _ in range(n_iter):
        start = time()
        _ = kmeans_diamonds(n, k)
        runtime = time() - start
        times.append(runtime)
    
    # Return average time
    return np.mean(times)


# Bonus Exercise: Binary Search with Step Counting
def bin_search_counted(n):
    """
    Binary search with step counting for time complexity analysis.
    
    Args:
        n: Size of array to search
        
    Returns:
        Tuple (result_index, steps_taken)
    """
    global step_count
    step_count = 0
    
    arr = np.arange(n)
    left = 0
    right = n - 1
    x = n - 1  # Worst case: search for last element
    
    step_count += 1  # Array initialization
    
    while left <= right:
        step_count += 1  # Comparison in while condition
        
        middle = left + (right - left) // 2
        step_count += 1  # Middle calculation
        
        # Check if x is present at mid
        if arr[middle] == x:
            step_count += 1  # Comparison
            return middle, step_count
        
        step_count += 1  # First if comparison
        
        # If x greater, ignore left half
        if arr[middle] < x:
            step_count += 1  # Second if comparison
            left = middle + 1
            step_count += 1  # Assignment
        # If x is smaller, ignore right half
        else:
            right = middle - 1
            step_count += 1  # Assignment
    
    # If we reach here, element was not present
    return -1, step_count


def analyze_binary_search_complexity(max_n=10000, step=100):
    """
    Analyze time complexity of binary search algorithm.
    
    Args:
        max_n: Maximum array size to test
        step: Step size for n values
        
    Returns:
        DataFrame with columns: n, steps, log2_n
    """
    n_values = np.arange(10, max_n, step)
    steps_list = []
    
    for n in n_values:
        _, steps = bin_search_counted(n)
        steps_list.append(steps)
    
    # Create dataframe with results
    results = pd.DataFrame({
        'n': n_values,
        'steps': steps_list,
        'log2_n': np.log2(n_values)
    })
    
    return resultss