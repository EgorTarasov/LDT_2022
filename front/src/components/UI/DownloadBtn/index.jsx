import { DownloadOutlined } from "@ant-design/icons";
import html2canvas from "html2canvas";
import { Button } from "antd";

function DownloadBtn(props) {
  function handleClick(params) {
    html2canvas(document.body).then((canvas) => {
      var a = document.createElement("a");
      a.href = canvas
        .toDataURL("...assets/image/jpeg")
        .replace("image/jpeg", "image/octet-stream");
      a.download = "Postmats.jpg";
      a.click();
    });
  }

  return (
    <Button
      type="primary"
      icon={<DownloadOutlined />}
      size={"large"}
      onClick={handleClick}
    />
  );
}

export default DownloadBtn;
