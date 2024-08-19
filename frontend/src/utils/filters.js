import {
	parseTime
} from "@/utils/utils";

const timeStampFilter = (value) => {
	return value ? parseTime(value) : '--';
}

const timeFull = (value) => {
	let val = value - 1;
	return val < 10 ? "0" + val : "" + val;
}

const sizeFilter = (val) => {
	let unitList = ['B', 'KB', 'MB', 'GB', 'TB'];
	    let i = 0;
	    for (i = 0; i < unitList.length; i++) {
	        if (val < 1024 ** (i + 1)) {
	            return (val / (1024 ** i)).toFixed(2).replace(/\.?0*$/, '') + unitList[i];
	        }
	    }
	    // 如果超出最大单位，显示为最大单位
	    return (val / (1024 ** (i - 1))).toFixed(2).replace(/\.?0*$/, '') + unitList[i - 1];
}

export default {
	timeStampFilter,
	timeFull,
	sizeFilter
}