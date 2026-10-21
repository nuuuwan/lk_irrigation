# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_04:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 04:12:42 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 04:09:39 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-22 04:07:56 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-22 04:07:51 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-22 04:07:21 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-22 04:07:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 04:06:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 04:06:10 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.429 |  |
| 2026-10-22 04:04:27 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.129 |  |
| 2026-10-22 04:04:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 04:03:54 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 04:03:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 04:03:43 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:03:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-22 04:02:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:02:53 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-22 04:02:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:02:45 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 04:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.147 |  |
| 2026-10-22 04:02:44 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 04:02:38 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-10-22 04:02:28 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-10-22 04:02:08 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.062 |  |
| 2026-10-22 04:01:26 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | -0.103 |  |
| 2026-10-22 04:01:13 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:01:00 | Rathnapura (Kalu Ganga) | 5.52 | 🟡 Alert | 0.000 |  |
| 2026-10-22 04:00:36 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.090 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 04:01:00 | Rathnapura (Kalu Ganga) | 5.52 | 🟡 Alert | 0.000 |  |
| 2026-10-22 00:20:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 2.535 | 🔺 Rising |
| 2026-10-22 03:04:31 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-10-22 04:02:53 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-22 04:02:28 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-22 04:03:54 | Dunamale (Aththanagalu Oya) | 2.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 04:04:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-22 04:00:36 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-22 04:06:16 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 04:09:39 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-22 04:02:44 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 04:03:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-22 04:07:51 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 04:03:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 04:02:45 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 04:12:42 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 04:02:50 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:03:43 | Glencourse (Kelani Ganga) | 13.60 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:01:13 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:02:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 04:07:56 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-10-22 04:07:21 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-22 04:02:38 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-10-22 03:02:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-10-22 03:13:14 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.028 |  |
| 2026-10-22 04:07:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-10-22 02:04:21 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-10-22 03:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-10-22 03:09:34 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.058 |  |
| 2026-10-22 04:02:08 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.062 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-22 04:01:26 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | -0.103 |  |
| 2026-10-22 04:04:27 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.129 |  |
| 2026-10-22 03:06:32 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.140 |  |
| 2026-10-22 04:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.147 |  |
| 2026-10-22 02:03:32 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.325 |  |
| 2026-10-22 04:06:10 | Holombuwa (Kelani Ganga) | 1.98 | 🟢 Normal | -0.429 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)