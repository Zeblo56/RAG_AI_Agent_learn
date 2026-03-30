# 开发时间：2026/3/17  23:05
import numpy as np

#余弦相似度 = 两向量的点积/两向量模长的乘积

def get_dot(vec_a,vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError("2个向量维度数量不同")
    dot_sum = 0
    for a,b in zip(vec_a,vec_b):
        dot_sum += a*b
    return dot_sum

def get_norm(vec):
    sum_square = 0
    for v in vec:
        sum_square += v*v

    return np.sqrt(sum_square)

def cosine_similarity(vec_a,vec_b):
    result = get_dot(vec_a,vec_b) / (get_norm(vec_a)*get_norm(vec_b))
    return result
if __name__ == '__main__':
    vec_a = [1,2,3]
    vec_b = [4,5,6]
    vec_c = [1,2,4]
    vec_d = [5,6,7]
    print("ab:",cosine_similarity(vec_a,vec_b))
    print("ac:",cosine_similarity(vec_a,vec_c))
    print("bd:",cosine_similarity(vec_b,vec_d))