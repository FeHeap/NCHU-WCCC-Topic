import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(const MyApp());


class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Http request',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Http request'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            var url = 'https://nchu-wccc-topic-fe-test-01.herokuapp.com/receivePOST';
            http.post(Uri.parse(url), body: {'time': DateTime.now().toString(), 'message': 'Hello, flutter!'}).then((response) {
              print('status: ${response.statusCode}');
              print('content: ${response.body}');
            });
          },
          child: Text('發起http請求'),
        )
      ),
    );
  }
}
