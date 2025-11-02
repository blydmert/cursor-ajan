import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StyleSheet, View, Text } from 'react-native';

const Tab = createBottomTabNavigator();

// Placeholder screens
const WardrobeScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Gard?robum</Text>
    <Text style={styles.subtitle}>K?yafetlerinizi buradan y?netin</Text>
  </View>
);

const CombinationsScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Kombinasyonlar</Text>
    <Text style={styles.subtitle}>AI destekli kombinasyon ?nerileri</Text>
  </View>
);

const ShoppingScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Al??veri?</Text>
    <Text style={styles.subtitle}>Size ?zel al??veri? ?nerileri</Text>
  </View>
);

const TripsScreen = () => (
  <View style={styles.container}>
    <Text style={styles.title}>Seyahatler</Text>
    <Text style={styles.subtitle}>Bavul haz?rlama</Text>
  </View>
);

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Gard?robum" component={WardrobeScreen} />
        <Tab.Screen name="Kombinasyonlar" component={CombinationsScreen} />
        <Tab.Screen name="Al??veri?" component={ShoppingScreen} />
        <Tab.Screen name="Seyahatler" component={TripsScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
});
