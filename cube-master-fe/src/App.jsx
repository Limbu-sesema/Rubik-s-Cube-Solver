import React, { useRef } from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Solve from './components/Solve';
import Banner from './components/Banner';
import Nav from './components/Nav';
// import Faq from './components/Faq';


const App = () => {
  // const faqRef = useRef(null);
  const solveRef = useRef(null);

  // const scrollToFAQ = () => {
  //   faqRef.current?.scrollIntoView({ behavior: "smooth" });
  // };

  const scrollToSolve = () => {
    solveRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <Router>
      <div className="bg-black">

        <Nav
          onSolveClick={scrollToSolve}
        // onFAQClick={scrollToFAQ}
        />

        <Routes>

          <Route
            path="/"
            element={<Banner />}
          />

          <Route
            path="/solve"
            element={
              <div ref={solveRef} className="section">
                <Solve />
              </div>
            }
          />
        </Routes>

        {/* <div ref={faqRef} className="section">
          <Faq />
        </div> */}

      </div>
    </Router>
  );
};

export default App;
