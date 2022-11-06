import { useEffect, useState } from "react";

const useGetCoords = (props) => {
  const [data, setData] = useState(
    props.map((el) => {
      console.log("el " + el);
      return [el["long"], el["lat"]];
    })
  );

  useEffect(() => {
    setData(
      props.map((el) => {
        return [el["long"], el["lat"]];
      })
    );
  }, [props]);

  return data;
};
export default useGetCoords;
