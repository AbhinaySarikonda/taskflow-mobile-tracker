import React, { useState } from 'react';
import { View, TextInput, Button } from 'react-native';

export default function CreateTask({ route, navigation }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [tag, setTag] = useState('');
  const [status, setStatus] = useState('');
  const { userId } = route.params;

  const createTask = async () => {
    await fetch('http://localhost:8000/tasks/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, description, tag, status, owner_id: userId })
    });
    navigation.goBack();
  };

  return (
    <View>
      <TextInput placeholder="Title" onChangeText={setTitle} />
      <TextInput placeholder="Description" onChangeText={setDescription} />
      <TextInput placeholder="Tag" onChangeText={setTag} />
      <TextInput placeholder="Status" onChangeText={setStatus} />
      <Button title="Create" onPress={createTask} />
    </View>
  );
}
