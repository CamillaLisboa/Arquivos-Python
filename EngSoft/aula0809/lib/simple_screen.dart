import 'package:flutter/material.dart';

class SimpleScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Exemplo Flutter")),
      body: Center(
        child: Text("Olá! Essa é a tela simples."),
      ),
    );
  }
}
