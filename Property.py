class Property:
    def __init__(self, ID=0, color="none", value=0, name="No name"):
        self.id = ID # mã định danh duy nhát của tài sản
        self.color = color
        self.value = value
        self.name = name
        self.owned_flag = False # cờ đánh dấu tài sản đã đc mua
        self.owner = None #người sở hữu tài sản


#So sánh 2 tài sản có giống nhau ko( so sánh thuộc tính thay vì địa chỉ bộ nhớ) vd:khi bán tài sản cần xác định tài sản ( dựa trên thuộc tính) có trong danh sách ko để xóa nó
    def __eq__(self, other):
        if isinstance(other, Property):
            return (self.id == other.id and self.color == other.color and
                    self.value == other.value and self.name == other.name)
        return False

#trả về tên và giá trị tài sản
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

