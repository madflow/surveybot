import "survey-core/modern.min.css";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
const surveyJson = {
  elements: [
    {
      name: "Color",
      title: "Enter your favorite color:",
      type: "text",
      inputType: "color",
      isRequired: true,
    },
  ],
};

export default function Color() {
  const survey = new Model(surveyJson);
  return (
    <>
      <h1>Color</h1>
      <Survey model={survey} />
    </>
  );
}
