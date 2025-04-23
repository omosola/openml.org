import React from "react";
import { Helmet } from "react-helmet-async";
import { Typography } from "@mui/material";
import DashboardLayout from "../../layouts/Dashboard";

// Server-side translation
import { serverSideTranslations } from "next-i18next/serverSideTranslations";
export async function getStaticProps({ locale }) {
  return {
    props: {
      // pass the translation props to the page component
      ...(await serverSideTranslations(locale)),
    },
  };
}

function TaskList() {
  return (
    <React.Fragment>
      <Helmet title="OpenML Tasks" />
      <Typography variant="h3" gutterBottom>
        Task overview
      </Typography>
    </React.Fragment>
  );
}

TaskList.getLayout = function getLayout(page) {
  return <DashboardLayout>{page}</DashboardLayout>;
};

export default TaskList;
