capacity = 100                 #리스트 용량
array = [None]*capacity        #리스트 100개를 초기화
size = 0                       #리스트 항목의 개수를 0으로 초기화

def isEmpty():                 #isEmpty = 비어있는것
    if size == 0 : return True #size가 0이면 공백이므로 True 반환
    else : return False        #size가 0아니면 False 반환

def isFull():                  #isFull = 가득찼을때
    return size == capacity    #size가 리스트 용량과 같은 100일때 포화상태 / 비교연산 size == capacity 바로변환

def getEntry(pos) :            #getEntry = 재입력
    if 0 <= pos < size :       #pos가 유효한위치(0~size-1)까지면
        return array[pos]      #array 반환
    else : return None         #pos가 유효한위치가 아니면 None 반환

def insert(pos, e ) :          #insert = 배열 삽입
    global size                #전역변수
    if not isFull() and 0 <= pos <= size :   #리스트용량이 가득찬상태가 아니고 pos가 유효한위치라면
        for i in range(size, pos,-1) :       #리스트 내부의 pos+1부터 size-1까지의 모든 항목을 한 칸씩 뒤로 옮김
            array[i] = array[i-1]            #(2면 1, 3은 2)
        array[pos] = e                       #리스트 내부의 이동이끝나면 pos에 e를 삽입함
        size += 1                            #배열의 수 size하나를 증가함
    else :
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()
