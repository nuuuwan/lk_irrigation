# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_07:16:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,005 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 07:16:44 | Moragaswewa (Deduru Oya) | 2.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-08 07:13:58 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:12:15 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-08 07:11:15 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-11-08 07:10:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:08:41 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 07:08:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:08:11 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 07:06:53 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.122 |  |
| 2026-11-08 07:05:59 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.264 |  |
| 2026-11-08 07:05:50 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-11-08 07:05:43 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.060 |  |
| 2026-11-08 07:05:37 | Moraketiya (Walawe Ganga) | 3.43 | 🟡 Alert | -0.259 |  |
| 2026-11-08 07:05:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.300 |  |
| 2026-11-08 07:05:22 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.029 |  |
| 2026-11-08 07:05:11 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:05:10 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.019 |  |
| 2026-11-08 07:04:57 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 07:04:35 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-08 07:04:33 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 07:04:32 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.056 |  |
| 2026-11-08 07:04:25 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | -0.030 |  |
| 2026-11-08 07:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.35 | 🟡 Alert | 0.203 | 🔺 Rising |
| 2026-11-08 07:03:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-11-08 07:03:15 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:03:08 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.193 |  |
| 2026-11-08 07:02:56 | Giriulla (Maha Oya) | 3.13 | 🟢 Normal | -0.148 |  |
| 2026-11-08 07:02:48 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-11-08 07:02:44 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 07:02:08 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.000 |  |
| 2026-11-08 07:02:03 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-11-08 07:01:58 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.294 |  |
| 2026-11-08 07:01:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.065 |  |
| 2026-11-08 07:01:30 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-08 07:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-11-08 07:00:59 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.042 |  |
| 2026-11-08 07:00:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.132 |  |
| 2026-11-08 07:00:28 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-08 07:00:20 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 07:11:15 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-11-08 07:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.35 | 🟡 Alert | 0.203 | 🔺 Rising |
| 2026-11-08 07:04:25 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | -0.030 |  |
| 2026-11-08 07:00:59 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.042 |  |
| 2026-11-08 07:05:37 | Moraketiya (Walawe Ganga) | 3.43 | 🟡 Alert | -0.259 |  |
| 2026-11-08 07:00:28 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-08 07:16:44 | Moragaswewa (Deduru Oya) | 2.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-11-08 07:01:30 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-08 07:02:44 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 07:12:15 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-08 07:04:33 | Ellagawa (Kalu Ganga) | 7.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 07:04:57 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 07:08:41 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 07:00:20 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 07:08:11 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 07:08:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:13:58 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:10:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:05:11 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:03:15 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-08 07:02:08 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.000 |  |
| 2026-11-08 07:04:35 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-08 07:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-11-08 07:05:10 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.019 |  |
| 2026-11-08 07:05:50 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-11-08 07:05:22 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.029 |  |
| 2026-11-08 07:03:24 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-11-08 07:02:48 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-11-08 07:04:32 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.056 |  |
| 2026-11-08 07:05:43 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.060 |  |
| 2026-11-08 07:02:03 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-11-08 07:01:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.065 |  |
| 2026-11-08 07:06:53 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.122 |  |
| 2026-11-08 07:00:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.132 |  |
| 2026-11-08 07:02:56 | Giriulla (Maha Oya) | 3.13 | 🟢 Normal | -0.148 |  |
| 2026-11-08 07:03:08 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.193 |  |
| 2026-11-08 07:05:59 | Kuda Oya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.264 |  |
| 2026-11-08 07:01:58 | Thanamalwila (Kirindi Oya) | 2.16 | 🟢 Normal | -0.294 |  |
| 2026-11-08 07:05:37 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)