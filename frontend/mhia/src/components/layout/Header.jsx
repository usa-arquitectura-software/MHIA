import { useNavigate } from "react-router-dom";

function Header() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/LogIn"); 
  };

  return (
    <>
      <header>
        <button onClick={handleClick}>Log IN</button>
        <button onClick={handleClick}>Sing up</button>
      </header>
    </>
  );
}

export default Header;
