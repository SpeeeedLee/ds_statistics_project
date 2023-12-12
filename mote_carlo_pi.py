import numpy as np
import matplotlib.pyplot as plt

# np.random.rand() 會生成一個介於0到1的隨機數
# random.uniform(0, 1) 也有一樣的效果

n_dots = 1000
n_circle = 0
    

# 啟用交互模式
plt.ion()

'''

這樣之後每個點才能畫在同一個figure上，並且可以用pause
可是細節還要再查一下，不太懂

'''

# 創建一個圖形
fig, ax = plt.subplots()

# 繪製正方形
square = plt.Rectangle((-1, -1), 2, 2, color='green', fill=False)
ax.add_patch(square)

# 繪製圓形
theta = np.linspace(0, 2 * np.pi, 1000)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

ax.plot(x_circle, y_circle, color='red')

# 設置坐標軸範圍
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# 設置坐標軸標籤
ax.set_xlabel('X')
ax.set_ylabel('Y')

# x y 軸等比例
ax.axis('equal')

plt.show()

'''
fig, ax = plt.subplots() 中的 fig 用來管理 figure級別對象，ax用來管理座標軸級別對象
fig.add 可能是拿來用來興曾其他子圖
ax.add、ax.add_patch、axix_set_xlim ... 則是用來


'''

#################
#### 執行實驗 ####
for i in range (n_dots):
    x = 2 * np.random.rand() - 1
    y = 2 * np.random.rand() - 1

    if x**2 + y**2 <= 1:
        n_circle += 1
        ax.plot(x, y, marker='o', markersize=1.2, color='orange')

    else:
        ax.plot(x, y, marker='o', markersize=1.2, color='blue')

    simulated_pi = 4 * (n_circle / (i + 1))     
    # 添加文本到右上角
    x_text, y_text = 0.9, 1.1  # 调整文本的位置
    printed_text = ax.text(x_text, y_text, f"simulated pi : {simulated_pi:.4f}", ha='right', va='top')
    plt.pause(0.01)
    printed_text.remove()


final_simulated_pi = 4 * (n_circle / n_dots) 

ax.text(x_text, y_text, f"simulated pi : {simulated_pi:.4f}", ha='right', va='top')


# 關閉交互模式
plt.ioff()

plt.show()



print(f"value of pi via simulation is {final_simulated_pi}")
print(f"real value of pi {np.pi}")