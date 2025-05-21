import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, Button } from 'react-native';

export default function TaskList({ route, navigation }) {
  const [tasks, setTasks] = useState([]);
  const { userId } = route.params;

  useEffect(() => {
    fetch('http://localhost:8000/tasks')
      .then(res => res.json())
      .then(setTasks);
  }, []);

  return (
    <View>
      <FlatList
        data={tasks}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <Text>{item.title} - {item.status}</Text>
        )}
      />
      <Button title="Create Task" onPress={() => navigation.navigate('CreateTask', { userId })} />
    </View>
  );
}
