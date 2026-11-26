# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_21:18:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 21:18:47 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.016 |  |
| 2026-11-26 21:12:07 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:10:21 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-11-26 21:10:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-26 21:10:12 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.046 |  |
| 2026-11-26 21:09:36 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-26 21:09:17 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.106 |  |
| 2026-11-26 21:07:59 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-11-26 21:07:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-11-26 21:07:01 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-26 21:06:46 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-26 21:06:33 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-26 21:06:19 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-26 21:05:58 | Holombuwa (Kelani Ganga) | 3.04 | 🟡 Alert | -0.162 |  |
| 2026-11-26 21:05:23 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.083 |  |
| 2026-11-26 21:04:38 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:04:34 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 21:04:00 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | 1.414 | 🔺 Rising |
| 2026-11-26 21:04:00 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:03:49 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 21:03:17 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-11-26 21:03:13 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.212 |  |
| 2026-11-26 21:03:09 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-26 21:03:00 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.069 |  |
| 2026-11-26 21:03:00 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:03:00 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:02:38 | Moraketiya (Walawe Ganga) | 4.47 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-26 21:02:21 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-26 21:02:03 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 21:01:56 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-11-26 21:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:01:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-26 21:01:09 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:00:46 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.152 |  |
| 2026-11-26 21:00:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:00:40 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-26 21:01:18 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-26 21:02:38 | Moraketiya (Walawe Ganga) | 4.47 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-26 21:10:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.16 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-26 21:05:58 | Holombuwa (Kelani Ganga) | 3.04 | 🟡 Alert | -0.162 |  |
| 2026-11-26 21:04:00 | Kuda Oya (Kirindi Oya) | 4.10 | 🟢 Normal | 1.414 | 🔺 Rising |
| 2026-11-26 21:03:17 | Giriulla (Maha Oya) | 3.62 | 🟢 Normal | 0.740 | 🔺 Rising |
| 2026-11-26 21:01:56 | Nakkala (Kumbukkan Oya) | 2.10 | 🟢 Normal | 0.735 | 🔺 Rising |
| 2026-11-26 21:07:59 | Thanamalwila (Kirindi Oya) | 2.45 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-11-26 21:07:01 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-26 21:06:19 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-26 21:09:36 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-26 21:06:46 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-26 21:00:40 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-26 21:06:33 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-26 21:02:21 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-26 21:03:49 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 21:02:03 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 21:04:34 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 21:04:00 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:00:43 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:04:38 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:12:07 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 21:03:09 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-26 21:18:47 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.016 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 21:07:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-11-26 21:03:00 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:01:09 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.041 |  |
| 2026-11-26 21:10:12 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.046 |  |
| 2026-11-26 21:03:00 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.069 |  |
| 2026-11-26 21:10:21 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-11-26 21:05:23 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.083 |  |
| 2026-11-26 21:09:17 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.106 |  |
| 2026-11-26 21:00:46 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.152 |  |
| 2026-11-26 21:03:13 | Siyambalanduwa (Heda Oya) | 1.68 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)