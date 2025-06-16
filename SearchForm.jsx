import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function SearchForm() {
  const [form, setForm] = useState({ from: '', to: '', date: '',  seats: 1 })
  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault()
    navigate('/results', { state: form })
  }

  return (
    <div className="form-container">
      <h2>Find Cheapest Flights</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="From" required onChange={e => setForm({ ...form, from: e.target.value })} />
        <input type="text" placeholder="To" required onChange={e => setForm({ ...form, to: e.target.value })} />
        <input type="date" required onChange={e => setForm({ ...form, date: e.target.value })} />
        {/* <input type="number" min="1" placeholder="Seats" onChange={e => setForm({ ...form, seats: Number(e.target.value) })} /> */}
        {/* <select onChange={e => setForm({ ...form, sortBy: e.target.value })}> */}
          {/* <option value="">Sort By</option>
          <option value="ratings">Rate</option>
          <option value="class">Class</option>
          <option value="seats">Seats</option> */}
        {/* </select> */}
        <button type="submit">Search Flights</button>
      </form>
    </div>
  )
}

export default SearchForm


// import { useState } from 'react'
// import { useNavigate } from 'react-router-dom'
// import './SearchForm.css'

// function SearchForm({ sortBy }) {
//   const navigate = useNavigate()
//   const [form, setForm] = useState({
//     from: '',
//     to: '',
//     date: ''
//   })

//   const handleChange = (e) => {
//     setForm({ ...form, [e.target.name]: e.target.value })
//   }

//   const handleSubmit = async (e) => {
//     e.preventDefault()

//     if (!form.from || !form.to || !form.date) {
//       alert('Please fill all fields.')
//       return
//     }

   
//     navigate('/results', {
//       state: { ...form, sortBy }
//     })
//   }

//   return (
//     <div className="form-container">
//       <h2>Search Flights</h2>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           name="from"
//           placeholder="From"
//           value={form.from}
//           onChange={handleChange}
//           required
//         />

//         <input
//           type="text"
//           name="to"
//           placeholder="To"
//           value={form.to}
//           onChange={handleChange}
//           required
//         />

//         <input
//           type="date"
//           name="date"
//           value={form.date}
//           onChange={handleChange}
//           required
//         />

//         <button type="submit">Search Flights</button>
//       </form>
//     </div>
//   )
// }

// export default SearchForm
