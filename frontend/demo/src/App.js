import './App.css';
import axios from "axios";
import React, {useState, useEffect} from "react";


function App() {
    const DATA_URL = 'http://localhost:5005';

    const [data, setData] = useState({});

    const getData = () => {
        axios.get(DATA_URL)
            .then(response => {
                const data = response.data;
                console.log('getData response.data > ', data);
                setData(data);
            }).catch((error) => {
            console.error('Извините, проблемы с сервером.');
            console.error(error)
        })
    }

    useEffect( () => {
        getData();
    }, []);

    return (
        <div className="App">
            <h1>{JSON.stringify(data)}</h1>
        </div>
    );
}

export default App;
