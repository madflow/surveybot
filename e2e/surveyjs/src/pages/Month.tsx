import "survey-core/modern.min.css";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
const surveyJson = {
  elements: [
    {
      name: "Month",
      title: "Enter your birth month:",
      type: "text",
      inputType: "month",
      isRequired: true,
    },
  ],
};

export default function Month() {
  const survey = new Model(surveyJson);
  return (
    <>
      <h1>Month</h1>
      <Survey model={survey} />
    </>
  );
}
