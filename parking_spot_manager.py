"""
무료주차장의 데이터를 분석하고 관리하기 위한 클래스와 함수를 제공하는 모듈
parking_spot class를 이용하여 한 주차장에 관한 정보를 다루게됩니다.
str_list_to_class_list, print_spots함수로
각각 string데이터들을 파싱하여 class리스트를 만들어 반환하며,
    class목록을 입력받아 출력합니다.
"""
class parking_spot:
    """
    무료주차장에 관한 정보를 다루는 클래스입니다.
    parking_spot클래스는 name, city,... 등 주차장 한 곳의 정보를 저장하고 있습니다.
    외부에서 접근 불가능한 __item 변수가 있으며
    생성자를 통해 값을 입력하고, 접근하기 위해 get메소드를 사용합니다.
    """
    __item = {}
    def __init__(self,name,city,district,ptype,longitude,latitude):
        """
        생성자에서 __item에 저장할 주차장 정보를 받습니다.
        Args:
            name(string):       자원명 (주차장 이름)
            city(string):       시도 (도시명)
            district(string):   시군구 (도시의 구역)
            ptype(string):      주차장 유형
            longitude(float):  경도
            latitude(float):   위도
        """
        self.__item = {'name':name,'city':city,'district':district,'ptype':ptype,'longitude':longitude,'latitude':latitude}


    def __str__(self):
        """
        출력을 위해 형식을 지정한 특수메소드
        """
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self,keyword='name'):
        """
        주차장 정보의 keyword에 맞는 값을 반환합니다.
        Args:
            keyword(string) : 찾을 정보의 키워드
        Returns:
            item[keyword](string or float) : 저장하고 있는 선의 길이입니다.( 기본인수 'name')
        Examples:
            >>> obj.get('name') # obj의 name키의 값을 가져옴
        """
        return self.__item[keyword]


def str_list_to_class_list(str_list):
    """
    문자열리스트를 매개변수[str_list]로 받아 parking_spot 클래스 객체의 리스트로 변환 후 반환한다
     Args:
        str_list(string으로 이루어진 list) : 객체로 생성할 데이터리스트(문자열)
    Returns:
        class_list(parking_spot Class list) : 객체로 생성된 주차장데이터
    Examples:
        >>> spots = str_list_to_class_list(str_list) 
    """
    class_list = []
    for strLine in str_list:
        makeClassStr = strLine.split(',')
        spotClass = parking_spot(makeClassStr[1],makeClassStr[2],makeClassStr[3],makeClassStr[4],float(makeClassStr[5]),float(makeClassStr[6]))
        class_list.append(spotClass)
    return class_list

    

def print_spots(spots):
    """
    parking_spot 클래스 객체의 리스트[spots]를 매개변수로 받아, 객체 개수를 출력 후 모든 객체의 값을 출력한다.
    Args:
        spots(parking_spot Class list) : 출력할 주차장데이터 객체
    Returns:
        없음
    Examples:
        >>> print_spots(spots)
    """
    print(f"---print elements({len(spots)})---")
    for oneClass in spots:
        print(oneClass)

def filter_by_name(spots, name):
    """
    parking_spot 클래스 객체리스트[spots]와 이름[name]을 매개변수로 받아,
    name 매개변수의 내용이 이름영역의 값에 포함된 객체만 필터링하여 반환
    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        name(string)  :                             필터링 조건이 될 글자
    Returns:
        filtered_spots ((parking_spot Class list)) : 필터링된 주차장데이터 객체
    Examples:
        >>> spots = filter_by_name(spots, "대학교")
    """    
    filtered_spots = [spot for spot in spots if spot.get('name').find(name) != -1]
    return filtered_spots

def filter_by_city(spots, city):
    """
    parking_spot 클래스 객체리스트[spots]와 시도[city]을 매개변수로 받아,
    city 매개변수의 내용이 시도영역의 값에 포함된 객체만 필터링하여 반환
    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        city(string)  :                             필터링 조건이 될 글자
    Returns:
        filtered_spots ((parking_spot Class list)) : 필터링된 주차장데이터 객체
    Examples:
        >>> spots = filter_by_city(spots, "인천")
    """    
    filtered_spots = [spot for spot in spots if spot.get('city').find(city) != -1]
    return filtered_spots

def filter_by_district(spots, district):
    """
    parking_spot 클래스 객체리스트[spots]와 시군구[district]을 매개변수로 받아,
    district 매개변수가 시군구영역의 값에 포함된 객체만 필터링하여 반환
    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        district(string)  :                         필터링 조건이 될 글자
    Returns:
        filtered_spots ((parking_spot Class list)) : 필터링된 주차장데이터 객체
    Examples:
        >>> spots = filter_by_city(spots, "동작")
    """    
    filtered_spots = [spot for spot in spots if spot.get('district').find(district) != -1]
    return filtered_spots

def filter_by_ptype(spots, ptype):
    """
    parking_spot 클래스 객체리스트[spots]와 주차장유형[ptype]을 매개변수로 받아,
    ptype 매개변수가 주차장유형 영역의 값에 포함된 객체만 필터링하여 반환
    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        ptype(string)  :                         필터링 조건이 될 글자
    Returns:
        filtered_spots ((parking_spot Class list)) : 필터링된 주차장데이터 객체
    Examples:
        >>> spots = filter_by_city(spots, "동작")
    """    
    filtered_spots = [spot for spot in spots if spot.get('ptype').find(ptype) != -1]
    return filtered_spots

def filter_by_location(spots, locations):
    """
    parking_spot 클래스 객체리스트[spots]와 위치[locations] 튜플을 매개변수로 받아,
    위치 locations 매개변수 조건에 적합한 객체만 필터링하여 반환
    
    locations에는 (최소위도, 최대위도, 최소경도,최대경도)가 포함되어있으며
    최소위도 < 객체의 위도 < 최대위도
    최소경도 < 객체의 경도 < 최대경도 조건에 부합하는 객체만 필터링하여 반환됨.

    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        location(float tuple)  :                    필터링 조건이 될 float 튜플
    Returns:
        filtered_spots ((parking_spot Class list)) : 필터링된 주차장데이터 객체
    Examples:
        >>> spots = filter_by_city(spots, (35.5, 36.5, 127.5, 128.5))
    """ 
    #파라미터로 넘어온 튜플을 다시 꺼냄
    min_lat = locations[0]
    max_lat = locations[1]
    min_long = locations[2]
    max_long = locations[3]

    filtered_spots = [spot for spot in spots \
                      if ((min_lat < spot.get('latitude')) and (spot.get('latitude') < max_lat)) and \
                        ((min_long < spot.get('longitude')) and (spot.get('latitude') < max_long))]
    return filtered_spots

def sort_by_keyword(spots, keyword):
    """
    parking_spot 클래스 객체리스트[spots]와 keyword 문자열을 매개변수로 받아,
    keyword를 기준으로 정렬을 수행 후 반환
    
    Args:
        spots(parking_spot Class list) :            주차장데이터 객체
        keyword(string)  :                          정렬기준이 될 문자열
    Returns:
        spots ((parking_spot Class list)) : w정렬된 주차장데이터 객체
    Examples:
        >>> spots = sort_by_keyword(spots,keyword)
    """ 
    #참조 링크 : https://cigiko.cafe24.com/python-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-sort%EC%99%80-sorted/
    #spots의 객체 하나 spot을 람다함수에 입력받아 spot.get(keyword)를 호출하고,
    #키워드에 맞는 값을 기준으로 sort
    spots = sorted(spots, key=lambda spot: spot.get(keyword))
    return spots

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)