def WAI_A_00001(file_name):
    import pandas as pd
    
    f_base_path = "C:/code" #파일 경로 설정
    file_path = f_base_path + '/'+ file_name
    
    if "csv" in file_name:
        df0 = pd.read_csv(file_path)
        df1 = df0.apply(pd.to_numeric, errors = 'coerce').fillna(0)
        df1.to_csv(f_base_path + '/after_'+ file_name)
        
    elif "parquet" in file_name:
        df0 = pd.read_parquet(file_path)
        df1 = df.apply(pd.to_numeric, errors = 'coerce').fillna(0)
        df1.to_parquet(f_base_path + '/after_'+ file_name)
        
    return df1

#전처리 전 데이터
def WAI_A_00001_befo(file_name):
    
    file_path = f_base_path + '/'+ file_name
    
    if "csv" in file_name:
        df0 = pd.read_csv(file_path)
        df1 = df0.apply(pd.to_numeric, errors = 'coerce').fillna(0)
        df1.to_csv(f_base_path + '/after_'+ file_name)
        
    elif "parquet" in file_name:
        df0 = pd.read_parquet(file_path)
        df1 = df.apply(pd.to_numeric, errors = 'coerce').fillna(0)
        df1.to_parquet(f_base_path + '/after_'+ file_name)
        
    return df0

#CPU정보 구하기
def CPU_check():
    import psutil
    print(psutil.cpu_percent())
    print(psutil.cpu_times_percent())
    cpu = psutil.cpu_times_percent()
    print(psutil.cpu_freq() , ' : CPU 속도')
    print(psutil.cpu_count(), ' : 논리 프로세서 수') 
    print(psutil.cpu_count(logical=False), ' : 물리적인 코어 수') 

#메모리 정보 구하기
def memory_check():
    import psutil
    print(psutil.virtual_memory())
    mem = psutil.virtual_memory()
    print(mem.total/1024**3 , ' : 물리 메모리 크기')
    total = mem.total/1024**3
    avail = mem.available
    print(avail, ' : 사용 가능한 물리 메모리 크기')
    print(avail/1024**3)

#대용량 데이터
def Large_capacity_data(filename):
    import pandas as pd
    
    f_base_path = "C:/code" #파일 경로 설정
    file_path = f_base_path + '/'+ file_name
    
    if "csv" in file_name:
        csv_chunk = pd.read_csv(file_path, chunksize=100000)
        for chunk in csv_chunk :
            print(chunk.apply(pd.to_numeric, errors = 'coerce').fillna(0))
        
    elif "parquet" in file_name:
        parquet_chunk = pd.read_parquet(file_path, chunksize=100000)
        for chunk in csv_chunk :
            print(chunk.apply(pd.to_numeric, errors = 'coerce').fillna(0))