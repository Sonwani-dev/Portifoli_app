import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"nav_container":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"nav_bar_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"side_nav":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"hero_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"hero_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"heading_paragraph":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"hero_button_link":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"call_button_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"companies":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_main":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"sevices_head_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"head_2":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"sub_service_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_heading_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_1_paragraph1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_list_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_pointer_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_list_item_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex36":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_head_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex92":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex91":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_ponter_head_9ac":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex90":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div111":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_head_7":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div112":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div113":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"sub_service_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div118":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div119":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex96":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div117":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_head_4":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex94":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex95":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"projects_head_paragraph_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"projects_heading_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"heading_2_3_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"view_projects_button_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"projects_slider_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"projects_slider_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"project_slider_3_paragraph_head":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_3_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_item_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_item_2_head":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_item_2_link_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_item_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_item1_head_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex136":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"slider_button_left":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"sliderbutton_right":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"blogs_main_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"blogs_main_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"blogs_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"blogs_view_all_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"blog_list_div_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_1_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_1_date_time":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"heading_date_time_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_heading_2_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_1_read_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_2_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_2_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_2_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div166":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex158":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_3_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div168":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"point_div_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_3_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_3_link":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_4_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_4_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_4_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div172":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex164":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_5_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div174":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Flex167":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"vlist_5_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_5_link_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"pro_designer_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"designer_details_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"designer_deatails_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"designer_about_paragraph_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"designer_image_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"designer_2_image_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_main_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_left_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_1_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_1_year_1_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_2_year_2_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item__heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item__year_3_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_3_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div200":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_list_item_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_3_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_ist_item_3_year_3_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_list_item_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_2_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_ist_item_2_year_2_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_list_item_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_right_ist_item_1_year_1_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_1_heading_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"Div201":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"testimonials_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"testimonials_headings_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"testimonial_1_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"testimonial_details":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"detail_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"testimonial_name_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"left_arrow_button":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_arrow_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_main_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_left_list":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_item_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_heading_flex_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_item_4":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_item_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_list_item_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list_item_3":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list_item_2":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list_item_4":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list_item_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"faq_right_list_heading_flex_1":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"footer_main_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"footer_headings_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"footer_heading_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"footer_links_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"website_details_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"mail_flex":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"links_grid":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"copyright_div":{"styles":{"display":"","flexDirection":"row","alignItems":"stretch","justifyContent":"flex-start","flexWrap":"nowrap","alignContent":"stretch","rowGap":"","columnGap":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"webflow_div":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"trust_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"projects_view_button_back":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"logo_img":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"call_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"about_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"blog_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"project_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"services_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"nav_call_arrow":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"trusted_div_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"hero_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"heading_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"heading_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"paragraph":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"button_background":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"CV_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"call_button":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"company_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"company_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"company_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"company_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"projects_main":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"serices_paragraph":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"services_image_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_heading_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_paragraph_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"services_bullet_point_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_pointer_head_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div46":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"pointer_list_heading_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div47":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"services_image_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"Div109":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_heading_9":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div110":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_heading_8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"TextBox78":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div108":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_paragraph_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_heading_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"services_image_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_paragraph_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div114":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_pointer_head_5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div115":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_pointer_heading_6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Div116":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"projects_head_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"projects_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"projeccts_heading_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"view_projects_button":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":""}},"slider_3_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"slider_3_head_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_3_head_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_3_flex_head_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_3_head_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"slider_item_1_image_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"slider_item_2_head_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_item_2_product":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Image44":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"TextBox116":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_image_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"slider_item_1_head_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"slider_branding_head":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"arrow_image_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"slider_view_link_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"blog_left_arrow_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"blogs_right_arrow_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"heading_blogs":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"latest_blogs_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"view_all_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"arrow_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"heading_time":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"point_div1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"heading_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_item_1_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_1_read_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_link_arrow_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_arrow_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_2_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_item_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_item_2_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"point_div_2":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_item_2_time":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_3_time":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"point_div3":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_3_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_3_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_3_link_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"arrow_image_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"arrow_image_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_4_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_4_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_4_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"point_div_4":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_4_time":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_5_time":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"point_div_5":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"list_5_date_":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_5_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_5_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"arrow_image_5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"designer_heading_main":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"designer_about_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"designer_about_paragraph":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"designer_image_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"designer_image_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"designer_image_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"designer_image_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"education_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_border_div_1":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"experience_list_item_1_link_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"experience_list_item_1_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_item_1_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"up_right_arrow_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_border_div_2":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"up_right_arrow_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_item__date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_item_2_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"experience_list_item_2_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_border_div_3":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"up_right_arrow_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_item_3_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"experience_list_item_3_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"experience_list_item_3_link_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"list_border_div_6":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_3_image_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"experience_right_list_item_3_link_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"experience_right_list_item_3_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"right_list_item_3_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"up_right_arrow_6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_border_div_5":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_2_image_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"experience_right_list_item_2_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"experience_right_list_item_2_link_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"right_list_item_2_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"up_right_arrow_5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_border_div_4":{"styles":{"display":"","alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"}},"right_list_item_1_image_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"up_right_arrow_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"right_list_item_1_date":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"experience_right_list_item_1_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"experience_right_list_item_1_link_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"work_experience_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"testimonials_heading_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"testimonials_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"testimonial_1_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"double_quotes_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"detail":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"testimonial_name":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"testimonial_designation":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"left_arrow":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"right_arrow":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"faq_heading":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"faq_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_question_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_down_arrow_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_down_arrow_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_question_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_down_arrow_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_question_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_down_arrow_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_question_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"right_list_question_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"right_list_down_arrow_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"right_list_question_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"list_down_arrow_6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"right_list_question_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"right_list_down_arrow_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"list_down_arrow_5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"right_list_question_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"footer_heading_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"footer_heading_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"logo_link_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"address_text":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"mail_icon_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"mail_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_9":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_1":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_2":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_7":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_6":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_3":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_5":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_4":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"footer_link_8":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"rights_text":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Conversionflow_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"powered_rext":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Your text Here!"}},"Webflow_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"image_text_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"instructions_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"Changelog_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"last_link":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"text":"Link","url":"/"}},"webflow_logo":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}},"webflow_text_image":{"styles":{"alignSelf":"","flexGrow":"","flexShrink":"","order":"","marginTop":"","marginBottom":"","marginRight":"","marginLeft":"","paddingTop":"","paddingBottom":"","paddingRight":"","paddingLeft":"","width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":"","fontFamily":"","fontWeight":400,"fontSize":"","textAlign":"left","color":"","opacity":"","fontStyle":"","borderRadius":"","borderWidth":"","borderStyle":"","borderColor":"","backgroundImage":"","backgroundColor":"","backgroundClip":"","backgroundOrigin":"","backgroundAttachment":"","backgroundPositionX":"","backgroundPositionY":"","backgroundRepeat":"","position":"static","float":"none","clear":"none","top":"","left":"","bottom":"","right":"","zIndex":"","outlineStyle":"","outlineColor":"","outlineOffset":"","outlineWidth":"","cursor":"","boxSizing":"content-box"},"custom":{"alt":"No preview available","src":""}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.nav_container = state["nav_container"]
		self.nav_bar_div = state["nav_bar_div"]
		self.side_nav = state["side_nav"]
		self.hero_main = state["hero_main"]
		self.hero_flex = state["hero_flex"]
		self.heading_paragraph = state["heading_paragraph"]
		self.hero_button_link = state["hero_button_link"]
		self.call_button_div = state["call_button_div"]
		self.companies = state["companies"]
		self.services_div = state["services_div"]
		self.services_main = state["services_main"]
		self.sevices_head_main = state["sevices_head_main"]
		self.head_2 = state["head_2"]
		self.services_flex = state["services_flex"]
		self.sub_service_1 = state["sub_service_1"]
		self.services_heading_1 = state["services_heading_1"]
		self.services_1_paragraph1 = state["services_1_paragraph1"]
		self.services_list_1 = state["services_list_1"]
		self.services_pointer_1 = state["services_pointer_1"]
		self.services_list_item_1 = state["services_list_item_1"]
		self.Flex36 = state["Flex36"]
		self.list_pointer_head_3 = state["list_pointer_head_3"]
		self.Flex92 = state["Flex92"]
		self.Flex91 = state["Flex91"]
		self.list_ponter_head_9ac = state["list_ponter_head_9ac"]
		self.Flex90 = state["Flex90"]
		self.Div111 = state["Div111"]
		self.list_pointer_head_7 = state["list_pointer_head_7"]
		self.Div112 = state["Div112"]
		self.Div113 = state["Div113"]
		self.sub_service_2 = state["sub_service_2"]
		self.Div118 = state["Div118"]
		self.Div119 = state["Div119"]
		self.Flex96 = state["Flex96"]
		self.Div117 = state["Div117"]
		self.list_pointer_head_4 = state["list_pointer_head_4"]
		self.Flex94 = state["Flex94"]
		self.Flex95 = state["Flex95"]
		self.projects_head_paragraph_1 = state["projects_head_paragraph_1"]
		self.projects_heading_1 = state["projects_heading_1"]
		self.heading_2_3_div = state["heading_2_3_div"]
		self.view_projects_button_div = state["view_projects_button_div"]
		self.projects_slider_flex = state["projects_slider_flex"]
		self.projects_slider_3 = state["projects_slider_3"]
		self.project_slider_3_paragraph_head = state["project_slider_3_paragraph_head"]
		self.slider_3_link_flex = state["slider_3_link_flex"]
		self.slider_item_2 = state["slider_item_2"]
		self.slider_item_2_head = state["slider_item_2_head"]
		self.slider_item_2_link_2 = state["slider_item_2_link_2"]
		self.slider_item_1 = state["slider_item_1"]
		self.slider_item1_head_flex = state["slider_item1_head_flex"]
		self.Flex136 = state["Flex136"]
		self.slider_button_left = state["slider_button_left"]
		self.sliderbutton_right = state["sliderbutton_right"]
		self.blogs_main_div = state["blogs_main_div"]
		self.blogs_main_flex = state["blogs_main_flex"]
		self.blogs_heading_div = state["blogs_heading_div"]
		self.blogs_view_all_link_flex = state["blogs_view_all_link_flex"]
		self.blog_list_div_main = state["blog_list_div_main"]
		self.list_item_1_flex = state["list_item_1_flex"]
		self.list_item_1_date_time = state["list_item_1_date_time"]
		self.heading_date_time_flex = state["heading_date_time_flex"]
		self.list_heading_2_div = state["list_heading_2_div"]
		self.list_item_1_read_link_flex = state["list_item_1_read_link_flex"]
		self.list_item_2_flex = state["list_item_2_flex"]
		self.list_item_2_link_flex = state["list_item_2_link_flex"]
		self.list_item_2_heading_div = state["list_item_2_heading_div"]
		self.Div166 = state["Div166"]
		self.Flex158 = state["Flex158"]
		self.list_item_3_flex = state["list_item_3_flex"]
		self.Div168 = state["Div168"]
		self.point_div_3 = state["point_div_3"]
		self.list_3_heading_div = state["list_3_heading_div"]
		self.list_3_link = state["list_3_link"]
		self.list_item_4_flex = state["list_item_4_flex"]
		self.list_4_link_flex = state["list_4_link_flex"]
		self.list_4_heading_div = state["list_4_heading_div"]
		self.Div172 = state["Div172"]
		self.Flex164 = state["Flex164"]
		self.list_item_5_flex = state["list_item_5_flex"]
		self.Div174 = state["Div174"]
		self.Flex167 = state["Flex167"]
		self.vlist_5_heading_div = state["vlist_5_heading_div"]
		self.list_5_link_flex = state["list_5_link_flex"]
		self.pro_designer_main = state["pro_designer_main"]
		self.designer_details_flex = state["designer_details_flex"]
		self.designer_deatails_div = state["designer_deatails_div"]
		self.designer_about_paragraph_div = state["designer_about_paragraph_div"]
		self.designer_image_flex = state["designer_image_flex"]
		self.designer_2_image_flex = state["designer_2_image_flex"]
		self.experience_main_div = state["experience_main_div"]
		self.experience_flex = state["experience_flex"]
		self.experience_left_div = state["experience_left_div"]
		self.experience_heading_div = state["experience_heading_div"]
		self.experience_list = state["experience_list"]
		self.experience_list_item_1 = state["experience_list_item_1"]
		self.list_item_1_heading_div = state["list_item_1_heading_div"]
		self.experience_list_item_1_year_1_flex = state["experience_list_item_1_year_1_flex"]
		self.experience_list_item_2 = state["experience_list_item_2"]
		self.experience_list_item_2_year_2_flex = state["experience_list_item_2_year_2_flex"]
		self.list_item__heading_div = state["list_item__heading_div"]
		self.experience_list_item_3 = state["experience_list_item_3"]
		self.experience_list_item__year_3_flex = state["experience_list_item__year_3_flex"]
		self.list_item_3_heading_div = state["list_item_3_heading_div"]
		self.experience_right_div = state["experience_right_div"]
		self.Div200 = state["Div200"]
		self.experience_right_list_item_3 = state["experience_right_list_item_3"]
		self.right_list_item_3_heading_div = state["right_list_item_3_heading_div"]
		self.experience_right_ist_item_3_year_3_flex = state["experience_right_ist_item_3_year_3_flex"]
		self.experience_right_list_item_2 = state["experience_right_list_item_2"]
		self.right_list_item_2_heading_div = state["right_list_item_2_heading_div"]
		self.experience_right_ist_item_2_year_2_flex = state["experience_right_ist_item_2_year_2_flex"]
		self.experience_right_list_item_1 = state["experience_right_list_item_1"]
		self.experience_right_ist_item_1_year_1_flex = state["experience_right_ist_item_1_year_1_flex"]
		self.right_list_item_1_heading_div = state["right_list_item_1_heading_div"]
		self.Div201 = state["Div201"]
		self.testimonials_main = state["testimonials_main"]
		self.testimonials_headings_flex = state["testimonials_headings_flex"]
		self.testimonial_1_flex = state["testimonial_1_flex"]
		self.testimonial_details = state["testimonial_details"]
		self.detail_div = state["detail_div"]
		self.testimonial_name_div = state["testimonial_name_div"]
		self.left_arrow_button = state["left_arrow_button"]
		self.right_arrow_div = state["right_arrow_div"]
		self.faq_main = state["faq_main"]
		self.faq_heading_div = state["faq_heading_div"]
		self.faq_list_main_flex = state["faq_list_main_flex"]
		self.faq_left_list = state["faq_left_list"]
		self.faq_list_item_1 = state["faq_list_item_1"]
		self.faq_list_heading_flex_1 = state["faq_list_heading_flex_1"]
		self.faq_list_item_4 = state["faq_list_item_4"]
		self.faq_list_item_2 = state["faq_list_item_2"]
		self.faq_list_item_3 = state["faq_list_item_3"]
		self.faq_right_list = state["faq_right_list"]
		self.faq_right_list_item_3 = state["faq_right_list_item_3"]
		self.faq_right_list_item_2 = state["faq_right_list_item_2"]
		self.faq_right_list_item_4 = state["faq_right_list_item_4"]
		self.faq_right_list_item_1 = state["faq_right_list_item_1"]
		self.faq_right_list_heading_flex_1 = state["faq_right_list_heading_flex_1"]
		self.footer_main_div = state["footer_main_div"]
		self.footer_headings_flex = state["footer_headings_flex"]
		self.footer_heading_div = state["footer_heading_div"]
		self.footer_links_flex = state["footer_links_flex"]
		self.website_details_div = state["website_details_div"]
		self.mail_flex = state["mail_flex"]
		self.links_grid = state["links_grid"]
		self.copyright_div = state["copyright_div"]
		self.webflow_div = state["webflow_div"]
		self.trust_heading = state["trust_heading"]
		self.projects_view_button_back = state["projects_view_button_back"]
		self.logo_img = state["logo_img"]
		self.call_link = state["call_link"]
		self.about_link = state["about_link"]
		self.blog_link = state["blog_link"]
		self.project_link = state["project_link"]
		self.services_link = state["services_link"]
		self.nav_call_arrow = state["nav_call_arrow"]
		self.trusted_div_main = state["trusted_div_main"]
		self.hero_image = state["hero_image"]
		self.heading_1 = state["heading_1"]
		self.heading_2 = state["heading_2"]
		self.heading_3 = state["heading_3"]
		self.paragraph = state["paragraph"]
		self.button_background = state["button_background"]
		self.CV_link = state["CV_link"]
		self.call_button = state["call_button"]
		self.company_1 = state["company_1"]
		self.company_2 = state["company_2"]
		self.company_3 = state["company_3"]
		self.company_4 = state["company_4"]
		self.projects_main = state["projects_main"]
		self.services_heading = state["services_heading"]
		self.serices_paragraph = state["serices_paragraph"]
		self.services_image_1 = state["services_image_1"]
		self.list_heading_1 = state["list_heading_1"]
		self.list_paragraph_1 = state["list_paragraph_1"]
		self.services_bullet_point_1 = state["services_bullet_point_1"]
		self.list_pointer_heading = state["list_pointer_heading"]
		self.list_pointer_head_2 = state["list_pointer_head_2"]
		self.Div46 = state["Div46"]
		self.pointer_list_heading_3 = state["pointer_list_heading_3"]
		self.Div47 = state["Div47"]
		self.services_image_3 = state["services_image_3"]
		self.Div109 = state["Div109"]
		self.list_pointer_heading_9 = state["list_pointer_heading_9"]
		self.Div110 = state["Div110"]
		self.list_pointer_heading_8 = state["list_pointer_heading_8"]
		self.TextBox78 = state["TextBox78"]
		self.Div108 = state["Div108"]
		self.list_paragraph_3 = state["list_paragraph_3"]
		self.list_heading_3 = state["list_heading_3"]
		self.services_image_2 = state["services_image_2"]
		self.list_heading_2 = state["list_heading_2"]
		self.list_paragraph_2 = state["list_paragraph_2"]
		self.Div114 = state["Div114"]
		self.list_pointer_heading_2 = state["list_pointer_heading_2"]
		self.list_pointer_head_5 = state["list_pointer_head_5"]
		self.Div115 = state["Div115"]
		self.list_pointer_heading_6 = state["list_pointer_heading_6"]
		self.Div116 = state["Div116"]
		self.projects_head_1 = state["projects_head_1"]
		self.projects_heading_2 = state["projects_heading_2"]
		self.projeccts_heading_3 = state["projeccts_heading_3"]
		self.view_projects_button = state["view_projects_button"]
		self.slider_3_image = state["slider_3_image"]
		self.slider_3_head_1 = state["slider_3_head_1"]
		self.slider_3_head_2 = state["slider_3_head_2"]
		self.slider_3_flex_head_3 = state["slider_3_flex_head_3"]
		self.slider_3_head_image = state["slider_3_head_image"]
		self.slider_item_1_image_2 = state["slider_item_1_image_2"]
		self.slider_item_2_head_2 = state["slider_item_2_head_2"]
		self.slider_item_2_product = state["slider_item_2_product"]
		self.Image44 = state["Image44"]
		self.TextBox116 = state["TextBox116"]
		self.slider_image_1 = state["slider_image_1"]
		self.slider_item_1_head_2 = state["slider_item_1_head_2"]
		self.slider_branding_head = state["slider_branding_head"]
		self.arrow_image_1 = state["arrow_image_1"]
		self.slider_view_link_1 = state["slider_view_link_1"]
		self.blog_left_arrow_image = state["blog_left_arrow_image"]
		self.blogs_right_arrow_image = state["blogs_right_arrow_image"]
		self.heading_blogs = state["heading_blogs"]
		self.latest_blogs_heading = state["latest_blogs_heading"]
		self.view_all_link = state["view_all_link"]
		self.arrow_image = state["arrow_image"]
		self.heading_time = state["heading_time"]
		self.point_div1 = state["point_div1"]
		self.heading_date = state["heading_date"]
		self.list_item_1_heading_2 = state["list_item_1_heading_2"]
		self.list_1_read_link = state["list_1_read_link"]
		self.list_link_arrow_image = state["list_link_arrow_image"]
		self.list_arrow_image = state["list_arrow_image"]
		self.list_2_link = state["list_2_link"]
		self.list_item_heading_2 = state["list_item_heading_2"]
		self.list_item_2_date = state["list_item_2_date"]
		self.point_div_2 = state["point_div_2"]
		self.list_item_2_time = state["list_item_2_time"]
		self.list_3_time = state["list_3_time"]
		self.point_div3 = state["point_div3"]
		self.list_3_date = state["list_3_date"]
		self.list_3_heading = state["list_3_heading"]
		self.list_3_link_3 = state["list_3_link_3"]
		self.arrow_image_3 = state["arrow_image_3"]
		self.arrow_image_4 = state["arrow_image_4"]
		self.list_4_link = state["list_4_link"]
		self.list_4_heading = state["list_4_heading"]
		self.list_4_date = state["list_4_date"]
		self.point_div_4 = state["point_div_4"]
		self.list_4_time = state["list_4_time"]
		self.list_5_time = state["list_5_time"]
		self.point_div_5 = state["point_div_5"]
		self.list_5_date_ = state["list_5_date_"]
		self.list_5_heading = state["list_5_heading"]
		self.list_5_link = state["list_5_link"]
		self.arrow_image_5 = state["arrow_image_5"]
		self.designer_heading_main = state["designer_heading_main"]
		self.designer_about_heading_2 = state["designer_about_heading_2"]
		self.designer_about_paragraph = state["designer_about_paragraph"]
		self.designer_image_2 = state["designer_image_2"]
		self.designer_image_1 = state["designer_image_1"]
		self.designer_image_3 = state["designer_image_3"]
		self.designer_image_4 = state["designer_image_4"]
		self.education_heading = state["education_heading"]
		self.list_border_div_1 = state["list_border_div_1"]
		self.experience_list_item_1_link_1 = state["experience_list_item_1_link_1"]
		self.experience_list_item_1_heading = state["experience_list_item_1_heading"]
		self.list_item_1_date = state["list_item_1_date"]
		self.up_right_arrow_1 = state["up_right_arrow_1"]
		self.list_border_div_2 = state["list_border_div_2"]
		self.up_right_arrow_2 = state["up_right_arrow_2"]
		self.list_item__date = state["list_item__date"]
		self.list_item_2_link = state["list_item_2_link"]
		self.experience_list_item_2_heading = state["experience_list_item_2_heading"]
		self.list_border_div_3 = state["list_border_div_3"]
		self.up_right_arrow_3 = state["up_right_arrow_3"]
		self.list_item_3_date = state["list_item_3_date"]
		self.experience_list_item_3_heading = state["experience_list_item_3_heading"]
		self.experience_list_item_3_link_3 = state["experience_list_item_3_link_3"]
		self.list_border_div_6 = state["list_border_div_6"]
		self.right_list_item_3_image_3 = state["right_list_item_3_image_3"]
		self.experience_right_list_item_3_link_3 = state["experience_right_list_item_3_link_3"]
		self.experience_right_list_item_3_heading = state["experience_right_list_item_3_heading"]
		self.right_list_item_3_date = state["right_list_item_3_date"]
		self.up_right_arrow_6 = state["up_right_arrow_6"]
		self.list_border_div_5 = state["list_border_div_5"]
		self.right_list_item_2_image_2 = state["right_list_item_2_image_2"]
		self.experience_right_list_item_2_heading = state["experience_right_list_item_2_heading"]
		self.experience_right_list_item_2_link_2 = state["experience_right_list_item_2_link_2"]
		self.right_list_item_2_date = state["right_list_item_2_date"]
		self.up_right_arrow_5 = state["up_right_arrow_5"]
		self.list_border_div_4 = state["list_border_div_4"]
		self.right_list_item_1_image_1 = state["right_list_item_1_image_1"]
		self.up_right_arrow_4 = state["up_right_arrow_4"]
		self.right_list_item_1_date = state["right_list_item_1_date"]
		self.experience_right_list_item_1_heading = state["experience_right_list_item_1_heading"]
		self.experience_right_list_item_1_link_1 = state["experience_right_list_item_1_link_1"]
		self.work_experience_heading = state["work_experience_heading"]
		self.testimonials_heading_1 = state["testimonials_heading_1"]
		self.testimonials_heading_2 = state["testimonials_heading_2"]
		self.testimonial_1_image = state["testimonial_1_image"]
		self.double_quotes_image = state["double_quotes_image"]
		self.detail = state["detail"]
		self.testimonial_name = state["testimonial_name"]
		self.testimonial_designation = state["testimonial_designation"]
		self.left_arrow = state["left_arrow"]
		self.right_arrow = state["right_arrow"]
		self.faq_heading = state["faq_heading"]
		self.faq_heading_2 = state["faq_heading_2"]
		self.list_question_1 = state["list_question_1"]
		self.list_down_arrow_1 = state["list_down_arrow_1"]
		self.list_down_arrow_4 = state["list_down_arrow_4"]
		self.list_question_4 = state["list_question_4"]
		self.list_down_arrow_2 = state["list_down_arrow_2"]
		self.list_question_2 = state["list_question_2"]
		self.list_down_arrow_3 = state["list_down_arrow_3"]
		self.list_question_3 = state["list_question_3"]
		self.right_list_question_3 = state["right_list_question_3"]
		self.right_list_down_arrow_3 = state["right_list_down_arrow_3"]
		self.right_list_question_2 = state["right_list_question_2"]
		self.list_down_arrow_6 = state["list_down_arrow_6"]
		self.right_list_question_4 = state["right_list_question_4"]
		self.right_list_down_arrow_4 = state["right_list_down_arrow_4"]
		self.list_down_arrow_5 = state["list_down_arrow_5"]
		self.right_list_question_1 = state["right_list_question_1"]
		self.footer_heading_1 = state["footer_heading_1"]
		self.footer_heading_2 = state["footer_heading_2"]
		self.logo_link_image = state["logo_link_image"]
		self.address_text = state["address_text"]
		self.mail_icon_image = state["mail_icon_image"]
		self.mail_link = state["mail_link"]
		self.footer_link_9 = state["footer_link_9"]
		self.footer_link_1 = state["footer_link_1"]
		self.footer_link_2 = state["footer_link_2"]
		self.footer_link_7 = state["footer_link_7"]
		self.footer_link_6 = state["footer_link_6"]
		self.footer_link_3 = state["footer_link_3"]
		self.footer_link_5 = state["footer_link_5"]
		self.footer_link_4 = state["footer_link_4"]
		self.footer_link_8 = state["footer_link_8"]
		self.rights_text = state["rights_text"]
		self.Conversionflow_link = state["Conversionflow_link"]
		self.powered_rext = state["powered_rext"]
		self.Webflow_link = state["Webflow_link"]
		self.image_text_link = state["image_text_link"]
		self.instructions_link = state["instructions_link"]
		self.Changelog_link = state["Changelog_link"]
		self.last_link = state["last_link"]
		self.webflow_logo = state["webflow_logo"]
		self.webflow_text_image = state["webflow_text_image"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def nav_container(self):
		self._getter_access_tracker["nav_container"] = {}
		return self._nav_container
	@nav_container.setter
	def nav_container(self, new_state):
		self._setter_access_tracker["nav_container"] = {}
		global default_state
		self._nav_container = Div(new_state, default_state["nav_container"])

	@property
	def nav_bar_div(self):
		self._getter_access_tracker["nav_bar_div"] = {}
		return self._nav_bar_div
	@nav_bar_div.setter
	def nav_bar_div(self, new_state):
		self._setter_access_tracker["nav_bar_div"] = {}
		global default_state
		self._nav_bar_div = Flex(new_state, default_state["nav_bar_div"])

	@property
	def side_nav(self):
		self._getter_access_tracker["side_nav"] = {}
		return self._side_nav
	@side_nav.setter
	def side_nav(self, new_state):
		self._setter_access_tracker["side_nav"] = {}
		global default_state
		self._side_nav = Flex(new_state, default_state["side_nav"])

	@property
	def hero_main(self):
		self._getter_access_tracker["hero_main"] = {}
		return self._hero_main
	@hero_main.setter
	def hero_main(self, new_state):
		self._setter_access_tracker["hero_main"] = {}
		global default_state
		self._hero_main = Div(new_state, default_state["hero_main"])

	@property
	def hero_flex(self):
		self._getter_access_tracker["hero_flex"] = {}
		return self._hero_flex
	@hero_flex.setter
	def hero_flex(self, new_state):
		self._setter_access_tracker["hero_flex"] = {}
		global default_state
		self._hero_flex = Flex(new_state, default_state["hero_flex"])

	@property
	def heading_paragraph(self):
		self._getter_access_tracker["heading_paragraph"] = {}
		return self._heading_paragraph
	@heading_paragraph.setter
	def heading_paragraph(self, new_state):
		self._setter_access_tracker["heading_paragraph"] = {}
		global default_state
		self._heading_paragraph = Div(new_state, default_state["heading_paragraph"])

	@property
	def hero_button_link(self):
		self._getter_access_tracker["hero_button_link"] = {}
		return self._hero_button_link
	@hero_button_link.setter
	def hero_button_link(self, new_state):
		self._setter_access_tracker["hero_button_link"] = {}
		global default_state
		self._hero_button_link = Flex(new_state, default_state["hero_button_link"])

	@property
	def call_button_div(self):
		self._getter_access_tracker["call_button_div"] = {}
		return self._call_button_div
	@call_button_div.setter
	def call_button_div(self, new_state):
		self._setter_access_tracker["call_button_div"] = {}
		global default_state
		self._call_button_div = Div(new_state, default_state["call_button_div"])

	@property
	def companies(self):
		self._getter_access_tracker["companies"] = {}
		return self._companies
	@companies.setter
	def companies(self, new_state):
		self._setter_access_tracker["companies"] = {}
		global default_state
		self._companies = Flex(new_state, default_state["companies"])

	@property
	def services_div(self):
		self._getter_access_tracker["services_div"] = {}
		return self._services_div
	@services_div.setter
	def services_div(self, new_state):
		self._setter_access_tracker["services_div"] = {}
		global default_state
		self._services_div = Div(new_state, default_state["services_div"])

	@property
	def services_main(self):
		self._getter_access_tracker["services_main"] = {}
		return self._services_main
	@services_main.setter
	def services_main(self, new_state):
		self._setter_access_tracker["services_main"] = {}
		global default_state
		self._services_main = Flex(new_state, default_state["services_main"])

	@property
	def sevices_head_main(self):
		self._getter_access_tracker["sevices_head_main"] = {}
		return self._sevices_head_main
	@sevices_head_main.setter
	def sevices_head_main(self, new_state):
		self._setter_access_tracker["sevices_head_main"] = {}
		global default_state
		self._sevices_head_main = Div(new_state, default_state["sevices_head_main"])

	@property
	def head_2(self):
		self._getter_access_tracker["head_2"] = {}
		return self._head_2
	@head_2.setter
	def head_2(self, new_state):
		self._setter_access_tracker["head_2"] = {}
		global default_state
		self._head_2 = Div(new_state, default_state["head_2"])

	@property
	def services_flex(self):
		self._getter_access_tracker["services_flex"] = {}
		return self._services_flex
	@services_flex.setter
	def services_flex(self, new_state):
		self._setter_access_tracker["services_flex"] = {}
		global default_state
		self._services_flex = Flex(new_state, default_state["services_flex"])

	@property
	def sub_service_1(self):
		self._getter_access_tracker["sub_service_1"] = {}
		return self._sub_service_1
	@sub_service_1.setter
	def sub_service_1(self, new_state):
		self._setter_access_tracker["sub_service_1"] = {}
		global default_state
		self._sub_service_1 = Flex(new_state, default_state["sub_service_1"])

	@property
	def services_heading_1(self):
		self._getter_access_tracker["services_heading_1"] = {}
		return self._services_heading_1
	@services_heading_1.setter
	def services_heading_1(self, new_state):
		self._setter_access_tracker["services_heading_1"] = {}
		global default_state
		self._services_heading_1 = Div(new_state, default_state["services_heading_1"])

	@property
	def services_1_paragraph1(self):
		self._getter_access_tracker["services_1_paragraph1"] = {}
		return self._services_1_paragraph1
	@services_1_paragraph1.setter
	def services_1_paragraph1(self, new_state):
		self._setter_access_tracker["services_1_paragraph1"] = {}
		global default_state
		self._services_1_paragraph1 = Div(new_state, default_state["services_1_paragraph1"])

	@property
	def services_list_1(self):
		self._getter_access_tracker["services_list_1"] = {}
		return self._services_list_1
	@services_list_1.setter
	def services_list_1(self, new_state):
		self._setter_access_tracker["services_list_1"] = {}
		global default_state
		self._services_list_1 = Flex(new_state, default_state["services_list_1"])

	@property
	def services_pointer_1(self):
		self._getter_access_tracker["services_pointer_1"] = {}
		return self._services_pointer_1
	@services_pointer_1.setter
	def services_pointer_1(self, new_state):
		self._setter_access_tracker["services_pointer_1"] = {}
		global default_state
		self._services_pointer_1 = Div(new_state, default_state["services_pointer_1"])

	@property
	def services_list_item_1(self):
		self._getter_access_tracker["services_list_item_1"] = {}
		return self._services_list_item_1
	@services_list_item_1.setter
	def services_list_item_1(self, new_state):
		self._setter_access_tracker["services_list_item_1"] = {}
		global default_state
		self._services_list_item_1 = Flex(new_state, default_state["services_list_item_1"])

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		global default_state
		self._Flex36 = Flex(new_state, default_state["Flex36"])

	@property
	def list_pointer_head_3(self):
		self._getter_access_tracker["list_pointer_head_3"] = {}
		return self._list_pointer_head_3
	@list_pointer_head_3.setter
	def list_pointer_head_3(self, new_state):
		self._setter_access_tracker["list_pointer_head_3"] = {}
		global default_state
		self._list_pointer_head_3 = Flex(new_state, default_state["list_pointer_head_3"])

	@property
	def Flex92(self):
		self._getter_access_tracker["Flex92"] = {}
		return self._Flex92
	@Flex92.setter
	def Flex92(self, new_state):
		self._setter_access_tracker["Flex92"] = {}
		global default_state
		self._Flex92 = Flex(new_state, default_state["Flex92"])

	@property
	def Flex91(self):
		self._getter_access_tracker["Flex91"] = {}
		return self._Flex91
	@Flex91.setter
	def Flex91(self, new_state):
		self._setter_access_tracker["Flex91"] = {}
		global default_state
		self._Flex91 = Flex(new_state, default_state["Flex91"])

	@property
	def list_ponter_head_9ac(self):
		self._getter_access_tracker["list_ponter_head_9ac"] = {}
		return self._list_ponter_head_9ac
	@list_ponter_head_9ac.setter
	def list_ponter_head_9ac(self, new_state):
		self._setter_access_tracker["list_ponter_head_9ac"] = {}
		global default_state
		self._list_ponter_head_9ac = Flex(new_state, default_state["list_ponter_head_9ac"])

	@property
	def Flex90(self):
		self._getter_access_tracker["Flex90"] = {}
		return self._Flex90
	@Flex90.setter
	def Flex90(self, new_state):
		self._setter_access_tracker["Flex90"] = {}
		global default_state
		self._Flex90 = Flex(new_state, default_state["Flex90"])

	@property
	def Div111(self):
		self._getter_access_tracker["Div111"] = {}
		return self._Div111
	@Div111.setter
	def Div111(self, new_state):
		self._setter_access_tracker["Div111"] = {}
		global default_state
		self._Div111 = Div(new_state, default_state["Div111"])

	@property
	def list_pointer_head_7(self):
		self._getter_access_tracker["list_pointer_head_7"] = {}
		return self._list_pointer_head_7
	@list_pointer_head_7.setter
	def list_pointer_head_7(self, new_state):
		self._setter_access_tracker["list_pointer_head_7"] = {}
		global default_state
		self._list_pointer_head_7 = Flex(new_state, default_state["list_pointer_head_7"])

	@property
	def Div112(self):
		self._getter_access_tracker["Div112"] = {}
		return self._Div112
	@Div112.setter
	def Div112(self, new_state):
		self._setter_access_tracker["Div112"] = {}
		global default_state
		self._Div112 = Div(new_state, default_state["Div112"])

	@property
	def Div113(self):
		self._getter_access_tracker["Div113"] = {}
		return self._Div113
	@Div113.setter
	def Div113(self, new_state):
		self._setter_access_tracker["Div113"] = {}
		global default_state
		self._Div113 = Div(new_state, default_state["Div113"])

	@property
	def sub_service_2(self):
		self._getter_access_tracker["sub_service_2"] = {}
		return self._sub_service_2
	@sub_service_2.setter
	def sub_service_2(self, new_state):
		self._setter_access_tracker["sub_service_2"] = {}
		global default_state
		self._sub_service_2 = Flex(new_state, default_state["sub_service_2"])

	@property
	def Div118(self):
		self._getter_access_tracker["Div118"] = {}
		return self._Div118
	@Div118.setter
	def Div118(self, new_state):
		self._setter_access_tracker["Div118"] = {}
		global default_state
		self._Div118 = Div(new_state, default_state["Div118"])

	@property
	def Div119(self):
		self._getter_access_tracker["Div119"] = {}
		return self._Div119
	@Div119.setter
	def Div119(self, new_state):
		self._setter_access_tracker["Div119"] = {}
		global default_state
		self._Div119 = Div(new_state, default_state["Div119"])

	@property
	def Flex96(self):
		self._getter_access_tracker["Flex96"] = {}
		return self._Flex96
	@Flex96.setter
	def Flex96(self, new_state):
		self._setter_access_tracker["Flex96"] = {}
		global default_state
		self._Flex96 = Flex(new_state, default_state["Flex96"])

	@property
	def Div117(self):
		self._getter_access_tracker["Div117"] = {}
		return self._Div117
	@Div117.setter
	def Div117(self, new_state):
		self._setter_access_tracker["Div117"] = {}
		global default_state
		self._Div117 = Div(new_state, default_state["Div117"])

	@property
	def list_pointer_head_4(self):
		self._getter_access_tracker["list_pointer_head_4"] = {}
		return self._list_pointer_head_4
	@list_pointer_head_4.setter
	def list_pointer_head_4(self, new_state):
		self._setter_access_tracker["list_pointer_head_4"] = {}
		global default_state
		self._list_pointer_head_4 = Flex(new_state, default_state["list_pointer_head_4"])

	@property
	def Flex94(self):
		self._getter_access_tracker["Flex94"] = {}
		return self._Flex94
	@Flex94.setter
	def Flex94(self, new_state):
		self._setter_access_tracker["Flex94"] = {}
		global default_state
		self._Flex94 = Flex(new_state, default_state["Flex94"])

	@property
	def Flex95(self):
		self._getter_access_tracker["Flex95"] = {}
		return self._Flex95
	@Flex95.setter
	def Flex95(self, new_state):
		self._setter_access_tracker["Flex95"] = {}
		global default_state
		self._Flex95 = Flex(new_state, default_state["Flex95"])

	@property
	def projects_head_paragraph_1(self):
		self._getter_access_tracker["projects_head_paragraph_1"] = {}
		return self._projects_head_paragraph_1
	@projects_head_paragraph_1.setter
	def projects_head_paragraph_1(self, new_state):
		self._setter_access_tracker["projects_head_paragraph_1"] = {}
		global default_state
		self._projects_head_paragraph_1 = Flex(new_state, default_state["projects_head_paragraph_1"])

	@property
	def projects_heading_1(self):
		self._getter_access_tracker["projects_heading_1"] = {}
		return self._projects_heading_1
	@projects_heading_1.setter
	def projects_heading_1(self, new_state):
		self._setter_access_tracker["projects_heading_1"] = {}
		global default_state
		self._projects_heading_1 = Flex(new_state, default_state["projects_heading_1"])

	@property
	def heading_2_3_div(self):
		self._getter_access_tracker["heading_2_3_div"] = {}
		return self._heading_2_3_div
	@heading_2_3_div.setter
	def heading_2_3_div(self, new_state):
		self._setter_access_tracker["heading_2_3_div"] = {}
		global default_state
		self._heading_2_3_div = Div(new_state, default_state["heading_2_3_div"])

	@property
	def view_projects_button_div(self):
		self._getter_access_tracker["view_projects_button_div"] = {}
		return self._view_projects_button_div
	@view_projects_button_div.setter
	def view_projects_button_div(self, new_state):
		self._setter_access_tracker["view_projects_button_div"] = {}
		global default_state
		self._view_projects_button_div = Div(new_state, default_state["view_projects_button_div"])

	@property
	def projects_slider_flex(self):
		self._getter_access_tracker["projects_slider_flex"] = {}
		return self._projects_slider_flex
	@projects_slider_flex.setter
	def projects_slider_flex(self, new_state):
		self._setter_access_tracker["projects_slider_flex"] = {}
		global default_state
		self._projects_slider_flex = Flex(new_state, default_state["projects_slider_flex"])

	@property
	def projects_slider_3(self):
		self._getter_access_tracker["projects_slider_3"] = {}
		return self._projects_slider_3
	@projects_slider_3.setter
	def projects_slider_3(self, new_state):
		self._setter_access_tracker["projects_slider_3"] = {}
		global default_state
		self._projects_slider_3 = Flex(new_state, default_state["projects_slider_3"])

	@property
	def project_slider_3_paragraph_head(self):
		self._getter_access_tracker["project_slider_3_paragraph_head"] = {}
		return self._project_slider_3_paragraph_head
	@project_slider_3_paragraph_head.setter
	def project_slider_3_paragraph_head(self, new_state):
		self._setter_access_tracker["project_slider_3_paragraph_head"] = {}
		global default_state
		self._project_slider_3_paragraph_head = Flex(new_state, default_state["project_slider_3_paragraph_head"])

	@property
	def slider_3_link_flex(self):
		self._getter_access_tracker["slider_3_link_flex"] = {}
		return self._slider_3_link_flex
	@slider_3_link_flex.setter
	def slider_3_link_flex(self, new_state):
		self._setter_access_tracker["slider_3_link_flex"] = {}
		global default_state
		self._slider_3_link_flex = Flex(new_state, default_state["slider_3_link_flex"])

	@property
	def slider_item_2(self):
		self._getter_access_tracker["slider_item_2"] = {}
		return self._slider_item_2
	@slider_item_2.setter
	def slider_item_2(self, new_state):
		self._setter_access_tracker["slider_item_2"] = {}
		global default_state
		self._slider_item_2 = Flex(new_state, default_state["slider_item_2"])

	@property
	def slider_item_2_head(self):
		self._getter_access_tracker["slider_item_2_head"] = {}
		return self._slider_item_2_head
	@slider_item_2_head.setter
	def slider_item_2_head(self, new_state):
		self._setter_access_tracker["slider_item_2_head"] = {}
		global default_state
		self._slider_item_2_head = Flex(new_state, default_state["slider_item_2_head"])

	@property
	def slider_item_2_link_2(self):
		self._getter_access_tracker["slider_item_2_link_2"] = {}
		return self._slider_item_2_link_2
	@slider_item_2_link_2.setter
	def slider_item_2_link_2(self, new_state):
		self._setter_access_tracker["slider_item_2_link_2"] = {}
		global default_state
		self._slider_item_2_link_2 = Flex(new_state, default_state["slider_item_2_link_2"])

	@property
	def slider_item_1(self):
		self._getter_access_tracker["slider_item_1"] = {}
		return self._slider_item_1
	@slider_item_1.setter
	def slider_item_1(self, new_state):
		self._setter_access_tracker["slider_item_1"] = {}
		global default_state
		self._slider_item_1 = Flex(new_state, default_state["slider_item_1"])

	@property
	def slider_item1_head_flex(self):
		self._getter_access_tracker["slider_item1_head_flex"] = {}
		return self._slider_item1_head_flex
	@slider_item1_head_flex.setter
	def slider_item1_head_flex(self, new_state):
		self._setter_access_tracker["slider_item1_head_flex"] = {}
		global default_state
		self._slider_item1_head_flex = Flex(new_state, default_state["slider_item1_head_flex"])

	@property
	def Flex136(self):
		self._getter_access_tracker["Flex136"] = {}
		return self._Flex136
	@Flex136.setter
	def Flex136(self, new_state):
		self._setter_access_tracker["Flex136"] = {}
		global default_state
		self._Flex136 = Flex(new_state, default_state["Flex136"])

	@property
	def slider_button_left(self):
		self._getter_access_tracker["slider_button_left"] = {}
		return self._slider_button_left
	@slider_button_left.setter
	def slider_button_left(self, new_state):
		self._setter_access_tracker["slider_button_left"] = {}
		global default_state
		self._slider_button_left = Flex(new_state, default_state["slider_button_left"])

	@property
	def sliderbutton_right(self):
		self._getter_access_tracker["sliderbutton_right"] = {}
		return self._sliderbutton_right
	@sliderbutton_right.setter
	def sliderbutton_right(self, new_state):
		self._setter_access_tracker["sliderbutton_right"] = {}
		global default_state
		self._sliderbutton_right = Flex(new_state, default_state["sliderbutton_right"])

	@property
	def blogs_main_div(self):
		self._getter_access_tracker["blogs_main_div"] = {}
		return self._blogs_main_div
	@blogs_main_div.setter
	def blogs_main_div(self, new_state):
		self._setter_access_tracker["blogs_main_div"] = {}
		global default_state
		self._blogs_main_div = Div(new_state, default_state["blogs_main_div"])

	@property
	def blogs_main_flex(self):
		self._getter_access_tracker["blogs_main_flex"] = {}
		return self._blogs_main_flex
	@blogs_main_flex.setter
	def blogs_main_flex(self, new_state):
		self._setter_access_tracker["blogs_main_flex"] = {}
		global default_state
		self._blogs_main_flex = Flex(new_state, default_state["blogs_main_flex"])

	@property
	def blogs_heading_div(self):
		self._getter_access_tracker["blogs_heading_div"] = {}
		return self._blogs_heading_div
	@blogs_heading_div.setter
	def blogs_heading_div(self, new_state):
		self._setter_access_tracker["blogs_heading_div"] = {}
		global default_state
		self._blogs_heading_div = Flex(new_state, default_state["blogs_heading_div"])

	@property
	def blogs_view_all_link_flex(self):
		self._getter_access_tracker["blogs_view_all_link_flex"] = {}
		return self._blogs_view_all_link_flex
	@blogs_view_all_link_flex.setter
	def blogs_view_all_link_flex(self, new_state):
		self._setter_access_tracker["blogs_view_all_link_flex"] = {}
		global default_state
		self._blogs_view_all_link_flex = Flex(new_state, default_state["blogs_view_all_link_flex"])

	@property
	def blog_list_div_main(self):
		self._getter_access_tracker["blog_list_div_main"] = {}
		return self._blog_list_div_main
	@blog_list_div_main.setter
	def blog_list_div_main(self, new_state):
		self._setter_access_tracker["blog_list_div_main"] = {}
		global default_state
		self._blog_list_div_main = Div(new_state, default_state["blog_list_div_main"])

	@property
	def list_item_1_flex(self):
		self._getter_access_tracker["list_item_1_flex"] = {}
		return self._list_item_1_flex
	@list_item_1_flex.setter
	def list_item_1_flex(self, new_state):
		self._setter_access_tracker["list_item_1_flex"] = {}
		global default_state
		self._list_item_1_flex = Flex(new_state, default_state["list_item_1_flex"])

	@property
	def list_item_1_date_time(self):
		self._getter_access_tracker["list_item_1_date_time"] = {}
		return self._list_item_1_date_time
	@list_item_1_date_time.setter
	def list_item_1_date_time(self, new_state):
		self._setter_access_tracker["list_item_1_date_time"] = {}
		global default_state
		self._list_item_1_date_time = Div(new_state, default_state["list_item_1_date_time"])

	@property
	def heading_date_time_flex(self):
		self._getter_access_tracker["heading_date_time_flex"] = {}
		return self._heading_date_time_flex
	@heading_date_time_flex.setter
	def heading_date_time_flex(self, new_state):
		self._setter_access_tracker["heading_date_time_flex"] = {}
		global default_state
		self._heading_date_time_flex = Flex(new_state, default_state["heading_date_time_flex"])

	@property
	def list_heading_2_div(self):
		self._getter_access_tracker["list_heading_2_div"] = {}
		return self._list_heading_2_div
	@list_heading_2_div.setter
	def list_heading_2_div(self, new_state):
		self._setter_access_tracker["list_heading_2_div"] = {}
		global default_state
		self._list_heading_2_div = Div(new_state, default_state["list_heading_2_div"])

	@property
	def list_item_1_read_link_flex(self):
		self._getter_access_tracker["list_item_1_read_link_flex"] = {}
		return self._list_item_1_read_link_flex
	@list_item_1_read_link_flex.setter
	def list_item_1_read_link_flex(self, new_state):
		self._setter_access_tracker["list_item_1_read_link_flex"] = {}
		global default_state
		self._list_item_1_read_link_flex = Flex(new_state, default_state["list_item_1_read_link_flex"])

	@property
	def list_item_2_flex(self):
		self._getter_access_tracker["list_item_2_flex"] = {}
		return self._list_item_2_flex
	@list_item_2_flex.setter
	def list_item_2_flex(self, new_state):
		self._setter_access_tracker["list_item_2_flex"] = {}
		global default_state
		self._list_item_2_flex = Flex(new_state, default_state["list_item_2_flex"])

	@property
	def list_item_2_link_flex(self):
		self._getter_access_tracker["list_item_2_link_flex"] = {}
		return self._list_item_2_link_flex
	@list_item_2_link_flex.setter
	def list_item_2_link_flex(self, new_state):
		self._setter_access_tracker["list_item_2_link_flex"] = {}
		global default_state
		self._list_item_2_link_flex = Flex(new_state, default_state["list_item_2_link_flex"])

	@property
	def list_item_2_heading_div(self):
		self._getter_access_tracker["list_item_2_heading_div"] = {}
		return self._list_item_2_heading_div
	@list_item_2_heading_div.setter
	def list_item_2_heading_div(self, new_state):
		self._setter_access_tracker["list_item_2_heading_div"] = {}
		global default_state
		self._list_item_2_heading_div = Div(new_state, default_state["list_item_2_heading_div"])

	@property
	def Div166(self):
		self._getter_access_tracker["Div166"] = {}
		return self._Div166
	@Div166.setter
	def Div166(self, new_state):
		self._setter_access_tracker["Div166"] = {}
		global default_state
		self._Div166 = Div(new_state, default_state["Div166"])

	@property
	def Flex158(self):
		self._getter_access_tracker["Flex158"] = {}
		return self._Flex158
	@Flex158.setter
	def Flex158(self, new_state):
		self._setter_access_tracker["Flex158"] = {}
		global default_state
		self._Flex158 = Flex(new_state, default_state["Flex158"])

	@property
	def list_item_3_flex(self):
		self._getter_access_tracker["list_item_3_flex"] = {}
		return self._list_item_3_flex
	@list_item_3_flex.setter
	def list_item_3_flex(self, new_state):
		self._setter_access_tracker["list_item_3_flex"] = {}
		global default_state
		self._list_item_3_flex = Flex(new_state, default_state["list_item_3_flex"])

	@property
	def Div168(self):
		self._getter_access_tracker["Div168"] = {}
		return self._Div168
	@Div168.setter
	def Div168(self, new_state):
		self._setter_access_tracker["Div168"] = {}
		global default_state
		self._Div168 = Div(new_state, default_state["Div168"])

	@property
	def point_div_3(self):
		self._getter_access_tracker["point_div_3"] = {}
		return self._point_div_3
	@point_div_3.setter
	def point_div_3(self, new_state):
		self._setter_access_tracker["point_div_3"] = {}
		global default_state
		self._point_div_3 = Flex(new_state, default_state["point_div_3"])

	@property
	def list_3_heading_div(self):
		self._getter_access_tracker["list_3_heading_div"] = {}
		return self._list_3_heading_div
	@list_3_heading_div.setter
	def list_3_heading_div(self, new_state):
		self._setter_access_tracker["list_3_heading_div"] = {}
		global default_state
		self._list_3_heading_div = Div(new_state, default_state["list_3_heading_div"])

	@property
	def list_3_link(self):
		self._getter_access_tracker["list_3_link"] = {}
		return self._list_3_link
	@list_3_link.setter
	def list_3_link(self, new_state):
		self._setter_access_tracker["list_3_link"] = {}
		global default_state
		self._list_3_link = Flex(new_state, default_state["list_3_link"])

	@property
	def list_item_4_flex(self):
		self._getter_access_tracker["list_item_4_flex"] = {}
		return self._list_item_4_flex
	@list_item_4_flex.setter
	def list_item_4_flex(self, new_state):
		self._setter_access_tracker["list_item_4_flex"] = {}
		global default_state
		self._list_item_4_flex = Flex(new_state, default_state["list_item_4_flex"])

	@property
	def list_4_link_flex(self):
		self._getter_access_tracker["list_4_link_flex"] = {}
		return self._list_4_link_flex
	@list_4_link_flex.setter
	def list_4_link_flex(self, new_state):
		self._setter_access_tracker["list_4_link_flex"] = {}
		global default_state
		self._list_4_link_flex = Flex(new_state, default_state["list_4_link_flex"])

	@property
	def list_4_heading_div(self):
		self._getter_access_tracker["list_4_heading_div"] = {}
		return self._list_4_heading_div
	@list_4_heading_div.setter
	def list_4_heading_div(self, new_state):
		self._setter_access_tracker["list_4_heading_div"] = {}
		global default_state
		self._list_4_heading_div = Div(new_state, default_state["list_4_heading_div"])

	@property
	def Div172(self):
		self._getter_access_tracker["Div172"] = {}
		return self._Div172
	@Div172.setter
	def Div172(self, new_state):
		self._setter_access_tracker["Div172"] = {}
		global default_state
		self._Div172 = Div(new_state, default_state["Div172"])

	@property
	def Flex164(self):
		self._getter_access_tracker["Flex164"] = {}
		return self._Flex164
	@Flex164.setter
	def Flex164(self, new_state):
		self._setter_access_tracker["Flex164"] = {}
		global default_state
		self._Flex164 = Flex(new_state, default_state["Flex164"])

	@property
	def list_item_5_flex(self):
		self._getter_access_tracker["list_item_5_flex"] = {}
		return self._list_item_5_flex
	@list_item_5_flex.setter
	def list_item_5_flex(self, new_state):
		self._setter_access_tracker["list_item_5_flex"] = {}
		global default_state
		self._list_item_5_flex = Flex(new_state, default_state["list_item_5_flex"])

	@property
	def Div174(self):
		self._getter_access_tracker["Div174"] = {}
		return self._Div174
	@Div174.setter
	def Div174(self, new_state):
		self._setter_access_tracker["Div174"] = {}
		global default_state
		self._Div174 = Div(new_state, default_state["Div174"])

	@property
	def Flex167(self):
		self._getter_access_tracker["Flex167"] = {}
		return self._Flex167
	@Flex167.setter
	def Flex167(self, new_state):
		self._setter_access_tracker["Flex167"] = {}
		global default_state
		self._Flex167 = Flex(new_state, default_state["Flex167"])

	@property
	def vlist_5_heading_div(self):
		self._getter_access_tracker["vlist_5_heading_div"] = {}
		return self._vlist_5_heading_div
	@vlist_5_heading_div.setter
	def vlist_5_heading_div(self, new_state):
		self._setter_access_tracker["vlist_5_heading_div"] = {}
		global default_state
		self._vlist_5_heading_div = Div(new_state, default_state["vlist_5_heading_div"])

	@property
	def list_5_link_flex(self):
		self._getter_access_tracker["list_5_link_flex"] = {}
		return self._list_5_link_flex
	@list_5_link_flex.setter
	def list_5_link_flex(self, new_state):
		self._setter_access_tracker["list_5_link_flex"] = {}
		global default_state
		self._list_5_link_flex = Flex(new_state, default_state["list_5_link_flex"])

	@property
	def pro_designer_main(self):
		self._getter_access_tracker["pro_designer_main"] = {}
		return self._pro_designer_main
	@pro_designer_main.setter
	def pro_designer_main(self, new_state):
		self._setter_access_tracker["pro_designer_main"] = {}
		global default_state
		self._pro_designer_main = Div(new_state, default_state["pro_designer_main"])

	@property
	def designer_details_flex(self):
		self._getter_access_tracker["designer_details_flex"] = {}
		return self._designer_details_flex
	@designer_details_flex.setter
	def designer_details_flex(self, new_state):
		self._setter_access_tracker["designer_details_flex"] = {}
		global default_state
		self._designer_details_flex = Flex(new_state, default_state["designer_details_flex"])

	@property
	def designer_deatails_div(self):
		self._getter_access_tracker["designer_deatails_div"] = {}
		return self._designer_deatails_div
	@designer_deatails_div.setter
	def designer_deatails_div(self, new_state):
		self._setter_access_tracker["designer_deatails_div"] = {}
		global default_state
		self._designer_deatails_div = Div(new_state, default_state["designer_deatails_div"])

	@property
	def designer_about_paragraph_div(self):
		self._getter_access_tracker["designer_about_paragraph_div"] = {}
		return self._designer_about_paragraph_div
	@designer_about_paragraph_div.setter
	def designer_about_paragraph_div(self, new_state):
		self._setter_access_tracker["designer_about_paragraph_div"] = {}
		global default_state
		self._designer_about_paragraph_div = Div(new_state, default_state["designer_about_paragraph_div"])

	@property
	def designer_image_flex(self):
		self._getter_access_tracker["designer_image_flex"] = {}
		return self._designer_image_flex
	@designer_image_flex.setter
	def designer_image_flex(self, new_state):
		self._setter_access_tracker["designer_image_flex"] = {}
		global default_state
		self._designer_image_flex = Flex(new_state, default_state["designer_image_flex"])

	@property
	def designer_2_image_flex(self):
		self._getter_access_tracker["designer_2_image_flex"] = {}
		return self._designer_2_image_flex
	@designer_2_image_flex.setter
	def designer_2_image_flex(self, new_state):
		self._setter_access_tracker["designer_2_image_flex"] = {}
		global default_state
		self._designer_2_image_flex = Flex(new_state, default_state["designer_2_image_flex"])

	@property
	def experience_main_div(self):
		self._getter_access_tracker["experience_main_div"] = {}
		return self._experience_main_div
	@experience_main_div.setter
	def experience_main_div(self, new_state):
		self._setter_access_tracker["experience_main_div"] = {}
		global default_state
		self._experience_main_div = Div(new_state, default_state["experience_main_div"])

	@property
	def experience_flex(self):
		self._getter_access_tracker["experience_flex"] = {}
		return self._experience_flex
	@experience_flex.setter
	def experience_flex(self, new_state):
		self._setter_access_tracker["experience_flex"] = {}
		global default_state
		self._experience_flex = Flex(new_state, default_state["experience_flex"])

	@property
	def experience_left_div(self):
		self._getter_access_tracker["experience_left_div"] = {}
		return self._experience_left_div
	@experience_left_div.setter
	def experience_left_div(self, new_state):
		self._setter_access_tracker["experience_left_div"] = {}
		global default_state
		self._experience_left_div = Div(new_state, default_state["experience_left_div"])

	@property
	def experience_heading_div(self):
		self._getter_access_tracker["experience_heading_div"] = {}
		return self._experience_heading_div
	@experience_heading_div.setter
	def experience_heading_div(self, new_state):
		self._setter_access_tracker["experience_heading_div"] = {}
		global default_state
		self._experience_heading_div = Div(new_state, default_state["experience_heading_div"])

	@property
	def experience_list(self):
		self._getter_access_tracker["experience_list"] = {}
		return self._experience_list
	@experience_list.setter
	def experience_list(self, new_state):
		self._setter_access_tracker["experience_list"] = {}
		global default_state
		self._experience_list = Div(new_state, default_state["experience_list"])

	@property
	def experience_list_item_1(self):
		self._getter_access_tracker["experience_list_item_1"] = {}
		return self._experience_list_item_1
	@experience_list_item_1.setter
	def experience_list_item_1(self, new_state):
		self._setter_access_tracker["experience_list_item_1"] = {}
		global default_state
		self._experience_list_item_1 = Flex(new_state, default_state["experience_list_item_1"])

	@property
	def list_item_1_heading_div(self):
		self._getter_access_tracker["list_item_1_heading_div"] = {}
		return self._list_item_1_heading_div
	@list_item_1_heading_div.setter
	def list_item_1_heading_div(self, new_state):
		self._setter_access_tracker["list_item_1_heading_div"] = {}
		global default_state
		self._list_item_1_heading_div = Flex(new_state, default_state["list_item_1_heading_div"])

	@property
	def experience_list_item_1_year_1_flex(self):
		self._getter_access_tracker["experience_list_item_1_year_1_flex"] = {}
		return self._experience_list_item_1_year_1_flex
	@experience_list_item_1_year_1_flex.setter
	def experience_list_item_1_year_1_flex(self, new_state):
		self._setter_access_tracker["experience_list_item_1_year_1_flex"] = {}
		global default_state
		self._experience_list_item_1_year_1_flex = Flex(new_state, default_state["experience_list_item_1_year_1_flex"])

	@property
	def experience_list_item_2(self):
		self._getter_access_tracker["experience_list_item_2"] = {}
		return self._experience_list_item_2
	@experience_list_item_2.setter
	def experience_list_item_2(self, new_state):
		self._setter_access_tracker["experience_list_item_2"] = {}
		global default_state
		self._experience_list_item_2 = Flex(new_state, default_state["experience_list_item_2"])

	@property
	def experience_list_item_2_year_2_flex(self):
		self._getter_access_tracker["experience_list_item_2_year_2_flex"] = {}
		return self._experience_list_item_2_year_2_flex
	@experience_list_item_2_year_2_flex.setter
	def experience_list_item_2_year_2_flex(self, new_state):
		self._setter_access_tracker["experience_list_item_2_year_2_flex"] = {}
		global default_state
		self._experience_list_item_2_year_2_flex = Flex(new_state, default_state["experience_list_item_2_year_2_flex"])

	@property
	def list_item__heading_div(self):
		self._getter_access_tracker["list_item__heading_div"] = {}
		return self._list_item__heading_div
	@list_item__heading_div.setter
	def list_item__heading_div(self, new_state):
		self._setter_access_tracker["list_item__heading_div"] = {}
		global default_state
		self._list_item__heading_div = Flex(new_state, default_state["list_item__heading_div"])

	@property
	def experience_list_item_3(self):
		self._getter_access_tracker["experience_list_item_3"] = {}
		return self._experience_list_item_3
	@experience_list_item_3.setter
	def experience_list_item_3(self, new_state):
		self._setter_access_tracker["experience_list_item_3"] = {}
		global default_state
		self._experience_list_item_3 = Flex(new_state, default_state["experience_list_item_3"])

	@property
	def experience_list_item__year_3_flex(self):
		self._getter_access_tracker["experience_list_item__year_3_flex"] = {}
		return self._experience_list_item__year_3_flex
	@experience_list_item__year_3_flex.setter
	def experience_list_item__year_3_flex(self, new_state):
		self._setter_access_tracker["experience_list_item__year_3_flex"] = {}
		global default_state
		self._experience_list_item__year_3_flex = Flex(new_state, default_state["experience_list_item__year_3_flex"])

	@property
	def list_item_3_heading_div(self):
		self._getter_access_tracker["list_item_3_heading_div"] = {}
		return self._list_item_3_heading_div
	@list_item_3_heading_div.setter
	def list_item_3_heading_div(self, new_state):
		self._setter_access_tracker["list_item_3_heading_div"] = {}
		global default_state
		self._list_item_3_heading_div = Flex(new_state, default_state["list_item_3_heading_div"])

	@property
	def experience_right_div(self):
		self._getter_access_tracker["experience_right_div"] = {}
		return self._experience_right_div
	@experience_right_div.setter
	def experience_right_div(self, new_state):
		self._setter_access_tracker["experience_right_div"] = {}
		global default_state
		self._experience_right_div = Div(new_state, default_state["experience_right_div"])

	@property
	def Div200(self):
		self._getter_access_tracker["Div200"] = {}
		return self._Div200
	@Div200.setter
	def Div200(self, new_state):
		self._setter_access_tracker["Div200"] = {}
		global default_state
		self._Div200 = Div(new_state, default_state["Div200"])

	@property
	def experience_right_list_item_3(self):
		self._getter_access_tracker["experience_right_list_item_3"] = {}
		return self._experience_right_list_item_3
	@experience_right_list_item_3.setter
	def experience_right_list_item_3(self, new_state):
		self._setter_access_tracker["experience_right_list_item_3"] = {}
		global default_state
		self._experience_right_list_item_3 = Flex(new_state, default_state["experience_right_list_item_3"])

	@property
	def right_list_item_3_heading_div(self):
		self._getter_access_tracker["right_list_item_3_heading_div"] = {}
		return self._right_list_item_3_heading_div
	@right_list_item_3_heading_div.setter
	def right_list_item_3_heading_div(self, new_state):
		self._setter_access_tracker["right_list_item_3_heading_div"] = {}
		global default_state
		self._right_list_item_3_heading_div = Flex(new_state, default_state["right_list_item_3_heading_div"])

	@property
	def experience_right_ist_item_3_year_3_flex(self):
		self._getter_access_tracker["experience_right_ist_item_3_year_3_flex"] = {}
		return self._experience_right_ist_item_3_year_3_flex
	@experience_right_ist_item_3_year_3_flex.setter
	def experience_right_ist_item_3_year_3_flex(self, new_state):
		self._setter_access_tracker["experience_right_ist_item_3_year_3_flex"] = {}
		global default_state
		self._experience_right_ist_item_3_year_3_flex = Flex(new_state, default_state["experience_right_ist_item_3_year_3_flex"])

	@property
	def experience_right_list_item_2(self):
		self._getter_access_tracker["experience_right_list_item_2"] = {}
		return self._experience_right_list_item_2
	@experience_right_list_item_2.setter
	def experience_right_list_item_2(self, new_state):
		self._setter_access_tracker["experience_right_list_item_2"] = {}
		global default_state
		self._experience_right_list_item_2 = Flex(new_state, default_state["experience_right_list_item_2"])

	@property
	def right_list_item_2_heading_div(self):
		self._getter_access_tracker["right_list_item_2_heading_div"] = {}
		return self._right_list_item_2_heading_div
	@right_list_item_2_heading_div.setter
	def right_list_item_2_heading_div(self, new_state):
		self._setter_access_tracker["right_list_item_2_heading_div"] = {}
		global default_state
		self._right_list_item_2_heading_div = Flex(new_state, default_state["right_list_item_2_heading_div"])

	@property
	def experience_right_ist_item_2_year_2_flex(self):
		self._getter_access_tracker["experience_right_ist_item_2_year_2_flex"] = {}
		return self._experience_right_ist_item_2_year_2_flex
	@experience_right_ist_item_2_year_2_flex.setter
	def experience_right_ist_item_2_year_2_flex(self, new_state):
		self._setter_access_tracker["experience_right_ist_item_2_year_2_flex"] = {}
		global default_state
		self._experience_right_ist_item_2_year_2_flex = Flex(new_state, default_state["experience_right_ist_item_2_year_2_flex"])

	@property
	def experience_right_list_item_1(self):
		self._getter_access_tracker["experience_right_list_item_1"] = {}
		return self._experience_right_list_item_1
	@experience_right_list_item_1.setter
	def experience_right_list_item_1(self, new_state):
		self._setter_access_tracker["experience_right_list_item_1"] = {}
		global default_state
		self._experience_right_list_item_1 = Flex(new_state, default_state["experience_right_list_item_1"])

	@property
	def experience_right_ist_item_1_year_1_flex(self):
		self._getter_access_tracker["experience_right_ist_item_1_year_1_flex"] = {}
		return self._experience_right_ist_item_1_year_1_flex
	@experience_right_ist_item_1_year_1_flex.setter
	def experience_right_ist_item_1_year_1_flex(self, new_state):
		self._setter_access_tracker["experience_right_ist_item_1_year_1_flex"] = {}
		global default_state
		self._experience_right_ist_item_1_year_1_flex = Flex(new_state, default_state["experience_right_ist_item_1_year_1_flex"])

	@property
	def right_list_item_1_heading_div(self):
		self._getter_access_tracker["right_list_item_1_heading_div"] = {}
		return self._right_list_item_1_heading_div
	@right_list_item_1_heading_div.setter
	def right_list_item_1_heading_div(self, new_state):
		self._setter_access_tracker["right_list_item_1_heading_div"] = {}
		global default_state
		self._right_list_item_1_heading_div = Flex(new_state, default_state["right_list_item_1_heading_div"])

	@property
	def Div201(self):
		self._getter_access_tracker["Div201"] = {}
		return self._Div201
	@Div201.setter
	def Div201(self, new_state):
		self._setter_access_tracker["Div201"] = {}
		global default_state
		self._Div201 = Div(new_state, default_state["Div201"])

	@property
	def testimonials_main(self):
		self._getter_access_tracker["testimonials_main"] = {}
		return self._testimonials_main
	@testimonials_main.setter
	def testimonials_main(self, new_state):
		self._setter_access_tracker["testimonials_main"] = {}
		global default_state
		self._testimonials_main = Div(new_state, default_state["testimonials_main"])

	@property
	def testimonials_headings_flex(self):
		self._getter_access_tracker["testimonials_headings_flex"] = {}
		return self._testimonials_headings_flex
	@testimonials_headings_flex.setter
	def testimonials_headings_flex(self, new_state):
		self._setter_access_tracker["testimonials_headings_flex"] = {}
		global default_state
		self._testimonials_headings_flex = Flex(new_state, default_state["testimonials_headings_flex"])

	@property
	def testimonial_1_flex(self):
		self._getter_access_tracker["testimonial_1_flex"] = {}
		return self._testimonial_1_flex
	@testimonial_1_flex.setter
	def testimonial_1_flex(self, new_state):
		self._setter_access_tracker["testimonial_1_flex"] = {}
		global default_state
		self._testimonial_1_flex = Flex(new_state, default_state["testimonial_1_flex"])

	@property
	def testimonial_details(self):
		self._getter_access_tracker["testimonial_details"] = {}
		return self._testimonial_details
	@testimonial_details.setter
	def testimonial_details(self, new_state):
		self._setter_access_tracker["testimonial_details"] = {}
		global default_state
		self._testimonial_details = Div(new_state, default_state["testimonial_details"])

	@property
	def detail_div(self):
		self._getter_access_tracker["detail_div"] = {}
		return self._detail_div
	@detail_div.setter
	def detail_div(self, new_state):
		self._setter_access_tracker["detail_div"] = {}
		global default_state
		self._detail_div = Div(new_state, default_state["detail_div"])

	@property
	def testimonial_name_div(self):
		self._getter_access_tracker["testimonial_name_div"] = {}
		return self._testimonial_name_div
	@testimonial_name_div.setter
	def testimonial_name_div(self, new_state):
		self._setter_access_tracker["testimonial_name_div"] = {}
		global default_state
		self._testimonial_name_div = Div(new_state, default_state["testimonial_name_div"])

	@property
	def left_arrow_button(self):
		self._getter_access_tracker["left_arrow_button"] = {}
		return self._left_arrow_button
	@left_arrow_button.setter
	def left_arrow_button(self, new_state):
		self._setter_access_tracker["left_arrow_button"] = {}
		global default_state
		self._left_arrow_button = Flex(new_state, default_state["left_arrow_button"])

	@property
	def right_arrow_div(self):
		self._getter_access_tracker["right_arrow_div"] = {}
		return self._right_arrow_div
	@right_arrow_div.setter
	def right_arrow_div(self, new_state):
		self._setter_access_tracker["right_arrow_div"] = {}
		global default_state
		self._right_arrow_div = Flex(new_state, default_state["right_arrow_div"])

	@property
	def faq_main(self):
		self._getter_access_tracker["faq_main"] = {}
		return self._faq_main
	@faq_main.setter
	def faq_main(self, new_state):
		self._setter_access_tracker["faq_main"] = {}
		global default_state
		self._faq_main = Div(new_state, default_state["faq_main"])

	@property
	def faq_heading_div(self):
		self._getter_access_tracker["faq_heading_div"] = {}
		return self._faq_heading_div
	@faq_heading_div.setter
	def faq_heading_div(self, new_state):
		self._setter_access_tracker["faq_heading_div"] = {}
		global default_state
		self._faq_heading_div = Div(new_state, default_state["faq_heading_div"])

	@property
	def faq_list_main_flex(self):
		self._getter_access_tracker["faq_list_main_flex"] = {}
		return self._faq_list_main_flex
	@faq_list_main_flex.setter
	def faq_list_main_flex(self, new_state):
		self._setter_access_tracker["faq_list_main_flex"] = {}
		global default_state
		self._faq_list_main_flex = Flex(new_state, default_state["faq_list_main_flex"])

	@property
	def faq_left_list(self):
		self._getter_access_tracker["faq_left_list"] = {}
		return self._faq_left_list
	@faq_left_list.setter
	def faq_left_list(self, new_state):
		self._setter_access_tracker["faq_left_list"] = {}
		global default_state
		self._faq_left_list = Flex(new_state, default_state["faq_left_list"])

	@property
	def faq_list_item_1(self):
		self._getter_access_tracker["faq_list_item_1"] = {}
		return self._faq_list_item_1
	@faq_list_item_1.setter
	def faq_list_item_1(self, new_state):
		self._setter_access_tracker["faq_list_item_1"] = {}
		global default_state
		self._faq_list_item_1 = Div(new_state, default_state["faq_list_item_1"])

	@property
	def faq_list_heading_flex_1(self):
		self._getter_access_tracker["faq_list_heading_flex_1"] = {}
		return self._faq_list_heading_flex_1
	@faq_list_heading_flex_1.setter
	def faq_list_heading_flex_1(self, new_state):
		self._setter_access_tracker["faq_list_heading_flex_1"] = {}
		global default_state
		self._faq_list_heading_flex_1 = Flex(new_state, default_state["faq_list_heading_flex_1"])

	@property
	def faq_list_item_4(self):
		self._getter_access_tracker["faq_list_item_4"] = {}
		return self._faq_list_item_4
	@faq_list_item_4.setter
	def faq_list_item_4(self, new_state):
		self._setter_access_tracker["faq_list_item_4"] = {}
		global default_state
		self._faq_list_item_4 = Flex(new_state, default_state["faq_list_item_4"])

	@property
	def faq_list_item_2(self):
		self._getter_access_tracker["faq_list_item_2"] = {}
		return self._faq_list_item_2
	@faq_list_item_2.setter
	def faq_list_item_2(self, new_state):
		self._setter_access_tracker["faq_list_item_2"] = {}
		global default_state
		self._faq_list_item_2 = Flex(new_state, default_state["faq_list_item_2"])

	@property
	def faq_list_item_3(self):
		self._getter_access_tracker["faq_list_item_3"] = {}
		return self._faq_list_item_3
	@faq_list_item_3.setter
	def faq_list_item_3(self, new_state):
		self._setter_access_tracker["faq_list_item_3"] = {}
		global default_state
		self._faq_list_item_3 = Flex(new_state, default_state["faq_list_item_3"])

	@property
	def faq_right_list(self):
		self._getter_access_tracker["faq_right_list"] = {}
		return self._faq_right_list
	@faq_right_list.setter
	def faq_right_list(self, new_state):
		self._setter_access_tracker["faq_right_list"] = {}
		global default_state
		self._faq_right_list = Flex(new_state, default_state["faq_right_list"])

	@property
	def faq_right_list_item_3(self):
		self._getter_access_tracker["faq_right_list_item_3"] = {}
		return self._faq_right_list_item_3
	@faq_right_list_item_3.setter
	def faq_right_list_item_3(self, new_state):
		self._setter_access_tracker["faq_right_list_item_3"] = {}
		global default_state
		self._faq_right_list_item_3 = Flex(new_state, default_state["faq_right_list_item_3"])

	@property
	def faq_right_list_item_2(self):
		self._getter_access_tracker["faq_right_list_item_2"] = {}
		return self._faq_right_list_item_2
	@faq_right_list_item_2.setter
	def faq_right_list_item_2(self, new_state):
		self._setter_access_tracker["faq_right_list_item_2"] = {}
		global default_state
		self._faq_right_list_item_2 = Flex(new_state, default_state["faq_right_list_item_2"])

	@property
	def faq_right_list_item_4(self):
		self._getter_access_tracker["faq_right_list_item_4"] = {}
		return self._faq_right_list_item_4
	@faq_right_list_item_4.setter
	def faq_right_list_item_4(self, new_state):
		self._setter_access_tracker["faq_right_list_item_4"] = {}
		global default_state
		self._faq_right_list_item_4 = Flex(new_state, default_state["faq_right_list_item_4"])

	@property
	def faq_right_list_item_1(self):
		self._getter_access_tracker["faq_right_list_item_1"] = {}
		return self._faq_right_list_item_1
	@faq_right_list_item_1.setter
	def faq_right_list_item_1(self, new_state):
		self._setter_access_tracker["faq_right_list_item_1"] = {}
		global default_state
		self._faq_right_list_item_1 = Div(new_state, default_state["faq_right_list_item_1"])

	@property
	def faq_right_list_heading_flex_1(self):
		self._getter_access_tracker["faq_right_list_heading_flex_1"] = {}
		return self._faq_right_list_heading_flex_1
	@faq_right_list_heading_flex_1.setter
	def faq_right_list_heading_flex_1(self, new_state):
		self._setter_access_tracker["faq_right_list_heading_flex_1"] = {}
		global default_state
		self._faq_right_list_heading_flex_1 = Flex(new_state, default_state["faq_right_list_heading_flex_1"])

	@property
	def footer_main_div(self):
		self._getter_access_tracker["footer_main_div"] = {}
		return self._footer_main_div
	@footer_main_div.setter
	def footer_main_div(self, new_state):
		self._setter_access_tracker["footer_main_div"] = {}
		global default_state
		self._footer_main_div = Div(new_state, default_state["footer_main_div"])

	@property
	def footer_headings_flex(self):
		self._getter_access_tracker["footer_headings_flex"] = {}
		return self._footer_headings_flex
	@footer_headings_flex.setter
	def footer_headings_flex(self, new_state):
		self._setter_access_tracker["footer_headings_flex"] = {}
		global default_state
		self._footer_headings_flex = Flex(new_state, default_state["footer_headings_flex"])

	@property
	def footer_heading_div(self):
		self._getter_access_tracker["footer_heading_div"] = {}
		return self._footer_heading_div
	@footer_heading_div.setter
	def footer_heading_div(self, new_state):
		self._setter_access_tracker["footer_heading_div"] = {}
		global default_state
		self._footer_heading_div = Div(new_state, default_state["footer_heading_div"])

	@property
	def footer_links_flex(self):
		self._getter_access_tracker["footer_links_flex"] = {}
		return self._footer_links_flex
	@footer_links_flex.setter
	def footer_links_flex(self, new_state):
		self._setter_access_tracker["footer_links_flex"] = {}
		global default_state
		self._footer_links_flex = Flex(new_state, default_state["footer_links_flex"])

	@property
	def website_details_div(self):
		self._getter_access_tracker["website_details_div"] = {}
		return self._website_details_div
	@website_details_div.setter
	def website_details_div(self, new_state):
		self._setter_access_tracker["website_details_div"] = {}
		global default_state
		self._website_details_div = Div(new_state, default_state["website_details_div"])

	@property
	def mail_flex(self):
		self._getter_access_tracker["mail_flex"] = {}
		return self._mail_flex
	@mail_flex.setter
	def mail_flex(self, new_state):
		self._setter_access_tracker["mail_flex"] = {}
		global default_state
		self._mail_flex = Flex(new_state, default_state["mail_flex"])

	@property
	def links_grid(self):
		self._getter_access_tracker["links_grid"] = {}
		return self._links_grid
	@links_grid.setter
	def links_grid(self, new_state):
		self._setter_access_tracker["links_grid"] = {}
		global default_state
		self._links_grid = Div(new_state, default_state["links_grid"])

	@property
	def copyright_div(self):
		self._getter_access_tracker["copyright_div"] = {}
		return self._copyright_div
	@copyright_div.setter
	def copyright_div(self, new_state):
		self._setter_access_tracker["copyright_div"] = {}
		global default_state
		self._copyright_div = Flex(new_state, default_state["copyright_div"])

	@property
	def webflow_div(self):
		self._getter_access_tracker["webflow_div"] = {}
		return self._webflow_div
	@webflow_div.setter
	def webflow_div(self, new_state):
		self._setter_access_tracker["webflow_div"] = {}
		global default_state
		self._webflow_div = Div(new_state, default_state["webflow_div"])

	@property
	def trust_heading(self):
		self._getter_access_tracker["trust_heading"] = {}
		return self._trust_heading
	@trust_heading.setter
	def trust_heading(self, new_state):
		self._setter_access_tracker["trust_heading"] = {}
		global default_state
		self._trust_heading = TextBox(new_state, default_state["trust_heading"])

	@property
	def projects_view_button_back(self):
		self._getter_access_tracker["projects_view_button_back"] = {}
		return self._projects_view_button_back
	@projects_view_button_back.setter
	def projects_view_button_back(self, new_state):
		self._setter_access_tracker["projects_view_button_back"] = {}
		global default_state
		self._projects_view_button_back = Div(new_state, default_state["projects_view_button_back"])

	@property
	def logo_img(self):
		self._getter_access_tracker["logo_img"] = {}
		return self._logo_img
	@logo_img.setter
	def logo_img(self, new_state):
		self._setter_access_tracker["logo_img"] = {}
		global default_state
		self._logo_img = Image(new_state, default_state["logo_img"])

	@property
	def call_link(self):
		self._getter_access_tracker["call_link"] = {}
		return self._call_link
	@call_link.setter
	def call_link(self, new_state):
		self._setter_access_tracker["call_link"] = {}
		global default_state
		self._call_link = Link(new_state, default_state["call_link"])

	@property
	def about_link(self):
		self._getter_access_tracker["about_link"] = {}
		return self._about_link
	@about_link.setter
	def about_link(self, new_state):
		self._setter_access_tracker["about_link"] = {}
		global default_state
		self._about_link = Link(new_state, default_state["about_link"])

	@property
	def blog_link(self):
		self._getter_access_tracker["blog_link"] = {}
		return self._blog_link
	@blog_link.setter
	def blog_link(self, new_state):
		self._setter_access_tracker["blog_link"] = {}
		global default_state
		self._blog_link = Link(new_state, default_state["blog_link"])

	@property
	def project_link(self):
		self._getter_access_tracker["project_link"] = {}
		return self._project_link
	@project_link.setter
	def project_link(self, new_state):
		self._setter_access_tracker["project_link"] = {}
		global default_state
		self._project_link = Link(new_state, default_state["project_link"])

	@property
	def services_link(self):
		self._getter_access_tracker["services_link"] = {}
		return self._services_link
	@services_link.setter
	def services_link(self, new_state):
		self._setter_access_tracker["services_link"] = {}
		global default_state
		self._services_link = Link(new_state, default_state["services_link"])

	@property
	def nav_call_arrow(self):
		self._getter_access_tracker["nav_call_arrow"] = {}
		return self._nav_call_arrow
	@nav_call_arrow.setter
	def nav_call_arrow(self, new_state):
		self._setter_access_tracker["nav_call_arrow"] = {}
		global default_state
		self._nav_call_arrow = Image(new_state, default_state["nav_call_arrow"])

	@property
	def trusted_div_main(self):
		self._getter_access_tracker["trusted_div_main"] = {}
		return self._trusted_div_main
	@trusted_div_main.setter
	def trusted_div_main(self, new_state):
		self._setter_access_tracker["trusted_div_main"] = {}
		global default_state
		self._trusted_div_main = Div(new_state, default_state["trusted_div_main"])

	@property
	def hero_image(self):
		self._getter_access_tracker["hero_image"] = {}
		return self._hero_image
	@hero_image.setter
	def hero_image(self, new_state):
		self._setter_access_tracker["hero_image"] = {}
		global default_state
		self._hero_image = Image(new_state, default_state["hero_image"])

	@property
	def heading_1(self):
		self._getter_access_tracker["heading_1"] = {}
		return self._heading_1
	@heading_1.setter
	def heading_1(self, new_state):
		self._setter_access_tracker["heading_1"] = {}
		global default_state
		self._heading_1 = TextBox(new_state, default_state["heading_1"])

	@property
	def heading_2(self):
		self._getter_access_tracker["heading_2"] = {}
		return self._heading_2
	@heading_2.setter
	def heading_2(self, new_state):
		self._setter_access_tracker["heading_2"] = {}
		global default_state
		self._heading_2 = TextBox(new_state, default_state["heading_2"])

	@property
	def heading_3(self):
		self._getter_access_tracker["heading_3"] = {}
		return self._heading_3
	@heading_3.setter
	def heading_3(self, new_state):
		self._setter_access_tracker["heading_3"] = {}
		global default_state
		self._heading_3 = TextBox(new_state, default_state["heading_3"])

	@property
	def paragraph(self):
		self._getter_access_tracker["paragraph"] = {}
		return self._paragraph
	@paragraph.setter
	def paragraph(self, new_state):
		self._setter_access_tracker["paragraph"] = {}
		global default_state
		self._paragraph = TextBox(new_state, default_state["paragraph"])

	@property
	def button_background(self):
		self._getter_access_tracker["button_background"] = {}
		return self._button_background
	@button_background.setter
	def button_background(self, new_state):
		self._setter_access_tracker["button_background"] = {}
		global default_state
		self._button_background = Div(new_state, default_state["button_background"])

	@property
	def CV_link(self):
		self._getter_access_tracker["CV_link"] = {}
		return self._CV_link
	@CV_link.setter
	def CV_link(self, new_state):
		self._setter_access_tracker["CV_link"] = {}
		global default_state
		self._CV_link = Link(new_state, default_state["CV_link"])

	@property
	def call_button(self):
		self._getter_access_tracker["call_button"] = {}
		return self._call_button
	@call_button.setter
	def call_button(self, new_state):
		self._setter_access_tracker["call_button"] = {}
		global default_state
		self._call_button = Button(new_state, default_state["call_button"])

	@property
	def company_1(self):
		self._getter_access_tracker["company_1"] = {}
		return self._company_1
	@company_1.setter
	def company_1(self, new_state):
		self._setter_access_tracker["company_1"] = {}
		global default_state
		self._company_1 = Image(new_state, default_state["company_1"])

	@property
	def company_2(self):
		self._getter_access_tracker["company_2"] = {}
		return self._company_2
	@company_2.setter
	def company_2(self, new_state):
		self._setter_access_tracker["company_2"] = {}
		global default_state
		self._company_2 = Image(new_state, default_state["company_2"])

	@property
	def company_3(self):
		self._getter_access_tracker["company_3"] = {}
		return self._company_3
	@company_3.setter
	def company_3(self, new_state):
		self._setter_access_tracker["company_3"] = {}
		global default_state
		self._company_3 = Image(new_state, default_state["company_3"])

	@property
	def company_4(self):
		self._getter_access_tracker["company_4"] = {}
		return self._company_4
	@company_4.setter
	def company_4(self, new_state):
		self._setter_access_tracker["company_4"] = {}
		global default_state
		self._company_4 = Image(new_state, default_state["company_4"])

	@property
	def projects_main(self):
		self._getter_access_tracker["projects_main"] = {}
		return self._projects_main
	@projects_main.setter
	def projects_main(self, new_state):
		self._setter_access_tracker["projects_main"] = {}
		global default_state
		self._projects_main = Div(new_state, default_state["projects_main"])

	@property
	def services_heading(self):
		self._getter_access_tracker["services_heading"] = {}
		return self._services_heading
	@services_heading.setter
	def services_heading(self, new_state):
		self._setter_access_tracker["services_heading"] = {}
		global default_state
		self._services_heading = TextBox(new_state, default_state["services_heading"])

	@property
	def serices_paragraph(self):
		self._getter_access_tracker["serices_paragraph"] = {}
		return self._serices_paragraph
	@serices_paragraph.setter
	def serices_paragraph(self, new_state):
		self._setter_access_tracker["serices_paragraph"] = {}
		global default_state
		self._serices_paragraph = TextBox(new_state, default_state["serices_paragraph"])

	@property
	def services_image_1(self):
		self._getter_access_tracker["services_image_1"] = {}
		return self._services_image_1
	@services_image_1.setter
	def services_image_1(self, new_state):
		self._setter_access_tracker["services_image_1"] = {}
		global default_state
		self._services_image_1 = Image(new_state, default_state["services_image_1"])

	@property
	def list_heading_1(self):
		self._getter_access_tracker["list_heading_1"] = {}
		return self._list_heading_1
	@list_heading_1.setter
	def list_heading_1(self, new_state):
		self._setter_access_tracker["list_heading_1"] = {}
		global default_state
		self._list_heading_1 = TextBox(new_state, default_state["list_heading_1"])

	@property
	def list_paragraph_1(self):
		self._getter_access_tracker["list_paragraph_1"] = {}
		return self._list_paragraph_1
	@list_paragraph_1.setter
	def list_paragraph_1(self, new_state):
		self._setter_access_tracker["list_paragraph_1"] = {}
		global default_state
		self._list_paragraph_1 = TextBox(new_state, default_state["list_paragraph_1"])

	@property
	def services_bullet_point_1(self):
		self._getter_access_tracker["services_bullet_point_1"] = {}
		return self._services_bullet_point_1
	@services_bullet_point_1.setter
	def services_bullet_point_1(self, new_state):
		self._setter_access_tracker["services_bullet_point_1"] = {}
		global default_state
		self._services_bullet_point_1 = Div(new_state, default_state["services_bullet_point_1"])

	@property
	def list_pointer_heading(self):
		self._getter_access_tracker["list_pointer_heading"] = {}
		return self._list_pointer_heading
	@list_pointer_heading.setter
	def list_pointer_heading(self, new_state):
		self._setter_access_tracker["list_pointer_heading"] = {}
		global default_state
		self._list_pointer_heading = TextBox(new_state, default_state["list_pointer_heading"])

	@property
	def list_pointer_head_2(self):
		self._getter_access_tracker["list_pointer_head_2"] = {}
		return self._list_pointer_head_2
	@list_pointer_head_2.setter
	def list_pointer_head_2(self, new_state):
		self._setter_access_tracker["list_pointer_head_2"] = {}
		global default_state
		self._list_pointer_head_2 = TextBox(new_state, default_state["list_pointer_head_2"])

	@property
	def Div46(self):
		self._getter_access_tracker["Div46"] = {}
		return self._Div46
	@Div46.setter
	def Div46(self, new_state):
		self._setter_access_tracker["Div46"] = {}
		global default_state
		self._Div46 = Div(new_state, default_state["Div46"])

	@property
	def pointer_list_heading_3(self):
		self._getter_access_tracker["pointer_list_heading_3"] = {}
		return self._pointer_list_heading_3
	@pointer_list_heading_3.setter
	def pointer_list_heading_3(self, new_state):
		self._setter_access_tracker["pointer_list_heading_3"] = {}
		global default_state
		self._pointer_list_heading_3 = TextBox(new_state, default_state["pointer_list_heading_3"])

	@property
	def Div47(self):
		self._getter_access_tracker["Div47"] = {}
		return self._Div47
	@Div47.setter
	def Div47(self, new_state):
		self._setter_access_tracker["Div47"] = {}
		global default_state
		self._Div47 = Div(new_state, default_state["Div47"])

	@property
	def services_image_3(self):
		self._getter_access_tracker["services_image_3"] = {}
		return self._services_image_3
	@services_image_3.setter
	def services_image_3(self, new_state):
		self._setter_access_tracker["services_image_3"] = {}
		global default_state
		self._services_image_3 = Image(new_state, default_state["services_image_3"])

	@property
	def Div109(self):
		self._getter_access_tracker["Div109"] = {}
		return self._Div109
	@Div109.setter
	def Div109(self, new_state):
		self._setter_access_tracker["Div109"] = {}
		global default_state
		self._Div109 = Div(new_state, default_state["Div109"])

	@property
	def list_pointer_heading_9(self):
		self._getter_access_tracker["list_pointer_heading_9"] = {}
		return self._list_pointer_heading_9
	@list_pointer_heading_9.setter
	def list_pointer_heading_9(self, new_state):
		self._setter_access_tracker["list_pointer_heading_9"] = {}
		global default_state
		self._list_pointer_heading_9 = TextBox(new_state, default_state["list_pointer_heading_9"])

	@property
	def Div110(self):
		self._getter_access_tracker["Div110"] = {}
		return self._Div110
	@Div110.setter
	def Div110(self, new_state):
		self._setter_access_tracker["Div110"] = {}
		global default_state
		self._Div110 = Div(new_state, default_state["Div110"])

	@property
	def list_pointer_heading_8(self):
		self._getter_access_tracker["list_pointer_heading_8"] = {}
		return self._list_pointer_heading_8
	@list_pointer_heading_8.setter
	def list_pointer_heading_8(self, new_state):
		self._setter_access_tracker["list_pointer_heading_8"] = {}
		global default_state
		self._list_pointer_heading_8 = TextBox(new_state, default_state["list_pointer_heading_8"])

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		global default_state
		self._TextBox78 = TextBox(new_state, default_state["TextBox78"])

	@property
	def Div108(self):
		self._getter_access_tracker["Div108"] = {}
		return self._Div108
	@Div108.setter
	def Div108(self, new_state):
		self._setter_access_tracker["Div108"] = {}
		global default_state
		self._Div108 = Div(new_state, default_state["Div108"])

	@property
	def list_paragraph_3(self):
		self._getter_access_tracker["list_paragraph_3"] = {}
		return self._list_paragraph_3
	@list_paragraph_3.setter
	def list_paragraph_3(self, new_state):
		self._setter_access_tracker["list_paragraph_3"] = {}
		global default_state
		self._list_paragraph_3 = TextBox(new_state, default_state["list_paragraph_3"])

	@property
	def list_heading_3(self):
		self._getter_access_tracker["list_heading_3"] = {}
		return self._list_heading_3
	@list_heading_3.setter
	def list_heading_3(self, new_state):
		self._setter_access_tracker["list_heading_3"] = {}
		global default_state
		self._list_heading_3 = TextBox(new_state, default_state["list_heading_3"])

	@property
	def services_image_2(self):
		self._getter_access_tracker["services_image_2"] = {}
		return self._services_image_2
	@services_image_2.setter
	def services_image_2(self, new_state):
		self._setter_access_tracker["services_image_2"] = {}
		global default_state
		self._services_image_2 = Image(new_state, default_state["services_image_2"])

	@property
	def list_heading_2(self):
		self._getter_access_tracker["list_heading_2"] = {}
		return self._list_heading_2
	@list_heading_2.setter
	def list_heading_2(self, new_state):
		self._setter_access_tracker["list_heading_2"] = {}
		global default_state
		self._list_heading_2 = TextBox(new_state, default_state["list_heading_2"])

	@property
	def list_paragraph_2(self):
		self._getter_access_tracker["list_paragraph_2"] = {}
		return self._list_paragraph_2
	@list_paragraph_2.setter
	def list_paragraph_2(self, new_state):
		self._setter_access_tracker["list_paragraph_2"] = {}
		global default_state
		self._list_paragraph_2 = TextBox(new_state, default_state["list_paragraph_2"])

	@property
	def Div114(self):
		self._getter_access_tracker["Div114"] = {}
		return self._Div114
	@Div114.setter
	def Div114(self, new_state):
		self._setter_access_tracker["Div114"] = {}
		global default_state
		self._Div114 = Div(new_state, default_state["Div114"])

	@property
	def list_pointer_heading_2(self):
		self._getter_access_tracker["list_pointer_heading_2"] = {}
		return self._list_pointer_heading_2
	@list_pointer_heading_2.setter
	def list_pointer_heading_2(self, new_state):
		self._setter_access_tracker["list_pointer_heading_2"] = {}
		global default_state
		self._list_pointer_heading_2 = TextBox(new_state, default_state["list_pointer_heading_2"])

	@property
	def list_pointer_head_5(self):
		self._getter_access_tracker["list_pointer_head_5"] = {}
		return self._list_pointer_head_5
	@list_pointer_head_5.setter
	def list_pointer_head_5(self, new_state):
		self._setter_access_tracker["list_pointer_head_5"] = {}
		global default_state
		self._list_pointer_head_5 = TextBox(new_state, default_state["list_pointer_head_5"])

	@property
	def Div115(self):
		self._getter_access_tracker["Div115"] = {}
		return self._Div115
	@Div115.setter
	def Div115(self, new_state):
		self._setter_access_tracker["Div115"] = {}
		global default_state
		self._Div115 = Div(new_state, default_state["Div115"])

	@property
	def list_pointer_heading_6(self):
		self._getter_access_tracker["list_pointer_heading_6"] = {}
		return self._list_pointer_heading_6
	@list_pointer_heading_6.setter
	def list_pointer_heading_6(self, new_state):
		self._setter_access_tracker["list_pointer_heading_6"] = {}
		global default_state
		self._list_pointer_heading_6 = TextBox(new_state, default_state["list_pointer_heading_6"])

	@property
	def Div116(self):
		self._getter_access_tracker["Div116"] = {}
		return self._Div116
	@Div116.setter
	def Div116(self, new_state):
		self._setter_access_tracker["Div116"] = {}
		global default_state
		self._Div116 = Div(new_state, default_state["Div116"])

	@property
	def projects_head_1(self):
		self._getter_access_tracker["projects_head_1"] = {}
		return self._projects_head_1
	@projects_head_1.setter
	def projects_head_1(self, new_state):
		self._setter_access_tracker["projects_head_1"] = {}
		global default_state
		self._projects_head_1 = TextBox(new_state, default_state["projects_head_1"])

	@property
	def projects_heading_2(self):
		self._getter_access_tracker["projects_heading_2"] = {}
		return self._projects_heading_2
	@projects_heading_2.setter
	def projects_heading_2(self, new_state):
		self._setter_access_tracker["projects_heading_2"] = {}
		global default_state
		self._projects_heading_2 = TextBox(new_state, default_state["projects_heading_2"])

	@property
	def projeccts_heading_3(self):
		self._getter_access_tracker["projeccts_heading_3"] = {}
		return self._projeccts_heading_3
	@projeccts_heading_3.setter
	def projeccts_heading_3(self, new_state):
		self._setter_access_tracker["projeccts_heading_3"] = {}
		global default_state
		self._projeccts_heading_3 = TextBox(new_state, default_state["projeccts_heading_3"])

	@property
	def view_projects_button(self):
		self._getter_access_tracker["view_projects_button"] = {}
		return self._view_projects_button
	@view_projects_button.setter
	def view_projects_button(self, new_state):
		self._setter_access_tracker["view_projects_button"] = {}
		global default_state
		self._view_projects_button = Button(new_state, default_state["view_projects_button"])

	@property
	def slider_3_image(self):
		self._getter_access_tracker["slider_3_image"] = {}
		return self._slider_3_image
	@slider_3_image.setter
	def slider_3_image(self, new_state):
		self._setter_access_tracker["slider_3_image"] = {}
		global default_state
		self._slider_3_image = Image(new_state, default_state["slider_3_image"])

	@property
	def slider_3_head_1(self):
		self._getter_access_tracker["slider_3_head_1"] = {}
		return self._slider_3_head_1
	@slider_3_head_1.setter
	def slider_3_head_1(self, new_state):
		self._setter_access_tracker["slider_3_head_1"] = {}
		global default_state
		self._slider_3_head_1 = TextBox(new_state, default_state["slider_3_head_1"])

	@property
	def slider_3_head_2(self):
		self._getter_access_tracker["slider_3_head_2"] = {}
		return self._slider_3_head_2
	@slider_3_head_2.setter
	def slider_3_head_2(self, new_state):
		self._setter_access_tracker["slider_3_head_2"] = {}
		global default_state
		self._slider_3_head_2 = TextBox(new_state, default_state["slider_3_head_2"])

	@property
	def slider_3_flex_head_3(self):
		self._getter_access_tracker["slider_3_flex_head_3"] = {}
		return self._slider_3_flex_head_3
	@slider_3_flex_head_3.setter
	def slider_3_flex_head_3(self, new_state):
		self._setter_access_tracker["slider_3_flex_head_3"] = {}
		global default_state
		self._slider_3_flex_head_3 = TextBox(new_state, default_state["slider_3_flex_head_3"])

	@property
	def slider_3_head_image(self):
		self._getter_access_tracker["slider_3_head_image"] = {}
		return self._slider_3_head_image
	@slider_3_head_image.setter
	def slider_3_head_image(self, new_state):
		self._setter_access_tracker["slider_3_head_image"] = {}
		global default_state
		self._slider_3_head_image = Image(new_state, default_state["slider_3_head_image"])

	@property
	def slider_item_1_image_2(self):
		self._getter_access_tracker["slider_item_1_image_2"] = {}
		return self._slider_item_1_image_2
	@slider_item_1_image_2.setter
	def slider_item_1_image_2(self, new_state):
		self._setter_access_tracker["slider_item_1_image_2"] = {}
		global default_state
		self._slider_item_1_image_2 = Image(new_state, default_state["slider_item_1_image_2"])

	@property
	def slider_item_2_head_2(self):
		self._getter_access_tracker["slider_item_2_head_2"] = {}
		return self._slider_item_2_head_2
	@slider_item_2_head_2.setter
	def slider_item_2_head_2(self, new_state):
		self._setter_access_tracker["slider_item_2_head_2"] = {}
		global default_state
		self._slider_item_2_head_2 = TextBox(new_state, default_state["slider_item_2_head_2"])

	@property
	def slider_item_2_product(self):
		self._getter_access_tracker["slider_item_2_product"] = {}
		return self._slider_item_2_product
	@slider_item_2_product.setter
	def slider_item_2_product(self, new_state):
		self._setter_access_tracker["slider_item_2_product"] = {}
		global default_state
		self._slider_item_2_product = TextBox(new_state, default_state["slider_item_2_product"])

	@property
	def Image44(self):
		self._getter_access_tracker["Image44"] = {}
		return self._Image44
	@Image44.setter
	def Image44(self, new_state):
		self._setter_access_tracker["Image44"] = {}
		global default_state
		self._Image44 = Image(new_state, default_state["Image44"])

	@property
	def TextBox116(self):
		self._getter_access_tracker["TextBox116"] = {}
		return self._TextBox116
	@TextBox116.setter
	def TextBox116(self, new_state):
		self._setter_access_tracker["TextBox116"] = {}
		global default_state
		self._TextBox116 = TextBox(new_state, default_state["TextBox116"])

	@property
	def slider_image_1(self):
		self._getter_access_tracker["slider_image_1"] = {}
		return self._slider_image_1
	@slider_image_1.setter
	def slider_image_1(self, new_state):
		self._setter_access_tracker["slider_image_1"] = {}
		global default_state
		self._slider_image_1 = Image(new_state, default_state["slider_image_1"])

	@property
	def slider_item_1_head_2(self):
		self._getter_access_tracker["slider_item_1_head_2"] = {}
		return self._slider_item_1_head_2
	@slider_item_1_head_2.setter
	def slider_item_1_head_2(self, new_state):
		self._setter_access_tracker["slider_item_1_head_2"] = {}
		global default_state
		self._slider_item_1_head_2 = TextBox(new_state, default_state["slider_item_1_head_2"])

	@property
	def slider_branding_head(self):
		self._getter_access_tracker["slider_branding_head"] = {}
		return self._slider_branding_head
	@slider_branding_head.setter
	def slider_branding_head(self, new_state):
		self._setter_access_tracker["slider_branding_head"] = {}
		global default_state
		self._slider_branding_head = TextBox(new_state, default_state["slider_branding_head"])

	@property
	def arrow_image_1(self):
		self._getter_access_tracker["arrow_image_1"] = {}
		return self._arrow_image_1
	@arrow_image_1.setter
	def arrow_image_1(self, new_state):
		self._setter_access_tracker["arrow_image_1"] = {}
		global default_state
		self._arrow_image_1 = Image(new_state, default_state["arrow_image_1"])

	@property
	def slider_view_link_1(self):
		self._getter_access_tracker["slider_view_link_1"] = {}
		return self._slider_view_link_1
	@slider_view_link_1.setter
	def slider_view_link_1(self, new_state):
		self._setter_access_tracker["slider_view_link_1"] = {}
		global default_state
		self._slider_view_link_1 = TextBox(new_state, default_state["slider_view_link_1"])

	@property
	def blog_left_arrow_image(self):
		self._getter_access_tracker["blog_left_arrow_image"] = {}
		return self._blog_left_arrow_image
	@blog_left_arrow_image.setter
	def blog_left_arrow_image(self, new_state):
		self._setter_access_tracker["blog_left_arrow_image"] = {}
		global default_state
		self._blog_left_arrow_image = Image(new_state, default_state["blog_left_arrow_image"])

	@property
	def blogs_right_arrow_image(self):
		self._getter_access_tracker["blogs_right_arrow_image"] = {}
		return self._blogs_right_arrow_image
	@blogs_right_arrow_image.setter
	def blogs_right_arrow_image(self, new_state):
		self._setter_access_tracker["blogs_right_arrow_image"] = {}
		global default_state
		self._blogs_right_arrow_image = Image(new_state, default_state["blogs_right_arrow_image"])

	@property
	def heading_blogs(self):
		self._getter_access_tracker["heading_blogs"] = {}
		return self._heading_blogs
	@heading_blogs.setter
	def heading_blogs(self, new_state):
		self._setter_access_tracker["heading_blogs"] = {}
		global default_state
		self._heading_blogs = TextBox(new_state, default_state["heading_blogs"])

	@property
	def latest_blogs_heading(self):
		self._getter_access_tracker["latest_blogs_heading"] = {}
		return self._latest_blogs_heading
	@latest_blogs_heading.setter
	def latest_blogs_heading(self, new_state):
		self._setter_access_tracker["latest_blogs_heading"] = {}
		global default_state
		self._latest_blogs_heading = TextBox(new_state, default_state["latest_blogs_heading"])

	@property
	def view_all_link(self):
		self._getter_access_tracker["view_all_link"] = {}
		return self._view_all_link
	@view_all_link.setter
	def view_all_link(self, new_state):
		self._setter_access_tracker["view_all_link"] = {}
		global default_state
		self._view_all_link = TextBox(new_state, default_state["view_all_link"])

	@property
	def arrow_image(self):
		self._getter_access_tracker["arrow_image"] = {}
		return self._arrow_image
	@arrow_image.setter
	def arrow_image(self, new_state):
		self._setter_access_tracker["arrow_image"] = {}
		global default_state
		self._arrow_image = Image(new_state, default_state["arrow_image"])

	@property
	def heading_time(self):
		self._getter_access_tracker["heading_time"] = {}
		return self._heading_time
	@heading_time.setter
	def heading_time(self, new_state):
		self._setter_access_tracker["heading_time"] = {}
		global default_state
		self._heading_time = TextBox(new_state, default_state["heading_time"])

	@property
	def point_div1(self):
		self._getter_access_tracker["point_div1"] = {}
		return self._point_div1
	@point_div1.setter
	def point_div1(self, new_state):
		self._setter_access_tracker["point_div1"] = {}
		global default_state
		self._point_div1 = Div(new_state, default_state["point_div1"])

	@property
	def heading_date(self):
		self._getter_access_tracker["heading_date"] = {}
		return self._heading_date
	@heading_date.setter
	def heading_date(self, new_state):
		self._setter_access_tracker["heading_date"] = {}
		global default_state
		self._heading_date = TextBox(new_state, default_state["heading_date"])

	@property
	def list_item_1_heading_2(self):
		self._getter_access_tracker["list_item_1_heading_2"] = {}
		return self._list_item_1_heading_2
	@list_item_1_heading_2.setter
	def list_item_1_heading_2(self, new_state):
		self._setter_access_tracker["list_item_1_heading_2"] = {}
		global default_state
		self._list_item_1_heading_2 = TextBox(new_state, default_state["list_item_1_heading_2"])

	@property
	def list_1_read_link(self):
		self._getter_access_tracker["list_1_read_link"] = {}
		return self._list_1_read_link
	@list_1_read_link.setter
	def list_1_read_link(self, new_state):
		self._setter_access_tracker["list_1_read_link"] = {}
		global default_state
		self._list_1_read_link = TextBox(new_state, default_state["list_1_read_link"])

	@property
	def list_link_arrow_image(self):
		self._getter_access_tracker["list_link_arrow_image"] = {}
		return self._list_link_arrow_image
	@list_link_arrow_image.setter
	def list_link_arrow_image(self, new_state):
		self._setter_access_tracker["list_link_arrow_image"] = {}
		global default_state
		self._list_link_arrow_image = Image(new_state, default_state["list_link_arrow_image"])

	@property
	def list_arrow_image(self):
		self._getter_access_tracker["list_arrow_image"] = {}
		return self._list_arrow_image
	@list_arrow_image.setter
	def list_arrow_image(self, new_state):
		self._setter_access_tracker["list_arrow_image"] = {}
		global default_state
		self._list_arrow_image = Image(new_state, default_state["list_arrow_image"])

	@property
	def list_2_link(self):
		self._getter_access_tracker["list_2_link"] = {}
		return self._list_2_link
	@list_2_link.setter
	def list_2_link(self, new_state):
		self._setter_access_tracker["list_2_link"] = {}
		global default_state
		self._list_2_link = TextBox(new_state, default_state["list_2_link"])

	@property
	def list_item_heading_2(self):
		self._getter_access_tracker["list_item_heading_2"] = {}
		return self._list_item_heading_2
	@list_item_heading_2.setter
	def list_item_heading_2(self, new_state):
		self._setter_access_tracker["list_item_heading_2"] = {}
		global default_state
		self._list_item_heading_2 = TextBox(new_state, default_state["list_item_heading_2"])

	@property
	def list_item_2_date(self):
		self._getter_access_tracker["list_item_2_date"] = {}
		return self._list_item_2_date
	@list_item_2_date.setter
	def list_item_2_date(self, new_state):
		self._setter_access_tracker["list_item_2_date"] = {}
		global default_state
		self._list_item_2_date = TextBox(new_state, default_state["list_item_2_date"])

	@property
	def point_div_2(self):
		self._getter_access_tracker["point_div_2"] = {}
		return self._point_div_2
	@point_div_2.setter
	def point_div_2(self, new_state):
		self._setter_access_tracker["point_div_2"] = {}
		global default_state
		self._point_div_2 = Div(new_state, default_state["point_div_2"])

	@property
	def list_item_2_time(self):
		self._getter_access_tracker["list_item_2_time"] = {}
		return self._list_item_2_time
	@list_item_2_time.setter
	def list_item_2_time(self, new_state):
		self._setter_access_tracker["list_item_2_time"] = {}
		global default_state
		self._list_item_2_time = TextBox(new_state, default_state["list_item_2_time"])

	@property
	def list_3_time(self):
		self._getter_access_tracker["list_3_time"] = {}
		return self._list_3_time
	@list_3_time.setter
	def list_3_time(self, new_state):
		self._setter_access_tracker["list_3_time"] = {}
		global default_state
		self._list_3_time = TextBox(new_state, default_state["list_3_time"])

	@property
	def point_div3(self):
		self._getter_access_tracker["point_div3"] = {}
		return self._point_div3
	@point_div3.setter
	def point_div3(self, new_state):
		self._setter_access_tracker["point_div3"] = {}
		global default_state
		self._point_div3 = Div(new_state, default_state["point_div3"])

	@property
	def list_3_date(self):
		self._getter_access_tracker["list_3_date"] = {}
		return self._list_3_date
	@list_3_date.setter
	def list_3_date(self, new_state):
		self._setter_access_tracker["list_3_date"] = {}
		global default_state
		self._list_3_date = TextBox(new_state, default_state["list_3_date"])

	@property
	def list_3_heading(self):
		self._getter_access_tracker["list_3_heading"] = {}
		return self._list_3_heading
	@list_3_heading.setter
	def list_3_heading(self, new_state):
		self._setter_access_tracker["list_3_heading"] = {}
		global default_state
		self._list_3_heading = TextBox(new_state, default_state["list_3_heading"])

	@property
	def list_3_link_3(self):
		self._getter_access_tracker["list_3_link_3"] = {}
		return self._list_3_link_3
	@list_3_link_3.setter
	def list_3_link_3(self, new_state):
		self._setter_access_tracker["list_3_link_3"] = {}
		global default_state
		self._list_3_link_3 = TextBox(new_state, default_state["list_3_link_3"])

	@property
	def arrow_image_3(self):
		self._getter_access_tracker["arrow_image_3"] = {}
		return self._arrow_image_3
	@arrow_image_3.setter
	def arrow_image_3(self, new_state):
		self._setter_access_tracker["arrow_image_3"] = {}
		global default_state
		self._arrow_image_3 = Image(new_state, default_state["arrow_image_3"])

	@property
	def arrow_image_4(self):
		self._getter_access_tracker["arrow_image_4"] = {}
		return self._arrow_image_4
	@arrow_image_4.setter
	def arrow_image_4(self, new_state):
		self._setter_access_tracker["arrow_image_4"] = {}
		global default_state
		self._arrow_image_4 = Image(new_state, default_state["arrow_image_4"])

	@property
	def list_4_link(self):
		self._getter_access_tracker["list_4_link"] = {}
		return self._list_4_link
	@list_4_link.setter
	def list_4_link(self, new_state):
		self._setter_access_tracker["list_4_link"] = {}
		global default_state
		self._list_4_link = TextBox(new_state, default_state["list_4_link"])

	@property
	def list_4_heading(self):
		self._getter_access_tracker["list_4_heading"] = {}
		return self._list_4_heading
	@list_4_heading.setter
	def list_4_heading(self, new_state):
		self._setter_access_tracker["list_4_heading"] = {}
		global default_state
		self._list_4_heading = TextBox(new_state, default_state["list_4_heading"])

	@property
	def list_4_date(self):
		self._getter_access_tracker["list_4_date"] = {}
		return self._list_4_date
	@list_4_date.setter
	def list_4_date(self, new_state):
		self._setter_access_tracker["list_4_date"] = {}
		global default_state
		self._list_4_date = TextBox(new_state, default_state["list_4_date"])

	@property
	def point_div_4(self):
		self._getter_access_tracker["point_div_4"] = {}
		return self._point_div_4
	@point_div_4.setter
	def point_div_4(self, new_state):
		self._setter_access_tracker["point_div_4"] = {}
		global default_state
		self._point_div_4 = Div(new_state, default_state["point_div_4"])

	@property
	def list_4_time(self):
		self._getter_access_tracker["list_4_time"] = {}
		return self._list_4_time
	@list_4_time.setter
	def list_4_time(self, new_state):
		self._setter_access_tracker["list_4_time"] = {}
		global default_state
		self._list_4_time = TextBox(new_state, default_state["list_4_time"])

	@property
	def list_5_time(self):
		self._getter_access_tracker["list_5_time"] = {}
		return self._list_5_time
	@list_5_time.setter
	def list_5_time(self, new_state):
		self._setter_access_tracker["list_5_time"] = {}
		global default_state
		self._list_5_time = TextBox(new_state, default_state["list_5_time"])

	@property
	def point_div_5(self):
		self._getter_access_tracker["point_div_5"] = {}
		return self._point_div_5
	@point_div_5.setter
	def point_div_5(self, new_state):
		self._setter_access_tracker["point_div_5"] = {}
		global default_state
		self._point_div_5 = Div(new_state, default_state["point_div_5"])

	@property
	def list_5_date_(self):
		self._getter_access_tracker["list_5_date_"] = {}
		return self._list_5_date_
	@list_5_date_.setter
	def list_5_date_(self, new_state):
		self._setter_access_tracker["list_5_date_"] = {}
		global default_state
		self._list_5_date_ = TextBox(new_state, default_state["list_5_date_"])

	@property
	def list_5_heading(self):
		self._getter_access_tracker["list_5_heading"] = {}
		return self._list_5_heading
	@list_5_heading.setter
	def list_5_heading(self, new_state):
		self._setter_access_tracker["list_5_heading"] = {}
		global default_state
		self._list_5_heading = TextBox(new_state, default_state["list_5_heading"])

	@property
	def list_5_link(self):
		self._getter_access_tracker["list_5_link"] = {}
		return self._list_5_link
	@list_5_link.setter
	def list_5_link(self, new_state):
		self._setter_access_tracker["list_5_link"] = {}
		global default_state
		self._list_5_link = TextBox(new_state, default_state["list_5_link"])

	@property
	def arrow_image_5(self):
		self._getter_access_tracker["arrow_image_5"] = {}
		return self._arrow_image_5
	@arrow_image_5.setter
	def arrow_image_5(self, new_state):
		self._setter_access_tracker["arrow_image_5"] = {}
		global default_state
		self._arrow_image_5 = Image(new_state, default_state["arrow_image_5"])

	@property
	def designer_heading_main(self):
		self._getter_access_tracker["designer_heading_main"] = {}
		return self._designer_heading_main
	@designer_heading_main.setter
	def designer_heading_main(self, new_state):
		self._setter_access_tracker["designer_heading_main"] = {}
		global default_state
		self._designer_heading_main = TextBox(new_state, default_state["designer_heading_main"])

	@property
	def designer_about_heading_2(self):
		self._getter_access_tracker["designer_about_heading_2"] = {}
		return self._designer_about_heading_2
	@designer_about_heading_2.setter
	def designer_about_heading_2(self, new_state):
		self._setter_access_tracker["designer_about_heading_2"] = {}
		global default_state
		self._designer_about_heading_2 = TextBox(new_state, default_state["designer_about_heading_2"])

	@property
	def designer_about_paragraph(self):
		self._getter_access_tracker["designer_about_paragraph"] = {}
		return self._designer_about_paragraph
	@designer_about_paragraph.setter
	def designer_about_paragraph(self, new_state):
		self._setter_access_tracker["designer_about_paragraph"] = {}
		global default_state
		self._designer_about_paragraph = TextBox(new_state, default_state["designer_about_paragraph"])

	@property
	def designer_image_2(self):
		self._getter_access_tracker["designer_image_2"] = {}
		return self._designer_image_2
	@designer_image_2.setter
	def designer_image_2(self, new_state):
		self._setter_access_tracker["designer_image_2"] = {}
		global default_state
		self._designer_image_2 = Image(new_state, default_state["designer_image_2"])

	@property
	def designer_image_1(self):
		self._getter_access_tracker["designer_image_1"] = {}
		return self._designer_image_1
	@designer_image_1.setter
	def designer_image_1(self, new_state):
		self._setter_access_tracker["designer_image_1"] = {}
		global default_state
		self._designer_image_1 = Image(new_state, default_state["designer_image_1"])

	@property
	def designer_image_3(self):
		self._getter_access_tracker["designer_image_3"] = {}
		return self._designer_image_3
	@designer_image_3.setter
	def designer_image_3(self, new_state):
		self._setter_access_tracker["designer_image_3"] = {}
		global default_state
		self._designer_image_3 = Image(new_state, default_state["designer_image_3"])

	@property
	def designer_image_4(self):
		self._getter_access_tracker["designer_image_4"] = {}
		return self._designer_image_4
	@designer_image_4.setter
	def designer_image_4(self, new_state):
		self._setter_access_tracker["designer_image_4"] = {}
		global default_state
		self._designer_image_4 = Image(new_state, default_state["designer_image_4"])

	@property
	def education_heading(self):
		self._getter_access_tracker["education_heading"] = {}
		return self._education_heading
	@education_heading.setter
	def education_heading(self, new_state):
		self._setter_access_tracker["education_heading"] = {}
		global default_state
		self._education_heading = TextBox(new_state, default_state["education_heading"])

	@property
	def list_border_div_1(self):
		self._getter_access_tracker["list_border_div_1"] = {}
		return self._list_border_div_1
	@list_border_div_1.setter
	def list_border_div_1(self, new_state):
		self._setter_access_tracker["list_border_div_1"] = {}
		global default_state
		self._list_border_div_1 = Div(new_state, default_state["list_border_div_1"])

	@property
	def experience_list_item_1_link_1(self):
		self._getter_access_tracker["experience_list_item_1_link_1"] = {}
		return self._experience_list_item_1_link_1
	@experience_list_item_1_link_1.setter
	def experience_list_item_1_link_1(self, new_state):
		self._setter_access_tracker["experience_list_item_1_link_1"] = {}
		global default_state
		self._experience_list_item_1_link_1 = Link(new_state, default_state["experience_list_item_1_link_1"])

	@property
	def experience_list_item_1_heading(self):
		self._getter_access_tracker["experience_list_item_1_heading"] = {}
		return self._experience_list_item_1_heading
	@experience_list_item_1_heading.setter
	def experience_list_item_1_heading(self, new_state):
		self._setter_access_tracker["experience_list_item_1_heading"] = {}
		global default_state
		self._experience_list_item_1_heading = TextBox(new_state, default_state["experience_list_item_1_heading"])

	@property
	def list_item_1_date(self):
		self._getter_access_tracker["list_item_1_date"] = {}
		return self._list_item_1_date
	@list_item_1_date.setter
	def list_item_1_date(self, new_state):
		self._setter_access_tracker["list_item_1_date"] = {}
		global default_state
		self._list_item_1_date = TextBox(new_state, default_state["list_item_1_date"])

	@property
	def up_right_arrow_1(self):
		self._getter_access_tracker["up_right_arrow_1"] = {}
		return self._up_right_arrow_1
	@up_right_arrow_1.setter
	def up_right_arrow_1(self, new_state):
		self._setter_access_tracker["up_right_arrow_1"] = {}
		global default_state
		self._up_right_arrow_1 = Image(new_state, default_state["up_right_arrow_1"])

	@property
	def list_border_div_2(self):
		self._getter_access_tracker["list_border_div_2"] = {}
		return self._list_border_div_2
	@list_border_div_2.setter
	def list_border_div_2(self, new_state):
		self._setter_access_tracker["list_border_div_2"] = {}
		global default_state
		self._list_border_div_2 = Div(new_state, default_state["list_border_div_2"])

	@property
	def up_right_arrow_2(self):
		self._getter_access_tracker["up_right_arrow_2"] = {}
		return self._up_right_arrow_2
	@up_right_arrow_2.setter
	def up_right_arrow_2(self, new_state):
		self._setter_access_tracker["up_right_arrow_2"] = {}
		global default_state
		self._up_right_arrow_2 = Image(new_state, default_state["up_right_arrow_2"])

	@property
	def list_item__date(self):
		self._getter_access_tracker["list_item__date"] = {}
		return self._list_item__date
	@list_item__date.setter
	def list_item__date(self, new_state):
		self._setter_access_tracker["list_item__date"] = {}
		global default_state
		self._list_item__date = TextBox(new_state, default_state["list_item__date"])

	@property
	def list_item_2_link(self):
		self._getter_access_tracker["list_item_2_link"] = {}
		return self._list_item_2_link
	@list_item_2_link.setter
	def list_item_2_link(self, new_state):
		self._setter_access_tracker["list_item_2_link"] = {}
		global default_state
		self._list_item_2_link = Link(new_state, default_state["list_item_2_link"])

	@property
	def experience_list_item_2_heading(self):
		self._getter_access_tracker["experience_list_item_2_heading"] = {}
		return self._experience_list_item_2_heading
	@experience_list_item_2_heading.setter
	def experience_list_item_2_heading(self, new_state):
		self._setter_access_tracker["experience_list_item_2_heading"] = {}
		global default_state
		self._experience_list_item_2_heading = TextBox(new_state, default_state["experience_list_item_2_heading"])

	@property
	def list_border_div_3(self):
		self._getter_access_tracker["list_border_div_3"] = {}
		return self._list_border_div_3
	@list_border_div_3.setter
	def list_border_div_3(self, new_state):
		self._setter_access_tracker["list_border_div_3"] = {}
		global default_state
		self._list_border_div_3 = Div(new_state, default_state["list_border_div_3"])

	@property
	def up_right_arrow_3(self):
		self._getter_access_tracker["up_right_arrow_3"] = {}
		return self._up_right_arrow_3
	@up_right_arrow_3.setter
	def up_right_arrow_3(self, new_state):
		self._setter_access_tracker["up_right_arrow_3"] = {}
		global default_state
		self._up_right_arrow_3 = Image(new_state, default_state["up_right_arrow_3"])

	@property
	def list_item_3_date(self):
		self._getter_access_tracker["list_item_3_date"] = {}
		return self._list_item_3_date
	@list_item_3_date.setter
	def list_item_3_date(self, new_state):
		self._setter_access_tracker["list_item_3_date"] = {}
		global default_state
		self._list_item_3_date = TextBox(new_state, default_state["list_item_3_date"])

	@property
	def experience_list_item_3_heading(self):
		self._getter_access_tracker["experience_list_item_3_heading"] = {}
		return self._experience_list_item_3_heading
	@experience_list_item_3_heading.setter
	def experience_list_item_3_heading(self, new_state):
		self._setter_access_tracker["experience_list_item_3_heading"] = {}
		global default_state
		self._experience_list_item_3_heading = TextBox(new_state, default_state["experience_list_item_3_heading"])

	@property
	def experience_list_item_3_link_3(self):
		self._getter_access_tracker["experience_list_item_3_link_3"] = {}
		return self._experience_list_item_3_link_3
	@experience_list_item_3_link_3.setter
	def experience_list_item_3_link_3(self, new_state):
		self._setter_access_tracker["experience_list_item_3_link_3"] = {}
		global default_state
		self._experience_list_item_3_link_3 = Link(new_state, default_state["experience_list_item_3_link_3"])

	@property
	def list_border_div_6(self):
		self._getter_access_tracker["list_border_div_6"] = {}
		return self._list_border_div_6
	@list_border_div_6.setter
	def list_border_div_6(self, new_state):
		self._setter_access_tracker["list_border_div_6"] = {}
		global default_state
		self._list_border_div_6 = Div(new_state, default_state["list_border_div_6"])

	@property
	def right_list_item_3_image_3(self):
		self._getter_access_tracker["right_list_item_3_image_3"] = {}
		return self._right_list_item_3_image_3
	@right_list_item_3_image_3.setter
	def right_list_item_3_image_3(self, new_state):
		self._setter_access_tracker["right_list_item_3_image_3"] = {}
		global default_state
		self._right_list_item_3_image_3 = Image(new_state, default_state["right_list_item_3_image_3"])

	@property
	def experience_right_list_item_3_link_3(self):
		self._getter_access_tracker["experience_right_list_item_3_link_3"] = {}
		return self._experience_right_list_item_3_link_3
	@experience_right_list_item_3_link_3.setter
	def experience_right_list_item_3_link_3(self, new_state):
		self._setter_access_tracker["experience_right_list_item_3_link_3"] = {}
		global default_state
		self._experience_right_list_item_3_link_3 = Link(new_state, default_state["experience_right_list_item_3_link_3"])

	@property
	def experience_right_list_item_3_heading(self):
		self._getter_access_tracker["experience_right_list_item_3_heading"] = {}
		return self._experience_right_list_item_3_heading
	@experience_right_list_item_3_heading.setter
	def experience_right_list_item_3_heading(self, new_state):
		self._setter_access_tracker["experience_right_list_item_3_heading"] = {}
		global default_state
		self._experience_right_list_item_3_heading = TextBox(new_state, default_state["experience_right_list_item_3_heading"])

	@property
	def right_list_item_3_date(self):
		self._getter_access_tracker["right_list_item_3_date"] = {}
		return self._right_list_item_3_date
	@right_list_item_3_date.setter
	def right_list_item_3_date(self, new_state):
		self._setter_access_tracker["right_list_item_3_date"] = {}
		global default_state
		self._right_list_item_3_date = TextBox(new_state, default_state["right_list_item_3_date"])

	@property
	def up_right_arrow_6(self):
		self._getter_access_tracker["up_right_arrow_6"] = {}
		return self._up_right_arrow_6
	@up_right_arrow_6.setter
	def up_right_arrow_6(self, new_state):
		self._setter_access_tracker["up_right_arrow_6"] = {}
		global default_state
		self._up_right_arrow_6 = Image(new_state, default_state["up_right_arrow_6"])

	@property
	def list_border_div_5(self):
		self._getter_access_tracker["list_border_div_5"] = {}
		return self._list_border_div_5
	@list_border_div_5.setter
	def list_border_div_5(self, new_state):
		self._setter_access_tracker["list_border_div_5"] = {}
		global default_state
		self._list_border_div_5 = Div(new_state, default_state["list_border_div_5"])

	@property
	def right_list_item_2_image_2(self):
		self._getter_access_tracker["right_list_item_2_image_2"] = {}
		return self._right_list_item_2_image_2
	@right_list_item_2_image_2.setter
	def right_list_item_2_image_2(self, new_state):
		self._setter_access_tracker["right_list_item_2_image_2"] = {}
		global default_state
		self._right_list_item_2_image_2 = Image(new_state, default_state["right_list_item_2_image_2"])

	@property
	def experience_right_list_item_2_heading(self):
		self._getter_access_tracker["experience_right_list_item_2_heading"] = {}
		return self._experience_right_list_item_2_heading
	@experience_right_list_item_2_heading.setter
	def experience_right_list_item_2_heading(self, new_state):
		self._setter_access_tracker["experience_right_list_item_2_heading"] = {}
		global default_state
		self._experience_right_list_item_2_heading = TextBox(new_state, default_state["experience_right_list_item_2_heading"])

	@property
	def experience_right_list_item_2_link_2(self):
		self._getter_access_tracker["experience_right_list_item_2_link_2"] = {}
		return self._experience_right_list_item_2_link_2
	@experience_right_list_item_2_link_2.setter
	def experience_right_list_item_2_link_2(self, new_state):
		self._setter_access_tracker["experience_right_list_item_2_link_2"] = {}
		global default_state
		self._experience_right_list_item_2_link_2 = Link(new_state, default_state["experience_right_list_item_2_link_2"])

	@property
	def right_list_item_2_date(self):
		self._getter_access_tracker["right_list_item_2_date"] = {}
		return self._right_list_item_2_date
	@right_list_item_2_date.setter
	def right_list_item_2_date(self, new_state):
		self._setter_access_tracker["right_list_item_2_date"] = {}
		global default_state
		self._right_list_item_2_date = TextBox(new_state, default_state["right_list_item_2_date"])

	@property
	def up_right_arrow_5(self):
		self._getter_access_tracker["up_right_arrow_5"] = {}
		return self._up_right_arrow_5
	@up_right_arrow_5.setter
	def up_right_arrow_5(self, new_state):
		self._setter_access_tracker["up_right_arrow_5"] = {}
		global default_state
		self._up_right_arrow_5 = Image(new_state, default_state["up_right_arrow_5"])

	@property
	def list_border_div_4(self):
		self._getter_access_tracker["list_border_div_4"] = {}
		return self._list_border_div_4
	@list_border_div_4.setter
	def list_border_div_4(self, new_state):
		self._setter_access_tracker["list_border_div_4"] = {}
		global default_state
		self._list_border_div_4 = Div(new_state, default_state["list_border_div_4"])

	@property
	def right_list_item_1_image_1(self):
		self._getter_access_tracker["right_list_item_1_image_1"] = {}
		return self._right_list_item_1_image_1
	@right_list_item_1_image_1.setter
	def right_list_item_1_image_1(self, new_state):
		self._setter_access_tracker["right_list_item_1_image_1"] = {}
		global default_state
		self._right_list_item_1_image_1 = Image(new_state, default_state["right_list_item_1_image_1"])

	@property
	def up_right_arrow_4(self):
		self._getter_access_tracker["up_right_arrow_4"] = {}
		return self._up_right_arrow_4
	@up_right_arrow_4.setter
	def up_right_arrow_4(self, new_state):
		self._setter_access_tracker["up_right_arrow_4"] = {}
		global default_state
		self._up_right_arrow_4 = Image(new_state, default_state["up_right_arrow_4"])

	@property
	def right_list_item_1_date(self):
		self._getter_access_tracker["right_list_item_1_date"] = {}
		return self._right_list_item_1_date
	@right_list_item_1_date.setter
	def right_list_item_1_date(self, new_state):
		self._setter_access_tracker["right_list_item_1_date"] = {}
		global default_state
		self._right_list_item_1_date = TextBox(new_state, default_state["right_list_item_1_date"])

	@property
	def experience_right_list_item_1_heading(self):
		self._getter_access_tracker["experience_right_list_item_1_heading"] = {}
		return self._experience_right_list_item_1_heading
	@experience_right_list_item_1_heading.setter
	def experience_right_list_item_1_heading(self, new_state):
		self._setter_access_tracker["experience_right_list_item_1_heading"] = {}
		global default_state
		self._experience_right_list_item_1_heading = TextBox(new_state, default_state["experience_right_list_item_1_heading"])

	@property
	def experience_right_list_item_1_link_1(self):
		self._getter_access_tracker["experience_right_list_item_1_link_1"] = {}
		return self._experience_right_list_item_1_link_1
	@experience_right_list_item_1_link_1.setter
	def experience_right_list_item_1_link_1(self, new_state):
		self._setter_access_tracker["experience_right_list_item_1_link_1"] = {}
		global default_state
		self._experience_right_list_item_1_link_1 = Link(new_state, default_state["experience_right_list_item_1_link_1"])

	@property
	def work_experience_heading(self):
		self._getter_access_tracker["work_experience_heading"] = {}
		return self._work_experience_heading
	@work_experience_heading.setter
	def work_experience_heading(self, new_state):
		self._setter_access_tracker["work_experience_heading"] = {}
		global default_state
		self._work_experience_heading = TextBox(new_state, default_state["work_experience_heading"])

	@property
	def testimonials_heading_1(self):
		self._getter_access_tracker["testimonials_heading_1"] = {}
		return self._testimonials_heading_1
	@testimonials_heading_1.setter
	def testimonials_heading_1(self, new_state):
		self._setter_access_tracker["testimonials_heading_1"] = {}
		global default_state
		self._testimonials_heading_1 = TextBox(new_state, default_state["testimonials_heading_1"])

	@property
	def testimonials_heading_2(self):
		self._getter_access_tracker["testimonials_heading_2"] = {}
		return self._testimonials_heading_2
	@testimonials_heading_2.setter
	def testimonials_heading_2(self, new_state):
		self._setter_access_tracker["testimonials_heading_2"] = {}
		global default_state
		self._testimonials_heading_2 = TextBox(new_state, default_state["testimonials_heading_2"])

	@property
	def testimonial_1_image(self):
		self._getter_access_tracker["testimonial_1_image"] = {}
		return self._testimonial_1_image
	@testimonial_1_image.setter
	def testimonial_1_image(self, new_state):
		self._setter_access_tracker["testimonial_1_image"] = {}
		global default_state
		self._testimonial_1_image = Image(new_state, default_state["testimonial_1_image"])

	@property
	def double_quotes_image(self):
		self._getter_access_tracker["double_quotes_image"] = {}
		return self._double_quotes_image
	@double_quotes_image.setter
	def double_quotes_image(self, new_state):
		self._setter_access_tracker["double_quotes_image"] = {}
		global default_state
		self._double_quotes_image = Image(new_state, default_state["double_quotes_image"])

	@property
	def detail(self):
		self._getter_access_tracker["detail"] = {}
		return self._detail
	@detail.setter
	def detail(self, new_state):
		self._setter_access_tracker["detail"] = {}
		global default_state
		self._detail = TextBox(new_state, default_state["detail"])

	@property
	def testimonial_name(self):
		self._getter_access_tracker["testimonial_name"] = {}
		return self._testimonial_name
	@testimonial_name.setter
	def testimonial_name(self, new_state):
		self._setter_access_tracker["testimonial_name"] = {}
		global default_state
		self._testimonial_name = TextBox(new_state, default_state["testimonial_name"])

	@property
	def testimonial_designation(self):
		self._getter_access_tracker["testimonial_designation"] = {}
		return self._testimonial_designation
	@testimonial_designation.setter
	def testimonial_designation(self, new_state):
		self._setter_access_tracker["testimonial_designation"] = {}
		global default_state
		self._testimonial_designation = TextBox(new_state, default_state["testimonial_designation"])

	@property
	def left_arrow(self):
		self._getter_access_tracker["left_arrow"] = {}
		return self._left_arrow
	@left_arrow.setter
	def left_arrow(self, new_state):
		self._setter_access_tracker["left_arrow"] = {}
		global default_state
		self._left_arrow = Image(new_state, default_state["left_arrow"])

	@property
	def right_arrow(self):
		self._getter_access_tracker["right_arrow"] = {}
		return self._right_arrow
	@right_arrow.setter
	def right_arrow(self, new_state):
		self._setter_access_tracker["right_arrow"] = {}
		global default_state
		self._right_arrow = Image(new_state, default_state["right_arrow"])

	@property
	def faq_heading(self):
		self._getter_access_tracker["faq_heading"] = {}
		return self._faq_heading
	@faq_heading.setter
	def faq_heading(self, new_state):
		self._setter_access_tracker["faq_heading"] = {}
		global default_state
		self._faq_heading = TextBox(new_state, default_state["faq_heading"])

	@property
	def faq_heading_2(self):
		self._getter_access_tracker["faq_heading_2"] = {}
		return self._faq_heading_2
	@faq_heading_2.setter
	def faq_heading_2(self, new_state):
		self._setter_access_tracker["faq_heading_2"] = {}
		global default_state
		self._faq_heading_2 = TextBox(new_state, default_state["faq_heading_2"])

	@property
	def list_question_1(self):
		self._getter_access_tracker["list_question_1"] = {}
		return self._list_question_1
	@list_question_1.setter
	def list_question_1(self, new_state):
		self._setter_access_tracker["list_question_1"] = {}
		global default_state
		self._list_question_1 = TextBox(new_state, default_state["list_question_1"])

	@property
	def list_down_arrow_1(self):
		self._getter_access_tracker["list_down_arrow_1"] = {}
		return self._list_down_arrow_1
	@list_down_arrow_1.setter
	def list_down_arrow_1(self, new_state):
		self._setter_access_tracker["list_down_arrow_1"] = {}
		global default_state
		self._list_down_arrow_1 = Image(new_state, default_state["list_down_arrow_1"])

	@property
	def list_down_arrow_4(self):
		self._getter_access_tracker["list_down_arrow_4"] = {}
		return self._list_down_arrow_4
	@list_down_arrow_4.setter
	def list_down_arrow_4(self, new_state):
		self._setter_access_tracker["list_down_arrow_4"] = {}
		global default_state
		self._list_down_arrow_4 = Image(new_state, default_state["list_down_arrow_4"])

	@property
	def list_question_4(self):
		self._getter_access_tracker["list_question_4"] = {}
		return self._list_question_4
	@list_question_4.setter
	def list_question_4(self, new_state):
		self._setter_access_tracker["list_question_4"] = {}
		global default_state
		self._list_question_4 = TextBox(new_state, default_state["list_question_4"])

	@property
	def list_down_arrow_2(self):
		self._getter_access_tracker["list_down_arrow_2"] = {}
		return self._list_down_arrow_2
	@list_down_arrow_2.setter
	def list_down_arrow_2(self, new_state):
		self._setter_access_tracker["list_down_arrow_2"] = {}
		global default_state
		self._list_down_arrow_2 = Image(new_state, default_state["list_down_arrow_2"])

	@property
	def list_question_2(self):
		self._getter_access_tracker["list_question_2"] = {}
		return self._list_question_2
	@list_question_2.setter
	def list_question_2(self, new_state):
		self._setter_access_tracker["list_question_2"] = {}
		global default_state
		self._list_question_2 = TextBox(new_state, default_state["list_question_2"])

	@property
	def list_down_arrow_3(self):
		self._getter_access_tracker["list_down_arrow_3"] = {}
		return self._list_down_arrow_3
	@list_down_arrow_3.setter
	def list_down_arrow_3(self, new_state):
		self._setter_access_tracker["list_down_arrow_3"] = {}
		global default_state
		self._list_down_arrow_3 = Image(new_state, default_state["list_down_arrow_3"])

	@property
	def list_question_3(self):
		self._getter_access_tracker["list_question_3"] = {}
		return self._list_question_3
	@list_question_3.setter
	def list_question_3(self, new_state):
		self._setter_access_tracker["list_question_3"] = {}
		global default_state
		self._list_question_3 = TextBox(new_state, default_state["list_question_3"])

	@property
	def right_list_question_3(self):
		self._getter_access_tracker["right_list_question_3"] = {}
		return self._right_list_question_3
	@right_list_question_3.setter
	def right_list_question_3(self, new_state):
		self._setter_access_tracker["right_list_question_3"] = {}
		global default_state
		self._right_list_question_3 = TextBox(new_state, default_state["right_list_question_3"])

	@property
	def right_list_down_arrow_3(self):
		self._getter_access_tracker["right_list_down_arrow_3"] = {}
		return self._right_list_down_arrow_3
	@right_list_down_arrow_3.setter
	def right_list_down_arrow_3(self, new_state):
		self._setter_access_tracker["right_list_down_arrow_3"] = {}
		global default_state
		self._right_list_down_arrow_3 = Image(new_state, default_state["right_list_down_arrow_3"])

	@property
	def right_list_question_2(self):
		self._getter_access_tracker["right_list_question_2"] = {}
		return self._right_list_question_2
	@right_list_question_2.setter
	def right_list_question_2(self, new_state):
		self._setter_access_tracker["right_list_question_2"] = {}
		global default_state
		self._right_list_question_2 = TextBox(new_state, default_state["right_list_question_2"])

	@property
	def list_down_arrow_6(self):
		self._getter_access_tracker["list_down_arrow_6"] = {}
		return self._list_down_arrow_6
	@list_down_arrow_6.setter
	def list_down_arrow_6(self, new_state):
		self._setter_access_tracker["list_down_arrow_6"] = {}
		global default_state
		self._list_down_arrow_6 = Image(new_state, default_state["list_down_arrow_6"])

	@property
	def right_list_question_4(self):
		self._getter_access_tracker["right_list_question_4"] = {}
		return self._right_list_question_4
	@right_list_question_4.setter
	def right_list_question_4(self, new_state):
		self._setter_access_tracker["right_list_question_4"] = {}
		global default_state
		self._right_list_question_4 = TextBox(new_state, default_state["right_list_question_4"])

	@property
	def right_list_down_arrow_4(self):
		self._getter_access_tracker["right_list_down_arrow_4"] = {}
		return self._right_list_down_arrow_4
	@right_list_down_arrow_4.setter
	def right_list_down_arrow_4(self, new_state):
		self._setter_access_tracker["right_list_down_arrow_4"] = {}
		global default_state
		self._right_list_down_arrow_4 = Image(new_state, default_state["right_list_down_arrow_4"])

	@property
	def list_down_arrow_5(self):
		self._getter_access_tracker["list_down_arrow_5"] = {}
		return self._list_down_arrow_5
	@list_down_arrow_5.setter
	def list_down_arrow_5(self, new_state):
		self._setter_access_tracker["list_down_arrow_5"] = {}
		global default_state
		self._list_down_arrow_5 = Image(new_state, default_state["list_down_arrow_5"])

	@property
	def right_list_question_1(self):
		self._getter_access_tracker["right_list_question_1"] = {}
		return self._right_list_question_1
	@right_list_question_1.setter
	def right_list_question_1(self, new_state):
		self._setter_access_tracker["right_list_question_1"] = {}
		global default_state
		self._right_list_question_1 = TextBox(new_state, default_state["right_list_question_1"])

	@property
	def footer_heading_1(self):
		self._getter_access_tracker["footer_heading_1"] = {}
		return self._footer_heading_1
	@footer_heading_1.setter
	def footer_heading_1(self, new_state):
		self._setter_access_tracker["footer_heading_1"] = {}
		global default_state
		self._footer_heading_1 = TextBox(new_state, default_state["footer_heading_1"])

	@property
	def footer_heading_2(self):
		self._getter_access_tracker["footer_heading_2"] = {}
		return self._footer_heading_2
	@footer_heading_2.setter
	def footer_heading_2(self, new_state):
		self._setter_access_tracker["footer_heading_2"] = {}
		global default_state
		self._footer_heading_2 = TextBox(new_state, default_state["footer_heading_2"])

	@property
	def logo_link_image(self):
		self._getter_access_tracker["logo_link_image"] = {}
		return self._logo_link_image
	@logo_link_image.setter
	def logo_link_image(self, new_state):
		self._setter_access_tracker["logo_link_image"] = {}
		global default_state
		self._logo_link_image = Image(new_state, default_state["logo_link_image"])

	@property
	def address_text(self):
		self._getter_access_tracker["address_text"] = {}
		return self._address_text
	@address_text.setter
	def address_text(self, new_state):
		self._setter_access_tracker["address_text"] = {}
		global default_state
		self._address_text = TextBox(new_state, default_state["address_text"])

	@property
	def mail_icon_image(self):
		self._getter_access_tracker["mail_icon_image"] = {}
		return self._mail_icon_image
	@mail_icon_image.setter
	def mail_icon_image(self, new_state):
		self._setter_access_tracker["mail_icon_image"] = {}
		global default_state
		self._mail_icon_image = Image(new_state, default_state["mail_icon_image"])

	@property
	def mail_link(self):
		self._getter_access_tracker["mail_link"] = {}
		return self._mail_link
	@mail_link.setter
	def mail_link(self, new_state):
		self._setter_access_tracker["mail_link"] = {}
		global default_state
		self._mail_link = Link(new_state, default_state["mail_link"])

	@property
	def footer_link_9(self):
		self._getter_access_tracker["footer_link_9"] = {}
		return self._footer_link_9
	@footer_link_9.setter
	def footer_link_9(self, new_state):
		self._setter_access_tracker["footer_link_9"] = {}
		global default_state
		self._footer_link_9 = Link(new_state, default_state["footer_link_9"])

	@property
	def footer_link_1(self):
		self._getter_access_tracker["footer_link_1"] = {}
		return self._footer_link_1
	@footer_link_1.setter
	def footer_link_1(self, new_state):
		self._setter_access_tracker["footer_link_1"] = {}
		global default_state
		self._footer_link_1 = Link(new_state, default_state["footer_link_1"])

	@property
	def footer_link_2(self):
		self._getter_access_tracker["footer_link_2"] = {}
		return self._footer_link_2
	@footer_link_2.setter
	def footer_link_2(self, new_state):
		self._setter_access_tracker["footer_link_2"] = {}
		global default_state
		self._footer_link_2 = Link(new_state, default_state["footer_link_2"])

	@property
	def footer_link_7(self):
		self._getter_access_tracker["footer_link_7"] = {}
		return self._footer_link_7
	@footer_link_7.setter
	def footer_link_7(self, new_state):
		self._setter_access_tracker["footer_link_7"] = {}
		global default_state
		self._footer_link_7 = Link(new_state, default_state["footer_link_7"])

	@property
	def footer_link_6(self):
		self._getter_access_tracker["footer_link_6"] = {}
		return self._footer_link_6
	@footer_link_6.setter
	def footer_link_6(self, new_state):
		self._setter_access_tracker["footer_link_6"] = {}
		global default_state
		self._footer_link_6 = Link(new_state, default_state["footer_link_6"])

	@property
	def footer_link_3(self):
		self._getter_access_tracker["footer_link_3"] = {}
		return self._footer_link_3
	@footer_link_3.setter
	def footer_link_3(self, new_state):
		self._setter_access_tracker["footer_link_3"] = {}
		global default_state
		self._footer_link_3 = Link(new_state, default_state["footer_link_3"])

	@property
	def footer_link_5(self):
		self._getter_access_tracker["footer_link_5"] = {}
		return self._footer_link_5
	@footer_link_5.setter
	def footer_link_5(self, new_state):
		self._setter_access_tracker["footer_link_5"] = {}
		global default_state
		self._footer_link_5 = Link(new_state, default_state["footer_link_5"])

	@property
	def footer_link_4(self):
		self._getter_access_tracker["footer_link_4"] = {}
		return self._footer_link_4
	@footer_link_4.setter
	def footer_link_4(self, new_state):
		self._setter_access_tracker["footer_link_4"] = {}
		global default_state
		self._footer_link_4 = Link(new_state, default_state["footer_link_4"])

	@property
	def footer_link_8(self):
		self._getter_access_tracker["footer_link_8"] = {}
		return self._footer_link_8
	@footer_link_8.setter
	def footer_link_8(self, new_state):
		self._setter_access_tracker["footer_link_8"] = {}
		global default_state
		self._footer_link_8 = Link(new_state, default_state["footer_link_8"])

	@property
	def rights_text(self):
		self._getter_access_tracker["rights_text"] = {}
		return self._rights_text
	@rights_text.setter
	def rights_text(self, new_state):
		self._setter_access_tracker["rights_text"] = {}
		global default_state
		self._rights_text = TextBox(new_state, default_state["rights_text"])

	@property
	def Conversionflow_link(self):
		self._getter_access_tracker["Conversionflow_link"] = {}
		return self._Conversionflow_link
	@Conversionflow_link.setter
	def Conversionflow_link(self, new_state):
		self._setter_access_tracker["Conversionflow_link"] = {}
		global default_state
		self._Conversionflow_link = Link(new_state, default_state["Conversionflow_link"])

	@property
	def powered_rext(self):
		self._getter_access_tracker["powered_rext"] = {}
		return self._powered_rext
	@powered_rext.setter
	def powered_rext(self, new_state):
		self._setter_access_tracker["powered_rext"] = {}
		global default_state
		self._powered_rext = TextBox(new_state, default_state["powered_rext"])

	@property
	def Webflow_link(self):
		self._getter_access_tracker["Webflow_link"] = {}
		return self._Webflow_link
	@Webflow_link.setter
	def Webflow_link(self, new_state):
		self._setter_access_tracker["Webflow_link"] = {}
		global default_state
		self._Webflow_link = Link(new_state, default_state["Webflow_link"])

	@property
	def image_text_link(self):
		self._getter_access_tracker["image_text_link"] = {}
		return self._image_text_link
	@image_text_link.setter
	def image_text_link(self, new_state):
		self._setter_access_tracker["image_text_link"] = {}
		global default_state
		self._image_text_link = Link(new_state, default_state["image_text_link"])

	@property
	def instructions_link(self):
		self._getter_access_tracker["instructions_link"] = {}
		return self._instructions_link
	@instructions_link.setter
	def instructions_link(self, new_state):
		self._setter_access_tracker["instructions_link"] = {}
		global default_state
		self._instructions_link = Link(new_state, default_state["instructions_link"])

	@property
	def Changelog_link(self):
		self._getter_access_tracker["Changelog_link"] = {}
		return self._Changelog_link
	@Changelog_link.setter
	def Changelog_link(self, new_state):
		self._setter_access_tracker["Changelog_link"] = {}
		global default_state
		self._Changelog_link = Link(new_state, default_state["Changelog_link"])

	@property
	def last_link(self):
		self._getter_access_tracker["last_link"] = {}
		return self._last_link
	@last_link.setter
	def last_link(self, new_state):
		self._setter_access_tracker["last_link"] = {}
		global default_state
		self._last_link = Link(new_state, default_state["last_link"])

	@property
	def webflow_logo(self):
		self._getter_access_tracker["webflow_logo"] = {}
		return self._webflow_logo
	@webflow_logo.setter
	def webflow_logo(self, new_state):
		self._setter_access_tracker["webflow_logo"] = {}
		global default_state
		self._webflow_logo = Image(new_state, default_state["webflow_logo"])

	@property
	def webflow_text_image(self):
		self._getter_access_tracker["webflow_text_image"] = {}
		return self._webflow_text_image
	@webflow_text_image.setter
	def webflow_text_image(self, new_state):
		self._setter_access_tracker["webflow_text_image"] = {}
		global default_state
		self._webflow_text_image = Image(new_state, default_state["webflow_text_image"])

	def _to_json_fields(self):
		return {
			"nav_container": self._nav_container,
			"nav_bar_div": self._nav_bar_div,
			"side_nav": self._side_nav,
			"hero_main": self._hero_main,
			"hero_flex": self._hero_flex,
			"heading_paragraph": self._heading_paragraph,
			"hero_button_link": self._hero_button_link,
			"call_button_div": self._call_button_div,
			"companies": self._companies,
			"services_div": self._services_div,
			"services_main": self._services_main,
			"sevices_head_main": self._sevices_head_main,
			"head_2": self._head_2,
			"services_flex": self._services_flex,
			"sub_service_1": self._sub_service_1,
			"services_heading_1": self._services_heading_1,
			"services_1_paragraph1": self._services_1_paragraph1,
			"services_list_1": self._services_list_1,
			"services_pointer_1": self._services_pointer_1,
			"services_list_item_1": self._services_list_item_1,
			"Flex36": self._Flex36,
			"list_pointer_head_3": self._list_pointer_head_3,
			"Flex92": self._Flex92,
			"Flex91": self._Flex91,
			"list_ponter_head_9ac": self._list_ponter_head_9ac,
			"Flex90": self._Flex90,
			"Div111": self._Div111,
			"list_pointer_head_7": self._list_pointer_head_7,
			"Div112": self._Div112,
			"Div113": self._Div113,
			"sub_service_2": self._sub_service_2,
			"Div118": self._Div118,
			"Div119": self._Div119,
			"Flex96": self._Flex96,
			"Div117": self._Div117,
			"list_pointer_head_4": self._list_pointer_head_4,
			"Flex94": self._Flex94,
			"Flex95": self._Flex95,
			"projects_head_paragraph_1": self._projects_head_paragraph_1,
			"projects_heading_1": self._projects_heading_1,
			"heading_2_3_div": self._heading_2_3_div,
			"view_projects_button_div": self._view_projects_button_div,
			"projects_slider_flex": self._projects_slider_flex,
			"projects_slider_3": self._projects_slider_3,
			"project_slider_3_paragraph_head": self._project_slider_3_paragraph_head,
			"slider_3_link_flex": self._slider_3_link_flex,
			"slider_item_2": self._slider_item_2,
			"slider_item_2_head": self._slider_item_2_head,
			"slider_item_2_link_2": self._slider_item_2_link_2,
			"slider_item_1": self._slider_item_1,
			"slider_item1_head_flex": self._slider_item1_head_flex,
			"Flex136": self._Flex136,
			"slider_button_left": self._slider_button_left,
			"sliderbutton_right": self._sliderbutton_right,
			"blogs_main_div": self._blogs_main_div,
			"blogs_main_flex": self._blogs_main_flex,
			"blogs_heading_div": self._blogs_heading_div,
			"blogs_view_all_link_flex": self._blogs_view_all_link_flex,
			"blog_list_div_main": self._blog_list_div_main,
			"list_item_1_flex": self._list_item_1_flex,
			"list_item_1_date_time": self._list_item_1_date_time,
			"heading_date_time_flex": self._heading_date_time_flex,
			"list_heading_2_div": self._list_heading_2_div,
			"list_item_1_read_link_flex": self._list_item_1_read_link_flex,
			"list_item_2_flex": self._list_item_2_flex,
			"list_item_2_link_flex": self._list_item_2_link_flex,
			"list_item_2_heading_div": self._list_item_2_heading_div,
			"Div166": self._Div166,
			"Flex158": self._Flex158,
			"list_item_3_flex": self._list_item_3_flex,
			"Div168": self._Div168,
			"point_div_3": self._point_div_3,
			"list_3_heading_div": self._list_3_heading_div,
			"list_3_link": self._list_3_link,
			"list_item_4_flex": self._list_item_4_flex,
			"list_4_link_flex": self._list_4_link_flex,
			"list_4_heading_div": self._list_4_heading_div,
			"Div172": self._Div172,
			"Flex164": self._Flex164,
			"list_item_5_flex": self._list_item_5_flex,
			"Div174": self._Div174,
			"Flex167": self._Flex167,
			"vlist_5_heading_div": self._vlist_5_heading_div,
			"list_5_link_flex": self._list_5_link_flex,
			"pro_designer_main": self._pro_designer_main,
			"designer_details_flex": self._designer_details_flex,
			"designer_deatails_div": self._designer_deatails_div,
			"designer_about_paragraph_div": self._designer_about_paragraph_div,
			"designer_image_flex": self._designer_image_flex,
			"designer_2_image_flex": self._designer_2_image_flex,
			"experience_main_div": self._experience_main_div,
			"experience_flex": self._experience_flex,
			"experience_left_div": self._experience_left_div,
			"experience_heading_div": self._experience_heading_div,
			"experience_list": self._experience_list,
			"experience_list_item_1": self._experience_list_item_1,
			"list_item_1_heading_div": self._list_item_1_heading_div,
			"experience_list_item_1_year_1_flex": self._experience_list_item_1_year_1_flex,
			"experience_list_item_2": self._experience_list_item_2,
			"experience_list_item_2_year_2_flex": self._experience_list_item_2_year_2_flex,
			"list_item__heading_div": self._list_item__heading_div,
			"experience_list_item_3": self._experience_list_item_3,
			"experience_list_item__year_3_flex": self._experience_list_item__year_3_flex,
			"list_item_3_heading_div": self._list_item_3_heading_div,
			"experience_right_div": self._experience_right_div,
			"Div200": self._Div200,
			"experience_right_list_item_3": self._experience_right_list_item_3,
			"right_list_item_3_heading_div": self._right_list_item_3_heading_div,
			"experience_right_ist_item_3_year_3_flex": self._experience_right_ist_item_3_year_3_flex,
			"experience_right_list_item_2": self._experience_right_list_item_2,
			"right_list_item_2_heading_div": self._right_list_item_2_heading_div,
			"experience_right_ist_item_2_year_2_flex": self._experience_right_ist_item_2_year_2_flex,
			"experience_right_list_item_1": self._experience_right_list_item_1,
			"experience_right_ist_item_1_year_1_flex": self._experience_right_ist_item_1_year_1_flex,
			"right_list_item_1_heading_div": self._right_list_item_1_heading_div,
			"Div201": self._Div201,
			"testimonials_main": self._testimonials_main,
			"testimonials_headings_flex": self._testimonials_headings_flex,
			"testimonial_1_flex": self._testimonial_1_flex,
			"testimonial_details": self._testimonial_details,
			"detail_div": self._detail_div,
			"testimonial_name_div": self._testimonial_name_div,
			"left_arrow_button": self._left_arrow_button,
			"right_arrow_div": self._right_arrow_div,
			"faq_main": self._faq_main,
			"faq_heading_div": self._faq_heading_div,
			"faq_list_main_flex": self._faq_list_main_flex,
			"faq_left_list": self._faq_left_list,
			"faq_list_item_1": self._faq_list_item_1,
			"faq_list_heading_flex_1": self._faq_list_heading_flex_1,
			"faq_list_item_4": self._faq_list_item_4,
			"faq_list_item_2": self._faq_list_item_2,
			"faq_list_item_3": self._faq_list_item_3,
			"faq_right_list": self._faq_right_list,
			"faq_right_list_item_3": self._faq_right_list_item_3,
			"faq_right_list_item_2": self._faq_right_list_item_2,
			"faq_right_list_item_4": self._faq_right_list_item_4,
			"faq_right_list_item_1": self._faq_right_list_item_1,
			"faq_right_list_heading_flex_1": self._faq_right_list_heading_flex_1,
			"footer_main_div": self._footer_main_div,
			"footer_headings_flex": self._footer_headings_flex,
			"footer_heading_div": self._footer_heading_div,
			"footer_links_flex": self._footer_links_flex,
			"website_details_div": self._website_details_div,
			"mail_flex": self._mail_flex,
			"links_grid": self._links_grid,
			"copyright_div": self._copyright_div,
			"webflow_div": self._webflow_div,
			"trust_heading": self._trust_heading,
			"projects_view_button_back": self._projects_view_button_back,
			"logo_img": self._logo_img,
			"call_link": self._call_link,
			"about_link": self._about_link,
			"blog_link": self._blog_link,
			"project_link": self._project_link,
			"services_link": self._services_link,
			"nav_call_arrow": self._nav_call_arrow,
			"trusted_div_main": self._trusted_div_main,
			"hero_image": self._hero_image,
			"heading_1": self._heading_1,
			"heading_2": self._heading_2,
			"heading_3": self._heading_3,
			"paragraph": self._paragraph,
			"button_background": self._button_background,
			"CV_link": self._CV_link,
			"call_button": self._call_button,
			"company_1": self._company_1,
			"company_2": self._company_2,
			"company_3": self._company_3,
			"company_4": self._company_4,
			"projects_main": self._projects_main,
			"services_heading": self._services_heading,
			"serices_paragraph": self._serices_paragraph,
			"services_image_1": self._services_image_1,
			"list_heading_1": self._list_heading_1,
			"list_paragraph_1": self._list_paragraph_1,
			"services_bullet_point_1": self._services_bullet_point_1,
			"list_pointer_heading": self._list_pointer_heading,
			"list_pointer_head_2": self._list_pointer_head_2,
			"Div46": self._Div46,
			"pointer_list_heading_3": self._pointer_list_heading_3,
			"Div47": self._Div47,
			"services_image_3": self._services_image_3,
			"Div109": self._Div109,
			"list_pointer_heading_9": self._list_pointer_heading_9,
			"Div110": self._Div110,
			"list_pointer_heading_8": self._list_pointer_heading_8,
			"TextBox78": self._TextBox78,
			"Div108": self._Div108,
			"list_paragraph_3": self._list_paragraph_3,
			"list_heading_3": self._list_heading_3,
			"services_image_2": self._services_image_2,
			"list_heading_2": self._list_heading_2,
			"list_paragraph_2": self._list_paragraph_2,
			"Div114": self._Div114,
			"list_pointer_heading_2": self._list_pointer_heading_2,
			"list_pointer_head_5": self._list_pointer_head_5,
			"Div115": self._Div115,
			"list_pointer_heading_6": self._list_pointer_heading_6,
			"Div116": self._Div116,
			"projects_head_1": self._projects_head_1,
			"projects_heading_2": self._projects_heading_2,
			"projeccts_heading_3": self._projeccts_heading_3,
			"view_projects_button": self._view_projects_button,
			"slider_3_image": self._slider_3_image,
			"slider_3_head_1": self._slider_3_head_1,
			"slider_3_head_2": self._slider_3_head_2,
			"slider_3_flex_head_3": self._slider_3_flex_head_3,
			"slider_3_head_image": self._slider_3_head_image,
			"slider_item_1_image_2": self._slider_item_1_image_2,
			"slider_item_2_head_2": self._slider_item_2_head_2,
			"slider_item_2_product": self._slider_item_2_product,
			"Image44": self._Image44,
			"TextBox116": self._TextBox116,
			"slider_image_1": self._slider_image_1,
			"slider_item_1_head_2": self._slider_item_1_head_2,
			"slider_branding_head": self._slider_branding_head,
			"arrow_image_1": self._arrow_image_1,
			"slider_view_link_1": self._slider_view_link_1,
			"blog_left_arrow_image": self._blog_left_arrow_image,
			"blogs_right_arrow_image": self._blogs_right_arrow_image,
			"heading_blogs": self._heading_blogs,
			"latest_blogs_heading": self._latest_blogs_heading,
			"view_all_link": self._view_all_link,
			"arrow_image": self._arrow_image,
			"heading_time": self._heading_time,
			"point_div1": self._point_div1,
			"heading_date": self._heading_date,
			"list_item_1_heading_2": self._list_item_1_heading_2,
			"list_1_read_link": self._list_1_read_link,
			"list_link_arrow_image": self._list_link_arrow_image,
			"list_arrow_image": self._list_arrow_image,
			"list_2_link": self._list_2_link,
			"list_item_heading_2": self._list_item_heading_2,
			"list_item_2_date": self._list_item_2_date,
			"point_div_2": self._point_div_2,
			"list_item_2_time": self._list_item_2_time,
			"list_3_time": self._list_3_time,
			"point_div3": self._point_div3,
			"list_3_date": self._list_3_date,
			"list_3_heading": self._list_3_heading,
			"list_3_link_3": self._list_3_link_3,
			"arrow_image_3": self._arrow_image_3,
			"arrow_image_4": self._arrow_image_4,
			"list_4_link": self._list_4_link,
			"list_4_heading": self._list_4_heading,
			"list_4_date": self._list_4_date,
			"point_div_4": self._point_div_4,
			"list_4_time": self._list_4_time,
			"list_5_time": self._list_5_time,
			"point_div_5": self._point_div_5,
			"list_5_date_": self._list_5_date_,
			"list_5_heading": self._list_5_heading,
			"list_5_link": self._list_5_link,
			"arrow_image_5": self._arrow_image_5,
			"designer_heading_main": self._designer_heading_main,
			"designer_about_heading_2": self._designer_about_heading_2,
			"designer_about_paragraph": self._designer_about_paragraph,
			"designer_image_2": self._designer_image_2,
			"designer_image_1": self._designer_image_1,
			"designer_image_3": self._designer_image_3,
			"designer_image_4": self._designer_image_4,
			"education_heading": self._education_heading,
			"list_border_div_1": self._list_border_div_1,
			"experience_list_item_1_link_1": self._experience_list_item_1_link_1,
			"experience_list_item_1_heading": self._experience_list_item_1_heading,
			"list_item_1_date": self._list_item_1_date,
			"up_right_arrow_1": self._up_right_arrow_1,
			"list_border_div_2": self._list_border_div_2,
			"up_right_arrow_2": self._up_right_arrow_2,
			"list_item__date": self._list_item__date,
			"list_item_2_link": self._list_item_2_link,
			"experience_list_item_2_heading": self._experience_list_item_2_heading,
			"list_border_div_3": self._list_border_div_3,
			"up_right_arrow_3": self._up_right_arrow_3,
			"list_item_3_date": self._list_item_3_date,
			"experience_list_item_3_heading": self._experience_list_item_3_heading,
			"experience_list_item_3_link_3": self._experience_list_item_3_link_3,
			"list_border_div_6": self._list_border_div_6,
			"right_list_item_3_image_3": self._right_list_item_3_image_3,
			"experience_right_list_item_3_link_3": self._experience_right_list_item_3_link_3,
			"experience_right_list_item_3_heading": self._experience_right_list_item_3_heading,
			"right_list_item_3_date": self._right_list_item_3_date,
			"up_right_arrow_6": self._up_right_arrow_6,
			"list_border_div_5": self._list_border_div_5,
			"right_list_item_2_image_2": self._right_list_item_2_image_2,
			"experience_right_list_item_2_heading": self._experience_right_list_item_2_heading,
			"experience_right_list_item_2_link_2": self._experience_right_list_item_2_link_2,
			"right_list_item_2_date": self._right_list_item_2_date,
			"up_right_arrow_5": self._up_right_arrow_5,
			"list_border_div_4": self._list_border_div_4,
			"right_list_item_1_image_1": self._right_list_item_1_image_1,
			"up_right_arrow_4": self._up_right_arrow_4,
			"right_list_item_1_date": self._right_list_item_1_date,
			"experience_right_list_item_1_heading": self._experience_right_list_item_1_heading,
			"experience_right_list_item_1_link_1": self._experience_right_list_item_1_link_1,
			"work_experience_heading": self._work_experience_heading,
			"testimonials_heading_1": self._testimonials_heading_1,
			"testimonials_heading_2": self._testimonials_heading_2,
			"testimonial_1_image": self._testimonial_1_image,
			"double_quotes_image": self._double_quotes_image,
			"detail": self._detail,
			"testimonial_name": self._testimonial_name,
			"testimonial_designation": self._testimonial_designation,
			"left_arrow": self._left_arrow,
			"right_arrow": self._right_arrow,
			"faq_heading": self._faq_heading,
			"faq_heading_2": self._faq_heading_2,
			"list_question_1": self._list_question_1,
			"list_down_arrow_1": self._list_down_arrow_1,
			"list_down_arrow_4": self._list_down_arrow_4,
			"list_question_4": self._list_question_4,
			"list_down_arrow_2": self._list_down_arrow_2,
			"list_question_2": self._list_question_2,
			"list_down_arrow_3": self._list_down_arrow_3,
			"list_question_3": self._list_question_3,
			"right_list_question_3": self._right_list_question_3,
			"right_list_down_arrow_3": self._right_list_down_arrow_3,
			"right_list_question_2": self._right_list_question_2,
			"list_down_arrow_6": self._list_down_arrow_6,
			"right_list_question_4": self._right_list_question_4,
			"right_list_down_arrow_4": self._right_list_down_arrow_4,
			"list_down_arrow_5": self._list_down_arrow_5,
			"right_list_question_1": self._right_list_question_1,
			"footer_heading_1": self._footer_heading_1,
			"footer_heading_2": self._footer_heading_2,
			"logo_link_image": self._logo_link_image,
			"address_text": self._address_text,
			"mail_icon_image": self._mail_icon_image,
			"mail_link": self._mail_link,
			"footer_link_9": self._footer_link_9,
			"footer_link_1": self._footer_link_1,
			"footer_link_2": self._footer_link_2,
			"footer_link_7": self._footer_link_7,
			"footer_link_6": self._footer_link_6,
			"footer_link_3": self._footer_link_3,
			"footer_link_5": self._footer_link_5,
			"footer_link_4": self._footer_link_4,
			"footer_link_8": self._footer_link_8,
			"rights_text": self._rights_text,
			"Conversionflow_link": self._Conversionflow_link,
			"powered_rext": self._powered_rext,
			"Webflow_link": self._Webflow_link,
			"image_text_link": self._image_text_link,
			"instructions_link": self._instructions_link,
			"Changelog_link": self._Changelog_link,
			"last_link": self._last_link,
			"webflow_logo": self._webflow_logo,
			"webflow_text_image": self._webflow_text_image,
			}


class DivstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Div:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: DivstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = DivstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class FlexstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.display: str = get_defined_value(state, def_state, "display")
		self.flexDirection: str = get_defined_value(state, def_state, "flexDirection")
		self.alignItems: str = get_defined_value(state, def_state, "alignItems")
		self.justifyContent: str = get_defined_value(state, def_state, "justifyContent")
		self.flexWrap: str = get_defined_value(state, def_state, "flexWrap")
		self.alignContent: str = get_defined_value(state, def_state, "alignContent")
		self.rowGap: str = get_defined_value(state, def_state, "rowGap")
		self.columnGap: str = get_defined_value(state, def_state, "columnGap")
		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def display(self):
		self._getter_access_tracker["display"] = {}
		return self._display
	@display.setter
	def display(self, state):
		self._setter_access_tracker["display"] = {}
		self._display = state
	@property
	def flexDirection(self):
		self._getter_access_tracker["flexDirection"] = {}
		return self._flexDirection
	@flexDirection.setter
	def flexDirection(self, state):
		self._setter_access_tracker["flexDirection"] = {}
		self._flexDirection = state
	@property
	def alignItems(self):
		self._getter_access_tracker["alignItems"] = {}
		return self._alignItems
	@alignItems.setter
	def alignItems(self, state):
		self._setter_access_tracker["alignItems"] = {}
		self._alignItems = state
	@property
	def justifyContent(self):
		self._getter_access_tracker["justifyContent"] = {}
		return self._justifyContent
	@justifyContent.setter
	def justifyContent(self, state):
		self._setter_access_tracker["justifyContent"] = {}
		self._justifyContent = state
	@property
	def flexWrap(self):
		self._getter_access_tracker["flexWrap"] = {}
		return self._flexWrap
	@flexWrap.setter
	def flexWrap(self, state):
		self._setter_access_tracker["flexWrap"] = {}
		self._flexWrap = state
	@property
	def alignContent(self):
		self._getter_access_tracker["alignContent"] = {}
		return self._alignContent
	@alignContent.setter
	def alignContent(self, state):
		self._setter_access_tracker["alignContent"] = {}
		self._alignContent = state
	@property
	def rowGap(self):
		self._getter_access_tracker["rowGap"] = {}
		return self._rowGap
	@rowGap.setter
	def rowGap(self, state):
		self._setter_access_tracker["rowGap"] = {}
		self._rowGap = state
	@property
	def columnGap(self):
		self._getter_access_tracker["columnGap"] = {}
		return self._columnGap
	@columnGap.setter
	def columnGap(self, state):
		self._setter_access_tracker["columnGap"] = {}
		self._columnGap = state
	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"display": self._display,
			"flexDirection": self._flexDirection,
			"alignItems": self._alignItems,
			"justifyContent": self._justifyContent,
			"flexWrap": self._flexWrap,
			"alignContent": self._alignContent,
			"rowGap": self._rowGap,
			"columnGap": self._columnGap,
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class Flex:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: FlexstylesClass = get_defined_value(state, def_state, "styles")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = FlexstylesClass(state, self._def_state["styles"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			}


class TextBoxstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class TextBoxcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class TextBox:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: TextBoxstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: TextBoxcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = TextBoxstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = TextBoxcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ImagestylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ImagecustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alt: str = get_defined_value(state, def_state, "alt")
		self.src: str = get_defined_value(state, def_state, "src")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alt(self):
		self._getter_access_tracker["alt"] = {}
		return self._alt
	@alt.setter
	def alt(self, state):
		self._setter_access_tracker["alt"] = {}
		self._alt = state
	@property
	def src(self):
		self._getter_access_tracker["src"] = {}
		return self._src
	@src.setter
	def src(self, state):
		self._setter_access_tracker["src"] = {}
		self._src = state
	def _to_json_fields(self):
		return {
			"alt": self._alt,
			"src": self._src,
			}


class Image:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ImagestylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ImagecustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ImagestylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ImagecustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class LinkstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class LinkcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self.url: str = get_defined_value(state, def_state, "url")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	@property
	def url(self):
		self._getter_access_tracker["url"] = {}
		return self._url
	@url.setter
	def url(self, state):
		self._setter_access_tracker["url"] = {}
		self._url = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			"url": self._url,
			}


class Link:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.styles: LinkstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: LinkcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = LinkstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = LinkcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}


class ButtonstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.alignSelf: str = get_defined_value(state, def_state, "alignSelf")
		self.flexGrow: str = get_defined_value(state, def_state, "flexGrow")
		self.flexShrink: str = get_defined_value(state, def_state, "flexShrink")
		self.order: str = get_defined_value(state, def_state, "order")
		self.marginTop: str = get_defined_value(state, def_state, "marginTop")
		self.marginBottom: str = get_defined_value(state, def_state, "marginBottom")
		self.marginRight: str = get_defined_value(state, def_state, "marginRight")
		self.marginLeft: str = get_defined_value(state, def_state, "marginLeft")
		self.paddingTop: str = get_defined_value(state, def_state, "paddingTop")
		self.paddingBottom: str = get_defined_value(state, def_state, "paddingBottom")
		self.paddingRight: str = get_defined_value(state, def_state, "paddingRight")
		self.paddingLeft: str = get_defined_value(state, def_state, "paddingLeft")
		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self.fontFamily: str = get_defined_value(state, def_state, "fontFamily")
		self.fontWeight: int = get_defined_value(state, def_state, "fontWeight")
		self.fontSize: str = get_defined_value(state, def_state, "fontSize")
		self.textAlign: str = get_defined_value(state, def_state, "textAlign")
		self.color: str = get_defined_value(state, def_state, "color")
		self.opacity: str = get_defined_value(state, def_state, "opacity")
		self.fontStyle: str = get_defined_value(state, def_state, "fontStyle")
		self.borderRadius: str = get_defined_value(state, def_state, "borderRadius")
		self.borderWidth: str = get_defined_value(state, def_state, "borderWidth")
		self.borderStyle: str = get_defined_value(state, def_state, "borderStyle")
		self.borderColor: str = get_defined_value(state, def_state, "borderColor")
		self.backgroundImage: str = get_defined_value(state, def_state, "backgroundImage")
		self.backgroundColor: str = get_defined_value(state, def_state, "backgroundColor")
		self.backgroundClip: str = get_defined_value(state, def_state, "backgroundClip")
		self.backgroundOrigin: str = get_defined_value(state, def_state, "backgroundOrigin")
		self.backgroundAttachment: str = get_defined_value(state, def_state, "backgroundAttachment")
		self.backgroundPositionX: str = get_defined_value(state, def_state, "backgroundPositionX")
		self.backgroundPositionY: str = get_defined_value(state, def_state, "backgroundPositionY")
		self.backgroundRepeat: str = get_defined_value(state, def_state, "backgroundRepeat")
		self.position: str = get_defined_value(state, def_state, "position")
		self.float: str = get_defined_value(state, def_state, "float")
		self.clear: str = get_defined_value(state, def_state, "clear")
		self.top: str = get_defined_value(state, def_state, "top")
		self.left: str = get_defined_value(state, def_state, "left")
		self.bottom: str = get_defined_value(state, def_state, "bottom")
		self.right: str = get_defined_value(state, def_state, "right")
		self.zIndex: str = get_defined_value(state, def_state, "zIndex")
		self.outlineStyle: str = get_defined_value(state, def_state, "outlineStyle")
		self.outlineColor: str = get_defined_value(state, def_state, "outlineColor")
		self.outlineOffset: str = get_defined_value(state, def_state, "outlineOffset")
		self.outlineWidth: str = get_defined_value(state, def_state, "outlineWidth")
		self.cursor: str = get_defined_value(state, def_state, "cursor")
		self.boxSizing: str = get_defined_value(state, def_state, "boxSizing")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def alignSelf(self):
		self._getter_access_tracker["alignSelf"] = {}
		return self._alignSelf
	@alignSelf.setter
	def alignSelf(self, state):
		self._setter_access_tracker["alignSelf"] = {}
		self._alignSelf = state
	@property
	def flexGrow(self):
		self._getter_access_tracker["flexGrow"] = {}
		return self._flexGrow
	@flexGrow.setter
	def flexGrow(self, state):
		self._setter_access_tracker["flexGrow"] = {}
		self._flexGrow = state
	@property
	def flexShrink(self):
		self._getter_access_tracker["flexShrink"] = {}
		return self._flexShrink
	@flexShrink.setter
	def flexShrink(self, state):
		self._setter_access_tracker["flexShrink"] = {}
		self._flexShrink = state
	@property
	def order(self):
		self._getter_access_tracker["order"] = {}
		return self._order
	@order.setter
	def order(self, state):
		self._setter_access_tracker["order"] = {}
		self._order = state
	@property
	def marginTop(self):
		self._getter_access_tracker["marginTop"] = {}
		return self._marginTop
	@marginTop.setter
	def marginTop(self, state):
		self._setter_access_tracker["marginTop"] = {}
		self._marginTop = state
	@property
	def marginBottom(self):
		self._getter_access_tracker["marginBottom"] = {}
		return self._marginBottom
	@marginBottom.setter
	def marginBottom(self, state):
		self._setter_access_tracker["marginBottom"] = {}
		self._marginBottom = state
	@property
	def marginRight(self):
		self._getter_access_tracker["marginRight"] = {}
		return self._marginRight
	@marginRight.setter
	def marginRight(self, state):
		self._setter_access_tracker["marginRight"] = {}
		self._marginRight = state
	@property
	def marginLeft(self):
		self._getter_access_tracker["marginLeft"] = {}
		return self._marginLeft
	@marginLeft.setter
	def marginLeft(self, state):
		self._setter_access_tracker["marginLeft"] = {}
		self._marginLeft = state
	@property
	def paddingTop(self):
		self._getter_access_tracker["paddingTop"] = {}
		return self._paddingTop
	@paddingTop.setter
	def paddingTop(self, state):
		self._setter_access_tracker["paddingTop"] = {}
		self._paddingTop = state
	@property
	def paddingBottom(self):
		self._getter_access_tracker["paddingBottom"] = {}
		return self._paddingBottom
	@paddingBottom.setter
	def paddingBottom(self, state):
		self._setter_access_tracker["paddingBottom"] = {}
		self._paddingBottom = state
	@property
	def paddingRight(self):
		self._getter_access_tracker["paddingRight"] = {}
		return self._paddingRight
	@paddingRight.setter
	def paddingRight(self, state):
		self._setter_access_tracker["paddingRight"] = {}
		self._paddingRight = state
	@property
	def paddingLeft(self):
		self._getter_access_tracker["paddingLeft"] = {}
		return self._paddingLeft
	@paddingLeft.setter
	def paddingLeft(self, state):
		self._setter_access_tracker["paddingLeft"] = {}
		self._paddingLeft = state
	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	@property
	def fontFamily(self):
		self._getter_access_tracker["fontFamily"] = {}
		return self._fontFamily
	@fontFamily.setter
	def fontFamily(self, state):
		self._setter_access_tracker["fontFamily"] = {}
		self._fontFamily = state
	@property
	def fontWeight(self):
		self._getter_access_tracker["fontWeight"] = {}
		return self._fontWeight
	@fontWeight.setter
	def fontWeight(self, state):
		self._setter_access_tracker["fontWeight"] = {}
		self._fontWeight = state
	@property
	def fontSize(self):
		self._getter_access_tracker["fontSize"] = {}
		return self._fontSize
	@fontSize.setter
	def fontSize(self, state):
		self._setter_access_tracker["fontSize"] = {}
		self._fontSize = state
	@property
	def textAlign(self):
		self._getter_access_tracker["textAlign"] = {}
		return self._textAlign
	@textAlign.setter
	def textAlign(self, state):
		self._setter_access_tracker["textAlign"] = {}
		self._textAlign = state
	@property
	def color(self):
		self._getter_access_tracker["color"] = {}
		return self._color
	@color.setter
	def color(self, state):
		self._setter_access_tracker["color"] = {}
		self._color = state
	@property
	def opacity(self):
		self._getter_access_tracker["opacity"] = {}
		return self._opacity
	@opacity.setter
	def opacity(self, state):
		self._setter_access_tracker["opacity"] = {}
		self._opacity = state
	@property
	def fontStyle(self):
		self._getter_access_tracker["fontStyle"] = {}
		return self._fontStyle
	@fontStyle.setter
	def fontStyle(self, state):
		self._setter_access_tracker["fontStyle"] = {}
		self._fontStyle = state
	@property
	def borderRadius(self):
		self._getter_access_tracker["borderRadius"] = {}
		return self._borderRadius
	@borderRadius.setter
	def borderRadius(self, state):
		self._setter_access_tracker["borderRadius"] = {}
		self._borderRadius = state
	@property
	def borderWidth(self):
		self._getter_access_tracker["borderWidth"] = {}
		return self._borderWidth
	@borderWidth.setter
	def borderWidth(self, state):
		self._setter_access_tracker["borderWidth"] = {}
		self._borderWidth = state
	@property
	def borderStyle(self):
		self._getter_access_tracker["borderStyle"] = {}
		return self._borderStyle
	@borderStyle.setter
	def borderStyle(self, state):
		self._setter_access_tracker["borderStyle"] = {}
		self._borderStyle = state
	@property
	def borderColor(self):
		self._getter_access_tracker["borderColor"] = {}
		return self._borderColor
	@borderColor.setter
	def borderColor(self, state):
		self._setter_access_tracker["borderColor"] = {}
		self._borderColor = state
	@property
	def backgroundImage(self):
		self._getter_access_tracker["backgroundImage"] = {}
		return self._backgroundImage
	@backgroundImage.setter
	def backgroundImage(self, state):
		self._setter_access_tracker["backgroundImage"] = {}
		self._backgroundImage = state
	@property
	def backgroundColor(self):
		self._getter_access_tracker["backgroundColor"] = {}
		return self._backgroundColor
	@backgroundColor.setter
	def backgroundColor(self, state):
		self._setter_access_tracker["backgroundColor"] = {}
		self._backgroundColor = state
	@property
	def backgroundClip(self):
		self._getter_access_tracker["backgroundClip"] = {}
		return self._backgroundClip
	@backgroundClip.setter
	def backgroundClip(self, state):
		self._setter_access_tracker["backgroundClip"] = {}
		self._backgroundClip = state
	@property
	def backgroundOrigin(self):
		self._getter_access_tracker["backgroundOrigin"] = {}
		return self._backgroundOrigin
	@backgroundOrigin.setter
	def backgroundOrigin(self, state):
		self._setter_access_tracker["backgroundOrigin"] = {}
		self._backgroundOrigin = state
	@property
	def backgroundAttachment(self):
		self._getter_access_tracker["backgroundAttachment"] = {}
		return self._backgroundAttachment
	@backgroundAttachment.setter
	def backgroundAttachment(self, state):
		self._setter_access_tracker["backgroundAttachment"] = {}
		self._backgroundAttachment = state
	@property
	def backgroundPositionX(self):
		self._getter_access_tracker["backgroundPositionX"] = {}
		return self._backgroundPositionX
	@backgroundPositionX.setter
	def backgroundPositionX(self, state):
		self._setter_access_tracker["backgroundPositionX"] = {}
		self._backgroundPositionX = state
	@property
	def backgroundPositionY(self):
		self._getter_access_tracker["backgroundPositionY"] = {}
		return self._backgroundPositionY
	@backgroundPositionY.setter
	def backgroundPositionY(self, state):
		self._setter_access_tracker["backgroundPositionY"] = {}
		self._backgroundPositionY = state
	@property
	def backgroundRepeat(self):
		self._getter_access_tracker["backgroundRepeat"] = {}
		return self._backgroundRepeat
	@backgroundRepeat.setter
	def backgroundRepeat(self, state):
		self._setter_access_tracker["backgroundRepeat"] = {}
		self._backgroundRepeat = state
	@property
	def position(self):
		self._getter_access_tracker["position"] = {}
		return self._position
	@position.setter
	def position(self, state):
		self._setter_access_tracker["position"] = {}
		self._position = state
	@property
	def float(self):
		self._getter_access_tracker["float"] = {}
		return self._float
	@float.setter
	def float(self, state):
		self._setter_access_tracker["float"] = {}
		self._float = state
	@property
	def clear(self):
		self._getter_access_tracker["clear"] = {}
		return self._clear
	@clear.setter
	def clear(self, state):
		self._setter_access_tracker["clear"] = {}
		self._clear = state
	@property
	def top(self):
		self._getter_access_tracker["top"] = {}
		return self._top
	@top.setter
	def top(self, state):
		self._setter_access_tracker["top"] = {}
		self._top = state
	@property
	def left(self):
		self._getter_access_tracker["left"] = {}
		return self._left
	@left.setter
	def left(self, state):
		self._setter_access_tracker["left"] = {}
		self._left = state
	@property
	def bottom(self):
		self._getter_access_tracker["bottom"] = {}
		return self._bottom
	@bottom.setter
	def bottom(self, state):
		self._setter_access_tracker["bottom"] = {}
		self._bottom = state
	@property
	def right(self):
		self._getter_access_tracker["right"] = {}
		return self._right
	@right.setter
	def right(self, state):
		self._setter_access_tracker["right"] = {}
		self._right = state
	@property
	def zIndex(self):
		self._getter_access_tracker["zIndex"] = {}
		return self._zIndex
	@zIndex.setter
	def zIndex(self, state):
		self._setter_access_tracker["zIndex"] = {}
		self._zIndex = state
	@property
	def outlineStyle(self):
		self._getter_access_tracker["outlineStyle"] = {}
		return self._outlineStyle
	@outlineStyle.setter
	def outlineStyle(self, state):
		self._setter_access_tracker["outlineStyle"] = {}
		self._outlineStyle = state
	@property
	def outlineColor(self):
		self._getter_access_tracker["outlineColor"] = {}
		return self._outlineColor
	@outlineColor.setter
	def outlineColor(self, state):
		self._setter_access_tracker["outlineColor"] = {}
		self._outlineColor = state
	@property
	def outlineOffset(self):
		self._getter_access_tracker["outlineOffset"] = {}
		return self._outlineOffset
	@outlineOffset.setter
	def outlineOffset(self, state):
		self._setter_access_tracker["outlineOffset"] = {}
		self._outlineOffset = state
	@property
	def outlineWidth(self):
		self._getter_access_tracker["outlineWidth"] = {}
		return self._outlineWidth
	@outlineWidth.setter
	def outlineWidth(self, state):
		self._setter_access_tracker["outlineWidth"] = {}
		self._outlineWidth = state
	@property
	def cursor(self):
		self._getter_access_tracker["cursor"] = {}
		return self._cursor
	@cursor.setter
	def cursor(self, state):
		self._setter_access_tracker["cursor"] = {}
		self._cursor = state
	@property
	def boxSizing(self):
		self._getter_access_tracker["boxSizing"] = {}
		return self._boxSizing
	@boxSizing.setter
	def boxSizing(self, state):
		self._setter_access_tracker["boxSizing"] = {}
		self._boxSizing = state
	def _to_json_fields(self):
		return {
			"alignSelf": self._alignSelf,
			"flexGrow": self._flexGrow,
			"flexShrink": self._flexShrink,
			"order": self._order,
			"marginTop": self._marginTop,
			"marginBottom": self._marginBottom,
			"marginRight": self._marginRight,
			"marginLeft": self._marginLeft,
			"paddingTop": self._paddingTop,
			"paddingBottom": self._paddingBottom,
			"paddingRight": self._paddingRight,
			"paddingLeft": self._paddingLeft,
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			"fontFamily": self._fontFamily,
			"fontWeight": self._fontWeight,
			"fontSize": self._fontSize,
			"textAlign": self._textAlign,
			"color": self._color,
			"opacity": self._opacity,
			"fontStyle": self._fontStyle,
			"borderRadius": self._borderRadius,
			"borderWidth": self._borderWidth,
			"borderStyle": self._borderStyle,
			"borderColor": self._borderColor,
			"backgroundImage": self._backgroundImage,
			"backgroundColor": self._backgroundColor,
			"backgroundClip": self._backgroundClip,
			"backgroundOrigin": self._backgroundOrigin,
			"backgroundAttachment": self._backgroundAttachment,
			"backgroundPositionX": self._backgroundPositionX,
			"backgroundPositionY": self._backgroundPositionY,
			"backgroundRepeat": self._backgroundRepeat,
			"position": self._position,
			"float": self._float,
			"clear": self._clear,
			"top": self._top,
			"left": self._left,
			"bottom": self._bottom,
			"right": self._right,
			"zIndex": self._zIndex,
			"outlineStyle": self._outlineStyle,
			"outlineColor": self._outlineColor,
			"outlineOffset": self._outlineOffset,
			"outlineWidth": self._outlineWidth,
			"cursor": self._cursor,
			"boxSizing": self._boxSizing,
			}


class ButtoncustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.text: str = get_defined_value(state, def_state, "text")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def text(self):
		self._getter_access_tracker["text"] = {}
		return self._text
	@text.setter
	def text(self, state):
		self._setter_access_tracker["text"] = {}
		self._text = state
	def _to_json_fields(self):
		return {
			"text": self._text,
			}


class Button:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state
		self.onClick = False
		self.styles: ButtonstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: ButtoncustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = ButtonstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = ButtoncustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

