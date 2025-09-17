import 'package:flutter/material.dart';
import 'package:front_flutter/core/paleta_colores.dart';
import 'package:front_flutter/screens/home.dart';
import 'package:front_flutter/screens/profile.dart';
import 'package:front_flutter/screens/workout.dart';

class NavegacionInf extends StatefulWidget {

  const NavegacionInf({super.key});

  @override
  State<NavegacionInf> createState() => _NavegacionInfState();
}

class _NavegacionInfState extends State<NavegacionInf> {

  int _indiceActual = 0;
  final List<Widget> _pantallas = [
    HomeScreen(),
    WorkoutScreen(),
    ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: _pantallas[_indiceActual],
      bottomNavigationBar: BottomNavigationBar(
          currentIndex: _indiceActual,
          onTap: (index) {
            setState(() {
              _indiceActual = index;
            });
          },
          type: BottomNavigationBarType.fixed, 
          selectedItemColor: AppColors.primary,
          unselectedItemColor: Colors.grey,
          backgroundColor: AppColors.backgroundComponents,
          items: [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'Home',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.fitness_center),
              label: 'Workout',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.person),
              label: 'Profile',
            ),
          ],
        ),
    );
  }
}