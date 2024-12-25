import re

# Hàm kiểm tra biểu thức logic có hợp lệ hay không
def kiem_tra_bieu_thuc_hop_le(bieu_thuc):
    ky_tu_hop_le = re.compile(r'^[a-zA-Z0-9&|!->() ]+$')
    if not ky_tu_hop_le.match(bieu_thuc):
        return False

    can_bang = 0
    for ky_tu in bieu_thuc:
        if ky_tu == '(':
            can_bang += 1
        elif ky_tu == ')':
            can_bang -= 1
        if can_bang < 0:
            return False
    return can_bang == 0

# Hàm tính giá trị biểu thức logic
def tinh_gia_tri_bieu_thuc(bieu_thuc, gia_tri):
    # Thay thế các biến trong biểu thức bằng giá trị tương ứng trong từ điển gia_tri
    for bien, gia_tri_bien in gia_tri.items():
        bieu_thuc = bieu_thuc.replace(bien, str(gia_tri_bien))

    # Thay các toán tử logic thành các từ khóa Python
    bieu_thuc = bieu_thuc.replace('&', ' and ')
    bieu_thuc = bieu_thuc.replace('|', ' or ')
    bieu_thuc = bieu_thuc.replace('!', ' not ')
    
    # Sửa lại biểu thức "->" thành "not (A & B) or !C" (kéo theo đúng)
    bieu_thuc = bieu_thuc.replace('->', ' not or ')  # A -> B => not A or B

    try:
        return eval(bieu_thuc)  # Tính toán biểu thức đã thay thế
    except Exception as e:
        print(f"Có lỗi trong việc tính toán: {e}")
        return None

# Hàm chuyển đổi chuỗi nhập thành từ điển
def chuyen_doi_dau_vao(dau_vao):
    gia_tri = {}
    # Chuyển dấu phẩy thành dấu cách để tách các cặp
    dau_vao = dau_vao.replace(",", " ")
    # Tạo từ điển từ các cặp khóa-giá trị
    for item in dau_vao.split():
        key, value = item.split('=')
        gia_tri[key.strip()] = value.strip() == "True"
    return gia_tri

# Hàm chính để lấy đầu vào, kiểm tra và tính toán
def main():
    bieu_thuc = input("Nhập biểu thức logic (sử dụng &, |, !, ->): ")
    gia_tri_dau_vao = input("Nhập danh sách giá trị cho các biến (ví dụ: A=True B=False C=True): ")
    
    # Chuyển chuỗi đầu vào thành từ điển
    try:
        gia_tri = chuyen_doi_dau_vao(gia_tri_dau_vao)
    except:
        print("Lỗi trong việc nhập giá trị cho các biến. Hãy kiểm tra định dạng.")
        return

    if not kiem_tra_bieu_thuc_hop_le(bieu_thuc):
        print("Biểu thức không hợp lệ. Vui lòng kiểm tra lại.")
        return
    
    ket_qua = tinh_gia_tri_bieu_thuc(bieu_thuc, gia_tri)
    if ket_qua is None:
        print("Không thể tính giá trị của biểu thức. Có lỗi trong quá trình xử lý.")
    else:
        print(f"Giá trị của biểu thức là: {ket_qua}")

# Chạy chương trình
if __name__ == "__main__":
    main()
