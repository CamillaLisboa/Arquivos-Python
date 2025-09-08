import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tela Simples',
      home: SimpleScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class SimpleScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Minha primeira tela Flutter"),
        centerTitle: true,
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(16),
          color: Colors.blue[50],
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                "Bem-vindo ao Flutter!",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              Divider(
                color: Colors.blue,
                thickness: 2,
                height: 24,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text("Você está lendo o lado esquerdo"),
                  SizedBox(width: 20),
                  Text("Agora está lendo o lado direito"),
                ],
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // Ação do botão
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text("Você clicou no botão! Danadinho....")),
                  );
                },
                child: Padding(
                  padding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  child: Text("Não clique aqui"),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
