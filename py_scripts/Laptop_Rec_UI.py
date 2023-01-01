'''
Overview: User-input interface for laptops they should be recommended.

Details:
-User is given an initial prompt (a greeting + a brief introduction)
-User wants a laptop that bests suits their needs.
-Each prompt would slowly break down various questions regarding different computer specifications (e.g. memory, screen size).
-There would be no more than 5-10 questions.
-Program offers a list of suggestions from database based on user specs.

Implementation Details:
-Create functions for different categories of laptop specs
-Establish global variables that could act as flags based on user input
-Use nested conditional statements under an if-else statement that divides the program between new and experienced computer users (i.e. if? new#1: else? exp#2).
-Keep track of how many people used this program via a counter system in the greeting code.

Tổng quan: Giao diện người dùng nhập liệu cho máy tính xách tay nên được khuyến nghị.

Chi tiết:
-Người dùng được nhắc nhở ban đầu (lời chào + giới thiệu ngắn gọn)
-Người dùng muốn một chiếc máy tính xách tay phù hợp nhất với nhu cầu của họ.
-Mỗi lời nhắc sẽ từ từ chia nhỏ các câu hỏi khác nhau liên quan đến các thông số kỹ thuật khác nhau của máy tính (ví dụ: bộ nhớ, kích thước màn hình).
-Sẽ không có nhiều hơn 5-10 câu hỏi.
-Chương trình đưa ra danh sách gợi ý từ cơ sở dữ liệu dựa trên thông số kỹ thuật của người dùng.

Chi tiết triển khai:
-Tạo các chức năng cho các loại thông số kỹ thuật máy tính xách tay khác nhau
-Thiết lập các biến toàn cục có thể đóng vai trò là cờ dựa trên đầu vào của người dùng
-Sử dụng các câu lệnh điều kiện lồng nhau bên dưới câu lệnh if-else phân chia chương trình giữa người dùng máy tính mới và người dùng máy tính có kinh nghiệm (ví dụ: if? new#1: other? exp#2).
-Theo dõi có bao nhiêu người đã sử dụng chương trình này thông qua hệ thống đếm trong mã chào mừng.
'''
###LIBRARIES###
'TO BE DECIDED'
'ĐƯỢC QUYẾT ĐỊNH'

###GLOBAL VARIABLES###

user_id = 0 #default case (trường hợp mặc định)
user_name = ""	#placeholder for the name of the user (giữ chỗ cho tên của người dùng)
user_type = None #default case; determines if user is new, average, or experienced (trường hợp default; xác định xem người dùng là mới, trung bình hay có kinh nghiệm)
user_input = ""	#placeholder for any input strings from the user (trình giữ chỗ cho bất kỳ chuỗi đầu vào nào từ người dùng)
user_app = None #default case; determines what the user would be using the laptop for (trường hợp default; xác định những gì người dùng sẽ sử dụng máy tính xách tay cho)

budget = None #default case, $300
prompt_fin = 0 #default case, 0=continue prompting, 1=finish prompting
confidence = None #default case, determines how confident a person is with tech jargon.
dim_screen = None #default case, determines dimensions of screen.
laptop_purpose = None #default case, original answer of what the user would be using the laptop for in user_app; utilized in closing()
RAM = None #default case, determines how much RAM a laptop must have.
storage_cap = None #default case, determines how much storage a laptop must have.

#Placeholder statements used in closing functions.
laptop_purpose_print = ""
budget_print = ""
screen_size_print_closing = ""
storage_size_print_closing = ""
RAM_capacity_print_closing = ""

rating = 0 #default case, will be divided into 3 groups: none → 2, 3 → 5)

###FUNCTIONS###

# Greeting
# Say hello to the user
# Ask for their name
# Introduce the user to the program
# Increment the user_id by 1 (PROTOTYPE)

# Lời chào
# Nói xin chào với người dùng
# Hỏi tên của họ
# Giới thiệu người dùng về chương trình
# Tăng user_id lên 1 (PROTOTYPE)

def greeting():
	global user_id
	global user_name
	
	print("Xin chào! Đây là dịch vụ đề xuất máy tính xách tay giúp cá nhân bạn tìm đúng máy tính xách tay phù hợp với nhu cầu của bản thân.")
	user_name=input("Trước khi chúng tôi đi vào chi tiết, tên của bạn là gì?\n>>>")
	#user_id+=1
	print("Hân hạnh được gặp bạn, " +user_name+ ", chúng tôi hy vọng có thể giúp bạn tìm được loại máy tính xách tay bạn muốn.\n")
	#print(user_id)


#Prompt user for how confident/familiar they are with laptops and their specs.
# Is confidence level correctly inputted as an integer?
# Used for type_user(); see below

#Nhắc nhở người dùng về mức độ tự tin/quen thuộc của họ với máy tính xách tay và thông số kỹ thuật của chúng.
# Mức độ tin cậy có được nhập chính xác dưới dạng số nguyên không?
# Dùng cho type_user(); xem bên dưới
def confidence_lvl_int():
	global confidence
	while(confidence==None):
		try:
			confidence=int(input("Trên thang điểm từ 0 đến 10, bạn quen thuộc với máy tính xách tay và thông số kỹ thuật của chúng nói chung đến mức nào?\n>>>"))
		except:
			print("Chúng tôi xin lỗi, nhưng chúng tôi không hiểu ý của bạn, " +user_name+". Vui lòng nhập lại số.")

#5 prompts based on level of experience for users.
#Used for type_user(); see below
#5 dựa trên mức độ trải nghiệm của người dùng.
#Được sử dụng cho type_user(); xem bên dưới
def test_user_newbie():
	global user_type
	user_type=0
	print("\nKhông sao cả, không biết gì là bước khởi đầu để biết điều gì đó và đó là lý do tại sao chúng tôi ở đây để giúp bạn và giữ mọi thứ đơn giản nhất có thể.\n")
	return user_type

def test_user_average():
	global user_type
	user_type=1
	print("\nTuyệt vời, chúng tôi sẽ cố gắng giữ mọi thứ đơn giản cho bạn.\n")
	return user_type

def test_user_experienced():
	global user_type
	user_type=2
	print("\nTuyệt vời, chúng tôi sẽ xem xét các chi tiết chính xác hơn để tinh chỉnh máy tính xách tay hoàn hảo cho bạn khi chúng tôi thực hiện việc này.\n")
	return user_type

def test_user_hopeless():
	global user_type
	user_type=0
	print("\nĐừng lo lắng, chúng tôi ở đây để giúp những người như bạn bắt đầu đi đúng hướng.\n")
	return user_type

def test_user_narcissistic():
	global user_type
	user_type=2
	print("\nChúng tôi ngưỡng mộ sự tự tin của bạn. Chúng tôi mong muốn làm hài lòng bạn sau đó.\n")
	return user_type

# The type of user
# Ask if they are tech savvy or not on a scale of 0-10.
# 0-3=NEW, 4-6=AVERAGE, 7-10=EXPERIENCED
# Lays initial pathway into new_user(), average_user(), and experienced_user()
# Loại người dùng
# Hỏi xem họ có hiểu biết về công nghệ hay không trên thang điểm từ 0-10.
# 0-3=MỚI, 4-6=TRUNG BÌNH, 7-10=TRẢI NGHIỆM
# Đặt đường dẫn ban đầu vào new_user(), average_user() và Experience_user()
def type_user():
	global user_name
	global user_type
	global confidence
	
	while(user_type==None):
		#Ask for input; Is the input an integer? (# Yêu cầu đầu vào; Đầu vào có phải là số nguyên không?)
		confidence_lvl_int()
			
		#For the newbies. (#Dành cho người mới.)
		if (confidence<=3) and (confidence>=0):
			test_user_newbie()
		#For the average. (#Đối với mức trung bình.)
		elif (confidence>=4) and (confidence<=6):
			test_user_average()
		#For the experienced. (#Dành cho người có kinh nghiệm.)
		elif (confidence>=7) and (confidence<=10):
			test_user_experienced()
		#For the real smartasses. (#Đối với những người thông minh thực sự.)
		elif (confidence>=11):
			test_user_narcissistic()
		#For anyone who is just somehow negative. (#Dành cho bất kỳ ai chỉ tiêu cực bằng cách nào đó.)
		elif (confidence<0):
			test_user_hopeless()
		else:
			print("Chúng tôi xin lỗi, nhưng chúng tôi không hiểu ý của bạn, " +user_name+". Vui lòng nhập lại số.")
	return user_type

#Print statements for application type options
#Used for application(); see below	
#Print câu lệnh cho các tùy chọn loại ứng dụng
#Được sử dụng cho application(); xem bên dưới
def application_print_options():
	global user_name
	print("OK, "+user_name+", câu hỏi quan trọng nhất mà chúng tôi có thể hỏi bạn bây giờ là: bạn định sử dụng chiếc máy tính xách tay này để làm gì?")
	print("Dưới đây là 1 lựa chọn trong số 5 tùy chọn để bạn chọn:") 
	print("Option 1: Trò chơi điện tử")
	print("Option 2: Công việc văn phòng/trường học")
	print("Option 3: Dự án nâng cao (bao gồm chỉnh sửa video, vẽ, phát triển chương trình, v.v.)")
	print("Option 4: Sử dụng nhẹ/tài liệu chung (ảnh và video của gia đình/bạn bè, khai thuế, đọc sách điện tử, v.v.).")
	print("Option 5: Khác/Không xác định (Chúng tôi sẽ chọn từ tiêu chuẩn chung của máy tính xách tay nếu không có tùy chọn nào ở trên phù hợp với tiêu chí của bạn)\n")

#Application
#What will the user be using the laptop for?
#Đăng kí
#Người dùng sẽ sử dụng máy tính xách tay để làm gì?
def application():
	global user_name
	global user_app
	global laptop_purpose
	flag=False
	
	application_print_options()
	while(flag==False):
		while(user_app==None):
				try:
					user_app=int(input("Vui lòng chọn và nhập 1 trong 5 tùy chọn (1, 2, 3, 4, or 5).\n>>>"))
				except:
					print("Chúng tôi xin lỗi, nhưng chúng tôi không thể hiểu ý của bạn là gì, " +user_name+". Hãy chắc chắn rằng bạn đang gõ 1 trong 5 số.")
		#Laptop_purpose will be used later for the closing().
		laptop_purpose=user_app
		if(user_app<1) or (user_app>5):
			print("Chúng tôi xin lỗi, nhưng đó không phải là một đầu vào hợp lệ.")
			user_app=None
		else:
			#Make user_app set to gamer regardless if they are option 3 (most specs for gamers would apply to advanced projects)
			if (user_app==1) or (user_app==3):
				user_app=1
			#Make user_app set to office/school work even if they are options 4 or 5 (office/school work dedicated laptops can apply to all 3 options)
			if (user_app==2) or (user_app==4) or (user_app==5):
				user_app=2
			flag=True

#Two different prompts based on what the user would be using the laptop for.
#Reminder: user_app==1 means gaming; 2 means study.
#Used for budget_range(); see below
#Hai lời nhắc khác nhau dựa trên mục đích sử dụng máy tính xách tay của người dùng.
#Reminder: user_app==1 nghĩa là chơi game; 2 nghĩa là học.
#Được sử dụng cho budget_range(); xem bên dưới
def gamer_user_budget():
	global budget
	global user_name
	global user_app
	if (user_app==1):
		while(budget==None):
			try:
				budget=int(input("Số tiền tối đa bạn sẵn sàng chi cho một chiếc máy tính xách tay là bao nhiêu?\nPhạm vi giá được chấp nhận là từ $350 đến $6500.\n(LƯU Ý: Hầu hết các máy tính xách tay thường có giá khoảng $3425)\n>>>").replace(',','').replace('$',''))
			except:
				print("Chúng tôi xin lỗi, nhưng chúng tôi không hiểu ý của bạn, " +user_name+". Vui lòng nhập lại số.")
		if (budget<350) or (budget>6500):
			print("Chúng tôi không có bất kỳ sản phẩm nào phù hợp với ngân sách đó.")
			budget=None
		else:
			return True

def study_user_budget():
	global budget
	global user_name
	global user_app
	if (user_app==2):
		while(budget==None):
			try:
				budget=int(input("Số tiền tối đa bạn sẵn sàng chi cho một chiếc máy tính xách tay là bao nhiêu?\nPhạm vi giá được chấp nhận là từ $150 đến $2500.\n(LƯU Ý: Hầu hết các máy tính xách tay thường có giá khoảng $1325)\n>>>").replace(',','').replace('$',''))
			except:
				print("Chúng tôi xin lỗi, nhưng chúng tôi không hiểu ý của bạn, " +user_name+". Vui lòng nhập lại số.")
		if (budget<150) or (budget>2500):
			print("Chúng tôi không có bất kỳ sản phẩm nào phù hợp với ngân sách đó.")
			budget=None
		else:
			return True

#Budget range
#Determine how much money the user is willing to spend.
#Phạm vi ngân sách
#Xác định số tiền mà người dùng sẵn sàng chi tiêu.
def budget_amount():
	global budget
	flag = False	#Used for breaking out of while loop
	print("\nThật tuyệt vời! Điều tiếp theo chúng tôi cần biết bây giờ là ngân sách của bạn.")
	while (flag==False):
		#Gamer user
		if (gamer_user_budget()==True):
			flag=True
		#Study user
		if (study_user_budget()==True):
			flag=True
	return budget

#Print statements for displaying screen size options
#Used for screen_size(); see below
#Print câu lệnh để hiển thị các tùy chọn kích thước màn hình
#Được sử dụng cho screen_size(); xem bên dưới
def screen_size_print_options():
	print("\nĐược rồi, điều tiếp theo chúng ta cần xem xét là bạn muốn màn hình của mình lớn đến mức nào.\n")
	print("Bạn có 3 tùy chọn để chọn:")
	print("Option 1: 11.6\" to 13.5\". Đây được coi là nhỏ và hữu ích cho những người dùng hay di chuyển, những người thích thứ gì đó di động.")
	print("Option 2: 13.6\" to 15.4\". Đây được coi là mức trung bình và hữu ích cho mục đích sử dụng chung, bao gồm xem phim, công việc văn phòng/trường học và chơi game")
	print("Tùy chọn 3: 15,5\" đến 17,3\". Giá trị này được coi là lớn và thiết thực cho người dùng cố định và/hoặc những người gặp khó khăn về thị lực. Lý tưởng để chơi game cường độ cao, chỉnh sửa video, nghệ thuật hoặc bất kỳ dự án nào.")
	print("Option 4: 17.3\" to 18.4\". Đây được coi là rất lớn và thực tế là một máy tính để bàn di động. Tuy nhiên, kích thước cực lớn của nó gây khó khăn cho việc vận chuyển, mặc dù nó rất hữu ích cho các dự án quy mô lớn, chơi game chuyên sâu yêu cầu nhiều hình ảnh hoặc trải nghiệm xem phim điện ảnh.\n")

#Screen size
#How big does the user want their screen to be?
#Kích thước màn hình
#Người dùng muốn màn hình của họ lớn đến mức nào?
def screen_size():
	global user_name
	global dim_screen
	flag=False	#Used for breaking out of the while loop.

	screen_size_print_options()
	while(flag==False):
		while(dim_screen==None):
				try:
					dim_screen=int(input("Vui lòng chọn và nhập 1 trong 4 tùy chọn (1 nhỏ, 2 vừa, 3 lớn, 4 rất lớn)\n>>>"))
				except:
					print("Chúng tôi xin lỗi, nhưng chúng tôi không thể hiểu ý bạn là gì, " +user_name+". Hãy chắc chắn rằng bạn đang gõ một số.")
		if(dim_screen<1) or (dim_screen>4):
			print("Chúng tôi xin lỗi, nhưng đó không phải là một đầu vào hợp lệ.")
			dim_screen=None
		else:
			flag=True
	return dim_screen

#Print statements for displaying storage size options
#Used for storage_size(); see below
#Print câu lệnh để hiển thị các tùy chọn kích thước bộ nhớ
#Được sử dụng cho storage_size(); xem bên dưới
def storage_size_print_options():
	print("\n Tốt, điều tiếp theo cần tính toán là bạn muốn máy tính xách tay của mình có bao nhiêu dung lượng lưu trữ.\n")
	print("Bạn có 3 tùy chọn để chọn:")
	print("Tùy chọn 1: 64GB đến 256GB. Dung lượng này được coi là nhỏ và hữu ích để lưu trữ ghi chú, ảnh, video ngắn và một vài trò chơi cường độ thấp. Dung lượng này thường dành cho những người không có kế hoạch lưu trữ nhiều thông tin trên thiết bị của họ. Tốt để sử dụng trong khoảng thời gian dưới năm năm.")
	print("Tùy chọn 2: 256GB đến 512GB. Đây được coi là dung lượng trung bình và hữu ích cho mục đích sử dụng chung, bao gồm xem phim, công việc văn phòng/trường học liên quan đến nhiều tài liệu và tệp cũng như chơi game. Tốt để sử dụng trong khoảng thời gian từ 5 đến 10 năm.")
	print("Tùy chọn 3: 512GB trở lên. Dung lượng này được coi là lớn và lý tưởng để chơi game chuyên sâu, chỉnh sửa video, nghệ thuật hoặc bất kỳ dự án quy mô lớn nào. Xin lưu ý rằng điều này có nghĩa là máy tính xách tay có nhiều dung lượng lưu trữ này đắt hơn nhiều. Tốt để sử dụng trong hơn mười năm nói chung.\n")
	print("Thuật ngữ máy tính: MB= megabyte, GB= gigabyte, TB= terabyte\nMB < GB < TB\nCó 1000MB trong 1GB; 1000GB trong 1TB\n")


#Storage capacity
#How much space does the user want their laptop to have?
#Khả năng lưu trữ
#Người dùng muốn máy tính xách tay của họ có bao nhiêu dung lượng?
def storage_size():
	global user_name
	global storage_cap
	flag=False	#Used for breaking out of the while loop.

	storage_size_print_options()
	while(flag==False):
		while(storage_cap==None):
				try:
					storage_cap=int(input("Vui lòng chọn và nhập 1 trong 3 tùy chọn (1 nhỏ, 2 vừa, 3 lớn)\n>>>"))
				except:
					print("Chúng tôi xin lỗi, nhưng chúng tôi không thể hiểu ý bạn là gì, " +user_name+". Hãy chắc chắn rằng bạn đang gõ một số.")
		if(storage_cap<1) or (storage_cap>3):
			print("Chúng tôi xin lỗi, nhưng đó không phải là một đầu vào hợp lệ.")
			storage_cap=None
		else:
			flag=True
	return storage_cap
#Print statements for displaying RAM options
#Used for RAM_capacity(); see below
#In các câu lệnh để hiển thị các tùy chọn RAM
#Được sử dụng cho RAM_capacity(); xem bên dưới
def RAM_print_options():
	print("\nBây giờ, việc tiếp theo cần làm là hiểu và chọn dung lượng RAM mà bạn muốn máy tính xách tay của mình có.\n")
	print("RAM là viết tắt của Random-Access Memory. Đôi khi mọi người nhầm lẫn RAM với dung lượng lưu trữ vì cả hai đều sử dụng GB làm đơn vị đo lường.")
	print("RAM quyết định bạn có thể chạy bao nhiêu chương trình cùng lúc. Hãy coi nó giống như một cái bàn: nếu bạn có nhiều không gian trên bàn làm việc (tức là một lượng lớn RAM), thì bạn sẽ có nhiều không gian hơn để trải ra giấy tờ của bạn và đọc tất cả chúng cùng một lúc.\nMặt khác, nếu bạn có ít không gian trên bàn làm việc (tức là dung lượng RAM nhỏ), thì bạn sẽ có ít không gian hơn để xem giấy tờ của mình và phải chọn lọc xem cái nào để đọc cùng một lúc.\n NÓI CÁCH KHÁC: RAM xác định mức độ bạn có thể thực hiện nhiều tác vụ trên máy tính xách tay của mình cùng một lúc.\n")
	print("Bạn có 3 tùy chọn để chọn:")
	print("Option 1: 4GB. Đây là dung lượng RAM nhỏ cho phép bạn thực hiện một số tác vụ cùng lúc. Nó dành cho công việc và sử dụng cường độ thấp (bạn vẫn có thể xem phim hoặc sử dụng cho công việc, nhưng bạn có thể bị chậm lại.")
	print("Tùy chọn 2: 8GB. Đây là dung lượng RAM phù hợp cho phép thực hiện nhiều tác vụ hơn cùng một lúc. Nó hoàn thành phần lớn công việc và đáng tin cậy. Tuy nhiên, không lý tưởng cho mục đích chơi game và chủ yếu là dành cho công việc.")
	print("Tùy chọn 3: 16GB. Đây là dung lượng RAM tiêu chuẩn cho phép bạn thực hiện nhiều tác vụ khác nhau hàng ngày. Đây là dung lượng RAM tốt toàn diện, hoàn toàn có khả năng chơi game, làm việc và là dung lượng được khuyên dùng cho hầu hết người dùng.")
	print("Tùy chọn 4: 32GB trở lên. Đây là dung lượng RAM đặc biệt thường đắt hơn so với đối tác 16GB, nhưng rất lý tưởng cho những người chuyên về một lĩnh vực công việc cụ thể đòi hỏi nhiều năng lượng và năng lượng để sử dụng . Hãy nghĩ đây giống như một chiếc bàn làm việc dành cho thợ thủ công. Nó cũng là một chiếc máy tính xách tay chơi game tuyệt vời.\n")

def RAM_capacity():
	global user_name
	global RAM
	flag=False	#Used for breaking out of the while loop.

	RAM_print_options()
	while(flag==False):
		while(RAM==None):
				try:
					RAM=int(input("Vui lòng chọn và nhập 1 trong 4 tùy chọn (1 cho 4GB, 2 cho 8GB, 3 cho 16GB, 4 cho 32GB trở lên)\n>>>"))
				except:
					print("Chúng tôi xin lỗi, nhưng chúng tôi không thể hiểu ý bạn là gì, " +user_name+". Hãy chắc chắn rằng bạn đang gõ một số.")
		if(RAM<1) or (RAM>4):
			print("Chúng tôi xin lỗi, nhưng đó không phải là một đầu vào hợp lệ.")
			RAM=None
		else:
			flag=True
	return RAM

#Prompts dedicated to new, inexperienced users.
#Must be broken down into:
#Budget
#Application (what are they using the laptop for)
#Screen size (will they be moving a lot or staying in one spot)
#Storage (would they like a lot of storage space)
#Ram (how powerful do they need their laptops to be)

#Prompts dành riêng cho người dùng mới, thiếu kinh nghiệm.
#Phải được chia thành:
#Ngân sách
#Ứng dụng (họ đang sử dụng máy tính xách tay để làm gì)
#Kích thước màn hình (họ sẽ di chuyển nhiều hay ở yên một chỗ)
#Storage (họ có muốn nhiều không gian lưu trữ không)
#Ram (họ cần máy tính xách tay của họ mạnh đến mức nào)

def laptop_purpose_closing():
	global laptop_purpose
	global laptop_purpose_print
	if (laptop_purpose==1):
		laptop_purpose_print="1- Trò chơi điện tử"
	elif(laptop_purpose==2):
		laptop_purpose_print="2- Công việc văn phòng/trường học"
	elif(laptop_purpose==3):
		laptop_purpose_print="3- Dự án nâng cao"
	elif(laptop_purpose==4):
		laptop_purpose_print="4- Sử dụng nhẹ/Tài liệu chung"
	else:
		laptop_purpose_print="5- Khác/Không xác định"
	return (laptop_purpose_print)

def budget_closing():
	global budget_print
	global budget
	budget_print=str(budget)
	return (budget_print)
	
def screen_size_closing():
	global screen_size_print_closing
	if(dim_screen==1):
		screen_size_print_closing='1- 11.6\" to 13.5\"'
	elif(dim_screen==2):
		screen_size_print_closing='2- 13.6\" to 15.4\"'
	elif(dim_screen==3):
		screen_size_print_closing='3- 15.5\" to 17.3\"'
	else:
		screen_size_print_closing='4- 17.4\" to 18.4\"'
	return (screen_size_print_closing)
	
def storage_size_closing():
	global storage_size_print_closing
	if(storage_cap==1):
		storage_size_print_closing="1- 64GB to 256GB"
	elif(storage_cap==2):
		storage_size_print_closing="2- 256GB to 512GB"
	else:
		storage_size_print_closing="3- >= 512GB"
	return (storage_size_print_closing)

def RAM_capacity_closing():
	global RAM_capacity_print_closing
	if(RAM==1):
		RAM_capacity_print_closing="1- 4GB"
	elif(RAM==2):
		RAM_capacity_print_closing="2- 8GB"
	elif(RAM==3):
		RAM_capacity_print_closing="3- 16GB"
	else:
		RAM_capacity_print_closing="4- 32GB"
	return (RAM_capacity_print_closing)

def closing():
	global user_name
	flag=False
	recheck_flag=False
	
	print("\nCảm ơn bạn rất nhiều vì câu trả lời của bạn, " + user_name + "! Đây là bản ghi các thông tin đầu vào của bạn và chúng tôi muốn đảm bảo rằng chúng tôi đã nhận được câu trả lời đúng của bạn. Vui lòng xem qua câu trả lời của bạn và cho chúng tôi biết nếu bạn muốn thay đổi bất cứ điều gì trước khi chúng tôi đưa ra đề xuất của mình.\n")
	
	print("(1)Mục đích máy tính: " + laptop_purpose_closing())
	print("(2)Ngân sách: $" + budget_closing())
	print("(3)Kích thước màn hình: " + screen_size_closing())
	print("(4)Dung lượng lưu trữ: " + storage_size_closing())
	print("(5)Dung lượng RAM: " + RAM_capacity_closing())
	'''
	print (user_name)
	print (confidence)
	print (user_type)
	print (user_app)
	print (budget)
	print (dim_screen)
	print (storage_cap)
	print (RAM)
	'''
	while (flag==False):
		end_prompt=input("\nXác nhận đúng thông tin (Y\\N)\n>>>")
		if (end_prompt=="Y") or (end_prompt=="y"):
			print("Thật tuyệt vời.")
			flag=True
		elif (end_prompt=="N") or (end_prompt=="n"):
			print("Chúng tôi vô cùng xin lỗi. Vui lòng tải lại chương trình để nhập lại câu trả lời")
			flag=True
		else:
			print("Xin lỗi, đầu vào không hợp lệ. vui lòng gõ 'Y' or 'N'.")

###MAIN FUNCTION###

def main():
	global b, ss, sc, r
	greeting()
	type_user()
	#if the user is experienced at laptops (#nếu người dùng có kinh nghiệm sử dụng máy tính xách tay)
	if (type_user()==2):
		print("Người dùng có kinh nghiệm")
		application()
		b = budget_amount() # return budget
		ss = screen_size() # returns dim_screen
		sc = storage_size() # returns storage_cap
		r = RAM_capacity() # returns RAM
		closing()
	#if the user is average at laptops (#nếu người dùng sử dụng máy tính xách tay ở mức trung bình)
	elif (type_user()==1):
		print("Người dùng ở mức trung bình")
		application()
		b = budget_amount()
		ss = screen_size()
		sc = storage_size()
		r = RAM_capacity()
		closing()
	#if the user is new at laptops (#nếu người dùng mới sử dụng máy tính xách tay)
	else:
		print("Người dùng mới")
		application()
		b = budget_amount()
		ss = screen_size()
		sc = storage_size()
		r = RAM_capacity()
		closing()

main()
