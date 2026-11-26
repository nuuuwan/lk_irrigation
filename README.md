# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_04:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 04:16:18 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.025 |  |
| 2026-11-27 04:13:26 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-27 04:11:50 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:12 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:10 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:10:33 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 04:09:16 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:08:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 04:08:15 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-11-27 04:07:58 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-27 04:07:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.017 |  |
| 2026-11-27 04:07:28 | Moraketiya (Walawe Ganga) | 4.03 | 🟡 Alert | 0.027 | 🔺 Rising |
| 2026-11-27 04:07:18 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-27 04:07:01 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-27 04:05:57 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.081 |  |
| 2026-11-27 04:05:37 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:05:35 | Badalgama (Maha Oya) | 4.85 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-27 04:05:09 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 04:05:01 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 04:04:44 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:04:13 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:04:02 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-27 04:03:45 | Magura (Kalu Ganga) | 5.70 | 🟡 Alert | 1.110 | 🔺 Rising |
| 2026-11-27 04:03:39 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 04:03:34 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:03:16 | Moragaswewa (Deduru Oya) | 4.10 | 🟢 Normal | -0.386 |  |
| 2026-11-27 04:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.061 |  |
| 2026-11-27 04:02:25 | Giriulla (Maha Oya) | 4.51 | 🟢 Normal | -0.030 |  |
| 2026-11-27 04:02:20 | Dunamale (Aththanagalu Oya) | 3.85 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-27 04:02:10 | Kuda Oya (Kirindi Oya) | 2.79 | 🟢 Normal | -0.092 |  |
| 2026-11-27 04:01:32 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-27 04:01:13 | Peradeniya (Mahaweli Ganga) | 4.34 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-11-27 04:01:03 | Siyambalanduwa (Heda Oya) | 2.30 | 🟢 Normal | -0.169 |  |
| 2026-11-27 04:00:14 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.101 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 04:03:45 | Magura (Kalu Ganga) | 5.70 | 🟡 Alert | 1.110 | 🔺 Rising |
| 2026-11-27 04:02:20 | Dunamale (Aththanagalu Oya) | 3.85 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-27 04:07:28 | Moraketiya (Walawe Ganga) | 4.03 | 🟡 Alert | 0.027 | 🔺 Rising |
| 2026-11-27 04:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 04:01:13 | Peradeniya (Mahaweli Ganga) | 4.34 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-11-27 04:05:35 | Badalgama (Maha Oya) | 4.85 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-27 04:07:18 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-11-27 04:00:14 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-27 04:07:01 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-27 04:13:26 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-27 04:05:09 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 04:04:02 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-27 04:08:48 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-27 04:01:32 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-27 04:07:58 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-27 04:03:39 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-27 03:06:00 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-27 04:10:33 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-27 04:05:37 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:50 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:04:44 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:11:12 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-27 04:09:16 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-27 02:06:39 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-11-27 04:07:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.017 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-27 03:04:43 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.024 |  |
| 2026-11-27 04:16:18 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.025 |  |
| 2026-11-27 04:02:25 | Giriulla (Maha Oya) | 4.51 | 🟢 Normal | -0.030 |  |
| 2026-11-27 04:08:15 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-11-27 04:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.061 |  |
| 2026-11-27 04:05:57 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.081 |  |
| 2026-11-27 04:02:10 | Kuda Oya (Kirindi Oya) | 2.79 | 🟢 Normal | -0.092 |  |
| 2026-11-27 03:03:06 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | -0.167 |  |
| 2026-11-27 04:01:03 | Siyambalanduwa (Heda Oya) | 2.30 | 🟢 Normal | -0.169 |  |
| 2026-11-27 03:10:28 | Thanamalwila (Kirindi Oya) | 2.68 | 🟢 Normal | -0.210 |  |
| 2026-11-27 04:03:16 | Moragaswewa (Deduru Oya) | 4.10 | 🟢 Normal | -0.386 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)