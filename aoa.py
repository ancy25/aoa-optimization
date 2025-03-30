import streamlit as st
import numpy as np

# Define the Archimedes Optimization Algorithm (AOA)
def aoa(obj_function, num_agents=30, max_iter=100, dim=2, lower_bound=-10, upper_bound=10):
    positions = np.random.uniform(lower_bound, upper_bound, (num_agents, dim))
    best_solution = None
    best_fitness = float("inf")
    
    for iteration in range(max_iter):
        for i in range(num_agents):
            fitness = obj_function(positions[i])
            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = positions[i].copy()
        
        for i in range(num_agents):
            r = np.random.uniform(0, 1)
            positions[i] += r * (best_solution - positions[i])
            positions[i] = np.clip(positions[i], lower_bound, upper_bound)
    
    return best_solution, best_fitness

# Example objective function: Sphere Function
def sphere_function(x):
    return np.sum(x**2)

# Streamlit UI
st.title("⚙️ Archimedes Optimization Algorithm")

st.sidebar.header("Algorithm Settings")
num_agents = st.sidebar.slider("Number of Agents", 5, 50, 30)
max_iter = st.sidebar.slider("Max Iterations", 10, 500, 100)
dim = st.sidebar.slider("Number of Dimensions", 1, 10, 2)
lower_bound = st.sidebar.number_input("Lower Bound", -100, 0, -10)
upper_bound = st.sidebar.number_input("Upper Bound", 0, 100, 10)

if st.button("Run AOA"):
    best_solution, best_fitness = aoa(sphere_function, num_agents, max_iter, dim, lower_bound, upper_bound)
    st.success(f"Best Solution: {best_solution}")
    st.success(f"Best Fitness: {best_fitness}")
