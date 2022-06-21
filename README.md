# INT3411_20_Final_Project_Nhom2

Nhóm 2 : Hồ Công Phùng 

	Đoàn Đình AN 


Mô tả chung về App : App dùng để trợ giúp người dùng đánh văn bản

Tổng quan : 

Web của bọn em là web dùng để nhận biết giọng nói của người truyền vào , khi người nói thì web sẽ nhận biết được và sẽ trả ra 1 đoạn văn bản tương ứng với câu nói mà web được nhận 

Web gồm 2 phần xử lý đó là phần xử lý khi truyền giọng nói vào và phần xử lý xuất ra đoạn văn bản . Ở đây bọn em chọn ngôn ngữ tiếng anh và tiếng việt để có thể gia tăng số lượng người dùng hơn

 Báo cáo này sẽ tập trung nhiều đến phần điều khiển ghi âm và xuất văn bản , cụ thể là mô hình nhận diện được sử dụng.

Dựa trên thời gian đã test khi qua sử dụng , nhóm xác định độ trễ để web xử lý phần ghi âm đến khi cho ra kết quả là đoạn văn bản là khoảng 0,202s. Trong thời gian xử lý , trích xuất đặc 
trưng mất tầm 0,14s. Đây là độ trễ nhóm đã cố gắng giảm được.


Mô hình nhận diện 

Nhóm đã tiến hành  sử dụng thư viện speechRecognition để nhận dạng người dùng. Một thư viện được cho sẵn và đã được các nhà phát triển sử dụng ngôn ngữ Python kết hợp với ngôn ngữ Javascript 
phát triển.Giao diện SpeechRecognition của Web Speech API là giao diện bộ điều khiển cho dịch vụ nhận dạng; điều này cũng xử lý SpeechRecognitionEvent được gửi từ dịch vụ nhận dạng.

dùng hàm có sẵn webkitSpeechRecognition() để có thể nhận dạng được người dùng web và bọn em sử dùng SpeechRecognition.lang để có thể set được ngôn ngữ mà người máy có thể nhận diện được 

Tiếp tục sử dụng biến có sẵn của hàm SpeechRecognition.continuous để có thể giới hạn thời gian dành cho người nói , khi mà web nhận biết được người dùng không nói nữa hoặc chấm được 1 câu 
thì web sẽ tắt chế độ tìm kiếm bằng giọng nói.

SpeechRecognition.interimResults là dùng để Kiểm soát xem có nên trả về kết quả tạm thời (đúng) hay không (sai.) Kết quả tạm thời là kết quả chưa phải là cuối cùng vì khi người dùng phát âm 
không đúng tiếng anh hoặc dùng 1 ngôn ngữ khác ngôn ngữ tiếng anh thì web vẫn sẽ trả ra kết quả nhưng đó sẽ là kết quả tạm thời. 

Bộ nhận diện giọng nói 

Bọn em phát triển web dựa trên giao diện tìm kiếm giọng nói của google sẽ có 1 thanh tìm kiếm và 1 cái mic để nhận diện giọng nói của người dùng. Ở phần mic thì bọn em gán sự kiện click để
có thể cho người dùng quyền bắt đầu ghi âm rồi ở hàm sự kiện đấy bọn em sử dụng SpeechRecognition.start() Khởi động dịch vụ nhận dạng giọng nói, nghe âm thanh đến với mục đích 
nhận dạng ngữ pháp liên quan đến hiện tại và có thể sẽ bắt đầu nhận dạng ghi âm mới  cùng với SpeechRecognition.stop() Dừng dịch vụ nhận dạng giọng nói nghe âm thanh đến và cố gắng trả về
 kết quả đúng nhất.

Các vấn đề gặp phải trong quá trình thực hiện
	- Phần xử lý ban đầu bọn em muốn làm 1 thanh tìm kiếm như google nhưng gặp khó khăn trong việc phần xử lý tiếng việt , dôi lúc nó trả kết qủa đúng nhưng đôi khi nó lại trả kết quả sai 
muốn được kết quả đúng phải nói rõ từng chữ , từng dấu câu việc này có thể cho người dùng việc không thoải mái khi sử dụng 

Kết quả, kết luận
Video minh họa kết quả có tại đây.
https://drive.google.com/file/d/1em5XDe4aAtGPjKtaXzJ43HYP6_xrICnL/view?usp=sharing

https://drive.google.com/file/d/1T284Okm9qVOGsNnTL4e-wHiMAq9C0F3l/view?usp=sharing

Dựa vào kết quả từ thực tế, nhóm em rút ra nhận xét như sau:
- Độ chính xác của web chỉ lên đến 80-90 phần trăm. tỉ lệ này biến độ nhiều theo độ yên tĩnh và độ nhiễu của môi trường xung quanh . và có thể gặp khó khăn khi xử lý văn bản khi mình có thể 
phát âm sai và không chuẩn theo ngữ pháp và còn phải click chuột theo sự kiện được giao ra  để giao tiếp.
- Web này  chưa hề có gì là thông minh. Thực tế thì bọn em cố làm cho web này có thể nhận biết được ngôn ngữ tiếng việt nhưng con web này vẫn chuộng tiếng anh hơn là tiếng việt mặc dù không hiểu 
tại sao 

Lưu ý cài đặt

Sử dụng HTML , CSS, JS, Python và thư viện flask



	

