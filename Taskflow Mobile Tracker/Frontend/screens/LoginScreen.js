import React, { useState } from 'react';
import { View, TextInput, Button, Alert } from 'react-native';

export default function LoginScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const login = async () => {
    const res = await fetch('http://localhost:8000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    if (res.ok) {
      const data = await res.json();
      navigation.navigate('TaskList', { userId: data.user_id });
    } else {
      Alert.alert('Login Failed');
    }
  };

  return (
    <View>
      <TextInput placeholder="Username" onChangeText={setUsername} />
      <TextInput placeholder="Password" onChangeText={setPassword} secureTextEntry />
      <Button title="Login" onPress={login} />
    </View>
  );
}
