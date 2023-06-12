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
            name(string):       주차장 이름
            city(string):       도시명
            district(string):   도시의 구역
            ptype(string):      주차장 타입
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

    

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)