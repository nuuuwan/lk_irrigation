# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_20:24:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,481 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Magura — Alert; 🟡 Holombuwa — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:24:04 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:19:46 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:19:13 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.042 |  |
| 2026-11-26 20:17:04 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-11-26 20:14:39 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2026-11-26 20:14:10 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.017 |  |
| 2026-11-26 20:12:32 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-11-26 20:08:31 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-26 20:07:31 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 20:06:32 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 0.185 | 🔺 Rising |
| 2026-11-26 20:05:17 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-26 20:05:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-26 20:05:09 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:05:05 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.011 |  |
| 2026-11-26 20:04:49 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-26 20:04:49 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-11-26 20:04:44 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 20:04:41 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-11-26 20:04:14 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:03:57 | Moraketiya (Walawe Ganga) | 4.42 | 🟡 Alert | 0.326 | 🔺 Rising |
| 2026-11-26 20:03:39 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-11-26 20:03:11 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.069 |  |
| 2026-11-26 20:03:10 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-26 20:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-11-26 20:02:49 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-26 20:02:44 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-26 20:02:29 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-26 20:02:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-26 20:02:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-26 20:02:03 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 20:01:22 | Padiyathalawa (Maduru Oya) | 3.95 | 🟢 Normal | 2.135 | 🔺 Rising |
| 2026-11-26 20:01:09 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.085 |  |
| 2026-11-26 20:00:57 | Siyambalanduwa (Heda Oya) | 1.90 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-26 20:00:20 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.123 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:03:57 | Moraketiya (Walawe Ganga) | 4.42 | 🟡 Alert | 0.326 | 🔺 Rising |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-26 20:06:32 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 0.185 | 🔺 Rising |
| 2026-11-26 20:03:39 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-11-26 19:15:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-11-26 20:01:22 | Padiyathalawa (Maduru Oya) | 3.95 | 🟢 Normal | 2.135 | 🔺 Rising |
| 2026-11-26 20:04:49 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.831 | 🔺 Rising |
| 2026-11-26 20:02:29 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-26 20:12:32 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-11-26 20:17:04 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-11-26 20:05:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-11-26 20:00:57 | Siyambalanduwa (Heda Oya) | 1.90 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-26 20:04:49 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-26 20:05:17 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-26 20:00:20 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-26 20:02:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-26 20:02:49 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-26 20:02:44 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-26 20:04:44 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 20:02:03 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 20:07:31 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 20:19:46 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:05:09 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:04:14 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:24:04 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-26 20:08:31 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-26 20:05:05 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.011 |  |
| 2026-11-26 20:14:10 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.017 |  |
| 2026-11-26 20:02:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-26 20:03:10 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 20:19:13 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.042 |  |
| 2026-11-26 20:04:41 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-11-26 20:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-11-26 20:03:11 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.069 |  |
| 2026-11-26 20:14:39 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.070 |  |
| 2026-11-26 20:01:09 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)