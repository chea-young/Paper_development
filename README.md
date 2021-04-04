# Paper_development

### 참고 링크
- https://wikidocs.net/15881 (sqlite3 이미지 삽입)
- http://faculty.washington.edu/wlloyd/courses/tcss562/tutorials/TCSS562_f2019_tutorial_6.pdf (lambda에 이미지 삽입)

-https://ndb796.tistory.com/289 (AWS lambda와 s3연결)
### lambda에서 sqlite 사용
- 최대 6-8시간까지 사용할 수 있지만 더 오래 유지 하려면 S3에 저장을 해야 한다. 

# Lambda 함수
-  python 사용 시 필수적인 요소 3가지 handler, event, context

### Handler
- Lambda funtion이 호출될때 실행하는 handler를 위와 같은 형식으로 정의 해놓고  c나 java의 Main 함수 처럼 사용합니다. handler라는 이름은 당연히 수정하셔도 됩니다. main으로 실행할 함수를 정의하시고 추후 aws Lambda 콘솔에서 handler로 지정합니다. handler (event, context)의 포맷만 기억하시면 됩니다.
### Event
- Lambda function을 실행할때 넘겨주는 파라메터들을 이 event로 받아서 처리 할 수 있습니다. http로 lambda를 실행할때 get, post, put, delete 등의 메서드를 통해서 전달 할 수 있습니다. JAVA servlet 에서 doGet, doPost 등에 있는 requst 와 같은 역할을 합니다.
### Context
- Lambda function이 실행완료 하고 context를 통해 return 할 수 있습니다. 성공 메시지, 실패 메시지등을 리턴 할 수 있습니다. JAVA Servlet으로 보면 doGet doPost등의 response와 같은 역할을 합니다.
