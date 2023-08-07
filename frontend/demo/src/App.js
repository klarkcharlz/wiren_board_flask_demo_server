import './App.css';
import axios from "axios";
import React, {useState, useEffect} from "react";


function App() {
    const DATA_URL = 'http://127.0.0.1:5005';

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


    return (
        <div className="App">
            <button
                onClick={(e) => {
                    e.preventDefault();
                    getData();
                }}
                type='button'>
                Get Data
            </button>
            <div>
                <ul style={{border: '2px solid black'}}>
                    {Object.keys(data).map((key, index) => {
                        return (
                            <li key={index}>
                                {`${key}: ${data[key]}`}
                            </li>
                        );
                    })}
                </ul>
            </div>
        </div>
    );
}

export default App;
