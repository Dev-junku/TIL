# 카운팅 정렬
# 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능: 각 항목의 발생 회수를 기록하기 위해
# 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문.

# 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아함.

# 시간 복잡도는 O(n+k): n은 리스트의 길이, k는 정수의 최대값

def Counting_Sort(A, B, k):
    # A는 입력 배열
    # B는 정렬된 배열
    # C는 카운트 배열

    C = [0] * k + 1

    for i in range(0, len(B)):
        C[A[i]] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

# 원소의 개수가 얼마 없으나, 둘 원소 사이의 거리가 긴 경우
# 매우 큰 시간, 공간에 대한 소비가 일어날 수 있음.
# 따라서 원소간의 거리를 잘 비교해야함.