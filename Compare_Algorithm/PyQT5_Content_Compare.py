from decimal import Decimal, ROUND_DOWN
class Content_Compare():
    def __init__(self):
        print('Content Compare')
        # self.content_Brute()
    def calculator_Drops(self,drops):
        data_Clean = []
        seen_coordinates = set()

        for item in drops:
            volume, weight, latitude, longitude = item
            coordinates = (latitude, longitude)
            
            if coordinates not in seen_coordinates:
                data_Clean.append(item)
                seen_coordinates.add(coordinates)
        return data_Clean
    def content_Brute(self,distance,data_weight):
        distance_Brute=distance[0]
        text_Brute = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Brute += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Brute[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Brute
    
    def content_Branch(self,distance,data_weight):
        distance_Brute=distance[1]
        text_Branch = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Branch += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Brute[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Branch
    def content_Greedy(self,distance,data_weight):
        distance_Greedy=distance[2]
        text_Greedy = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Greedy += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Greedy[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Greedy
    def content_Hill(self,distance,data_weight):
        distance_Hill=distance[3]
        text_Hill = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Hill += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Hill[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Hill
    def content_Lin(self,distance,data_weight):
        distance_Lin=distance[4]
        text_Lin = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Lin += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Lin[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Lin
    def content_Nearest(self,distance,data_weight):
        distance_Nearest=distance[5]
        text_Nearest = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Nearest += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Nearest[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Nearest
    def content_OPT(self,distance,data_weight):
        distance_OPT=distance[6]
        text_OPT = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_OPT += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_OPT[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_OPT
    def content_Random(self,distance,data_weight):
        distance_Random=distance[7]
        text_Random = ""
        for index, value in enumerate(data_weight):
            sum_kg = 0
            sum_m3=0
            for item in value:
                volume = item[0]
                weight=item[1]
                sum_kg += volume
                sum_m3 += weight
            text_Random += f"""
            <div class=\"sub-event-date\">Trip {index+1}:</div> 
            <div class=\"sub-event-description\">
            KM:{distance_Random[index]} - KG:{sum_kg.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} 
            - M3:{sum_m3.quantize(Decimal("1.000"), rounding=ROUND_DOWN)} - 
            Drops:{len(self.calculator_Drops(value))} - Orders:{len(value)} 
            </div>
            """
        return text_Random