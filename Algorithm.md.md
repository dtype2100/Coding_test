# Algorithm

상태: Python

# 자료구조

## 정렬

[Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)

### 선택 정렬(Selection Sort)

1. 가장 먼저 정렬할 수 있는 값부터 정렬
    1. ex) 가장 작은 값부터 찾아서 정렬
2. 각 위치에 어떤 값이 들어갈지 찾음

### 삽입정렬(Insertion Sort)

1. 각 값이 어떤 위치에 들어갈지 찾음
2. 각 값을 정렬할 위치에 삽입
3. ex) 1, 3, 4, 5 의 값이 있을 때, 3을 옆으로 밀고 2를 삽입.  

# 알고리즘

## 선형탐색과 이진탐색

### 선형탐색

1. 처음부터 끝까지 하나씩 탐색하며 목표값을 찾는 알고리즘
2. 정렬된 리스트에서 좋음
3. ex) 목표가 50, 리스트 길이 100인 경우, 1부터 50까지 하나씩 탐색
    1. 50번의 탐색으로 50을 찾을 수 있음

### 이진탐색

1. 자료를 반씩 나누어 탐색하는 알고리즘
2. 정렬되지 않은 리스트에서 좋음
3. ex) 목표가 50, 리스트 길이 100인 경우, 100을 반으로 나누어 탐색
    1. 한 번의 탐색으로 50을 찾을 수 있음

## 그리디 알고리즘(Greedy Algorithm)

1. 장점: 간단하고 빠름
2. 단점: 최적의 답이 보장되지 않음
3. Greedy Algorithm이 최적의 답을 보장해 주는 문제
    1. 최적부분구조(Optimal Substructure)
        1. 부분 문제들의 최적의 답을 이용하여 기존 문제의 최적의 답을 구할 수 있음
        2. ex) 2000원을 거슬러 준다고 할 때, 10원, 50원, 100원, 500원 등의 동전으로 잔돈을 거슬러 줄 수 있음. 이때 다양한 경우의 수가 등장하는데, 각 사례를 비교하여 최적의 답을 도출하는 것이 최적부분구조.
    2. 탐욕적 선택속성(Greedy Choice Property)
        1. 각 단계에서의 탐욕스런 선택이 최종 답을 구하기 위한 최적의 선택
        2. ex) 매 순간 가장 큰 동전을 거슬러줄 수 있다면, 탐욕적 선택속성이 있음
    3. 최적부분구조와 탐욕적 선택소성이 있다면, Greedy Algorithm이 최적의 솔루션을 보장