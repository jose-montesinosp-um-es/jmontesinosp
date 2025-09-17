import 'package:flutter/material.dart';
import 'package:front_flutter/components/navegacion_inf.dart';
import 'package:front_flutter/core/paleta_colores.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(appBar: AppBar(
        title: Text('Fitness App'), 
        backgroundColor: AppColors.primary,
        centerTitle: true,
        foregroundColor: Colors.white,
        actions: [
          IconButton(onPressed: (){}, icon: const Icon(Icons.settings))
          ],
        ),
      backgroundColor: AppColors.background,
      body: NavegacionInf()
      )
    );
  }
}
