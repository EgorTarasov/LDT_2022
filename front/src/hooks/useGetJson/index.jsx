import { useEffect } from "react";
import { useSelector } from "react-redux";
import useGetParams from "../useGetParams";

const useGetJson = () => {
  const dots = useSelector((state) => state.dots.dots);
  const params = useGetParams();

  useEffect(() => {}, [params]);
  return dots;
};
export default useGetJson;
