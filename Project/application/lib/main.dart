import 'package:flutter/material.dart';
import 'dart:ui';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Project Practice',
      theme: ThemeData(
          primarySwatch: Colors.teal
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

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        actions: <Widget>[
          PopupMenuButton<String>(
            onSelected: handleClick,
            itemBuilder: (BuildContext context) {
              return {'App介紹', '每日接觸狀況','確診者上船隨機ID','注意事項及個資保護說明',
                '資料權限控制','常見問題','功能提示'}.map((String choice) {
                return PopupMenuItem<String>(
                  value: choice,
                  child: Text(choice),
                );
              }).toList();
            },
          ),
        ],
      ),
      body: Center (
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              '與確診者資料比對無接觸',
              style: TextStyle(
                  fontSize: 35,
                  fontWeight: FontWeight.w700,
                  color: Colors.teal
              ),
            ),
            Text(
              '請繼續保持社交距離',
              style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.w400,
                  color: Colors.teal
              ),
            ),

            Container(
                child: Column (
                  children: [
                    Container(
                      width: window.physicalSize.width,
                      color: Colors.teal,
                      child: Text('接觸通知功能已開啟'),
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
                )
            ),
          ],
        ),
      ),
    );
  }
}

void handleClick(String value) {
  switch (value) {
    case 'App介紹':
      break;
    case '每日接觸狀況':
      break;
  }
}
