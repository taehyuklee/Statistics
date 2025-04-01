import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 모집단 크기 & 샘플 크기
N = 1000000  
sample_size = 1000  

# 다양한 랜덤 분포 생성
distributions = {
    "Uniform (0, 1)": np.random.uniform(0, 1, N),  # 균등 분포
    "Random Normal Mix": np.concatenate([np.random.normal(-5, 1, N//2), np.random.normal(5, 2, N//2)]),  # 정규분포 혼합
    "Exponential (λ=1)": np.random.exponential(scale=1, size=N),  # 지수 분포
    "Custom Random Data": np.random.choice(np.linspace(-10, 10, 500), size=N, replace=True),  # 완전 랜덤한 데이터셋
    "Poisson (λ=10)": np.random.poisson(lam=10, size=N),
    "Chi-Square (df=4)": np.random.chisquare(df=4, size=N),
    "Gamma (α=2, β=2)": np.random.gamma(shape=2, scale=2, size=N),
    "Beta (α=2, β=5)": np.random.beta(a=2, b=5, size=N)
}

# 그래프 설정
fig, axes = plt.subplots(8, 2, figsize=(12, 16))  

for i, (dist_name, population) in enumerate(distributions.items()):
    # 1000개 랜덤 샘플링
    sample = np.random.choice(population, size=sample_size, replace=False)  

    # (좌) 모집단 히스토그램 & KDE
    sns.histplot(population, bins=50, kde=True, stat="density", color="blue", alpha=0.5, ax=axes[i, 0])
    axes[i, 0].set_title(f"Population: {dist_name} (N={N})")

    # (우) 샘플 히스토그램 & KDE
    sns.histplot(sample, bins=50, kde=True, stat="density", color="red", alpha=0.5, ax=axes[i, 1])
    axes[i, 1].set_title(f"Sample: {dist_name} (n={sample_size})")

plt.tight_layout()
plt.show()
