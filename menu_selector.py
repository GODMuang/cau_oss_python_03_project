"""
프로그램에서 사용자와 상호작용하기 위한 UI(User Interface)를 제공하는 모듈

start_process 함수만 존재하며,
 이를 이용하여 프로그램의 동작을 선택할 수 있습니다.
"""
import file_manager
import parking_spot_manager
def start_process(path):
    """
    프로그램의 동작을 선택하는 함수
    Args:
        path(string) : 분석할 데이터의 경로
    Returns:
        없음
    Examples:
        start_process("./input/free_parking_spot_seoul.csv") # 해당 경로의 데이터를 분석
    """
    spotsStr = file_manager.read_file(path) #파일을 읽어 스트링 받아오기
    spots = parking_spot_manager.str_list_to_class_list(spotsStr) #스트링으로 클래스 생성
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        # print
        if select == 1: 
            parking_spot_manager.print_spots(spots)

        # filter
        elif select == 2: 
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            #filter by name
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
            #filter by city
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
            #filter by district
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
            #filter by ptype
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
            #filter by location
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                location = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots,location)
            else:
                print("invalid input")
        
        #sort
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots,keyword)
            else: print("invalid input")

        #exit
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")