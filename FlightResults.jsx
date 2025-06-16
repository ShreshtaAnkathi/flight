import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'

function FlightResults() {
  const { state } = useLocation()
  const [flights, setFlights] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/api/flights', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from_: state.from,
        to: state.to,
        date: state.date,
        sortBy: state.sortBy,
        seats: state.seats
      })
    })
      .then(res => res.json())
      .then(data => setFlights(data.flights))
  }, [state])

  return (
    <div className="results-container">
      <h2>Available Flights</h2>
      {flights.length === 0 ? <p>No flights found</p> : (
        <ul>
          {flights.map((flight, idx) => (
            <li key={idx}>
              <strong>{flight.name}</strong> | {flight.class} | {flight.time} | ₹{flight.rate}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default FlightResults
