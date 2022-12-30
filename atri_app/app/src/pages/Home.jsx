import { useLayoutEffect, useEffect } from "react";
import useStore, { updateStoreStateFromController } from "../hooks/useStore";
import useIoStore from "../hooks/useIoStore";
import { useNavigate, useLocation } from "react-router-dom";
import { subscribeInternalNavigation } from "../utils/navigate";
import {fetchPageProps} from "../utils/fetchPageProps"
import { Div } from "@atrilabs/react-component-manifests/src/manifests/Div/Div.tsx";
import { Flex } from "@atrilabs/react-component-manifests/src/manifests/Flex/Flex.tsx";
import { TextBox } from "@atrilabs/react-component-manifests/src/manifests/TextBox/TextBox.tsx";
import { Image } from "@atrilabs/react-component-manifests/src/manifests/Image/Image.tsx";
import { Link } from "@atrilabs/react-component-manifests/src/manifests/Link/Link.tsx";
import { Button } from "@atrilabs/react-component-manifests/src/manifests/Button/Button.tsx";
import { usenav_containerCb, usenav_bar_divCb, useside_navCb, usehero_mainCb, usehero_flexCb, useheading_paragraphCb, usehero_button_linkCb, usecall_button_divCb, usecompaniesCb, useservices_divCb, useservices_mainCb, usesevices_head_mainCb, usehead_2Cb, useservices_flexCb, usesub_service_1Cb, useservices_heading_1Cb, useservices_1_paragraph1Cb, useservices_list_1Cb, useservices_pointer_1Cb, useservices_list_item_1Cb, useFlex36Cb, uselist_pointer_head_3Cb, useFlex92Cb, useFlex91Cb, uselist_ponter_head_9acCb, useFlex90Cb, useDiv111Cb, uselist_pointer_head_7Cb, useDiv112Cb, useDiv113Cb, usesub_service_2Cb, useDiv118Cb, useDiv119Cb, useFlex96Cb, useDiv117Cb, uselist_pointer_head_4Cb, useFlex94Cb, useFlex95Cb, useprojects_head_paragraph_1Cb, useprojects_heading_1Cb, useheading_2_3_divCb, useview_projects_button_divCb, useprojects_slider_flexCb, useprojects_slider_3Cb, useproject_slider_3_paragraph_headCb, useslider_3_link_flexCb, useslider_item_2Cb, useslider_item_2_headCb, useslider_item_2_link_2Cb, useslider_item_1Cb, useslider_item1_head_flexCb, useFlex136Cb, useslider_button_leftCb, usesliderbutton_rightCb, useblogs_main_divCb, useblogs_main_flexCb, useblogs_heading_divCb, useblogs_view_all_link_flexCb, useblog_list_div_mainCb, uselist_item_1_flexCb, uselist_item_1_date_timeCb, useheading_date_time_flexCb, uselist_heading_2_divCb, uselist_item_1_read_link_flexCb, uselist_item_2_flexCb, uselist_item_2_link_flexCb, uselist_item_2_heading_divCb, useDiv166Cb, useFlex158Cb, uselist_item_3_flexCb, useDiv168Cb, usepoint_div_3Cb, uselist_3_heading_divCb, uselist_3_linkCb, uselist_item_4_flexCb, uselist_4_link_flexCb, uselist_4_heading_divCb, useDiv172Cb, useFlex164Cb, uselist_item_5_flexCb, useDiv174Cb, useFlex167Cb, usevlist_5_heading_divCb, uselist_5_link_flexCb, usepro_designer_mainCb, usedesigner_details_flexCb, usedesigner_deatails_divCb, usedesigner_about_paragraph_divCb, usedesigner_image_flexCb, usedesigner_2_image_flexCb, useexperience_main_divCb, useexperience_flexCb, useexperience_left_divCb, useexperience_heading_divCb, useexperience_listCb, useexperience_list_item_1Cb, uselist_item_1_heading_divCb, useexperience_list_item_1_year_1_flexCb, useexperience_list_item_2Cb, useexperience_list_item_2_year_2_flexCb, uselist_item__heading_divCb, useexperience_list_item_3Cb, useexperience_list_item__year_3_flexCb, uselist_item_3_heading_divCb, useexperience_right_divCb, useDiv200Cb, useexperience_right_list_item_3Cb, useright_list_item_3_heading_divCb, useexperience_right_ist_item_3_year_3_flexCb, useexperience_right_list_item_2Cb, useright_list_item_2_heading_divCb, useexperience_right_ist_item_2_year_2_flexCb, useexperience_right_list_item_1Cb, useexperience_right_ist_item_1_year_1_flexCb, useright_list_item_1_heading_divCb, useDiv201Cb, usetestimonials_mainCb, usetestimonials_headings_flexCb, usetestimonial_1_flexCb, usetestimonial_detailsCb, usedetail_divCb, usetestimonial_name_divCb, useleft_arrow_buttonCb, useright_arrow_divCb, usefaq_mainCb, usefaq_heading_divCb, usefaq_list_main_flexCb, usefaq_left_listCb, usefaq_list_item_1Cb, usefaq_list_heading_flex_1Cb, usefaq_list_item_4Cb, usefaq_list_item_2Cb, usefaq_list_item_3Cb, usefaq_right_listCb, usefaq_right_list_item_3Cb, usefaq_right_list_item_2Cb, usefaq_right_list_item_4Cb, usefaq_right_list_item_1Cb, usefaq_right_list_heading_flex_1Cb, usefooter_main_divCb, usefooter_headings_flexCb, usefooter_heading_divCb, usefooter_links_flexCb, usewebsite_details_divCb, usemail_flexCb, uselinks_gridCb, usecopyright_divCb, usewebflow_divCb, usetrust_headingCb, useprojects_view_button_backCb, uselogo_imgCb, usecall_linkCb, useabout_linkCb, useblog_linkCb, useproject_linkCb, useservices_linkCb, usenav_call_arrowCb, usetrusted_div_mainCb, usehero_imageCb, useheading_1Cb, useheading_2Cb, useheading_3Cb, useparagraphCb, usebutton_backgroundCb, useCV_linkCb, usecall_buttonCb, usecompany_1Cb, usecompany_2Cb, usecompany_3Cb, usecompany_4Cb, useprojects_mainCb, useservices_headingCb, useserices_paragraphCb, useservices_image_1Cb, uselist_heading_1Cb, uselist_paragraph_1Cb, useservices_bullet_point_1Cb, uselist_pointer_headingCb, uselist_pointer_head_2Cb, useDiv46Cb, usepointer_list_heading_3Cb, useDiv47Cb, useservices_image_3Cb, useDiv109Cb, uselist_pointer_heading_9Cb, useDiv110Cb, uselist_pointer_heading_8Cb, useTextBox78Cb, useDiv108Cb, uselist_paragraph_3Cb, uselist_heading_3Cb, useservices_image_2Cb, uselist_heading_2Cb, uselist_paragraph_2Cb, useDiv114Cb, uselist_pointer_heading_2Cb, uselist_pointer_head_5Cb, useDiv115Cb, uselist_pointer_heading_6Cb, useDiv116Cb, useprojects_head_1Cb, useprojects_heading_2Cb, useprojeccts_heading_3Cb, useview_projects_buttonCb, useslider_3_imageCb, useslider_3_head_1Cb, useslider_3_head_2Cb, useslider_3_flex_head_3Cb, useslider_3_head_imageCb, useslider_item_1_image_2Cb, useslider_item_2_head_2Cb, useslider_item_2_productCb, useImage44Cb, useTextBox116Cb, useslider_image_1Cb, useslider_item_1_head_2Cb, useslider_branding_headCb, usearrow_image_1Cb, useslider_view_link_1Cb, useblog_left_arrow_imageCb, useblogs_right_arrow_imageCb, useheading_blogsCb, uselatest_blogs_headingCb, useview_all_linkCb, usearrow_imageCb, useheading_timeCb, usepoint_div1Cb, useheading_dateCb, uselist_item_1_heading_2Cb, uselist_1_read_linkCb, uselist_link_arrow_imageCb, uselist_arrow_imageCb, uselist_2_linkCb, uselist_item_heading_2Cb, uselist_item_2_dateCb, usepoint_div_2Cb, uselist_item_2_timeCb, uselist_3_timeCb, usepoint_div3Cb, uselist_3_dateCb, uselist_3_headingCb, uselist_3_link_3Cb, usearrow_image_3Cb, usearrow_image_4Cb, uselist_4_linkCb, uselist_4_headingCb, uselist_4_dateCb, usepoint_div_4Cb, uselist_4_timeCb, uselist_5_timeCb, usepoint_div_5Cb, uselist_5_date_Cb, uselist_5_headingCb, uselist_5_linkCb, usearrow_image_5Cb, usedesigner_heading_mainCb, usedesigner_about_heading_2Cb, usedesigner_about_paragraphCb, usedesigner_image_2Cb, usedesigner_image_1Cb, usedesigner_image_3Cb, usedesigner_image_4Cb, useeducation_headingCb, uselist_border_div_1Cb, useexperience_list_item_1_link_1Cb, useexperience_list_item_1_headingCb, uselist_item_1_dateCb, useup_right_arrow_1Cb, uselist_border_div_2Cb, useup_right_arrow_2Cb, uselist_item__dateCb, uselist_item_2_linkCb, useexperience_list_item_2_headingCb, uselist_border_div_3Cb, useup_right_arrow_3Cb, uselist_item_3_dateCb, useexperience_list_item_3_headingCb, useexperience_list_item_3_link_3Cb, uselist_border_div_6Cb, useright_list_item_3_image_3Cb, useexperience_right_list_item_3_link_3Cb, useexperience_right_list_item_3_headingCb, useright_list_item_3_dateCb, useup_right_arrow_6Cb, uselist_border_div_5Cb, useright_list_item_2_image_2Cb, useexperience_right_list_item_2_headingCb, useexperience_right_list_item_2_link_2Cb, useright_list_item_2_dateCb, useup_right_arrow_5Cb, uselist_border_div_4Cb, useright_list_item_1_image_1Cb, useup_right_arrow_4Cb, useright_list_item_1_dateCb, useexperience_right_list_item_1_headingCb, useexperience_right_list_item_1_link_1Cb, usework_experience_headingCb, usetestimonials_heading_1Cb, usetestimonials_heading_2Cb, usetestimonial_1_imageCb, usedouble_quotes_imageCb, usedetailCb, usetestimonial_nameCb, usetestimonial_designationCb, useleft_arrowCb, useright_arrowCb, usefaq_headingCb, usefaq_heading_2Cb, uselist_question_1Cb, uselist_down_arrow_1Cb, uselist_down_arrow_4Cb, uselist_question_4Cb, uselist_down_arrow_2Cb, uselist_question_2Cb, uselist_down_arrow_3Cb, uselist_question_3Cb, useright_list_question_3Cb, useright_list_down_arrow_3Cb, useright_list_question_2Cb, uselist_down_arrow_6Cb, useright_list_question_4Cb, useright_list_down_arrow_4Cb, uselist_down_arrow_5Cb, useright_list_question_1Cb, usefooter_heading_1Cb, usefooter_heading_2Cb, uselogo_link_imageCb, useaddress_textCb, usemail_icon_imageCb, usemail_linkCb, usefooter_link_9Cb, usefooter_link_1Cb, usefooter_link_2Cb, usefooter_link_7Cb, usefooter_link_6Cb, usefooter_link_3Cb, usefooter_link_5Cb, usefooter_link_4Cb, usefooter_link_8Cb, userights_textCb, useConversionflow_linkCb, usepowered_rextCb, useWebflow_linkCb, useimage_text_linkCb, useinstructions_linkCb, useChangelog_linkCb, uselast_linkCb, usewebflow_logoCb, usewebflow_text_imageCb } from "../page-cbs/Home";
import "../page-css/Home.css";
import "../custom/Home";

export default function Home() {
  const navigate = useNavigate();
  useEffect(() => {
    const unsub = subscribeInternalNavigation((url) => {
      navigate(url);
    });
    return unsub;
  }, [navigate]);

  const location = useLocation();
  useLayoutEffect(()=>{
    fetchPageProps(location.pathname, location.search).then((res)=>{
      updateStoreStateFromController(res.pageName, res.pageState)
    })
  }, [location])

  const nav_containerProps = useStore((state)=>state["Home"]["nav_container"]);
const nav_containerIoProps = useIoStore((state)=>state["Home"]["nav_container"]);
const nav_containerCb = usenav_containerCb()
const nav_bar_divProps = useStore((state)=>state["Home"]["nav_bar_div"]);
const nav_bar_divIoProps = useIoStore((state)=>state["Home"]["nav_bar_div"]);
const nav_bar_divCb = usenav_bar_divCb()
const side_navProps = useStore((state)=>state["Home"]["side_nav"]);
const side_navIoProps = useIoStore((state)=>state["Home"]["side_nav"]);
const side_navCb = useside_navCb()
const hero_mainProps = useStore((state)=>state["Home"]["hero_main"]);
const hero_mainIoProps = useIoStore((state)=>state["Home"]["hero_main"]);
const hero_mainCb = usehero_mainCb()
const hero_flexProps = useStore((state)=>state["Home"]["hero_flex"]);
const hero_flexIoProps = useIoStore((state)=>state["Home"]["hero_flex"]);
const hero_flexCb = usehero_flexCb()
const heading_paragraphProps = useStore((state)=>state["Home"]["heading_paragraph"]);
const heading_paragraphIoProps = useIoStore((state)=>state["Home"]["heading_paragraph"]);
const heading_paragraphCb = useheading_paragraphCb()
const hero_button_linkProps = useStore((state)=>state["Home"]["hero_button_link"]);
const hero_button_linkIoProps = useIoStore((state)=>state["Home"]["hero_button_link"]);
const hero_button_linkCb = usehero_button_linkCb()
const call_button_divProps = useStore((state)=>state["Home"]["call_button_div"]);
const call_button_divIoProps = useIoStore((state)=>state["Home"]["call_button_div"]);
const call_button_divCb = usecall_button_divCb()
const companiesProps = useStore((state)=>state["Home"]["companies"]);
const companiesIoProps = useIoStore((state)=>state["Home"]["companies"]);
const companiesCb = usecompaniesCb()
const services_divProps = useStore((state)=>state["Home"]["services_div"]);
const services_divIoProps = useIoStore((state)=>state["Home"]["services_div"]);
const services_divCb = useservices_divCb()
const services_mainProps = useStore((state)=>state["Home"]["services_main"]);
const services_mainIoProps = useIoStore((state)=>state["Home"]["services_main"]);
const services_mainCb = useservices_mainCb()
const sevices_head_mainProps = useStore((state)=>state["Home"]["sevices_head_main"]);
const sevices_head_mainIoProps = useIoStore((state)=>state["Home"]["sevices_head_main"]);
const sevices_head_mainCb = usesevices_head_mainCb()
const head_2Props = useStore((state)=>state["Home"]["head_2"]);
const head_2IoProps = useIoStore((state)=>state["Home"]["head_2"]);
const head_2Cb = usehead_2Cb()
const services_flexProps = useStore((state)=>state["Home"]["services_flex"]);
const services_flexIoProps = useIoStore((state)=>state["Home"]["services_flex"]);
const services_flexCb = useservices_flexCb()
const sub_service_1Props = useStore((state)=>state["Home"]["sub_service_1"]);
const sub_service_1IoProps = useIoStore((state)=>state["Home"]["sub_service_1"]);
const sub_service_1Cb = usesub_service_1Cb()
const services_heading_1Props = useStore((state)=>state["Home"]["services_heading_1"]);
const services_heading_1IoProps = useIoStore((state)=>state["Home"]["services_heading_1"]);
const services_heading_1Cb = useservices_heading_1Cb()
const services_1_paragraph1Props = useStore((state)=>state["Home"]["services_1_paragraph1"]);
const services_1_paragraph1IoProps = useIoStore((state)=>state["Home"]["services_1_paragraph1"]);
const services_1_paragraph1Cb = useservices_1_paragraph1Cb()
const services_list_1Props = useStore((state)=>state["Home"]["services_list_1"]);
const services_list_1IoProps = useIoStore((state)=>state["Home"]["services_list_1"]);
const services_list_1Cb = useservices_list_1Cb()
const services_pointer_1Props = useStore((state)=>state["Home"]["services_pointer_1"]);
const services_pointer_1IoProps = useIoStore((state)=>state["Home"]["services_pointer_1"]);
const services_pointer_1Cb = useservices_pointer_1Cb()
const services_list_item_1Props = useStore((state)=>state["Home"]["services_list_item_1"]);
const services_list_item_1IoProps = useIoStore((state)=>state["Home"]["services_list_item_1"]);
const services_list_item_1Cb = useservices_list_item_1Cb()
const Flex36Props = useStore((state)=>state["Home"]["Flex36"]);
const Flex36IoProps = useIoStore((state)=>state["Home"]["Flex36"]);
const Flex36Cb = useFlex36Cb()
const list_pointer_head_3Props = useStore((state)=>state["Home"]["list_pointer_head_3"]);
const list_pointer_head_3IoProps = useIoStore((state)=>state["Home"]["list_pointer_head_3"]);
const list_pointer_head_3Cb = uselist_pointer_head_3Cb()
const Flex92Props = useStore((state)=>state["Home"]["Flex92"]);
const Flex92IoProps = useIoStore((state)=>state["Home"]["Flex92"]);
const Flex92Cb = useFlex92Cb()
const Flex91Props = useStore((state)=>state["Home"]["Flex91"]);
const Flex91IoProps = useIoStore((state)=>state["Home"]["Flex91"]);
const Flex91Cb = useFlex91Cb()
const list_ponter_head_9acProps = useStore((state)=>state["Home"]["list_ponter_head_9ac"]);
const list_ponter_head_9acIoProps = useIoStore((state)=>state["Home"]["list_ponter_head_9ac"]);
const list_ponter_head_9acCb = uselist_ponter_head_9acCb()
const Flex90Props = useStore((state)=>state["Home"]["Flex90"]);
const Flex90IoProps = useIoStore((state)=>state["Home"]["Flex90"]);
const Flex90Cb = useFlex90Cb()
const Div111Props = useStore((state)=>state["Home"]["Div111"]);
const Div111IoProps = useIoStore((state)=>state["Home"]["Div111"]);
const Div111Cb = useDiv111Cb()
const list_pointer_head_7Props = useStore((state)=>state["Home"]["list_pointer_head_7"]);
const list_pointer_head_7IoProps = useIoStore((state)=>state["Home"]["list_pointer_head_7"]);
const list_pointer_head_7Cb = uselist_pointer_head_7Cb()
const Div112Props = useStore((state)=>state["Home"]["Div112"]);
const Div112IoProps = useIoStore((state)=>state["Home"]["Div112"]);
const Div112Cb = useDiv112Cb()
const Div113Props = useStore((state)=>state["Home"]["Div113"]);
const Div113IoProps = useIoStore((state)=>state["Home"]["Div113"]);
const Div113Cb = useDiv113Cb()
const sub_service_2Props = useStore((state)=>state["Home"]["sub_service_2"]);
const sub_service_2IoProps = useIoStore((state)=>state["Home"]["sub_service_2"]);
const sub_service_2Cb = usesub_service_2Cb()
const Div118Props = useStore((state)=>state["Home"]["Div118"]);
const Div118IoProps = useIoStore((state)=>state["Home"]["Div118"]);
const Div118Cb = useDiv118Cb()
const Div119Props = useStore((state)=>state["Home"]["Div119"]);
const Div119IoProps = useIoStore((state)=>state["Home"]["Div119"]);
const Div119Cb = useDiv119Cb()
const Flex96Props = useStore((state)=>state["Home"]["Flex96"]);
const Flex96IoProps = useIoStore((state)=>state["Home"]["Flex96"]);
const Flex96Cb = useFlex96Cb()
const Div117Props = useStore((state)=>state["Home"]["Div117"]);
const Div117IoProps = useIoStore((state)=>state["Home"]["Div117"]);
const Div117Cb = useDiv117Cb()
const list_pointer_head_4Props = useStore((state)=>state["Home"]["list_pointer_head_4"]);
const list_pointer_head_4IoProps = useIoStore((state)=>state["Home"]["list_pointer_head_4"]);
const list_pointer_head_4Cb = uselist_pointer_head_4Cb()
const Flex94Props = useStore((state)=>state["Home"]["Flex94"]);
const Flex94IoProps = useIoStore((state)=>state["Home"]["Flex94"]);
const Flex94Cb = useFlex94Cb()
const Flex95Props = useStore((state)=>state["Home"]["Flex95"]);
const Flex95IoProps = useIoStore((state)=>state["Home"]["Flex95"]);
const Flex95Cb = useFlex95Cb()
const projects_head_paragraph_1Props = useStore((state)=>state["Home"]["projects_head_paragraph_1"]);
const projects_head_paragraph_1IoProps = useIoStore((state)=>state["Home"]["projects_head_paragraph_1"]);
const projects_head_paragraph_1Cb = useprojects_head_paragraph_1Cb()
const projects_heading_1Props = useStore((state)=>state["Home"]["projects_heading_1"]);
const projects_heading_1IoProps = useIoStore((state)=>state["Home"]["projects_heading_1"]);
const projects_heading_1Cb = useprojects_heading_1Cb()
const heading_2_3_divProps = useStore((state)=>state["Home"]["heading_2_3_div"]);
const heading_2_3_divIoProps = useIoStore((state)=>state["Home"]["heading_2_3_div"]);
const heading_2_3_divCb = useheading_2_3_divCb()
const view_projects_button_divProps = useStore((state)=>state["Home"]["view_projects_button_div"]);
const view_projects_button_divIoProps = useIoStore((state)=>state["Home"]["view_projects_button_div"]);
const view_projects_button_divCb = useview_projects_button_divCb()
const projects_slider_flexProps = useStore((state)=>state["Home"]["projects_slider_flex"]);
const projects_slider_flexIoProps = useIoStore((state)=>state["Home"]["projects_slider_flex"]);
const projects_slider_flexCb = useprojects_slider_flexCb()
const projects_slider_3Props = useStore((state)=>state["Home"]["projects_slider_3"]);
const projects_slider_3IoProps = useIoStore((state)=>state["Home"]["projects_slider_3"]);
const projects_slider_3Cb = useprojects_slider_3Cb()
const project_slider_3_paragraph_headProps = useStore((state)=>state["Home"]["project_slider_3_paragraph_head"]);
const project_slider_3_paragraph_headIoProps = useIoStore((state)=>state["Home"]["project_slider_3_paragraph_head"]);
const project_slider_3_paragraph_headCb = useproject_slider_3_paragraph_headCb()
const slider_3_link_flexProps = useStore((state)=>state["Home"]["slider_3_link_flex"]);
const slider_3_link_flexIoProps = useIoStore((state)=>state["Home"]["slider_3_link_flex"]);
const slider_3_link_flexCb = useslider_3_link_flexCb()
const slider_item_2Props = useStore((state)=>state["Home"]["slider_item_2"]);
const slider_item_2IoProps = useIoStore((state)=>state["Home"]["slider_item_2"]);
const slider_item_2Cb = useslider_item_2Cb()
const slider_item_2_headProps = useStore((state)=>state["Home"]["slider_item_2_head"]);
const slider_item_2_headIoProps = useIoStore((state)=>state["Home"]["slider_item_2_head"]);
const slider_item_2_headCb = useslider_item_2_headCb()
const slider_item_2_link_2Props = useStore((state)=>state["Home"]["slider_item_2_link_2"]);
const slider_item_2_link_2IoProps = useIoStore((state)=>state["Home"]["slider_item_2_link_2"]);
const slider_item_2_link_2Cb = useslider_item_2_link_2Cb()
const slider_item_1Props = useStore((state)=>state["Home"]["slider_item_1"]);
const slider_item_1IoProps = useIoStore((state)=>state["Home"]["slider_item_1"]);
const slider_item_1Cb = useslider_item_1Cb()
const slider_item1_head_flexProps = useStore((state)=>state["Home"]["slider_item1_head_flex"]);
const slider_item1_head_flexIoProps = useIoStore((state)=>state["Home"]["slider_item1_head_flex"]);
const slider_item1_head_flexCb = useslider_item1_head_flexCb()
const Flex136Props = useStore((state)=>state["Home"]["Flex136"]);
const Flex136IoProps = useIoStore((state)=>state["Home"]["Flex136"]);
const Flex136Cb = useFlex136Cb()
const slider_button_leftProps = useStore((state)=>state["Home"]["slider_button_left"]);
const slider_button_leftIoProps = useIoStore((state)=>state["Home"]["slider_button_left"]);
const slider_button_leftCb = useslider_button_leftCb()
const sliderbutton_rightProps = useStore((state)=>state["Home"]["sliderbutton_right"]);
const sliderbutton_rightIoProps = useIoStore((state)=>state["Home"]["sliderbutton_right"]);
const sliderbutton_rightCb = usesliderbutton_rightCb()
const blogs_main_divProps = useStore((state)=>state["Home"]["blogs_main_div"]);
const blogs_main_divIoProps = useIoStore((state)=>state["Home"]["blogs_main_div"]);
const blogs_main_divCb = useblogs_main_divCb()
const blogs_main_flexProps = useStore((state)=>state["Home"]["blogs_main_flex"]);
const blogs_main_flexIoProps = useIoStore((state)=>state["Home"]["blogs_main_flex"]);
const blogs_main_flexCb = useblogs_main_flexCb()
const blogs_heading_divProps = useStore((state)=>state["Home"]["blogs_heading_div"]);
const blogs_heading_divIoProps = useIoStore((state)=>state["Home"]["blogs_heading_div"]);
const blogs_heading_divCb = useblogs_heading_divCb()
const blogs_view_all_link_flexProps = useStore((state)=>state["Home"]["blogs_view_all_link_flex"]);
const blogs_view_all_link_flexIoProps = useIoStore((state)=>state["Home"]["blogs_view_all_link_flex"]);
const blogs_view_all_link_flexCb = useblogs_view_all_link_flexCb()
const blog_list_div_mainProps = useStore((state)=>state["Home"]["blog_list_div_main"]);
const blog_list_div_mainIoProps = useIoStore((state)=>state["Home"]["blog_list_div_main"]);
const blog_list_div_mainCb = useblog_list_div_mainCb()
const list_item_1_flexProps = useStore((state)=>state["Home"]["list_item_1_flex"]);
const list_item_1_flexIoProps = useIoStore((state)=>state["Home"]["list_item_1_flex"]);
const list_item_1_flexCb = uselist_item_1_flexCb()
const list_item_1_date_timeProps = useStore((state)=>state["Home"]["list_item_1_date_time"]);
const list_item_1_date_timeIoProps = useIoStore((state)=>state["Home"]["list_item_1_date_time"]);
const list_item_1_date_timeCb = uselist_item_1_date_timeCb()
const heading_date_time_flexProps = useStore((state)=>state["Home"]["heading_date_time_flex"]);
const heading_date_time_flexIoProps = useIoStore((state)=>state["Home"]["heading_date_time_flex"]);
const heading_date_time_flexCb = useheading_date_time_flexCb()
const list_heading_2_divProps = useStore((state)=>state["Home"]["list_heading_2_div"]);
const list_heading_2_divIoProps = useIoStore((state)=>state["Home"]["list_heading_2_div"]);
const list_heading_2_divCb = uselist_heading_2_divCb()
const list_item_1_read_link_flexProps = useStore((state)=>state["Home"]["list_item_1_read_link_flex"]);
const list_item_1_read_link_flexIoProps = useIoStore((state)=>state["Home"]["list_item_1_read_link_flex"]);
const list_item_1_read_link_flexCb = uselist_item_1_read_link_flexCb()
const list_item_2_flexProps = useStore((state)=>state["Home"]["list_item_2_flex"]);
const list_item_2_flexIoProps = useIoStore((state)=>state["Home"]["list_item_2_flex"]);
const list_item_2_flexCb = uselist_item_2_flexCb()
const list_item_2_link_flexProps = useStore((state)=>state["Home"]["list_item_2_link_flex"]);
const list_item_2_link_flexIoProps = useIoStore((state)=>state["Home"]["list_item_2_link_flex"]);
const list_item_2_link_flexCb = uselist_item_2_link_flexCb()
const list_item_2_heading_divProps = useStore((state)=>state["Home"]["list_item_2_heading_div"]);
const list_item_2_heading_divIoProps = useIoStore((state)=>state["Home"]["list_item_2_heading_div"]);
const list_item_2_heading_divCb = uselist_item_2_heading_divCb()
const Div166Props = useStore((state)=>state["Home"]["Div166"]);
const Div166IoProps = useIoStore((state)=>state["Home"]["Div166"]);
const Div166Cb = useDiv166Cb()
const Flex158Props = useStore((state)=>state["Home"]["Flex158"]);
const Flex158IoProps = useIoStore((state)=>state["Home"]["Flex158"]);
const Flex158Cb = useFlex158Cb()
const list_item_3_flexProps = useStore((state)=>state["Home"]["list_item_3_flex"]);
const list_item_3_flexIoProps = useIoStore((state)=>state["Home"]["list_item_3_flex"]);
const list_item_3_flexCb = uselist_item_3_flexCb()
const Div168Props = useStore((state)=>state["Home"]["Div168"]);
const Div168IoProps = useIoStore((state)=>state["Home"]["Div168"]);
const Div168Cb = useDiv168Cb()
const point_div_3Props = useStore((state)=>state["Home"]["point_div_3"]);
const point_div_3IoProps = useIoStore((state)=>state["Home"]["point_div_3"]);
const point_div_3Cb = usepoint_div_3Cb()
const list_3_heading_divProps = useStore((state)=>state["Home"]["list_3_heading_div"]);
const list_3_heading_divIoProps = useIoStore((state)=>state["Home"]["list_3_heading_div"]);
const list_3_heading_divCb = uselist_3_heading_divCb()
const list_3_linkProps = useStore((state)=>state["Home"]["list_3_link"]);
const list_3_linkIoProps = useIoStore((state)=>state["Home"]["list_3_link"]);
const list_3_linkCb = uselist_3_linkCb()
const list_item_4_flexProps = useStore((state)=>state["Home"]["list_item_4_flex"]);
const list_item_4_flexIoProps = useIoStore((state)=>state["Home"]["list_item_4_flex"]);
const list_item_4_flexCb = uselist_item_4_flexCb()
const list_4_link_flexProps = useStore((state)=>state["Home"]["list_4_link_flex"]);
const list_4_link_flexIoProps = useIoStore((state)=>state["Home"]["list_4_link_flex"]);
const list_4_link_flexCb = uselist_4_link_flexCb()
const list_4_heading_divProps = useStore((state)=>state["Home"]["list_4_heading_div"]);
const list_4_heading_divIoProps = useIoStore((state)=>state["Home"]["list_4_heading_div"]);
const list_4_heading_divCb = uselist_4_heading_divCb()
const Div172Props = useStore((state)=>state["Home"]["Div172"]);
const Div172IoProps = useIoStore((state)=>state["Home"]["Div172"]);
const Div172Cb = useDiv172Cb()
const Flex164Props = useStore((state)=>state["Home"]["Flex164"]);
const Flex164IoProps = useIoStore((state)=>state["Home"]["Flex164"]);
const Flex164Cb = useFlex164Cb()
const list_item_5_flexProps = useStore((state)=>state["Home"]["list_item_5_flex"]);
const list_item_5_flexIoProps = useIoStore((state)=>state["Home"]["list_item_5_flex"]);
const list_item_5_flexCb = uselist_item_5_flexCb()
const Div174Props = useStore((state)=>state["Home"]["Div174"]);
const Div174IoProps = useIoStore((state)=>state["Home"]["Div174"]);
const Div174Cb = useDiv174Cb()
const Flex167Props = useStore((state)=>state["Home"]["Flex167"]);
const Flex167IoProps = useIoStore((state)=>state["Home"]["Flex167"]);
const Flex167Cb = useFlex167Cb()
const vlist_5_heading_divProps = useStore((state)=>state["Home"]["vlist_5_heading_div"]);
const vlist_5_heading_divIoProps = useIoStore((state)=>state["Home"]["vlist_5_heading_div"]);
const vlist_5_heading_divCb = usevlist_5_heading_divCb()
const list_5_link_flexProps = useStore((state)=>state["Home"]["list_5_link_flex"]);
const list_5_link_flexIoProps = useIoStore((state)=>state["Home"]["list_5_link_flex"]);
const list_5_link_flexCb = uselist_5_link_flexCb()
const pro_designer_mainProps = useStore((state)=>state["Home"]["pro_designer_main"]);
const pro_designer_mainIoProps = useIoStore((state)=>state["Home"]["pro_designer_main"]);
const pro_designer_mainCb = usepro_designer_mainCb()
const designer_details_flexProps = useStore((state)=>state["Home"]["designer_details_flex"]);
const designer_details_flexIoProps = useIoStore((state)=>state["Home"]["designer_details_flex"]);
const designer_details_flexCb = usedesigner_details_flexCb()
const designer_deatails_divProps = useStore((state)=>state["Home"]["designer_deatails_div"]);
const designer_deatails_divIoProps = useIoStore((state)=>state["Home"]["designer_deatails_div"]);
const designer_deatails_divCb = usedesigner_deatails_divCb()
const designer_about_paragraph_divProps = useStore((state)=>state["Home"]["designer_about_paragraph_div"]);
const designer_about_paragraph_divIoProps = useIoStore((state)=>state["Home"]["designer_about_paragraph_div"]);
const designer_about_paragraph_divCb = usedesigner_about_paragraph_divCb()
const designer_image_flexProps = useStore((state)=>state["Home"]["designer_image_flex"]);
const designer_image_flexIoProps = useIoStore((state)=>state["Home"]["designer_image_flex"]);
const designer_image_flexCb = usedesigner_image_flexCb()
const designer_2_image_flexProps = useStore((state)=>state["Home"]["designer_2_image_flex"]);
const designer_2_image_flexIoProps = useIoStore((state)=>state["Home"]["designer_2_image_flex"]);
const designer_2_image_flexCb = usedesigner_2_image_flexCb()
const experience_main_divProps = useStore((state)=>state["Home"]["experience_main_div"]);
const experience_main_divIoProps = useIoStore((state)=>state["Home"]["experience_main_div"]);
const experience_main_divCb = useexperience_main_divCb()
const experience_flexProps = useStore((state)=>state["Home"]["experience_flex"]);
const experience_flexIoProps = useIoStore((state)=>state["Home"]["experience_flex"]);
const experience_flexCb = useexperience_flexCb()
const experience_left_divProps = useStore((state)=>state["Home"]["experience_left_div"]);
const experience_left_divIoProps = useIoStore((state)=>state["Home"]["experience_left_div"]);
const experience_left_divCb = useexperience_left_divCb()
const experience_heading_divProps = useStore((state)=>state["Home"]["experience_heading_div"]);
const experience_heading_divIoProps = useIoStore((state)=>state["Home"]["experience_heading_div"]);
const experience_heading_divCb = useexperience_heading_divCb()
const experience_listProps = useStore((state)=>state["Home"]["experience_list"]);
const experience_listIoProps = useIoStore((state)=>state["Home"]["experience_list"]);
const experience_listCb = useexperience_listCb()
const experience_list_item_1Props = useStore((state)=>state["Home"]["experience_list_item_1"]);
const experience_list_item_1IoProps = useIoStore((state)=>state["Home"]["experience_list_item_1"]);
const experience_list_item_1Cb = useexperience_list_item_1Cb()
const list_item_1_heading_divProps = useStore((state)=>state["Home"]["list_item_1_heading_div"]);
const list_item_1_heading_divIoProps = useIoStore((state)=>state["Home"]["list_item_1_heading_div"]);
const list_item_1_heading_divCb = uselist_item_1_heading_divCb()
const experience_list_item_1_year_1_flexProps = useStore((state)=>state["Home"]["experience_list_item_1_year_1_flex"]);
const experience_list_item_1_year_1_flexIoProps = useIoStore((state)=>state["Home"]["experience_list_item_1_year_1_flex"]);
const experience_list_item_1_year_1_flexCb = useexperience_list_item_1_year_1_flexCb()
const experience_list_item_2Props = useStore((state)=>state["Home"]["experience_list_item_2"]);
const experience_list_item_2IoProps = useIoStore((state)=>state["Home"]["experience_list_item_2"]);
const experience_list_item_2Cb = useexperience_list_item_2Cb()
const experience_list_item_2_year_2_flexProps = useStore((state)=>state["Home"]["experience_list_item_2_year_2_flex"]);
const experience_list_item_2_year_2_flexIoProps = useIoStore((state)=>state["Home"]["experience_list_item_2_year_2_flex"]);
const experience_list_item_2_year_2_flexCb = useexperience_list_item_2_year_2_flexCb()
const list_item__heading_divProps = useStore((state)=>state["Home"]["list_item__heading_div"]);
const list_item__heading_divIoProps = useIoStore((state)=>state["Home"]["list_item__heading_div"]);
const list_item__heading_divCb = uselist_item__heading_divCb()
const experience_list_item_3Props = useStore((state)=>state["Home"]["experience_list_item_3"]);
const experience_list_item_3IoProps = useIoStore((state)=>state["Home"]["experience_list_item_3"]);
const experience_list_item_3Cb = useexperience_list_item_3Cb()
const experience_list_item__year_3_flexProps = useStore((state)=>state["Home"]["experience_list_item__year_3_flex"]);
const experience_list_item__year_3_flexIoProps = useIoStore((state)=>state["Home"]["experience_list_item__year_3_flex"]);
const experience_list_item__year_3_flexCb = useexperience_list_item__year_3_flexCb()
const list_item_3_heading_divProps = useStore((state)=>state["Home"]["list_item_3_heading_div"]);
const list_item_3_heading_divIoProps = useIoStore((state)=>state["Home"]["list_item_3_heading_div"]);
const list_item_3_heading_divCb = uselist_item_3_heading_divCb()
const experience_right_divProps = useStore((state)=>state["Home"]["experience_right_div"]);
const experience_right_divIoProps = useIoStore((state)=>state["Home"]["experience_right_div"]);
const experience_right_divCb = useexperience_right_divCb()
const Div200Props = useStore((state)=>state["Home"]["Div200"]);
const Div200IoProps = useIoStore((state)=>state["Home"]["Div200"]);
const Div200Cb = useDiv200Cb()
const experience_right_list_item_3Props = useStore((state)=>state["Home"]["experience_right_list_item_3"]);
const experience_right_list_item_3IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_3"]);
const experience_right_list_item_3Cb = useexperience_right_list_item_3Cb()
const right_list_item_3_heading_divProps = useStore((state)=>state["Home"]["right_list_item_3_heading_div"]);
const right_list_item_3_heading_divIoProps = useIoStore((state)=>state["Home"]["right_list_item_3_heading_div"]);
const right_list_item_3_heading_divCb = useright_list_item_3_heading_divCb()
const experience_right_ist_item_3_year_3_flexProps = useStore((state)=>state["Home"]["experience_right_ist_item_3_year_3_flex"]);
const experience_right_ist_item_3_year_3_flexIoProps = useIoStore((state)=>state["Home"]["experience_right_ist_item_3_year_3_flex"]);
const experience_right_ist_item_3_year_3_flexCb = useexperience_right_ist_item_3_year_3_flexCb()
const experience_right_list_item_2Props = useStore((state)=>state["Home"]["experience_right_list_item_2"]);
const experience_right_list_item_2IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_2"]);
const experience_right_list_item_2Cb = useexperience_right_list_item_2Cb()
const right_list_item_2_heading_divProps = useStore((state)=>state["Home"]["right_list_item_2_heading_div"]);
const right_list_item_2_heading_divIoProps = useIoStore((state)=>state["Home"]["right_list_item_2_heading_div"]);
const right_list_item_2_heading_divCb = useright_list_item_2_heading_divCb()
const experience_right_ist_item_2_year_2_flexProps = useStore((state)=>state["Home"]["experience_right_ist_item_2_year_2_flex"]);
const experience_right_ist_item_2_year_2_flexIoProps = useIoStore((state)=>state["Home"]["experience_right_ist_item_2_year_2_flex"]);
const experience_right_ist_item_2_year_2_flexCb = useexperience_right_ist_item_2_year_2_flexCb()
const experience_right_list_item_1Props = useStore((state)=>state["Home"]["experience_right_list_item_1"]);
const experience_right_list_item_1IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_1"]);
const experience_right_list_item_1Cb = useexperience_right_list_item_1Cb()
const experience_right_ist_item_1_year_1_flexProps = useStore((state)=>state["Home"]["experience_right_ist_item_1_year_1_flex"]);
const experience_right_ist_item_1_year_1_flexIoProps = useIoStore((state)=>state["Home"]["experience_right_ist_item_1_year_1_flex"]);
const experience_right_ist_item_1_year_1_flexCb = useexperience_right_ist_item_1_year_1_flexCb()
const right_list_item_1_heading_divProps = useStore((state)=>state["Home"]["right_list_item_1_heading_div"]);
const right_list_item_1_heading_divIoProps = useIoStore((state)=>state["Home"]["right_list_item_1_heading_div"]);
const right_list_item_1_heading_divCb = useright_list_item_1_heading_divCb()
const Div201Props = useStore((state)=>state["Home"]["Div201"]);
const Div201IoProps = useIoStore((state)=>state["Home"]["Div201"]);
const Div201Cb = useDiv201Cb()
const testimonials_mainProps = useStore((state)=>state["Home"]["testimonials_main"]);
const testimonials_mainIoProps = useIoStore((state)=>state["Home"]["testimonials_main"]);
const testimonials_mainCb = usetestimonials_mainCb()
const testimonials_headings_flexProps = useStore((state)=>state["Home"]["testimonials_headings_flex"]);
const testimonials_headings_flexIoProps = useIoStore((state)=>state["Home"]["testimonials_headings_flex"]);
const testimonials_headings_flexCb = usetestimonials_headings_flexCb()
const testimonial_1_flexProps = useStore((state)=>state["Home"]["testimonial_1_flex"]);
const testimonial_1_flexIoProps = useIoStore((state)=>state["Home"]["testimonial_1_flex"]);
const testimonial_1_flexCb = usetestimonial_1_flexCb()
const testimonial_detailsProps = useStore((state)=>state["Home"]["testimonial_details"]);
const testimonial_detailsIoProps = useIoStore((state)=>state["Home"]["testimonial_details"]);
const testimonial_detailsCb = usetestimonial_detailsCb()
const detail_divProps = useStore((state)=>state["Home"]["detail_div"]);
const detail_divIoProps = useIoStore((state)=>state["Home"]["detail_div"]);
const detail_divCb = usedetail_divCb()
const testimonial_name_divProps = useStore((state)=>state["Home"]["testimonial_name_div"]);
const testimonial_name_divIoProps = useIoStore((state)=>state["Home"]["testimonial_name_div"]);
const testimonial_name_divCb = usetestimonial_name_divCb()
const left_arrow_buttonProps = useStore((state)=>state["Home"]["left_arrow_button"]);
const left_arrow_buttonIoProps = useIoStore((state)=>state["Home"]["left_arrow_button"]);
const left_arrow_buttonCb = useleft_arrow_buttonCb()
const right_arrow_divProps = useStore((state)=>state["Home"]["right_arrow_div"]);
const right_arrow_divIoProps = useIoStore((state)=>state["Home"]["right_arrow_div"]);
const right_arrow_divCb = useright_arrow_divCb()
const faq_mainProps = useStore((state)=>state["Home"]["faq_main"]);
const faq_mainIoProps = useIoStore((state)=>state["Home"]["faq_main"]);
const faq_mainCb = usefaq_mainCb()
const faq_heading_divProps = useStore((state)=>state["Home"]["faq_heading_div"]);
const faq_heading_divIoProps = useIoStore((state)=>state["Home"]["faq_heading_div"]);
const faq_heading_divCb = usefaq_heading_divCb()
const faq_list_main_flexProps = useStore((state)=>state["Home"]["faq_list_main_flex"]);
const faq_list_main_flexIoProps = useIoStore((state)=>state["Home"]["faq_list_main_flex"]);
const faq_list_main_flexCb = usefaq_list_main_flexCb()
const faq_left_listProps = useStore((state)=>state["Home"]["faq_left_list"]);
const faq_left_listIoProps = useIoStore((state)=>state["Home"]["faq_left_list"]);
const faq_left_listCb = usefaq_left_listCb()
const faq_list_item_1Props = useStore((state)=>state["Home"]["faq_list_item_1"]);
const faq_list_item_1IoProps = useIoStore((state)=>state["Home"]["faq_list_item_1"]);
const faq_list_item_1Cb = usefaq_list_item_1Cb()
const faq_list_heading_flex_1Props = useStore((state)=>state["Home"]["faq_list_heading_flex_1"]);
const faq_list_heading_flex_1IoProps = useIoStore((state)=>state["Home"]["faq_list_heading_flex_1"]);
const faq_list_heading_flex_1Cb = usefaq_list_heading_flex_1Cb()
const faq_list_item_4Props = useStore((state)=>state["Home"]["faq_list_item_4"]);
const faq_list_item_4IoProps = useIoStore((state)=>state["Home"]["faq_list_item_4"]);
const faq_list_item_4Cb = usefaq_list_item_4Cb()
const faq_list_item_2Props = useStore((state)=>state["Home"]["faq_list_item_2"]);
const faq_list_item_2IoProps = useIoStore((state)=>state["Home"]["faq_list_item_2"]);
const faq_list_item_2Cb = usefaq_list_item_2Cb()
const faq_list_item_3Props = useStore((state)=>state["Home"]["faq_list_item_3"]);
const faq_list_item_3IoProps = useIoStore((state)=>state["Home"]["faq_list_item_3"]);
const faq_list_item_3Cb = usefaq_list_item_3Cb()
const faq_right_listProps = useStore((state)=>state["Home"]["faq_right_list"]);
const faq_right_listIoProps = useIoStore((state)=>state["Home"]["faq_right_list"]);
const faq_right_listCb = usefaq_right_listCb()
const faq_right_list_item_3Props = useStore((state)=>state["Home"]["faq_right_list_item_3"]);
const faq_right_list_item_3IoProps = useIoStore((state)=>state["Home"]["faq_right_list_item_3"]);
const faq_right_list_item_3Cb = usefaq_right_list_item_3Cb()
const faq_right_list_item_2Props = useStore((state)=>state["Home"]["faq_right_list_item_2"]);
const faq_right_list_item_2IoProps = useIoStore((state)=>state["Home"]["faq_right_list_item_2"]);
const faq_right_list_item_2Cb = usefaq_right_list_item_2Cb()
const faq_right_list_item_4Props = useStore((state)=>state["Home"]["faq_right_list_item_4"]);
const faq_right_list_item_4IoProps = useIoStore((state)=>state["Home"]["faq_right_list_item_4"]);
const faq_right_list_item_4Cb = usefaq_right_list_item_4Cb()
const faq_right_list_item_1Props = useStore((state)=>state["Home"]["faq_right_list_item_1"]);
const faq_right_list_item_1IoProps = useIoStore((state)=>state["Home"]["faq_right_list_item_1"]);
const faq_right_list_item_1Cb = usefaq_right_list_item_1Cb()
const faq_right_list_heading_flex_1Props = useStore((state)=>state["Home"]["faq_right_list_heading_flex_1"]);
const faq_right_list_heading_flex_1IoProps = useIoStore((state)=>state["Home"]["faq_right_list_heading_flex_1"]);
const faq_right_list_heading_flex_1Cb = usefaq_right_list_heading_flex_1Cb()
const footer_main_divProps = useStore((state)=>state["Home"]["footer_main_div"]);
const footer_main_divIoProps = useIoStore((state)=>state["Home"]["footer_main_div"]);
const footer_main_divCb = usefooter_main_divCb()
const footer_headings_flexProps = useStore((state)=>state["Home"]["footer_headings_flex"]);
const footer_headings_flexIoProps = useIoStore((state)=>state["Home"]["footer_headings_flex"]);
const footer_headings_flexCb = usefooter_headings_flexCb()
const footer_heading_divProps = useStore((state)=>state["Home"]["footer_heading_div"]);
const footer_heading_divIoProps = useIoStore((state)=>state["Home"]["footer_heading_div"]);
const footer_heading_divCb = usefooter_heading_divCb()
const footer_links_flexProps = useStore((state)=>state["Home"]["footer_links_flex"]);
const footer_links_flexIoProps = useIoStore((state)=>state["Home"]["footer_links_flex"]);
const footer_links_flexCb = usefooter_links_flexCb()
const website_details_divProps = useStore((state)=>state["Home"]["website_details_div"]);
const website_details_divIoProps = useIoStore((state)=>state["Home"]["website_details_div"]);
const website_details_divCb = usewebsite_details_divCb()
const mail_flexProps = useStore((state)=>state["Home"]["mail_flex"]);
const mail_flexIoProps = useIoStore((state)=>state["Home"]["mail_flex"]);
const mail_flexCb = usemail_flexCb()
const links_gridProps = useStore((state)=>state["Home"]["links_grid"]);
const links_gridIoProps = useIoStore((state)=>state["Home"]["links_grid"]);
const links_gridCb = uselinks_gridCb()
const copyright_divProps = useStore((state)=>state["Home"]["copyright_div"]);
const copyright_divIoProps = useIoStore((state)=>state["Home"]["copyright_div"]);
const copyright_divCb = usecopyright_divCb()
const webflow_divProps = useStore((state)=>state["Home"]["webflow_div"]);
const webflow_divIoProps = useIoStore((state)=>state["Home"]["webflow_div"]);
const webflow_divCb = usewebflow_divCb()
const trust_headingProps = useStore((state)=>state["Home"]["trust_heading"]);
const trust_headingIoProps = useIoStore((state)=>state["Home"]["trust_heading"]);
const trust_headingCb = usetrust_headingCb()
const projects_view_button_backProps = useStore((state)=>state["Home"]["projects_view_button_back"]);
const projects_view_button_backIoProps = useIoStore((state)=>state["Home"]["projects_view_button_back"]);
const projects_view_button_backCb = useprojects_view_button_backCb()
const logo_imgProps = useStore((state)=>state["Home"]["logo_img"]);
const logo_imgIoProps = useIoStore((state)=>state["Home"]["logo_img"]);
const logo_imgCb = uselogo_imgCb()
const call_linkProps = useStore((state)=>state["Home"]["call_link"]);
const call_linkIoProps = useIoStore((state)=>state["Home"]["call_link"]);
const call_linkCb = usecall_linkCb()
const about_linkProps = useStore((state)=>state["Home"]["about_link"]);
const about_linkIoProps = useIoStore((state)=>state["Home"]["about_link"]);
const about_linkCb = useabout_linkCb()
const blog_linkProps = useStore((state)=>state["Home"]["blog_link"]);
const blog_linkIoProps = useIoStore((state)=>state["Home"]["blog_link"]);
const blog_linkCb = useblog_linkCb()
const project_linkProps = useStore((state)=>state["Home"]["project_link"]);
const project_linkIoProps = useIoStore((state)=>state["Home"]["project_link"]);
const project_linkCb = useproject_linkCb()
const services_linkProps = useStore((state)=>state["Home"]["services_link"]);
const services_linkIoProps = useIoStore((state)=>state["Home"]["services_link"]);
const services_linkCb = useservices_linkCb()
const nav_call_arrowProps = useStore((state)=>state["Home"]["nav_call_arrow"]);
const nav_call_arrowIoProps = useIoStore((state)=>state["Home"]["nav_call_arrow"]);
const nav_call_arrowCb = usenav_call_arrowCb()
const trusted_div_mainProps = useStore((state)=>state["Home"]["trusted_div_main"]);
const trusted_div_mainIoProps = useIoStore((state)=>state["Home"]["trusted_div_main"]);
const trusted_div_mainCb = usetrusted_div_mainCb()
const hero_imageProps = useStore((state)=>state["Home"]["hero_image"]);
const hero_imageIoProps = useIoStore((state)=>state["Home"]["hero_image"]);
const hero_imageCb = usehero_imageCb()
const heading_1Props = useStore((state)=>state["Home"]["heading_1"]);
const heading_1IoProps = useIoStore((state)=>state["Home"]["heading_1"]);
const heading_1Cb = useheading_1Cb()
const heading_2Props = useStore((state)=>state["Home"]["heading_2"]);
const heading_2IoProps = useIoStore((state)=>state["Home"]["heading_2"]);
const heading_2Cb = useheading_2Cb()
const heading_3Props = useStore((state)=>state["Home"]["heading_3"]);
const heading_3IoProps = useIoStore((state)=>state["Home"]["heading_3"]);
const heading_3Cb = useheading_3Cb()
const paragraphProps = useStore((state)=>state["Home"]["paragraph"]);
const paragraphIoProps = useIoStore((state)=>state["Home"]["paragraph"]);
const paragraphCb = useparagraphCb()
const button_backgroundProps = useStore((state)=>state["Home"]["button_background"]);
const button_backgroundIoProps = useIoStore((state)=>state["Home"]["button_background"]);
const button_backgroundCb = usebutton_backgroundCb()
const CV_linkProps = useStore((state)=>state["Home"]["CV_link"]);
const CV_linkIoProps = useIoStore((state)=>state["Home"]["CV_link"]);
const CV_linkCb = useCV_linkCb()
const call_buttonProps = useStore((state)=>state["Home"]["call_button"]);
const call_buttonIoProps = useIoStore((state)=>state["Home"]["call_button"]);
const call_buttonCb = usecall_buttonCb()
const company_1Props = useStore((state)=>state["Home"]["company_1"]);
const company_1IoProps = useIoStore((state)=>state["Home"]["company_1"]);
const company_1Cb = usecompany_1Cb()
const company_2Props = useStore((state)=>state["Home"]["company_2"]);
const company_2IoProps = useIoStore((state)=>state["Home"]["company_2"]);
const company_2Cb = usecompany_2Cb()
const company_3Props = useStore((state)=>state["Home"]["company_3"]);
const company_3IoProps = useIoStore((state)=>state["Home"]["company_3"]);
const company_3Cb = usecompany_3Cb()
const company_4Props = useStore((state)=>state["Home"]["company_4"]);
const company_4IoProps = useIoStore((state)=>state["Home"]["company_4"]);
const company_4Cb = usecompany_4Cb()
const projects_mainProps = useStore((state)=>state["Home"]["projects_main"]);
const projects_mainIoProps = useIoStore((state)=>state["Home"]["projects_main"]);
const projects_mainCb = useprojects_mainCb()
const services_headingProps = useStore((state)=>state["Home"]["services_heading"]);
const services_headingIoProps = useIoStore((state)=>state["Home"]["services_heading"]);
const services_headingCb = useservices_headingCb()
const serices_paragraphProps = useStore((state)=>state["Home"]["serices_paragraph"]);
const serices_paragraphIoProps = useIoStore((state)=>state["Home"]["serices_paragraph"]);
const serices_paragraphCb = useserices_paragraphCb()
const services_image_1Props = useStore((state)=>state["Home"]["services_image_1"]);
const services_image_1IoProps = useIoStore((state)=>state["Home"]["services_image_1"]);
const services_image_1Cb = useservices_image_1Cb()
const list_heading_1Props = useStore((state)=>state["Home"]["list_heading_1"]);
const list_heading_1IoProps = useIoStore((state)=>state["Home"]["list_heading_1"]);
const list_heading_1Cb = uselist_heading_1Cb()
const list_paragraph_1Props = useStore((state)=>state["Home"]["list_paragraph_1"]);
const list_paragraph_1IoProps = useIoStore((state)=>state["Home"]["list_paragraph_1"]);
const list_paragraph_1Cb = uselist_paragraph_1Cb()
const services_bullet_point_1Props = useStore((state)=>state["Home"]["services_bullet_point_1"]);
const services_bullet_point_1IoProps = useIoStore((state)=>state["Home"]["services_bullet_point_1"]);
const services_bullet_point_1Cb = useservices_bullet_point_1Cb()
const list_pointer_headingProps = useStore((state)=>state["Home"]["list_pointer_heading"]);
const list_pointer_headingIoProps = useIoStore((state)=>state["Home"]["list_pointer_heading"]);
const list_pointer_headingCb = uselist_pointer_headingCb()
const list_pointer_head_2Props = useStore((state)=>state["Home"]["list_pointer_head_2"]);
const list_pointer_head_2IoProps = useIoStore((state)=>state["Home"]["list_pointer_head_2"]);
const list_pointer_head_2Cb = uselist_pointer_head_2Cb()
const Div46Props = useStore((state)=>state["Home"]["Div46"]);
const Div46IoProps = useIoStore((state)=>state["Home"]["Div46"]);
const Div46Cb = useDiv46Cb()
const pointer_list_heading_3Props = useStore((state)=>state["Home"]["pointer_list_heading_3"]);
const pointer_list_heading_3IoProps = useIoStore((state)=>state["Home"]["pointer_list_heading_3"]);
const pointer_list_heading_3Cb = usepointer_list_heading_3Cb()
const Div47Props = useStore((state)=>state["Home"]["Div47"]);
const Div47IoProps = useIoStore((state)=>state["Home"]["Div47"]);
const Div47Cb = useDiv47Cb()
const services_image_3Props = useStore((state)=>state["Home"]["services_image_3"]);
const services_image_3IoProps = useIoStore((state)=>state["Home"]["services_image_3"]);
const services_image_3Cb = useservices_image_3Cb()
const Div109Props = useStore((state)=>state["Home"]["Div109"]);
const Div109IoProps = useIoStore((state)=>state["Home"]["Div109"]);
const Div109Cb = useDiv109Cb()
const list_pointer_heading_9Props = useStore((state)=>state["Home"]["list_pointer_heading_9"]);
const list_pointer_heading_9IoProps = useIoStore((state)=>state["Home"]["list_pointer_heading_9"]);
const list_pointer_heading_9Cb = uselist_pointer_heading_9Cb()
const Div110Props = useStore((state)=>state["Home"]["Div110"]);
const Div110IoProps = useIoStore((state)=>state["Home"]["Div110"]);
const Div110Cb = useDiv110Cb()
const list_pointer_heading_8Props = useStore((state)=>state["Home"]["list_pointer_heading_8"]);
const list_pointer_heading_8IoProps = useIoStore((state)=>state["Home"]["list_pointer_heading_8"]);
const list_pointer_heading_8Cb = uselist_pointer_heading_8Cb()
const TextBox78Props = useStore((state)=>state["Home"]["TextBox78"]);
const TextBox78IoProps = useIoStore((state)=>state["Home"]["TextBox78"]);
const TextBox78Cb = useTextBox78Cb()
const Div108Props = useStore((state)=>state["Home"]["Div108"]);
const Div108IoProps = useIoStore((state)=>state["Home"]["Div108"]);
const Div108Cb = useDiv108Cb()
const list_paragraph_3Props = useStore((state)=>state["Home"]["list_paragraph_3"]);
const list_paragraph_3IoProps = useIoStore((state)=>state["Home"]["list_paragraph_3"]);
const list_paragraph_3Cb = uselist_paragraph_3Cb()
const list_heading_3Props = useStore((state)=>state["Home"]["list_heading_3"]);
const list_heading_3IoProps = useIoStore((state)=>state["Home"]["list_heading_3"]);
const list_heading_3Cb = uselist_heading_3Cb()
const services_image_2Props = useStore((state)=>state["Home"]["services_image_2"]);
const services_image_2IoProps = useIoStore((state)=>state["Home"]["services_image_2"]);
const services_image_2Cb = useservices_image_2Cb()
const list_heading_2Props = useStore((state)=>state["Home"]["list_heading_2"]);
const list_heading_2IoProps = useIoStore((state)=>state["Home"]["list_heading_2"]);
const list_heading_2Cb = uselist_heading_2Cb()
const list_paragraph_2Props = useStore((state)=>state["Home"]["list_paragraph_2"]);
const list_paragraph_2IoProps = useIoStore((state)=>state["Home"]["list_paragraph_2"]);
const list_paragraph_2Cb = uselist_paragraph_2Cb()
const Div114Props = useStore((state)=>state["Home"]["Div114"]);
const Div114IoProps = useIoStore((state)=>state["Home"]["Div114"]);
const Div114Cb = useDiv114Cb()
const list_pointer_heading_2Props = useStore((state)=>state["Home"]["list_pointer_heading_2"]);
const list_pointer_heading_2IoProps = useIoStore((state)=>state["Home"]["list_pointer_heading_2"]);
const list_pointer_heading_2Cb = uselist_pointer_heading_2Cb()
const list_pointer_head_5Props = useStore((state)=>state["Home"]["list_pointer_head_5"]);
const list_pointer_head_5IoProps = useIoStore((state)=>state["Home"]["list_pointer_head_5"]);
const list_pointer_head_5Cb = uselist_pointer_head_5Cb()
const Div115Props = useStore((state)=>state["Home"]["Div115"]);
const Div115IoProps = useIoStore((state)=>state["Home"]["Div115"]);
const Div115Cb = useDiv115Cb()
const list_pointer_heading_6Props = useStore((state)=>state["Home"]["list_pointer_heading_6"]);
const list_pointer_heading_6IoProps = useIoStore((state)=>state["Home"]["list_pointer_heading_6"]);
const list_pointer_heading_6Cb = uselist_pointer_heading_6Cb()
const Div116Props = useStore((state)=>state["Home"]["Div116"]);
const Div116IoProps = useIoStore((state)=>state["Home"]["Div116"]);
const Div116Cb = useDiv116Cb()
const projects_head_1Props = useStore((state)=>state["Home"]["projects_head_1"]);
const projects_head_1IoProps = useIoStore((state)=>state["Home"]["projects_head_1"]);
const projects_head_1Cb = useprojects_head_1Cb()
const projects_heading_2Props = useStore((state)=>state["Home"]["projects_heading_2"]);
const projects_heading_2IoProps = useIoStore((state)=>state["Home"]["projects_heading_2"]);
const projects_heading_2Cb = useprojects_heading_2Cb()
const projeccts_heading_3Props = useStore((state)=>state["Home"]["projeccts_heading_3"]);
const projeccts_heading_3IoProps = useIoStore((state)=>state["Home"]["projeccts_heading_3"]);
const projeccts_heading_3Cb = useprojeccts_heading_3Cb()
const view_projects_buttonProps = useStore((state)=>state["Home"]["view_projects_button"]);
const view_projects_buttonIoProps = useIoStore((state)=>state["Home"]["view_projects_button"]);
const view_projects_buttonCb = useview_projects_buttonCb()
const slider_3_imageProps = useStore((state)=>state["Home"]["slider_3_image"]);
const slider_3_imageIoProps = useIoStore((state)=>state["Home"]["slider_3_image"]);
const slider_3_imageCb = useslider_3_imageCb()
const slider_3_head_1Props = useStore((state)=>state["Home"]["slider_3_head_1"]);
const slider_3_head_1IoProps = useIoStore((state)=>state["Home"]["slider_3_head_1"]);
const slider_3_head_1Cb = useslider_3_head_1Cb()
const slider_3_head_2Props = useStore((state)=>state["Home"]["slider_3_head_2"]);
const slider_3_head_2IoProps = useIoStore((state)=>state["Home"]["slider_3_head_2"]);
const slider_3_head_2Cb = useslider_3_head_2Cb()
const slider_3_flex_head_3Props = useStore((state)=>state["Home"]["slider_3_flex_head_3"]);
const slider_3_flex_head_3IoProps = useIoStore((state)=>state["Home"]["slider_3_flex_head_3"]);
const slider_3_flex_head_3Cb = useslider_3_flex_head_3Cb()
const slider_3_head_imageProps = useStore((state)=>state["Home"]["slider_3_head_image"]);
const slider_3_head_imageIoProps = useIoStore((state)=>state["Home"]["slider_3_head_image"]);
const slider_3_head_imageCb = useslider_3_head_imageCb()
const slider_item_1_image_2Props = useStore((state)=>state["Home"]["slider_item_1_image_2"]);
const slider_item_1_image_2IoProps = useIoStore((state)=>state["Home"]["slider_item_1_image_2"]);
const slider_item_1_image_2Cb = useslider_item_1_image_2Cb()
const slider_item_2_head_2Props = useStore((state)=>state["Home"]["slider_item_2_head_2"]);
const slider_item_2_head_2IoProps = useIoStore((state)=>state["Home"]["slider_item_2_head_2"]);
const slider_item_2_head_2Cb = useslider_item_2_head_2Cb()
const slider_item_2_productProps = useStore((state)=>state["Home"]["slider_item_2_product"]);
const slider_item_2_productIoProps = useIoStore((state)=>state["Home"]["slider_item_2_product"]);
const slider_item_2_productCb = useslider_item_2_productCb()
const Image44Props = useStore((state)=>state["Home"]["Image44"]);
const Image44IoProps = useIoStore((state)=>state["Home"]["Image44"]);
const Image44Cb = useImage44Cb()
const TextBox116Props = useStore((state)=>state["Home"]["TextBox116"]);
const TextBox116IoProps = useIoStore((state)=>state["Home"]["TextBox116"]);
const TextBox116Cb = useTextBox116Cb()
const slider_image_1Props = useStore((state)=>state["Home"]["slider_image_1"]);
const slider_image_1IoProps = useIoStore((state)=>state["Home"]["slider_image_1"]);
const slider_image_1Cb = useslider_image_1Cb()
const slider_item_1_head_2Props = useStore((state)=>state["Home"]["slider_item_1_head_2"]);
const slider_item_1_head_2IoProps = useIoStore((state)=>state["Home"]["slider_item_1_head_2"]);
const slider_item_1_head_2Cb = useslider_item_1_head_2Cb()
const slider_branding_headProps = useStore((state)=>state["Home"]["slider_branding_head"]);
const slider_branding_headIoProps = useIoStore((state)=>state["Home"]["slider_branding_head"]);
const slider_branding_headCb = useslider_branding_headCb()
const arrow_image_1Props = useStore((state)=>state["Home"]["arrow_image_1"]);
const arrow_image_1IoProps = useIoStore((state)=>state["Home"]["arrow_image_1"]);
const arrow_image_1Cb = usearrow_image_1Cb()
const slider_view_link_1Props = useStore((state)=>state["Home"]["slider_view_link_1"]);
const slider_view_link_1IoProps = useIoStore((state)=>state["Home"]["slider_view_link_1"]);
const slider_view_link_1Cb = useslider_view_link_1Cb()
const blog_left_arrow_imageProps = useStore((state)=>state["Home"]["blog_left_arrow_image"]);
const blog_left_arrow_imageIoProps = useIoStore((state)=>state["Home"]["blog_left_arrow_image"]);
const blog_left_arrow_imageCb = useblog_left_arrow_imageCb()
const blogs_right_arrow_imageProps = useStore((state)=>state["Home"]["blogs_right_arrow_image"]);
const blogs_right_arrow_imageIoProps = useIoStore((state)=>state["Home"]["blogs_right_arrow_image"]);
const blogs_right_arrow_imageCb = useblogs_right_arrow_imageCb()
const heading_blogsProps = useStore((state)=>state["Home"]["heading_blogs"]);
const heading_blogsIoProps = useIoStore((state)=>state["Home"]["heading_blogs"]);
const heading_blogsCb = useheading_blogsCb()
const latest_blogs_headingProps = useStore((state)=>state["Home"]["latest_blogs_heading"]);
const latest_blogs_headingIoProps = useIoStore((state)=>state["Home"]["latest_blogs_heading"]);
const latest_blogs_headingCb = uselatest_blogs_headingCb()
const view_all_linkProps = useStore((state)=>state["Home"]["view_all_link"]);
const view_all_linkIoProps = useIoStore((state)=>state["Home"]["view_all_link"]);
const view_all_linkCb = useview_all_linkCb()
const arrow_imageProps = useStore((state)=>state["Home"]["arrow_image"]);
const arrow_imageIoProps = useIoStore((state)=>state["Home"]["arrow_image"]);
const arrow_imageCb = usearrow_imageCb()
const heading_timeProps = useStore((state)=>state["Home"]["heading_time"]);
const heading_timeIoProps = useIoStore((state)=>state["Home"]["heading_time"]);
const heading_timeCb = useheading_timeCb()
const point_div1Props = useStore((state)=>state["Home"]["point_div1"]);
const point_div1IoProps = useIoStore((state)=>state["Home"]["point_div1"]);
const point_div1Cb = usepoint_div1Cb()
const heading_dateProps = useStore((state)=>state["Home"]["heading_date"]);
const heading_dateIoProps = useIoStore((state)=>state["Home"]["heading_date"]);
const heading_dateCb = useheading_dateCb()
const list_item_1_heading_2Props = useStore((state)=>state["Home"]["list_item_1_heading_2"]);
const list_item_1_heading_2IoProps = useIoStore((state)=>state["Home"]["list_item_1_heading_2"]);
const list_item_1_heading_2Cb = uselist_item_1_heading_2Cb()
const list_1_read_linkProps = useStore((state)=>state["Home"]["list_1_read_link"]);
const list_1_read_linkIoProps = useIoStore((state)=>state["Home"]["list_1_read_link"]);
const list_1_read_linkCb = uselist_1_read_linkCb()
const list_link_arrow_imageProps = useStore((state)=>state["Home"]["list_link_arrow_image"]);
const list_link_arrow_imageIoProps = useIoStore((state)=>state["Home"]["list_link_arrow_image"]);
const list_link_arrow_imageCb = uselist_link_arrow_imageCb()
const list_arrow_imageProps = useStore((state)=>state["Home"]["list_arrow_image"]);
const list_arrow_imageIoProps = useIoStore((state)=>state["Home"]["list_arrow_image"]);
const list_arrow_imageCb = uselist_arrow_imageCb()
const list_2_linkProps = useStore((state)=>state["Home"]["list_2_link"]);
const list_2_linkIoProps = useIoStore((state)=>state["Home"]["list_2_link"]);
const list_2_linkCb = uselist_2_linkCb()
const list_item_heading_2Props = useStore((state)=>state["Home"]["list_item_heading_2"]);
const list_item_heading_2IoProps = useIoStore((state)=>state["Home"]["list_item_heading_2"]);
const list_item_heading_2Cb = uselist_item_heading_2Cb()
const list_item_2_dateProps = useStore((state)=>state["Home"]["list_item_2_date"]);
const list_item_2_dateIoProps = useIoStore((state)=>state["Home"]["list_item_2_date"]);
const list_item_2_dateCb = uselist_item_2_dateCb()
const point_div_2Props = useStore((state)=>state["Home"]["point_div_2"]);
const point_div_2IoProps = useIoStore((state)=>state["Home"]["point_div_2"]);
const point_div_2Cb = usepoint_div_2Cb()
const list_item_2_timeProps = useStore((state)=>state["Home"]["list_item_2_time"]);
const list_item_2_timeIoProps = useIoStore((state)=>state["Home"]["list_item_2_time"]);
const list_item_2_timeCb = uselist_item_2_timeCb()
const list_3_timeProps = useStore((state)=>state["Home"]["list_3_time"]);
const list_3_timeIoProps = useIoStore((state)=>state["Home"]["list_3_time"]);
const list_3_timeCb = uselist_3_timeCb()
const point_div3Props = useStore((state)=>state["Home"]["point_div3"]);
const point_div3IoProps = useIoStore((state)=>state["Home"]["point_div3"]);
const point_div3Cb = usepoint_div3Cb()
const list_3_dateProps = useStore((state)=>state["Home"]["list_3_date"]);
const list_3_dateIoProps = useIoStore((state)=>state["Home"]["list_3_date"]);
const list_3_dateCb = uselist_3_dateCb()
const list_3_headingProps = useStore((state)=>state["Home"]["list_3_heading"]);
const list_3_headingIoProps = useIoStore((state)=>state["Home"]["list_3_heading"]);
const list_3_headingCb = uselist_3_headingCb()
const list_3_link_3Props = useStore((state)=>state["Home"]["list_3_link_3"]);
const list_3_link_3IoProps = useIoStore((state)=>state["Home"]["list_3_link_3"]);
const list_3_link_3Cb = uselist_3_link_3Cb()
const arrow_image_3Props = useStore((state)=>state["Home"]["arrow_image_3"]);
const arrow_image_3IoProps = useIoStore((state)=>state["Home"]["arrow_image_3"]);
const arrow_image_3Cb = usearrow_image_3Cb()
const arrow_image_4Props = useStore((state)=>state["Home"]["arrow_image_4"]);
const arrow_image_4IoProps = useIoStore((state)=>state["Home"]["arrow_image_4"]);
const arrow_image_4Cb = usearrow_image_4Cb()
const list_4_linkProps = useStore((state)=>state["Home"]["list_4_link"]);
const list_4_linkIoProps = useIoStore((state)=>state["Home"]["list_4_link"]);
const list_4_linkCb = uselist_4_linkCb()
const list_4_headingProps = useStore((state)=>state["Home"]["list_4_heading"]);
const list_4_headingIoProps = useIoStore((state)=>state["Home"]["list_4_heading"]);
const list_4_headingCb = uselist_4_headingCb()
const list_4_dateProps = useStore((state)=>state["Home"]["list_4_date"]);
const list_4_dateIoProps = useIoStore((state)=>state["Home"]["list_4_date"]);
const list_4_dateCb = uselist_4_dateCb()
const point_div_4Props = useStore((state)=>state["Home"]["point_div_4"]);
const point_div_4IoProps = useIoStore((state)=>state["Home"]["point_div_4"]);
const point_div_4Cb = usepoint_div_4Cb()
const list_4_timeProps = useStore((state)=>state["Home"]["list_4_time"]);
const list_4_timeIoProps = useIoStore((state)=>state["Home"]["list_4_time"]);
const list_4_timeCb = uselist_4_timeCb()
const list_5_timeProps = useStore((state)=>state["Home"]["list_5_time"]);
const list_5_timeIoProps = useIoStore((state)=>state["Home"]["list_5_time"]);
const list_5_timeCb = uselist_5_timeCb()
const point_div_5Props = useStore((state)=>state["Home"]["point_div_5"]);
const point_div_5IoProps = useIoStore((state)=>state["Home"]["point_div_5"]);
const point_div_5Cb = usepoint_div_5Cb()
const list_5_date_Props = useStore((state)=>state["Home"]["list_5_date_"]);
const list_5_date_IoProps = useIoStore((state)=>state["Home"]["list_5_date_"]);
const list_5_date_Cb = uselist_5_date_Cb()
const list_5_headingProps = useStore((state)=>state["Home"]["list_5_heading"]);
const list_5_headingIoProps = useIoStore((state)=>state["Home"]["list_5_heading"]);
const list_5_headingCb = uselist_5_headingCb()
const list_5_linkProps = useStore((state)=>state["Home"]["list_5_link"]);
const list_5_linkIoProps = useIoStore((state)=>state["Home"]["list_5_link"]);
const list_5_linkCb = uselist_5_linkCb()
const arrow_image_5Props = useStore((state)=>state["Home"]["arrow_image_5"]);
const arrow_image_5IoProps = useIoStore((state)=>state["Home"]["arrow_image_5"]);
const arrow_image_5Cb = usearrow_image_5Cb()
const designer_heading_mainProps = useStore((state)=>state["Home"]["designer_heading_main"]);
const designer_heading_mainIoProps = useIoStore((state)=>state["Home"]["designer_heading_main"]);
const designer_heading_mainCb = usedesigner_heading_mainCb()
const designer_about_heading_2Props = useStore((state)=>state["Home"]["designer_about_heading_2"]);
const designer_about_heading_2IoProps = useIoStore((state)=>state["Home"]["designer_about_heading_2"]);
const designer_about_heading_2Cb = usedesigner_about_heading_2Cb()
const designer_about_paragraphProps = useStore((state)=>state["Home"]["designer_about_paragraph"]);
const designer_about_paragraphIoProps = useIoStore((state)=>state["Home"]["designer_about_paragraph"]);
const designer_about_paragraphCb = usedesigner_about_paragraphCb()
const designer_image_2Props = useStore((state)=>state["Home"]["designer_image_2"]);
const designer_image_2IoProps = useIoStore((state)=>state["Home"]["designer_image_2"]);
const designer_image_2Cb = usedesigner_image_2Cb()
const designer_image_1Props = useStore((state)=>state["Home"]["designer_image_1"]);
const designer_image_1IoProps = useIoStore((state)=>state["Home"]["designer_image_1"]);
const designer_image_1Cb = usedesigner_image_1Cb()
const designer_image_3Props = useStore((state)=>state["Home"]["designer_image_3"]);
const designer_image_3IoProps = useIoStore((state)=>state["Home"]["designer_image_3"]);
const designer_image_3Cb = usedesigner_image_3Cb()
const designer_image_4Props = useStore((state)=>state["Home"]["designer_image_4"]);
const designer_image_4IoProps = useIoStore((state)=>state["Home"]["designer_image_4"]);
const designer_image_4Cb = usedesigner_image_4Cb()
const education_headingProps = useStore((state)=>state["Home"]["education_heading"]);
const education_headingIoProps = useIoStore((state)=>state["Home"]["education_heading"]);
const education_headingCb = useeducation_headingCb()
const list_border_div_1Props = useStore((state)=>state["Home"]["list_border_div_1"]);
const list_border_div_1IoProps = useIoStore((state)=>state["Home"]["list_border_div_1"]);
const list_border_div_1Cb = uselist_border_div_1Cb()
const experience_list_item_1_link_1Props = useStore((state)=>state["Home"]["experience_list_item_1_link_1"]);
const experience_list_item_1_link_1IoProps = useIoStore((state)=>state["Home"]["experience_list_item_1_link_1"]);
const experience_list_item_1_link_1Cb = useexperience_list_item_1_link_1Cb()
const experience_list_item_1_headingProps = useStore((state)=>state["Home"]["experience_list_item_1_heading"]);
const experience_list_item_1_headingIoProps = useIoStore((state)=>state["Home"]["experience_list_item_1_heading"]);
const experience_list_item_1_headingCb = useexperience_list_item_1_headingCb()
const list_item_1_dateProps = useStore((state)=>state["Home"]["list_item_1_date"]);
const list_item_1_dateIoProps = useIoStore((state)=>state["Home"]["list_item_1_date"]);
const list_item_1_dateCb = uselist_item_1_dateCb()
const up_right_arrow_1Props = useStore((state)=>state["Home"]["up_right_arrow_1"]);
const up_right_arrow_1IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_1"]);
const up_right_arrow_1Cb = useup_right_arrow_1Cb()
const list_border_div_2Props = useStore((state)=>state["Home"]["list_border_div_2"]);
const list_border_div_2IoProps = useIoStore((state)=>state["Home"]["list_border_div_2"]);
const list_border_div_2Cb = uselist_border_div_2Cb()
const up_right_arrow_2Props = useStore((state)=>state["Home"]["up_right_arrow_2"]);
const up_right_arrow_2IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_2"]);
const up_right_arrow_2Cb = useup_right_arrow_2Cb()
const list_item__dateProps = useStore((state)=>state["Home"]["list_item__date"]);
const list_item__dateIoProps = useIoStore((state)=>state["Home"]["list_item__date"]);
const list_item__dateCb = uselist_item__dateCb()
const list_item_2_linkProps = useStore((state)=>state["Home"]["list_item_2_link"]);
const list_item_2_linkIoProps = useIoStore((state)=>state["Home"]["list_item_2_link"]);
const list_item_2_linkCb = uselist_item_2_linkCb()
const experience_list_item_2_headingProps = useStore((state)=>state["Home"]["experience_list_item_2_heading"]);
const experience_list_item_2_headingIoProps = useIoStore((state)=>state["Home"]["experience_list_item_2_heading"]);
const experience_list_item_2_headingCb = useexperience_list_item_2_headingCb()
const list_border_div_3Props = useStore((state)=>state["Home"]["list_border_div_3"]);
const list_border_div_3IoProps = useIoStore((state)=>state["Home"]["list_border_div_3"]);
const list_border_div_3Cb = uselist_border_div_3Cb()
const up_right_arrow_3Props = useStore((state)=>state["Home"]["up_right_arrow_3"]);
const up_right_arrow_3IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_3"]);
const up_right_arrow_3Cb = useup_right_arrow_3Cb()
const list_item_3_dateProps = useStore((state)=>state["Home"]["list_item_3_date"]);
const list_item_3_dateIoProps = useIoStore((state)=>state["Home"]["list_item_3_date"]);
const list_item_3_dateCb = uselist_item_3_dateCb()
const experience_list_item_3_headingProps = useStore((state)=>state["Home"]["experience_list_item_3_heading"]);
const experience_list_item_3_headingIoProps = useIoStore((state)=>state["Home"]["experience_list_item_3_heading"]);
const experience_list_item_3_headingCb = useexperience_list_item_3_headingCb()
const experience_list_item_3_link_3Props = useStore((state)=>state["Home"]["experience_list_item_3_link_3"]);
const experience_list_item_3_link_3IoProps = useIoStore((state)=>state["Home"]["experience_list_item_3_link_3"]);
const experience_list_item_3_link_3Cb = useexperience_list_item_3_link_3Cb()
const list_border_div_6Props = useStore((state)=>state["Home"]["list_border_div_6"]);
const list_border_div_6IoProps = useIoStore((state)=>state["Home"]["list_border_div_6"]);
const list_border_div_6Cb = uselist_border_div_6Cb()
const right_list_item_3_image_3Props = useStore((state)=>state["Home"]["right_list_item_3_image_3"]);
const right_list_item_3_image_3IoProps = useIoStore((state)=>state["Home"]["right_list_item_3_image_3"]);
const right_list_item_3_image_3Cb = useright_list_item_3_image_3Cb()
const experience_right_list_item_3_link_3Props = useStore((state)=>state["Home"]["experience_right_list_item_3_link_3"]);
const experience_right_list_item_3_link_3IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_3_link_3"]);
const experience_right_list_item_3_link_3Cb = useexperience_right_list_item_3_link_3Cb()
const experience_right_list_item_3_headingProps = useStore((state)=>state["Home"]["experience_right_list_item_3_heading"]);
const experience_right_list_item_3_headingIoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_3_heading"]);
const experience_right_list_item_3_headingCb = useexperience_right_list_item_3_headingCb()
const right_list_item_3_dateProps = useStore((state)=>state["Home"]["right_list_item_3_date"]);
const right_list_item_3_dateIoProps = useIoStore((state)=>state["Home"]["right_list_item_3_date"]);
const right_list_item_3_dateCb = useright_list_item_3_dateCb()
const up_right_arrow_6Props = useStore((state)=>state["Home"]["up_right_arrow_6"]);
const up_right_arrow_6IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_6"]);
const up_right_arrow_6Cb = useup_right_arrow_6Cb()
const list_border_div_5Props = useStore((state)=>state["Home"]["list_border_div_5"]);
const list_border_div_5IoProps = useIoStore((state)=>state["Home"]["list_border_div_5"]);
const list_border_div_5Cb = uselist_border_div_5Cb()
const right_list_item_2_image_2Props = useStore((state)=>state["Home"]["right_list_item_2_image_2"]);
const right_list_item_2_image_2IoProps = useIoStore((state)=>state["Home"]["right_list_item_2_image_2"]);
const right_list_item_2_image_2Cb = useright_list_item_2_image_2Cb()
const experience_right_list_item_2_headingProps = useStore((state)=>state["Home"]["experience_right_list_item_2_heading"]);
const experience_right_list_item_2_headingIoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_2_heading"]);
const experience_right_list_item_2_headingCb = useexperience_right_list_item_2_headingCb()
const experience_right_list_item_2_link_2Props = useStore((state)=>state["Home"]["experience_right_list_item_2_link_2"]);
const experience_right_list_item_2_link_2IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_2_link_2"]);
const experience_right_list_item_2_link_2Cb = useexperience_right_list_item_2_link_2Cb()
const right_list_item_2_dateProps = useStore((state)=>state["Home"]["right_list_item_2_date"]);
const right_list_item_2_dateIoProps = useIoStore((state)=>state["Home"]["right_list_item_2_date"]);
const right_list_item_2_dateCb = useright_list_item_2_dateCb()
const up_right_arrow_5Props = useStore((state)=>state["Home"]["up_right_arrow_5"]);
const up_right_arrow_5IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_5"]);
const up_right_arrow_5Cb = useup_right_arrow_5Cb()
const list_border_div_4Props = useStore((state)=>state["Home"]["list_border_div_4"]);
const list_border_div_4IoProps = useIoStore((state)=>state["Home"]["list_border_div_4"]);
const list_border_div_4Cb = uselist_border_div_4Cb()
const right_list_item_1_image_1Props = useStore((state)=>state["Home"]["right_list_item_1_image_1"]);
const right_list_item_1_image_1IoProps = useIoStore((state)=>state["Home"]["right_list_item_1_image_1"]);
const right_list_item_1_image_1Cb = useright_list_item_1_image_1Cb()
const up_right_arrow_4Props = useStore((state)=>state["Home"]["up_right_arrow_4"]);
const up_right_arrow_4IoProps = useIoStore((state)=>state["Home"]["up_right_arrow_4"]);
const up_right_arrow_4Cb = useup_right_arrow_4Cb()
const right_list_item_1_dateProps = useStore((state)=>state["Home"]["right_list_item_1_date"]);
const right_list_item_1_dateIoProps = useIoStore((state)=>state["Home"]["right_list_item_1_date"]);
const right_list_item_1_dateCb = useright_list_item_1_dateCb()
const experience_right_list_item_1_headingProps = useStore((state)=>state["Home"]["experience_right_list_item_1_heading"]);
const experience_right_list_item_1_headingIoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_1_heading"]);
const experience_right_list_item_1_headingCb = useexperience_right_list_item_1_headingCb()
const experience_right_list_item_1_link_1Props = useStore((state)=>state["Home"]["experience_right_list_item_1_link_1"]);
const experience_right_list_item_1_link_1IoProps = useIoStore((state)=>state["Home"]["experience_right_list_item_1_link_1"]);
const experience_right_list_item_1_link_1Cb = useexperience_right_list_item_1_link_1Cb()
const work_experience_headingProps = useStore((state)=>state["Home"]["work_experience_heading"]);
const work_experience_headingIoProps = useIoStore((state)=>state["Home"]["work_experience_heading"]);
const work_experience_headingCb = usework_experience_headingCb()
const testimonials_heading_1Props = useStore((state)=>state["Home"]["testimonials_heading_1"]);
const testimonials_heading_1IoProps = useIoStore((state)=>state["Home"]["testimonials_heading_1"]);
const testimonials_heading_1Cb = usetestimonials_heading_1Cb()
const testimonials_heading_2Props = useStore((state)=>state["Home"]["testimonials_heading_2"]);
const testimonials_heading_2IoProps = useIoStore((state)=>state["Home"]["testimonials_heading_2"]);
const testimonials_heading_2Cb = usetestimonials_heading_2Cb()
const testimonial_1_imageProps = useStore((state)=>state["Home"]["testimonial_1_image"]);
const testimonial_1_imageIoProps = useIoStore((state)=>state["Home"]["testimonial_1_image"]);
const testimonial_1_imageCb = usetestimonial_1_imageCb()
const double_quotes_imageProps = useStore((state)=>state["Home"]["double_quotes_image"]);
const double_quotes_imageIoProps = useIoStore((state)=>state["Home"]["double_quotes_image"]);
const double_quotes_imageCb = usedouble_quotes_imageCb()
const detailProps = useStore((state)=>state["Home"]["detail"]);
const detailIoProps = useIoStore((state)=>state["Home"]["detail"]);
const detailCb = usedetailCb()
const testimonial_nameProps = useStore((state)=>state["Home"]["testimonial_name"]);
const testimonial_nameIoProps = useIoStore((state)=>state["Home"]["testimonial_name"]);
const testimonial_nameCb = usetestimonial_nameCb()
const testimonial_designationProps = useStore((state)=>state["Home"]["testimonial_designation"]);
const testimonial_designationIoProps = useIoStore((state)=>state["Home"]["testimonial_designation"]);
const testimonial_designationCb = usetestimonial_designationCb()
const left_arrowProps = useStore((state)=>state["Home"]["left_arrow"]);
const left_arrowIoProps = useIoStore((state)=>state["Home"]["left_arrow"]);
const left_arrowCb = useleft_arrowCb()
const right_arrowProps = useStore((state)=>state["Home"]["right_arrow"]);
const right_arrowIoProps = useIoStore((state)=>state["Home"]["right_arrow"]);
const right_arrowCb = useright_arrowCb()
const faq_headingProps = useStore((state)=>state["Home"]["faq_heading"]);
const faq_headingIoProps = useIoStore((state)=>state["Home"]["faq_heading"]);
const faq_headingCb = usefaq_headingCb()
const faq_heading_2Props = useStore((state)=>state["Home"]["faq_heading_2"]);
const faq_heading_2IoProps = useIoStore((state)=>state["Home"]["faq_heading_2"]);
const faq_heading_2Cb = usefaq_heading_2Cb()
const list_question_1Props = useStore((state)=>state["Home"]["list_question_1"]);
const list_question_1IoProps = useIoStore((state)=>state["Home"]["list_question_1"]);
const list_question_1Cb = uselist_question_1Cb()
const list_down_arrow_1Props = useStore((state)=>state["Home"]["list_down_arrow_1"]);
const list_down_arrow_1IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_1"]);
const list_down_arrow_1Cb = uselist_down_arrow_1Cb()
const list_down_arrow_4Props = useStore((state)=>state["Home"]["list_down_arrow_4"]);
const list_down_arrow_4IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_4"]);
const list_down_arrow_4Cb = uselist_down_arrow_4Cb()
const list_question_4Props = useStore((state)=>state["Home"]["list_question_4"]);
const list_question_4IoProps = useIoStore((state)=>state["Home"]["list_question_4"]);
const list_question_4Cb = uselist_question_4Cb()
const list_down_arrow_2Props = useStore((state)=>state["Home"]["list_down_arrow_2"]);
const list_down_arrow_2IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_2"]);
const list_down_arrow_2Cb = uselist_down_arrow_2Cb()
const list_question_2Props = useStore((state)=>state["Home"]["list_question_2"]);
const list_question_2IoProps = useIoStore((state)=>state["Home"]["list_question_2"]);
const list_question_2Cb = uselist_question_2Cb()
const list_down_arrow_3Props = useStore((state)=>state["Home"]["list_down_arrow_3"]);
const list_down_arrow_3IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_3"]);
const list_down_arrow_3Cb = uselist_down_arrow_3Cb()
const list_question_3Props = useStore((state)=>state["Home"]["list_question_3"]);
const list_question_3IoProps = useIoStore((state)=>state["Home"]["list_question_3"]);
const list_question_3Cb = uselist_question_3Cb()
const right_list_question_3Props = useStore((state)=>state["Home"]["right_list_question_3"]);
const right_list_question_3IoProps = useIoStore((state)=>state["Home"]["right_list_question_3"]);
const right_list_question_3Cb = useright_list_question_3Cb()
const right_list_down_arrow_3Props = useStore((state)=>state["Home"]["right_list_down_arrow_3"]);
const right_list_down_arrow_3IoProps = useIoStore((state)=>state["Home"]["right_list_down_arrow_3"]);
const right_list_down_arrow_3Cb = useright_list_down_arrow_3Cb()
const right_list_question_2Props = useStore((state)=>state["Home"]["right_list_question_2"]);
const right_list_question_2IoProps = useIoStore((state)=>state["Home"]["right_list_question_2"]);
const right_list_question_2Cb = useright_list_question_2Cb()
const list_down_arrow_6Props = useStore((state)=>state["Home"]["list_down_arrow_6"]);
const list_down_arrow_6IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_6"]);
const list_down_arrow_6Cb = uselist_down_arrow_6Cb()
const right_list_question_4Props = useStore((state)=>state["Home"]["right_list_question_4"]);
const right_list_question_4IoProps = useIoStore((state)=>state["Home"]["right_list_question_4"]);
const right_list_question_4Cb = useright_list_question_4Cb()
const right_list_down_arrow_4Props = useStore((state)=>state["Home"]["right_list_down_arrow_4"]);
const right_list_down_arrow_4IoProps = useIoStore((state)=>state["Home"]["right_list_down_arrow_4"]);
const right_list_down_arrow_4Cb = useright_list_down_arrow_4Cb()
const list_down_arrow_5Props = useStore((state)=>state["Home"]["list_down_arrow_5"]);
const list_down_arrow_5IoProps = useIoStore((state)=>state["Home"]["list_down_arrow_5"]);
const list_down_arrow_5Cb = uselist_down_arrow_5Cb()
const right_list_question_1Props = useStore((state)=>state["Home"]["right_list_question_1"]);
const right_list_question_1IoProps = useIoStore((state)=>state["Home"]["right_list_question_1"]);
const right_list_question_1Cb = useright_list_question_1Cb()
const footer_heading_1Props = useStore((state)=>state["Home"]["footer_heading_1"]);
const footer_heading_1IoProps = useIoStore((state)=>state["Home"]["footer_heading_1"]);
const footer_heading_1Cb = usefooter_heading_1Cb()
const footer_heading_2Props = useStore((state)=>state["Home"]["footer_heading_2"]);
const footer_heading_2IoProps = useIoStore((state)=>state["Home"]["footer_heading_2"]);
const footer_heading_2Cb = usefooter_heading_2Cb()
const logo_link_imageProps = useStore((state)=>state["Home"]["logo_link_image"]);
const logo_link_imageIoProps = useIoStore((state)=>state["Home"]["logo_link_image"]);
const logo_link_imageCb = uselogo_link_imageCb()
const address_textProps = useStore((state)=>state["Home"]["address_text"]);
const address_textIoProps = useIoStore((state)=>state["Home"]["address_text"]);
const address_textCb = useaddress_textCb()
const mail_icon_imageProps = useStore((state)=>state["Home"]["mail_icon_image"]);
const mail_icon_imageIoProps = useIoStore((state)=>state["Home"]["mail_icon_image"]);
const mail_icon_imageCb = usemail_icon_imageCb()
const mail_linkProps = useStore((state)=>state["Home"]["mail_link"]);
const mail_linkIoProps = useIoStore((state)=>state["Home"]["mail_link"]);
const mail_linkCb = usemail_linkCb()
const footer_link_9Props = useStore((state)=>state["Home"]["footer_link_9"]);
const footer_link_9IoProps = useIoStore((state)=>state["Home"]["footer_link_9"]);
const footer_link_9Cb = usefooter_link_9Cb()
const footer_link_1Props = useStore((state)=>state["Home"]["footer_link_1"]);
const footer_link_1IoProps = useIoStore((state)=>state["Home"]["footer_link_1"]);
const footer_link_1Cb = usefooter_link_1Cb()
const footer_link_2Props = useStore((state)=>state["Home"]["footer_link_2"]);
const footer_link_2IoProps = useIoStore((state)=>state["Home"]["footer_link_2"]);
const footer_link_2Cb = usefooter_link_2Cb()
const footer_link_7Props = useStore((state)=>state["Home"]["footer_link_7"]);
const footer_link_7IoProps = useIoStore((state)=>state["Home"]["footer_link_7"]);
const footer_link_7Cb = usefooter_link_7Cb()
const footer_link_6Props = useStore((state)=>state["Home"]["footer_link_6"]);
const footer_link_6IoProps = useIoStore((state)=>state["Home"]["footer_link_6"]);
const footer_link_6Cb = usefooter_link_6Cb()
const footer_link_3Props = useStore((state)=>state["Home"]["footer_link_3"]);
const footer_link_3IoProps = useIoStore((state)=>state["Home"]["footer_link_3"]);
const footer_link_3Cb = usefooter_link_3Cb()
const footer_link_5Props = useStore((state)=>state["Home"]["footer_link_5"]);
const footer_link_5IoProps = useIoStore((state)=>state["Home"]["footer_link_5"]);
const footer_link_5Cb = usefooter_link_5Cb()
const footer_link_4Props = useStore((state)=>state["Home"]["footer_link_4"]);
const footer_link_4IoProps = useIoStore((state)=>state["Home"]["footer_link_4"]);
const footer_link_4Cb = usefooter_link_4Cb()
const footer_link_8Props = useStore((state)=>state["Home"]["footer_link_8"]);
const footer_link_8IoProps = useIoStore((state)=>state["Home"]["footer_link_8"]);
const footer_link_8Cb = usefooter_link_8Cb()
const rights_textProps = useStore((state)=>state["Home"]["rights_text"]);
const rights_textIoProps = useIoStore((state)=>state["Home"]["rights_text"]);
const rights_textCb = userights_textCb()
const Conversionflow_linkProps = useStore((state)=>state["Home"]["Conversionflow_link"]);
const Conversionflow_linkIoProps = useIoStore((state)=>state["Home"]["Conversionflow_link"]);
const Conversionflow_linkCb = useConversionflow_linkCb()
const powered_rextProps = useStore((state)=>state["Home"]["powered_rext"]);
const powered_rextIoProps = useIoStore((state)=>state["Home"]["powered_rext"]);
const powered_rextCb = usepowered_rextCb()
const Webflow_linkProps = useStore((state)=>state["Home"]["Webflow_link"]);
const Webflow_linkIoProps = useIoStore((state)=>state["Home"]["Webflow_link"]);
const Webflow_linkCb = useWebflow_linkCb()
const image_text_linkProps = useStore((state)=>state["Home"]["image_text_link"]);
const image_text_linkIoProps = useIoStore((state)=>state["Home"]["image_text_link"]);
const image_text_linkCb = useimage_text_linkCb()
const instructions_linkProps = useStore((state)=>state["Home"]["instructions_link"]);
const instructions_linkIoProps = useIoStore((state)=>state["Home"]["instructions_link"]);
const instructions_linkCb = useinstructions_linkCb()
const Changelog_linkProps = useStore((state)=>state["Home"]["Changelog_link"]);
const Changelog_linkIoProps = useIoStore((state)=>state["Home"]["Changelog_link"]);
const Changelog_linkCb = useChangelog_linkCb()
const last_linkProps = useStore((state)=>state["Home"]["last_link"]);
const last_linkIoProps = useIoStore((state)=>state["Home"]["last_link"]);
const last_linkCb = uselast_linkCb()
const webflow_logoProps = useStore((state)=>state["Home"]["webflow_logo"]);
const webflow_logoIoProps = useIoStore((state)=>state["Home"]["webflow_logo"]);
const webflow_logoCb = usewebflow_logoCb()
const webflow_text_imageProps = useStore((state)=>state["Home"]["webflow_text_image"]);
const webflow_text_imageIoProps = useIoStore((state)=>state["Home"]["webflow_text_image"]);
const webflow_text_imageCb = usewebflow_text_imageCb()

  return (<>
  <Div className="p-Home nav_container bpt" {...nav_containerProps} {...nav_containerCb} {...nav_containerIoProps}>
<Flex className="p-Home nav_bar_div bpt" {...nav_bar_divProps} {...nav_bar_divCb} {...nav_bar_divIoProps}>
<Image className="p-Home logo_img bpt" {...logo_imgProps} {...logo_imgCb} {...logo_imgIoProps}/>
<Flex className="p-Home side_nav bpt" {...side_navProps} {...side_navCb} {...side_navIoProps}>
<Link className="p-Home about_link bpt" {...about_linkProps} {...about_linkCb} {...about_linkIoProps}/>
<Link className="p-Home services_link bpt" {...services_linkProps} {...services_linkCb} {...services_linkIoProps}/>
<Link className="p-Home project_link bpt" {...project_linkProps} {...project_linkCb} {...project_linkIoProps}/>
<Link className="p-Home blog_link bpt" {...blog_linkProps} {...blog_linkCb} {...blog_linkIoProps}/>
<Link className="p-Home call_link bpt" {...call_linkProps} {...call_linkCb} {...call_linkIoProps}/>
<Image className="p-Home nav_call_arrow bpt" {...nav_call_arrowProps} {...nav_call_arrowCb} {...nav_call_arrowIoProps}/>
</Flex>
</Flex>
</Div>
<Div className="p-Home hero_main bpt" {...hero_mainProps} {...hero_mainCb} {...hero_mainIoProps}>
<Flex className="p-Home hero_flex bpt" {...hero_flexProps} {...hero_flexCb} {...hero_flexIoProps}>
<Div className="p-Home heading_paragraph bpt" {...heading_paragraphProps} {...heading_paragraphCb} {...heading_paragraphIoProps}>
<TextBox className="p-Home heading_1 bpt" {...heading_1Props} {...heading_1Cb} {...heading_1IoProps}/>
<TextBox className="p-Home heading_2 bpt" {...heading_2Props} {...heading_2Cb} {...heading_2IoProps}/>
<TextBox className="p-Home heading_3 bpt" {...heading_3Props} {...heading_3Cb} {...heading_3IoProps}/>
<TextBox className="p-Home paragraph bpt" {...paragraphProps} {...paragraphCb} {...paragraphIoProps}/>
<Div className="p-Home button_background bpt" {...button_backgroundProps} {...button_backgroundCb} {...button_backgroundIoProps}/>
<Flex className="p-Home hero_button_link bpt" {...hero_button_linkProps} {...hero_button_linkCb} {...hero_button_linkIoProps}>
<Div className="p-Home call_button_div bpt" {...call_button_divProps} {...call_button_divCb} {...call_button_divIoProps}>
<Button className="p-Home call_button bpt" {...call_buttonProps} {...call_buttonCb} {...call_buttonIoProps}/>
</Div>
<Link className="p-Home CV_link bpt" {...CV_linkProps} {...CV_linkCb} {...CV_linkIoProps}/>
</Flex>
</Div>
<Image className="p-Home hero_image bpt" {...hero_imageProps} {...hero_imageCb} {...hero_imageIoProps}/>
</Flex>
<Div className="p-Home trusted_div_main bpt" {...trusted_div_mainProps} {...trusted_div_mainCb} {...trusted_div_mainIoProps}/>
</Div>
<TextBox className="p-Home trust_heading bpt" {...trust_headingProps} {...trust_headingCb} {...trust_headingIoProps}/>
<Flex className="p-Home companies bpt" {...companiesProps} {...companiesCb} {...companiesIoProps}>
<Image className="p-Home company_1 bpt" {...company_1Props} {...company_1Cb} {...company_1IoProps}/>
<Image className="p-Home company_2 bpt" {...company_2Props} {...company_2Cb} {...company_2IoProps}/>
<Image className="p-Home company_3 bpt" {...company_3Props} {...company_3Cb} {...company_3IoProps}/>
<Image className="p-Home company_4 bpt" {...company_4Props} {...company_4Cb} {...company_4IoProps}/>
</Flex>
<Div className="p-Home services_div bpt" {...services_divProps} {...services_divCb} {...services_divIoProps}>
<Flex className="p-Home services_main bpt" {...services_mainProps} {...services_mainCb} {...services_mainIoProps}>
<Div className="p-Home sevices_head_main bpt" {...sevices_head_mainProps} {...sevices_head_mainCb} {...sevices_head_mainIoProps}>
<TextBox className="p-Home services_heading bpt" {...services_headingProps} {...services_headingCb} {...services_headingIoProps}/>
<Div className="p-Home head_2 bpt" {...head_2Props} {...head_2Cb} {...head_2IoProps}>
<TextBox className="p-Home serices_paragraph bpt" {...serices_paragraphProps} {...serices_paragraphCb} {...serices_paragraphIoProps}/>
</Div>
</Div>
<Flex className="p-Home services_flex bpt" {...services_flexProps} {...services_flexCb} {...services_flexIoProps}>
<Flex className="p-Home sub_service_1 bpt" {...sub_service_1Props} {...sub_service_1Cb} {...sub_service_1IoProps}>
<Image className="p-Home services_image_1 bpt" {...services_image_1Props} {...services_image_1Cb} {...services_image_1IoProps}/>
<Div className="p-Home services_heading_1 bpt" {...services_heading_1Props} {...services_heading_1Cb} {...services_heading_1IoProps}>
<TextBox className="p-Home list_heading_1 bpt" {...list_heading_1Props} {...list_heading_1Cb} {...list_heading_1IoProps}/>
</Div>
<Div className="p-Home services_1_paragraph1 bpt" {...services_1_paragraph1Props} {...services_1_paragraph1Cb} {...services_1_paragraph1IoProps}>
<TextBox className="p-Home list_paragraph_1 bpt" {...list_paragraph_1Props} {...list_paragraph_1Cb} {...list_paragraph_1IoProps}/>
</Div>
<Flex className="p-Home services_list_1 bpt" {...services_list_1Props} {...services_list_1Cb} {...services_list_1IoProps}>
<Div className="p-Home services_pointer_1 bpt" {...services_pointer_1Props} {...services_pointer_1Cb} {...services_pointer_1IoProps}>
<Flex className="p-Home services_list_item_1 bpt" {...services_list_item_1Props} {...services_list_item_1Cb} {...services_list_item_1IoProps}>
<Div className="p-Home services_bullet_point_1 bpt" {...services_bullet_point_1Props} {...services_bullet_point_1Cb} {...services_bullet_point_1IoProps}/>
<TextBox className="p-Home list_pointer_heading bpt" {...list_pointer_headingProps} {...list_pointer_headingCb} {...list_pointer_headingIoProps}/>
</Flex>
</Div>
<Flex className="p-Home Flex36 bpt" {...Flex36Props} {...Flex36Cb} {...Flex36IoProps}>
<Div className="p-Home Div46 bpt" {...Div46Props} {...Div46Cb} {...Div46IoProps}/>
<TextBox className="p-Home list_pointer_head_2 bpt" {...list_pointer_head_2Props} {...list_pointer_head_2Cb} {...list_pointer_head_2IoProps}/>
</Flex>
<Flex className="p-Home list_pointer_head_3 bpt" {...list_pointer_head_3Props} {...list_pointer_head_3Cb} {...list_pointer_head_3IoProps}>
<Div className="p-Home Div47 bpt" {...Div47Props} {...Div47Cb} {...Div47IoProps}/>
<TextBox className="p-Home pointer_list_heading_3 bpt" {...pointer_list_heading_3Props} {...pointer_list_heading_3Cb} {...pointer_list_heading_3IoProps}/>
</Flex>
</Flex>
</Flex>
<Flex className="p-Home sub_service_2 bpt" {...sub_service_2Props} {...sub_service_2Cb} {...sub_service_2IoProps}>
<Image className="p-Home services_image_2 bpt" {...services_image_2Props} {...services_image_2Cb} {...services_image_2IoProps}/>
<Div className="p-Home Div118 bpt" {...Div118Props} {...Div118Cb} {...Div118IoProps}>
<TextBox className="p-Home list_heading_2 bpt" {...list_heading_2Props} {...list_heading_2Cb} {...list_heading_2IoProps}/>
</Div>
<Div className="p-Home Div119 bpt" {...Div119Props} {...Div119Cb} {...Div119IoProps}>
<TextBox className="p-Home list_paragraph_2 bpt" {...list_paragraph_2Props} {...list_paragraph_2Cb} {...list_paragraph_2IoProps}/>
</Div>
<Flex className="p-Home Flex96 bpt" {...Flex96Props} {...Flex96Cb} {...Flex96IoProps}>
<Div className="p-Home Div117 bpt" {...Div117Props} {...Div117Cb} {...Div117IoProps}>
<Flex className="p-Home list_pointer_head_4 bpt" {...list_pointer_head_4Props} {...list_pointer_head_4Cb} {...list_pointer_head_4IoProps}>
<Div className="p-Home Div114 bpt" {...Div114Props} {...Div114Cb} {...Div114IoProps}/>
<TextBox className="p-Home list_pointer_heading_2 bpt" {...list_pointer_heading_2Props} {...list_pointer_heading_2Cb} {...list_pointer_heading_2IoProps}/>
</Flex>
</Div>
<Flex className="p-Home Flex94 bpt" {...Flex94Props} {...Flex94Cb} {...Flex94IoProps}>
<Div className="p-Home Div115 bpt" {...Div115Props} {...Div115Cb} {...Div115IoProps}/>
<TextBox className="p-Home list_pointer_head_5 bpt" {...list_pointer_head_5Props} {...list_pointer_head_5Cb} {...list_pointer_head_5IoProps}/>
</Flex>
<Flex className="p-Home Flex95 bpt" {...Flex95Props} {...Flex95Cb} {...Flex95IoProps}>
<Div className="p-Home Div116 bpt" {...Div116Props} {...Div116Cb} {...Div116IoProps}/>
<TextBox className="p-Home list_pointer_heading_6 bpt" {...list_pointer_heading_6Props} {...list_pointer_heading_6Cb} {...list_pointer_heading_6IoProps}/>
</Flex>
</Flex>
</Flex>
<Flex className="p-Home Flex92 bpt" {...Flex92Props} {...Flex92Cb} {...Flex92IoProps}>
<Image className="p-Home services_image_3 bpt" {...services_image_3Props} {...services_image_3Cb} {...services_image_3IoProps}/>
<Div className="p-Home Div113 bpt" {...Div113Props} {...Div113Cb} {...Div113IoProps}>
<TextBox className="p-Home list_heading_3 bpt" {...list_heading_3Props} {...list_heading_3Cb} {...list_heading_3IoProps}/>
</Div>
<Div className="p-Home Div112 bpt" {...Div112Props} {...Div112Cb} {...Div112IoProps}>
<TextBox className="p-Home list_paragraph_3 bpt" {...list_paragraph_3Props} {...list_paragraph_3Cb} {...list_paragraph_3IoProps}/>
</Div>
<Flex className="p-Home Flex91 bpt" {...Flex91Props} {...Flex91Cb} {...Flex91IoProps}>
<Div className="p-Home Div111 bpt" {...Div111Props} {...Div111Cb} {...Div111IoProps}>
<Flex className="p-Home list_pointer_head_7 bpt" {...list_pointer_head_7Props} {...list_pointer_head_7Cb} {...list_pointer_head_7IoProps}>
<Div className="p-Home Div108 bpt" {...Div108Props} {...Div108Cb} {...Div108IoProps}/>
<TextBox className="p-Home TextBox78 bpt" {...TextBox78Props} {...TextBox78Cb} {...TextBox78IoProps}/>
</Flex>
</Div>
<Flex className="p-Home Flex90 bpt" {...Flex90Props} {...Flex90Cb} {...Flex90IoProps}>
<Div className="p-Home Div110 bpt" {...Div110Props} {...Div110Cb} {...Div110IoProps}/>
<TextBox className="p-Home list_pointer_heading_8 bpt" {...list_pointer_heading_8Props} {...list_pointer_heading_8Cb} {...list_pointer_heading_8IoProps}/>
</Flex>
<Flex className="p-Home list_ponter_head_9ac bpt" {...list_ponter_head_9acProps} {...list_ponter_head_9acCb} {...list_ponter_head_9acIoProps}>
<Div className="p-Home Div109 bpt" {...Div109Props} {...Div109Cb} {...Div109IoProps}/>
<TextBox className="p-Home list_pointer_heading_9 bpt" {...list_pointer_heading_9Props} {...list_pointer_heading_9Cb} {...list_pointer_heading_9IoProps}/>
</Flex>
</Flex>
</Flex>
</Flex>
</Flex>
<Div className="p-Home projects_main bpt" {...projects_mainProps} {...projects_mainCb} {...projects_mainIoProps}/>
</Div>
<Div className="p-Home projects_view_button_back bpt" {...projects_view_button_backProps} {...projects_view_button_backCb} {...projects_view_button_backIoProps}/>
<Flex className="p-Home projects_head_paragraph_1 bpt" {...projects_head_paragraph_1Props} {...projects_head_paragraph_1Cb} {...projects_head_paragraph_1IoProps}>
<Flex className="p-Home projects_heading_1 bpt" {...projects_heading_1Props} {...projects_heading_1Cb} {...projects_heading_1IoProps}>
<TextBox className="p-Home projects_head_1 bpt" {...projects_head_1Props} {...projects_head_1Cb} {...projects_head_1IoProps}/>
<Div className="p-Home heading_2_3_div bpt" {...heading_2_3_divProps} {...heading_2_3_divCb} {...heading_2_3_divIoProps}>
<TextBox className="p-Home projects_heading_2 bpt" {...projects_heading_2Props} {...projects_heading_2Cb} {...projects_heading_2IoProps}/>
<TextBox className="p-Home projeccts_heading_3 bpt" {...projeccts_heading_3Props} {...projeccts_heading_3Cb} {...projeccts_heading_3IoProps}/>
</Div>
</Flex>
<Div className="p-Home view_projects_button_div bpt" {...view_projects_button_divProps} {...view_projects_button_divCb} {...view_projects_button_divIoProps}>
<Button className="p-Home view_projects_button bpt" {...view_projects_buttonProps} {...view_projects_buttonCb} {...view_projects_buttonIoProps}/>
</Div>
</Flex>
<Flex className="p-Home projects_slider_flex bpt" {...projects_slider_flexProps} {...projects_slider_flexCb} {...projects_slider_flexIoProps}>
<Flex className="p-Home slider_button_left bpt" {...slider_button_leftProps} {...slider_button_leftCb} {...slider_button_leftIoProps}>
<Image className="p-Home blog_left_arrow_image bpt" {...blog_left_arrow_imageProps} {...blog_left_arrow_imageCb} {...blog_left_arrow_imageIoProps}/>
</Flex>
<Flex className="p-Home slider_item_1 bpt" {...slider_item_1Props} {...slider_item_1Cb} {...slider_item_1IoProps}>
<Image className="p-Home slider_image_1 bpt" {...slider_image_1Props} {...slider_image_1Cb} {...slider_image_1IoProps}/>
<Flex className="p-Home slider_item1_head_flex bpt" {...slider_item1_head_flexProps} {...slider_item1_head_flexCb} {...slider_item1_head_flexIoProps}>
<TextBox className="p-Home slider_branding_head bpt" {...slider_branding_headProps} {...slider_branding_headCb} {...slider_branding_headIoProps}/>
<TextBox className="p-Home slider_item_1_head_2 bpt" {...slider_item_1_head_2Props} {...slider_item_1_head_2Cb} {...slider_item_1_head_2IoProps}/>
<Flex className="p-Home Flex136 bpt" {...Flex136Props} {...Flex136Cb} {...Flex136IoProps}>
<TextBox className="p-Home slider_view_link_1 bpt" {...slider_view_link_1Props} {...slider_view_link_1Cb} {...slider_view_link_1IoProps}/>
<Image className="p-Home arrow_image_1 bpt" {...arrow_image_1Props} {...arrow_image_1Cb} {...arrow_image_1IoProps}/>
</Flex>
</Flex>
</Flex>
<Flex className="p-Home slider_item_2 bpt" {...slider_item_2Props} {...slider_item_2Cb} {...slider_item_2IoProps}>
<Image className="p-Home slider_item_1_image_2 bpt" {...slider_item_1_image_2Props} {...slider_item_1_image_2Cb} {...slider_item_1_image_2IoProps}/>
<Flex className="p-Home slider_item_2_head bpt" {...slider_item_2_headProps} {...slider_item_2_headCb} {...slider_item_2_headIoProps}>
<TextBox className="p-Home slider_item_2_product bpt" {...slider_item_2_productProps} {...slider_item_2_productCb} {...slider_item_2_productIoProps}/>
<TextBox className="p-Home slider_item_2_head_2 bpt" {...slider_item_2_head_2Props} {...slider_item_2_head_2Cb} {...slider_item_2_head_2IoProps}/>
<Flex className="p-Home slider_item_2_link_2 bpt" {...slider_item_2_link_2Props} {...slider_item_2_link_2Cb} {...slider_item_2_link_2IoProps}>
<TextBox className="p-Home TextBox116 bpt" {...TextBox116Props} {...TextBox116Cb} {...TextBox116IoProps}/>
<Image className="p-Home Image44 bpt" {...Image44Props} {...Image44Cb} {...Image44IoProps}/>
</Flex>
</Flex>
</Flex>
<Flex className="p-Home projects_slider_3 bpt" {...projects_slider_3Props} {...projects_slider_3Cb} {...projects_slider_3IoProps}>
<Image className="p-Home slider_3_image bpt" {...slider_3_imageProps} {...slider_3_imageCb} {...slider_3_imageIoProps}/>
<Flex className="p-Home project_slider_3_paragraph_head bpt" {...project_slider_3_paragraph_headProps} {...project_slider_3_paragraph_headCb} {...project_slider_3_paragraph_headIoProps}>
<TextBox className="p-Home slider_3_head_1 bpt" {...slider_3_head_1Props} {...slider_3_head_1Cb} {...slider_3_head_1IoProps}/>
<TextBox className="p-Home slider_3_head_2 bpt" {...slider_3_head_2Props} {...slider_3_head_2Cb} {...slider_3_head_2IoProps}/>
<Flex className="p-Home slider_3_link_flex bpt" {...slider_3_link_flexProps} {...slider_3_link_flexCb} {...slider_3_link_flexIoProps}>
<TextBox className="p-Home slider_3_flex_head_3 bpt" {...slider_3_flex_head_3Props} {...slider_3_flex_head_3Cb} {...slider_3_flex_head_3IoProps}/>
<Image className="p-Home slider_3_head_image bpt" {...slider_3_head_imageProps} {...slider_3_head_imageCb} {...slider_3_head_imageIoProps}/>
</Flex>
</Flex>
</Flex>
<Flex className="p-Home sliderbutton_right bpt" {...sliderbutton_rightProps} {...sliderbutton_rightCb} {...sliderbutton_rightIoProps}>
<Image className="p-Home blogs_right_arrow_image bpt" {...blogs_right_arrow_imageProps} {...blogs_right_arrow_imageCb} {...blogs_right_arrow_imageIoProps}/>
</Flex>
</Flex>
<Div className="p-Home blogs_main_div bpt" {...blogs_main_divProps} {...blogs_main_divCb} {...blogs_main_divIoProps}>
<Flex className="p-Home blogs_main_flex bpt" {...blogs_main_flexProps} {...blogs_main_flexCb} {...blogs_main_flexIoProps}>
<Flex className="p-Home blogs_heading_div bpt" {...blogs_heading_divProps} {...blogs_heading_divCb} {...blogs_heading_divIoProps}>
<TextBox className="p-Home heading_blogs bpt" {...heading_blogsProps} {...heading_blogsCb} {...heading_blogsIoProps}/>
<TextBox className="p-Home latest_blogs_heading bpt" {...latest_blogs_headingProps} {...latest_blogs_headingCb} {...latest_blogs_headingIoProps}/>
<Flex className="p-Home blogs_view_all_link_flex bpt" {...blogs_view_all_link_flexProps} {...blogs_view_all_link_flexCb} {...blogs_view_all_link_flexIoProps}>
<TextBox className="p-Home view_all_link bpt" {...view_all_linkProps} {...view_all_linkCb} {...view_all_linkIoProps}/>
<Image className="p-Home arrow_image bpt" {...arrow_imageProps} {...arrow_imageCb} {...arrow_imageIoProps}/>
</Flex>
</Flex>
<Div className="p-Home blog_list_div_main bpt" {...blog_list_div_mainProps} {...blog_list_div_mainCb} {...blog_list_div_mainIoProps}>
<Flex className="p-Home list_item_1_flex bpt" {...list_item_1_flexProps} {...list_item_1_flexCb} {...list_item_1_flexIoProps}>
<Div className="p-Home list_item_1_date_time bpt" {...list_item_1_date_timeProps} {...list_item_1_date_timeCb} {...list_item_1_date_timeIoProps}>
<Flex className="p-Home heading_date_time_flex bpt" {...heading_date_time_flexProps} {...heading_date_time_flexCb} {...heading_date_time_flexIoProps}>
<TextBox className="p-Home heading_date bpt" {...heading_dateProps} {...heading_dateCb} {...heading_dateIoProps}/>
<Div className="p-Home point_div1 bpt" {...point_div1Props} {...point_div1Cb} {...point_div1IoProps}/>
<TextBox className="p-Home heading_time bpt" {...heading_timeProps} {...heading_timeCb} {...heading_timeIoProps}/>
</Flex>
</Div>
<Div className="p-Home list_heading_2_div bpt" {...list_heading_2_divProps} {...list_heading_2_divCb} {...list_heading_2_divIoProps}>
<TextBox className="p-Home list_item_1_heading_2 bpt" {...list_item_1_heading_2Props} {...list_item_1_heading_2Cb} {...list_item_1_heading_2IoProps}/>
</Div>
<Flex className="p-Home list_item_1_read_link_flex bpt" {...list_item_1_read_link_flexProps} {...list_item_1_read_link_flexCb} {...list_item_1_read_link_flexIoProps}>
<TextBox className="p-Home list_1_read_link bpt" {...list_1_read_linkProps} {...list_1_read_linkCb} {...list_1_read_linkIoProps}/>
<Image className="p-Home list_link_arrow_image bpt" {...list_link_arrow_imageProps} {...list_link_arrow_imageCb} {...list_link_arrow_imageIoProps}/>
</Flex>
</Flex>
<Flex className="p-Home list_item_2_flex bpt" {...list_item_2_flexProps} {...list_item_2_flexCb} {...list_item_2_flexIoProps}>
<Div className="p-Home Div166 bpt" {...Div166Props} {...Div166Cb} {...Div166IoProps}>
<Flex className="p-Home Flex158 bpt" {...Flex158Props} {...Flex158Cb} {...Flex158IoProps}>
<TextBox className="p-Home list_item_2_date bpt" {...list_item_2_dateProps} {...list_item_2_dateCb} {...list_item_2_dateIoProps}/>
<Div className="p-Home point_div_2 bpt" {...point_div_2Props} {...point_div_2Cb} {...point_div_2IoProps}/>
<TextBox className="p-Home list_item_2_time bpt" {...list_item_2_timeProps} {...list_item_2_timeCb} {...list_item_2_timeIoProps}/>
</Flex>
</Div>
<Div className="p-Home list_item_2_heading_div bpt" {...list_item_2_heading_divProps} {...list_item_2_heading_divCb} {...list_item_2_heading_divIoProps}>
<TextBox className="p-Home list_item_heading_2 bpt" {...list_item_heading_2Props} {...list_item_heading_2Cb} {...list_item_heading_2IoProps}/>
</Div>
<Flex className="p-Home list_item_2_link_flex bpt" {...list_item_2_link_flexProps} {...list_item_2_link_flexCb} {...list_item_2_link_flexIoProps}>
<TextBox className="p-Home list_2_link bpt" {...list_2_linkProps} {...list_2_linkCb} {...list_2_linkIoProps}/>
<Image className="p-Home list_arrow_image bpt" {...list_arrow_imageProps} {...list_arrow_imageCb} {...list_arrow_imageIoProps}/>
</Flex>
</Flex>
<Flex className="p-Home list_item_3_flex bpt" {...list_item_3_flexProps} {...list_item_3_flexCb} {...list_item_3_flexIoProps}>
<Div className="p-Home Div168 bpt" {...Div168Props} {...Div168Cb} {...Div168IoProps}>
<Flex className="p-Home point_div_3 bpt" {...point_div_3Props} {...point_div_3Cb} {...point_div_3IoProps}>
<TextBox className="p-Home list_3_date bpt" {...list_3_dateProps} {...list_3_dateCb} {...list_3_dateIoProps}/>
<Div className="p-Home point_div3 bpt" {...point_div3Props} {...point_div3Cb} {...point_div3IoProps}/>
<TextBox className="p-Home list_3_time bpt" {...list_3_timeProps} {...list_3_timeCb} {...list_3_timeIoProps}/>
</Flex>
</Div>
<Div className="p-Home list_3_heading_div bpt" {...list_3_heading_divProps} {...list_3_heading_divCb} {...list_3_heading_divIoProps}>
<TextBox className="p-Home list_3_heading bpt" {...list_3_headingProps} {...list_3_headingCb} {...list_3_headingIoProps}/>
</Div>
<Flex className="p-Home list_3_link bpt" {...list_3_linkProps} {...list_3_linkCb} {...list_3_linkIoProps}>
<TextBox className="p-Home list_3_link_3 bpt" {...list_3_link_3Props} {...list_3_link_3Cb} {...list_3_link_3IoProps}/>
<Image className="p-Home arrow_image_3 bpt" {...arrow_image_3Props} {...arrow_image_3Cb} {...arrow_image_3IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home list_item_4_flex bpt" {...list_item_4_flexProps} {...list_item_4_flexCb} {...list_item_4_flexIoProps}>
<Div className="p-Home Div172 bpt" {...Div172Props} {...Div172Cb} {...Div172IoProps}>
<Flex className="p-Home Flex164 bpt" {...Flex164Props} {...Flex164Cb} {...Flex164IoProps}>
<TextBox className="p-Home list_4_date bpt" {...list_4_dateProps} {...list_4_dateCb} {...list_4_dateIoProps}/>
<Div className="p-Home point_div_4 bpt" {...point_div_4Props} {...point_div_4Cb} {...point_div_4IoProps}/>
<TextBox className="p-Home list_4_time bpt" {...list_4_timeProps} {...list_4_timeCb} {...list_4_timeIoProps}/>
</Flex>
</Div>
<Div className="p-Home list_4_heading_div bpt" {...list_4_heading_divProps} {...list_4_heading_divCb} {...list_4_heading_divIoProps}>
<TextBox className="p-Home list_4_heading bpt" {...list_4_headingProps} {...list_4_headingCb} {...list_4_headingIoProps}/>
</Div>
<Flex className="p-Home list_4_link_flex bpt" {...list_4_link_flexProps} {...list_4_link_flexCb} {...list_4_link_flexIoProps}>
<TextBox className="p-Home list_4_link bpt" {...list_4_linkProps} {...list_4_linkCb} {...list_4_linkIoProps}/>
<Image className="p-Home arrow_image_4 bpt" {...arrow_image_4Props} {...arrow_image_4Cb} {...arrow_image_4IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home list_item_5_flex bpt" {...list_item_5_flexProps} {...list_item_5_flexCb} {...list_item_5_flexIoProps}>
<Div className="p-Home Div174 bpt" {...Div174Props} {...Div174Cb} {...Div174IoProps}>
<Flex className="p-Home Flex167 bpt" {...Flex167Props} {...Flex167Cb} {...Flex167IoProps}>
<TextBox className="p-Home list_5_date_ bpt" {...list_5_date_Props} {...list_5_date_Cb} {...list_5_date_IoProps}/>
<Div className="p-Home point_div_5 bpt" {...point_div_5Props} {...point_div_5Cb} {...point_div_5IoProps}/>
<TextBox className="p-Home list_5_time bpt" {...list_5_timeProps} {...list_5_timeCb} {...list_5_timeIoProps}/>
</Flex>
</Div>
<Div className="p-Home vlist_5_heading_div bpt" {...vlist_5_heading_divProps} {...vlist_5_heading_divCb} {...vlist_5_heading_divIoProps}>
<TextBox className="p-Home list_5_heading bpt" {...list_5_headingProps} {...list_5_headingCb} {...list_5_headingIoProps}/>
</Div>
<Flex className="p-Home list_5_link_flex bpt" {...list_5_link_flexProps} {...list_5_link_flexCb} {...list_5_link_flexIoProps}>
<TextBox className="p-Home list_5_link bpt" {...list_5_linkProps} {...list_5_linkCb} {...list_5_linkIoProps}/>
<Image className="p-Home arrow_image_5 bpt" {...arrow_image_5Props} {...arrow_image_5Cb} {...arrow_image_5IoProps}/>
</Flex>
</Flex>
</Div>
</Flex>
</Div>
<Div className="p-Home pro_designer_main bpt" {...pro_designer_mainProps} {...pro_designer_mainCb} {...pro_designer_mainIoProps}>
<Flex className="p-Home designer_details_flex bpt" {...designer_details_flexProps} {...designer_details_flexCb} {...designer_details_flexIoProps}>
<Div className="p-Home designer_deatails_div bpt" {...designer_deatails_divProps} {...designer_deatails_divCb} {...designer_deatails_divIoProps}>
<TextBox className="p-Home designer_heading_main bpt" {...designer_heading_mainProps} {...designer_heading_mainCb} {...designer_heading_mainIoProps}/>
<TextBox className="p-Home designer_about_heading_2 bpt" {...designer_about_heading_2Props} {...designer_about_heading_2Cb} {...designer_about_heading_2IoProps}/>
</Div>
<Div className="p-Home designer_about_paragraph_div bpt" {...designer_about_paragraph_divProps} {...designer_about_paragraph_divCb} {...designer_about_paragraph_divIoProps}>
<TextBox className="p-Home designer_about_paragraph bpt" {...designer_about_paragraphProps} {...designer_about_paragraphCb} {...designer_about_paragraphIoProps}/>
</Div>
</Flex>
<Flex className="p-Home designer_image_flex bpt" {...designer_image_flexProps} {...designer_image_flexCb} {...designer_image_flexIoProps}>
<Image className="p-Home designer_image_1 bpt" {...designer_image_1Props} {...designer_image_1Cb} {...designer_image_1IoProps}/>
<Image className="p-Home designer_image_2 bpt" {...designer_image_2Props} {...designer_image_2Cb} {...designer_image_2IoProps}/>
<Flex className="p-Home designer_2_image_flex bpt" {...designer_2_image_flexProps} {...designer_2_image_flexCb} {...designer_2_image_flexIoProps}>
<Image className="p-Home designer_image_3 bpt" {...designer_image_3Props} {...designer_image_3Cb} {...designer_image_3IoProps}/>
<Image className="p-Home designer_image_4 bpt" {...designer_image_4Props} {...designer_image_4Cb} {...designer_image_4IoProps}/>
</Flex>
</Flex>
</Div>
<Div className="p-Home experience_main_div bpt" {...experience_main_divProps} {...experience_main_divCb} {...experience_main_divIoProps}>
<Flex className="p-Home experience_flex bpt" {...experience_flexProps} {...experience_flexCb} {...experience_flexIoProps}>
<Div className="p-Home experience_left_div bpt" {...experience_left_divProps} {...experience_left_divCb} {...experience_left_divIoProps}>
<Div className="p-Home experience_heading_div bpt" {...experience_heading_divProps} {...experience_heading_divCb} {...experience_heading_divIoProps}>
<TextBox className="p-Home education_heading bpt" {...education_headingProps} {...education_headingCb} {...education_headingIoProps}/>
</Div>
<Div className="p-Home experience_list bpt" {...experience_listProps} {...experience_listCb} {...experience_listIoProps}>
<Flex className="p-Home experience_list_item_1 bpt" {...experience_list_item_1Props} {...experience_list_item_1Cb} {...experience_list_item_1IoProps}>
<Div className="p-Home list_border_div_1 bpt" {...list_border_div_1Props} {...list_border_div_1Cb} {...list_border_div_1IoProps}/>
<Flex className="p-Home list_item_1_heading_div bpt" {...list_item_1_heading_divProps} {...list_item_1_heading_divCb} {...list_item_1_heading_divIoProps}>
<Link className="p-Home experience_list_item_1_link_1 bpt" {...experience_list_item_1_link_1Props} {...experience_list_item_1_link_1Cb} {...experience_list_item_1_link_1IoProps}/>
<TextBox className="p-Home experience_list_item_1_heading bpt" {...experience_list_item_1_headingProps} {...experience_list_item_1_headingCb} {...experience_list_item_1_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_list_item_1_year_1_flex bpt" {...experience_list_item_1_year_1_flexProps} {...experience_list_item_1_year_1_flexCb} {...experience_list_item_1_year_1_flexIoProps}>
<TextBox className="p-Home list_item_1_date bpt" {...list_item_1_dateProps} {...list_item_1_dateCb} {...list_item_1_dateIoProps}/>
<Image className="p-Home up_right_arrow_1 bpt" {...up_right_arrow_1Props} {...up_right_arrow_1Cb} {...up_right_arrow_1IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home experience_list_item_2 bpt" {...experience_list_item_2Props} {...experience_list_item_2Cb} {...experience_list_item_2IoProps}>
<Div className="p-Home list_border_div_2 bpt" {...list_border_div_2Props} {...list_border_div_2Cb} {...list_border_div_2IoProps}/>
<Flex className="p-Home list_item__heading_div bpt" {...list_item__heading_divProps} {...list_item__heading_divCb} {...list_item__heading_divIoProps}>
<Link className="p-Home list_item_2_link bpt" {...list_item_2_linkProps} {...list_item_2_linkCb} {...list_item_2_linkIoProps}/>
<TextBox className="p-Home experience_list_item_2_heading bpt" {...experience_list_item_2_headingProps} {...experience_list_item_2_headingCb} {...experience_list_item_2_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_list_item_2_year_2_flex bpt" {...experience_list_item_2_year_2_flexProps} {...experience_list_item_2_year_2_flexCb} {...experience_list_item_2_year_2_flexIoProps}>
<TextBox className="p-Home list_item__date bpt" {...list_item__dateProps} {...list_item__dateCb} {...list_item__dateIoProps}/>
<Image className="p-Home up_right_arrow_2 bpt" {...up_right_arrow_2Props} {...up_right_arrow_2Cb} {...up_right_arrow_2IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home experience_list_item_3 bpt" {...experience_list_item_3Props} {...experience_list_item_3Cb} {...experience_list_item_3IoProps}>
<Div className="p-Home list_border_div_3 bpt" {...list_border_div_3Props} {...list_border_div_3Cb} {...list_border_div_3IoProps}/>
<Flex className="p-Home list_item_3_heading_div bpt" {...list_item_3_heading_divProps} {...list_item_3_heading_divCb} {...list_item_3_heading_divIoProps}>
<Link className="p-Home experience_list_item_3_link_3 bpt" {...experience_list_item_3_link_3Props} {...experience_list_item_3_link_3Cb} {...experience_list_item_3_link_3IoProps}/>
<TextBox className="p-Home experience_list_item_3_heading bpt" {...experience_list_item_3_headingProps} {...experience_list_item_3_headingCb} {...experience_list_item_3_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_list_item__year_3_flex bpt" {...experience_list_item__year_3_flexProps} {...experience_list_item__year_3_flexCb} {...experience_list_item__year_3_flexIoProps}>
<TextBox className="p-Home list_item_3_date bpt" {...list_item_3_dateProps} {...list_item_3_dateCb} {...list_item_3_dateIoProps}/>
<Image className="p-Home up_right_arrow_3 bpt" {...up_right_arrow_3Props} {...up_right_arrow_3Cb} {...up_right_arrow_3IoProps}/>
</Flex>
</Flex>
</Div>
</Div>
<Div className="p-Home experience_right_div bpt" {...experience_right_divProps} {...experience_right_divCb} {...experience_right_divIoProps}>
<Div className="p-Home Div201 bpt" {...Div201Props} {...Div201Cb} {...Div201IoProps}>
<TextBox className="p-Home work_experience_heading bpt" {...work_experience_headingProps} {...work_experience_headingCb} {...work_experience_headingIoProps}/>
</Div>
<Div className="p-Home Div200 bpt" {...Div200Props} {...Div200Cb} {...Div200IoProps}>
<Flex className="p-Home experience_right_list_item_1 bpt" {...experience_right_list_item_1Props} {...experience_right_list_item_1Cb} {...experience_right_list_item_1IoProps}>
<Div className="p-Home list_border_div_4 bpt" {...list_border_div_4Props} {...list_border_div_4Cb} {...list_border_div_4IoProps}/>
<Image className="p-Home right_list_item_1_image_1 bpt" {...right_list_item_1_image_1Props} {...right_list_item_1_image_1Cb} {...right_list_item_1_image_1IoProps}/>
<Flex className="p-Home right_list_item_1_heading_div bpt" {...right_list_item_1_heading_divProps} {...right_list_item_1_heading_divCb} {...right_list_item_1_heading_divIoProps}>
<Link className="p-Home experience_right_list_item_1_link_1 bpt" {...experience_right_list_item_1_link_1Props} {...experience_right_list_item_1_link_1Cb} {...experience_right_list_item_1_link_1IoProps}/>
<TextBox className="p-Home experience_right_list_item_1_heading bpt" {...experience_right_list_item_1_headingProps} {...experience_right_list_item_1_headingCb} {...experience_right_list_item_1_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_right_ist_item_1_year_1_flex bpt" {...experience_right_ist_item_1_year_1_flexProps} {...experience_right_ist_item_1_year_1_flexCb} {...experience_right_ist_item_1_year_1_flexIoProps}>
<TextBox className="p-Home right_list_item_1_date bpt" {...right_list_item_1_dateProps} {...right_list_item_1_dateCb} {...right_list_item_1_dateIoProps}/>
<Image className="p-Home up_right_arrow_4 bpt" {...up_right_arrow_4Props} {...up_right_arrow_4Cb} {...up_right_arrow_4IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home experience_right_list_item_2 bpt" {...experience_right_list_item_2Props} {...experience_right_list_item_2Cb} {...experience_right_list_item_2IoProps}>
<Div className="p-Home list_border_div_5 bpt" {...list_border_div_5Props} {...list_border_div_5Cb} {...list_border_div_5IoProps}/>
<Image className="p-Home right_list_item_2_image_2 bpt" {...right_list_item_2_image_2Props} {...right_list_item_2_image_2Cb} {...right_list_item_2_image_2IoProps}/>
<Flex className="p-Home right_list_item_2_heading_div bpt" {...right_list_item_2_heading_divProps} {...right_list_item_2_heading_divCb} {...right_list_item_2_heading_divIoProps}>
<Link className="p-Home experience_right_list_item_2_link_2 bpt" {...experience_right_list_item_2_link_2Props} {...experience_right_list_item_2_link_2Cb} {...experience_right_list_item_2_link_2IoProps}/>
<TextBox className="p-Home experience_right_list_item_2_heading bpt" {...experience_right_list_item_2_headingProps} {...experience_right_list_item_2_headingCb} {...experience_right_list_item_2_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_right_ist_item_2_year_2_flex bpt" {...experience_right_ist_item_2_year_2_flexProps} {...experience_right_ist_item_2_year_2_flexCb} {...experience_right_ist_item_2_year_2_flexIoProps}>
<TextBox className="p-Home right_list_item_2_date bpt" {...right_list_item_2_dateProps} {...right_list_item_2_dateCb} {...right_list_item_2_dateIoProps}/>
<Image className="p-Home up_right_arrow_5 bpt" {...up_right_arrow_5Props} {...up_right_arrow_5Cb} {...up_right_arrow_5IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home experience_right_list_item_3 bpt" {...experience_right_list_item_3Props} {...experience_right_list_item_3Cb} {...experience_right_list_item_3IoProps}>
<Div className="p-Home list_border_div_6 bpt" {...list_border_div_6Props} {...list_border_div_6Cb} {...list_border_div_6IoProps}/>
<Image className="p-Home right_list_item_3_image_3 bpt" {...right_list_item_3_image_3Props} {...right_list_item_3_image_3Cb} {...right_list_item_3_image_3IoProps}/>
<Flex className="p-Home right_list_item_3_heading_div bpt" {...right_list_item_3_heading_divProps} {...right_list_item_3_heading_divCb} {...right_list_item_3_heading_divIoProps}>
<Link className="p-Home experience_right_list_item_3_link_3 bpt" {...experience_right_list_item_3_link_3Props} {...experience_right_list_item_3_link_3Cb} {...experience_right_list_item_3_link_3IoProps}/>
<TextBox className="p-Home experience_right_list_item_3_heading bpt" {...experience_right_list_item_3_headingProps} {...experience_right_list_item_3_headingCb} {...experience_right_list_item_3_headingIoProps}/>
</Flex>
<Flex className="p-Home experience_right_ist_item_3_year_3_flex bpt" {...experience_right_ist_item_3_year_3_flexProps} {...experience_right_ist_item_3_year_3_flexCb} {...experience_right_ist_item_3_year_3_flexIoProps}>
<TextBox className="p-Home right_list_item_3_date bpt" {...right_list_item_3_dateProps} {...right_list_item_3_dateCb} {...right_list_item_3_dateIoProps}/>
<Image className="p-Home up_right_arrow_6 bpt" {...up_right_arrow_6Props} {...up_right_arrow_6Cb} {...up_right_arrow_6IoProps}/>
</Flex>
</Flex>
</Div>
</Div>
</Flex>
</Div>
<Div className="p-Home testimonials_main bpt" {...testimonials_mainProps} {...testimonials_mainCb} {...testimonials_mainIoProps}>
<Flex className="p-Home testimonials_headings_flex bpt" {...testimonials_headings_flexProps} {...testimonials_headings_flexCb} {...testimonials_headings_flexIoProps}>
<TextBox className="p-Home testimonials_heading_1 bpt" {...testimonials_heading_1Props} {...testimonials_heading_1Cb} {...testimonials_heading_1IoProps}/>
<TextBox className="p-Home testimonials_heading_2 bpt" {...testimonials_heading_2Props} {...testimonials_heading_2Cb} {...testimonials_heading_2IoProps}/>
</Flex>
<Flex className="p-Home testimonial_1_flex bpt" {...testimonial_1_flexProps} {...testimonial_1_flexCb} {...testimonial_1_flexIoProps}>
<Image className="p-Home testimonial_1_image bpt" {...testimonial_1_imageProps} {...testimonial_1_imageCb} {...testimonial_1_imageIoProps}/>
<Div className="p-Home testimonial_details bpt" {...testimonial_detailsProps} {...testimonial_detailsCb} {...testimonial_detailsIoProps}>
<Image className="p-Home double_quotes_image bpt" {...double_quotes_imageProps} {...double_quotes_imageCb} {...double_quotes_imageIoProps}/>
<Div className="p-Home detail_div bpt" {...detail_divProps} {...detail_divCb} {...detail_divIoProps}>
<TextBox className="p-Home detail bpt" {...detailProps} {...detailCb} {...detailIoProps}/>
</Div>
<Flex className="p-Home left_arrow_button bpt" {...left_arrow_buttonProps} {...left_arrow_buttonCb} {...left_arrow_buttonIoProps}>
<Image className="p-Home left_arrow bpt" {...left_arrowProps} {...left_arrowCb} {...left_arrowIoProps}/>
</Flex>
<Flex className="p-Home right_arrow_div bpt" {...right_arrow_divProps} {...right_arrow_divCb} {...right_arrow_divIoProps}>
<Image className="p-Home right_arrow bpt" {...right_arrowProps} {...right_arrowCb} {...right_arrowIoProps}/>
</Flex>
<Div className="p-Home testimonial_name_div bpt" {...testimonial_name_divProps} {...testimonial_name_divCb} {...testimonial_name_divIoProps}>
<TextBox className="p-Home testimonial_name bpt" {...testimonial_nameProps} {...testimonial_nameCb} {...testimonial_nameIoProps}/>
<TextBox className="p-Home testimonial_designation bpt" {...testimonial_designationProps} {...testimonial_designationCb} {...testimonial_designationIoProps}/>
</Div>
</Div>
</Flex>
</Div>
<Div className="p-Home faq_main bpt" {...faq_mainProps} {...faq_mainCb} {...faq_mainIoProps}>
<Div className="p-Home faq_heading_div bpt" {...faq_heading_divProps} {...faq_heading_divCb} {...faq_heading_divIoProps}>
<TextBox className="p-Home faq_heading bpt" {...faq_headingProps} {...faq_headingCb} {...faq_headingIoProps}/>
<TextBox className="p-Home faq_heading_2 bpt" {...faq_heading_2Props} {...faq_heading_2Cb} {...faq_heading_2IoProps}/>
</Div>
<Flex className="p-Home faq_list_main_flex bpt" {...faq_list_main_flexProps} {...faq_list_main_flexCb} {...faq_list_main_flexIoProps}>
<Flex className="p-Home faq_left_list bpt" {...faq_left_listProps} {...faq_left_listCb} {...faq_left_listIoProps}>
<Div className="p-Home faq_list_item_1 bpt" {...faq_list_item_1Props} {...faq_list_item_1Cb} {...faq_list_item_1IoProps}>
<Flex className="p-Home faq_list_heading_flex_1 bpt" {...faq_list_heading_flex_1Props} {...faq_list_heading_flex_1Cb} {...faq_list_heading_flex_1IoProps}>
<TextBox className="p-Home list_question_1 bpt" {...list_question_1Props} {...list_question_1Cb} {...list_question_1IoProps}/>
<Image className="p-Home list_down_arrow_1 bpt" {...list_down_arrow_1Props} {...list_down_arrow_1Cb} {...list_down_arrow_1IoProps}/>
</Flex>
</Div>
<Flex className="p-Home faq_list_item_2 bpt" {...faq_list_item_2Props} {...faq_list_item_2Cb} {...faq_list_item_2IoProps}>
<TextBox className="p-Home list_question_2 bpt" {...list_question_2Props} {...list_question_2Cb} {...list_question_2IoProps}/>
<Image className="p-Home list_down_arrow_2 bpt" {...list_down_arrow_2Props} {...list_down_arrow_2Cb} {...list_down_arrow_2IoProps}/>
</Flex>
<Flex className="p-Home faq_list_item_3 bpt" {...faq_list_item_3Props} {...faq_list_item_3Cb} {...faq_list_item_3IoProps}>
<TextBox className="p-Home list_question_3 bpt" {...list_question_3Props} {...list_question_3Cb} {...list_question_3IoProps}/>
<Image className="p-Home list_down_arrow_3 bpt" {...list_down_arrow_3Props} {...list_down_arrow_3Cb} {...list_down_arrow_3IoProps}/>
</Flex>
<Flex className="p-Home faq_list_item_4 bpt" {...faq_list_item_4Props} {...faq_list_item_4Cb} {...faq_list_item_4IoProps}>
<TextBox className="p-Home list_question_4 bpt" {...list_question_4Props} {...list_question_4Cb} {...list_question_4IoProps}/>
<Image className="p-Home list_down_arrow_4 bpt" {...list_down_arrow_4Props} {...list_down_arrow_4Cb} {...list_down_arrow_4IoProps}/>
</Flex>
</Flex>
<Flex className="p-Home faq_right_list bpt" {...faq_right_listProps} {...faq_right_listCb} {...faq_right_listIoProps}>
<Div className="p-Home faq_right_list_item_1 bpt" {...faq_right_list_item_1Props} {...faq_right_list_item_1Cb} {...faq_right_list_item_1IoProps}>
<Flex className="p-Home faq_right_list_heading_flex_1 bpt" {...faq_right_list_heading_flex_1Props} {...faq_right_list_heading_flex_1Cb} {...faq_right_list_heading_flex_1IoProps}>
<TextBox className="p-Home right_list_question_1 bpt" {...right_list_question_1Props} {...right_list_question_1Cb} {...right_list_question_1IoProps}/>
<Image className="p-Home list_down_arrow_5 bpt" {...list_down_arrow_5Props} {...list_down_arrow_5Cb} {...list_down_arrow_5IoProps}/>
</Flex>
</Div>
<Flex className="p-Home faq_right_list_item_2 bpt" {...faq_right_list_item_2Props} {...faq_right_list_item_2Cb} {...faq_right_list_item_2IoProps}>
<TextBox className="p-Home right_list_question_2 bpt" {...right_list_question_2Props} {...right_list_question_2Cb} {...right_list_question_2IoProps}/>
<Image className="p-Home list_down_arrow_6 bpt" {...list_down_arrow_6Props} {...list_down_arrow_6Cb} {...list_down_arrow_6IoProps}/>
</Flex>
<Flex className="p-Home faq_right_list_item_3 bpt" {...faq_right_list_item_3Props} {...faq_right_list_item_3Cb} {...faq_right_list_item_3IoProps}>
<TextBox className="p-Home right_list_question_3 bpt" {...right_list_question_3Props} {...right_list_question_3Cb} {...right_list_question_3IoProps}/>
<Image className="p-Home right_list_down_arrow_3 bpt" {...right_list_down_arrow_3Props} {...right_list_down_arrow_3Cb} {...right_list_down_arrow_3IoProps}/>
</Flex>
<Flex className="p-Home faq_right_list_item_4 bpt" {...faq_right_list_item_4Props} {...faq_right_list_item_4Cb} {...faq_right_list_item_4IoProps}>
<TextBox className="p-Home right_list_question_4 bpt" {...right_list_question_4Props} {...right_list_question_4Cb} {...right_list_question_4IoProps}/>
<Image className="p-Home right_list_down_arrow_4 bpt" {...right_list_down_arrow_4Props} {...right_list_down_arrow_4Cb} {...right_list_down_arrow_4IoProps}/>
</Flex>
</Flex>
</Flex>
</Div>
<Div className="p-Home footer_main_div bpt" {...footer_main_divProps} {...footer_main_divCb} {...footer_main_divIoProps}>
<Flex className="p-Home footer_headings_flex bpt" {...footer_headings_flexProps} {...footer_headings_flexCb} {...footer_headings_flexIoProps}>
<Div className="p-Home footer_heading_div bpt" {...footer_heading_divProps} {...footer_heading_divCb} {...footer_heading_divIoProps}>
<TextBox className="p-Home footer_heading_1 bpt" {...footer_heading_1Props} {...footer_heading_1Cb} {...footer_heading_1IoProps}/>
<TextBox className="p-Home footer_heading_2 bpt" {...footer_heading_2Props} {...footer_heading_2Cb} {...footer_heading_2IoProps}/>
</Div>
<Flex className="p-Home footer_links_flex bpt" {...footer_links_flexProps} {...footer_links_flexCb} {...footer_links_flexIoProps}>
<Div className="p-Home website_details_div bpt" {...website_details_divProps} {...website_details_divCb} {...website_details_divIoProps}>
<Image className="p-Home logo_link_image bpt" {...logo_link_imageProps} {...logo_link_imageCb} {...logo_link_imageIoProps}/>
<TextBox className="p-Home address_text bpt" {...address_textProps} {...address_textCb} {...address_textIoProps}/>
<Flex className="p-Home mail_flex bpt" {...mail_flexProps} {...mail_flexCb} {...mail_flexIoProps}>
<Image className="p-Home mail_icon_image bpt" {...mail_icon_imageProps} {...mail_icon_imageCb} {...mail_icon_imageIoProps}/>
<Link className="p-Home mail_link bpt" {...mail_linkProps} {...mail_linkCb} {...mail_linkIoProps}/>
</Flex>
</Div>
<Div className="p-Home links_grid bpt" {...links_gridProps} {...links_gridCb} {...links_gridIoProps}>
<Link className="p-Home footer_link_1 bpt" {...footer_link_1Props} {...footer_link_1Cb} {...footer_link_1IoProps}/>
<Link className="p-Home footer_link_2 bpt" {...footer_link_2Props} {...footer_link_2Cb} {...footer_link_2IoProps}/>
<Link className="p-Home footer_link_3 bpt" {...footer_link_3Props} {...footer_link_3Cb} {...footer_link_3IoProps}/>
<Link className="p-Home footer_link_5 bpt" {...footer_link_5Props} {...footer_link_5Cb} {...footer_link_5IoProps}/>
<Link className="p-Home footer_link_4 bpt" {...footer_link_4Props} {...footer_link_4Cb} {...footer_link_4IoProps}/>
<Link className="p-Home footer_link_6 bpt" {...footer_link_6Props} {...footer_link_6Cb} {...footer_link_6IoProps}/>
<Link className="p-Home footer_link_7 bpt" {...footer_link_7Props} {...footer_link_7Cb} {...footer_link_7IoProps}/>
<Link className="p-Home footer_link_8 bpt" {...footer_link_8Props} {...footer_link_8Cb} {...footer_link_8IoProps}/>
<Link className="p-Home footer_link_9 bpt" {...footer_link_9Props} {...footer_link_9Cb} {...footer_link_9IoProps}/>
</Div>
</Flex>
<Flex className="p-Home copyright_div bpt" {...copyright_divProps} {...copyright_divCb} {...copyright_divIoProps}>
<TextBox className="p-Home rights_text bpt" {...rights_textProps} {...rights_textCb} {...rights_textIoProps}/>
<Link className="p-Home Conversionflow_link bpt" {...Conversionflow_linkProps} {...Conversionflow_linkCb} {...Conversionflow_linkIoProps}/>
<TextBox className="p-Home powered_rext bpt" {...powered_rextProps} {...powered_rextCb} {...powered_rextIoProps}/>
<Link className="p-Home Webflow_link bpt" {...Webflow_linkProps} {...Webflow_linkCb} {...Webflow_linkIoProps}/>
<Link className="p-Home image_text_link bpt" {...image_text_linkProps} {...image_text_linkCb} {...image_text_linkIoProps}/>
<Link className="p-Home instructions_link bpt" {...instructions_linkProps} {...instructions_linkCb} {...instructions_linkIoProps}/>
<Link className="p-Home Changelog_link bpt" {...Changelog_linkProps} {...Changelog_linkCb} {...Changelog_linkIoProps}/>
<Link className="p-Home last_link bpt" {...last_linkProps} {...last_linkCb} {...last_linkIoProps}/>
</Flex>
<Div className="p-Home webflow_div bpt" {...webflow_divProps} {...webflow_divCb} {...webflow_divIoProps}>
<Image className="p-Home webflow_logo bpt" {...webflow_logoProps} {...webflow_logoCb} {...webflow_logoIoProps}/>
<Image className="p-Home webflow_text_image bpt" {...webflow_text_imageProps} {...webflow_text_imageCb} {...webflow_text_imageIoProps}/>
</Div>
</Flex>
</Div>
  </>);
}
