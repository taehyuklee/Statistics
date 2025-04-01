import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 모집단 생성 (정규 분포)
N = 100000
population = np.random.normal(loc=50, scale=15, size=N)  # 평균 50, 표준편차 15의 정규 분포

# 표본 크기 설정
sample_sizes = [30, 50, 1000, 2000]  # 작은 샘플과 큰 샘플 비교
colors = ["blue", "red", "green", "orange"]

# 실제 모집단 CDF
x = np.sort(population)
true_cdf = np.arange(1, N + 1) / N  # 실제 CDF

plt.figure(figsize=(10, 6))

# 모집단의 실제 CDF 그리기
plt.plot(x, true_cdf, label="True CDF (Population)", color="black", linewidth=2)

# 서로 다른 표본 크기에서 경험적 CDF 비교
for size, color in zip(sample_sizes, colors):
    sample = np.random.choice(population, size=size, replace=False)
    ecdf = sm.distributions.ECDF(sample)
    plt.step(np.sort(sample), ecdf(np.sort(sample)), label=f"Empirical CDF (n={size})", color=color, linestyle="--")

plt.xlabel("Value")
plt.ylabel("CDF")
plt.legend()
plt.title("Glivenko-Cantelli Theorem: ECDF vs True CDF (Normal Distribution)")
plt.show()
