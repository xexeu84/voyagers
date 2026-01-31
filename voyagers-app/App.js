import React from 'react';
import { StyleSheet, Text, View, ScrollView, TouchableOpacity } from 'react-native';

export default function App() {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.logo}>VOYAGERS</Text>
        <Text style={styles.subtitle}>App de Operaciones</Text>
      </View>
      <TouchableOpacity style={styles.card}>
        <Text style={styles.cardTitle}>Ruta Activa: MAD -> BCN</Text>
        <Text style={styles.cardDetail}>Ganancia Estimada: 15€</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', paddingTop: 60 },
  header: { padding: 20, borderBottomWidth: 1, borderBottomColor: '#eee' },
  logo: { fontSize: 24, fontWeight: '900', color: '#2563eb' },
  subtitle: { color: '#64748b' },
  card: { margin: 20, padding: 20, backgroundColor: '#f1f5f9', borderRadius: 20 },
  cardTitle: { fontSize: 18, fontWeight: 'bold' },
  cardDetail: { color: '#10b981', marginTop: 5 }
});
