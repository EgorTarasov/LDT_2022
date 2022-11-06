import axios from "axios";

function useFetch() {
  axios
    .get("/places/all", {
      params: {
        offset: 0,
        count: 1000,
      },
    })
    .catch((error) => {
      console.log("error " + error);
      console.log(error.request);
    })
    .then((response) => {});
}

export default useFetch;
