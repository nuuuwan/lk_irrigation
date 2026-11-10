# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_07:17:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 07:17:53 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-11-10 07:11:35 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.220 |  |
| 2026-11-10 07:10:11 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-11-10 07:09:58 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-10 07:09:41 | Glencourse (Kelani Ganga) | 13.84 | 🟢 Normal | -0.245 |  |
| 2026-11-10 07:09:24 | Magura (Kalu Ganga) | 5.14 | 🟡 Alert | -0.027 |  |
| 2026-11-10 07:08:52 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-10 07:07:32 | Thawalama (Gin Ganga) | 4.63 | 🟡 Alert | -0.098 |  |
| 2026-11-10 07:07:21 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-11-10 07:06:46 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-10 07:06:38 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-10 07:05:56 | Hanwella (Kelani Ganga) | 6.23 | 🟢 Normal | -0.062 |  |
| 2026-11-10 07:05:54 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.45 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-11-10 07:04:08 | Thanamalwila (Kirindi Oya) | 2.12 | 🟢 Normal | -0.091 |  |
| 2026-11-10 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-11-10 07:03:59 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.124 |  |
| 2026-11-10 07:03:53 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | -0.078 |  |
| 2026-11-10 07:03:17 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-10 07:03:17 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 07:03:14 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 07:03:03 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | -0.074 |  |
| 2026-11-10 07:02:52 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.143 |  |
| 2026-11-10 07:02:47 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.103 |  |
| 2026-11-10 07:02:47 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.157 |  |
| 2026-11-10 07:02:29 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-10 07:02:29 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:02:22 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-11-10 07:02:21 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-10 07:02:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:01:35 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-10 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:01:19 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.207 |  |
| 2026-11-10 07:01:17 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.247 |  |
| 2026-11-10 07:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.042 |  |
| 2026-11-10 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.033 |  |
| 2026-11-10 06:59:52 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 07:10:11 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-11-10 07:07:21 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-11-10 07:03:17 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 07:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.45 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-11-10 06:59:52 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.000 |  |
| 2026-11-10 07:09:24 | Magura (Kalu Ganga) | 5.14 | 🟡 Alert | -0.027 |  |
| 2026-11-10 07:07:32 | Thawalama (Gin Ganga) | 4.63 | 🟡 Alert | -0.098 |  |
| 2026-11-10 07:02:47 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.103 |  |
| 2026-11-10 07:03:17 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-10 07:08:52 | Badalgama (Maha Oya) | 4.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-10 07:09:58 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-10 07:02:21 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-10 07:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:02:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 07:03:14 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 07:02:29 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:05:54 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:01:33 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-10 07:17:53 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-11-10 07:01:35 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-10 07:06:38 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-10 07:02:22 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-11-10 07:06:46 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.029 |  |
| 2026-11-10 07:02:29 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-10 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.033 |  |
| 2026-11-10 07:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.042 |  |
| 2026-11-10 07:05:56 | Hanwella (Kelani Ganga) | 6.23 | 🟢 Normal | -0.062 |  |
| 2026-11-10 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.068 |  |
| 2026-11-10 07:03:03 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | -0.074 |  |
| 2026-11-10 07:03:53 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | -0.078 |  |
| 2026-11-10 07:04:08 | Thanamalwila (Kirindi Oya) | 2.12 | 🟢 Normal | -0.091 |  |
| 2026-11-10 07:03:59 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.124 |  |
| 2026-11-10 07:02:52 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.143 |  |
| 2026-11-10 07:02:47 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.157 |  |
| 2026-11-10 07:01:19 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.207 |  |
| 2026-11-10 07:11:35 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | -0.220 |  |
| 2026-11-10 07:09:41 | Glencourse (Kelani Ganga) | 13.84 | 🟢 Normal | -0.245 |  |
| 2026-11-10 07:01:17 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)