# 재귀적인 패턴으로 별찍기
# N이 3의 거듭제곱(3,9,27..)이라고 할때, 크기 N의 패턴은 N*N 정사각형 모양
# 크기가 만약 3이면 가운데 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴
# '''
#     ***
#     * *
#     ***
# '''
# N이 3보다 크면, 크기 N의 패턴은 공백으로 채워진 가운데의 N/3*N*3 정사각형을
# 크기 n/3 패턴으로 둘러싼 형태 = n/3만큼 중앙에 공백이 있음
# N은 3의 거듭제곱 3**(1~8)

# 별찍기는 약한 부분이기에 저항없이 블로그들을 찾아보았다.
# 그마저도 이해가 안가는 부분이 많아 여러개를 참고하였다.

# 설명
# 규칙을 찾아보면
# '''
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***   ***         ***   ***
# * *   * *         * *   * *
# ***   ***         ***   ***
# *********         *********
# * ** ** *         * ** ** *
# *********         *********
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************
# ***   ******   ******   ***
# * *   * ** *   * ** *   * *
# ***   ******   ******   ***
# ***************************
# * ** ** ** ** ** ** ** ** *
# ***************************'''
# 이 별들을 표로 만들어 x,y로 나눠본다면
# x,y가 3,4,5일때는 뻥 둘려있고, 1,4,7일때는 비워져잇었다.
# 1,4,7 -> 3으로 나눈 나머지가 1, 3,4,5-> 3으로 나눈 몫이 1

# 다른 풀이로는 https://imgzon.tistory.com/37
# 1. 크기가 N이라면 그 전단계인 N/3인 정사각형을 이용하여 배열하게됨
# 2. 따라서 크기를 나타내는 int값 한개, 전 단계의 배열을 지닌 list 한개, 
# 이렇게 두개의 피라미터를 받는 재귀함수 제작
def star(n: int, x:list)->list:
    out = []    # 이미 한번 처리한값
    if n==3:
        return x
    else:
        for i in x: # 위에 처음 3개의 구역
            out.append(i*3)
        for i in x: # 가운데 3개의 구역 (중앙 비어있음)
            out.append(i+' '*len(x)+i)
        for i in x: # 마지막 3개의 구역
            out.append(i*3)
        return star(n//3,out)

n = int(input())
first = ['***','* *','***']
final = star(n,first)
for i in final:
    print(i)

# 전체적으로 이해하는데 조금 힘들었다.
# 별 찍을때 n//3까지만 재귀를 돈다 n//3을 n으로 넘겨주며 3이면 종료한다.
# 그니까 27은 3^3제곱이라 3번 반복할거를 -1해서 2번만 돈다.
# *** * * *** 이거로 출발하여 for문 세개씩 3*3 :9-> 9*3:27줄이 되게한다.
# 이전의 배열을 사용하여 한줄씩 3의 배수로 곱하여 덮어씌운다.
# 두번째 for문에서 i*3개 곱할거를 i두개 중앙에 i개수만큼 띄워쓰기를 넣어 중앙 큰부분을 만들었다.
# 한칸씩 나눠본다면 x,y좌표가 같은 숫자부터 같은 개수로 구멍이 생기고 같은 위치에 별이 찍힌다.
# 디버깅으로 한줄씩 돌려보고 난 분석
