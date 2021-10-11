import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Project Practice',
      theme: ThemeData(
        primarySwatch: Colors.cyan
      ),
      home: MyHomePage(title: '臺灣社交距離'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

//

enum AppMenu { appIntroduction, dailyExposure, uploadsRandomID,
  instructions,DataAccessControl, commonProblem, functionTips }

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: <Widget>[
          PopupMenuButton<AppMenu>(
            onSelected: (AppMenu result) {
              switch(result) {
                case  AppMenu.uploadsRandomID:
                  showAlert(context);
                  break;
                /*case AppMenu.selfStarter:
                  print("hahahahaha");
                  break;*/
              }
            },
            itemBuilder: (BuildContext context) => <PopupMenuEntry<AppMenu>>[
              const PopupMenuItem<AppMenu>(
                value: AppMenu.appIntroduction,
                child: Text("App介紹"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.dailyExposure,
                child: Text("每日接觸狀況"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.uploadsRandomID,
                child: Text("確診者上傳隨機ID"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.instructions,
                child: Text("注意事項及個資保護說明"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.DataAccessControl,
                child: Text("資料權限控制"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.commonProblem,
                child: Text("常見問題"),
              ),
              const PopupMenuItem<AppMenu>(
                value: AppMenu.functionTips,
                child: Text("功能提示"),
              ),
            ],
          )
        ],
      ),
      body: //Center(
        /*child: */LayoutBuilder(
          builder: (context, constraints) => Column(
                mainAxisSize: MainAxisSize.min,
                //mainAxisSize: MainAxisSize.max,
                children: [
                  Container(
                    color: Colors.grey[350],
                    height: constraints.maxHeight * 0.65,
                    width: constraints.maxWidth ,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Text(
                          '與確診者資料比對無接觸\n',
                          style: TextStyle(
                              fontSize: 30,
                              fontWeight: FontWeight.w700,
                              color: Colors.cyan
                          ),
                          //textAlign: TextAlign.center,
                        ),
                        Text(
                          '請繼續保持社交距離',
                          style: TextStyle(
                              fontSize: 25,
                              fontWeight: FontWeight.w400,
                              color: Colors.cyan
                          ),
                          //textAlign: TextAlign.center,
                        ),
                      ],
                    ),
                  ),
                  Container(
                    //color: Color.fromARGB(20, 226, 207, 100),
                    color: Colors.cyan,
                    child: Column(
                      //mainAxisAlignment: MainAxisAlignment.center,
                      //mainAxisSize: MainAxisSize.max,
                      children: <Widget>[
                        Text('接觸通知功能已開啟'),
                      ]
                    ),
                    margin: EdgeInsets.fromLTRB(50, 20, 50, 0),
                  ),
                  Text(
                    '\n接觸通知功能啟用時間1967/2/20 19:58',
                    style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w400,
                        color: Colors.black
                    ),
                  ),
                  Text(
                    '運作時間比例為99%',
                    style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w400,
                        color: Colors.black
                    ),
                  ),
                  Text(
                    '上次檢查時間為2021/12/25 10:54',
                    style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w400,
                        color: Colors.black
                    ),
                  ),
                ],
              ),
            //)
      ),
    );
  }
}


Future<void> showAlert(BuildContext context) {
  return showDialog<void>(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("你是確診者嗎"),
        content: const Text("此功能為提供確診者上傳隨機ID以減少疫情擴散"),
        actions: <Widget>[
          TextButton(
            child: Text('否'),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
          TextButton(
            child: Text('是'),
            onPressed: () {
              var url = 'https://nchu-wccc-topic-fe-test-01.herokuapp.com/receivePOST';
              http.post(Uri.parse(url), body: {'time': DateTime.now().toString(), 'message': 'Hello, flutter!'}).then((response) {
                print('status: ${response.statusCode}');
                print('content: ${response.body}');
                }
              );
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}


