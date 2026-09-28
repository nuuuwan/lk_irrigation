# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_14:13:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,321 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 14:13:24 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:13:01 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-09-28 14:10:22 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:08:55 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:06:31 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-28 14:06:21 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:06:20 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-09-28 14:05:31 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.029 |  |
| 2026-09-28 14:05:15 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.022 |  |
| 2026-09-28 14:05:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:04:51 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-28 14:04:47 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.019 |  |
| 2026-09-28 14:04:41 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.130 |  |
| 2026-09-28 14:04:12 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-28 14:04:09 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:04:07 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-09-28 14:04:06 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:03:51 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.061 |  |
| 2026-09-28 14:03:50 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:43 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:03:41 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:40 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.71 | 🟢 Normal | -0.142 |  |
| 2026-09-28 14:03:19 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:03:06 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:03:01 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.042 |  |
| 2026-09-28 14:02:51 | Thalgahagoda (Nilwala Ganga) | 1.58 | 🟡 Alert | -0.024 |  |
| 2026-09-28 14:02:36 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:02:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:18 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:02:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:04 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-28 14:02:02 | Baddegama (Gin Ganga) | 3.91 | 🟡 Alert | -0.046 |  |
| 2026-09-28 14:01:56 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:53 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.019 |  |
| 2026-09-28 14:01:48 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:03 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 14:02:51 | Thalgahagoda (Nilwala Ganga) | 1.58 | 🟡 Alert | -0.024 |  |
| 2026-09-28 14:02:02 | Baddegama (Gin Ganga) | 3.91 | 🟡 Alert | -0.046 |  |
| 2026-09-28 14:06:31 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-28 14:04:12 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-28 14:04:51 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-28 14:02:04 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-28 14:03:06 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:03 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:13:24 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:48 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:03:43 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:10:22 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:06:21 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:01:56 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:04:09 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:05:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:13:01 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-09-28 14:06:20 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-09-28 14:08:55 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:40 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:41 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:02:36 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:03:50 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-09-28 14:02:18 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:04:06 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:03:19 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-09-28 14:04:47 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.019 |  |
| 2026-09-28 14:01:53 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.019 |  |
| 2026-09-28 14:04:07 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-09-28 14:05:15 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.022 |  |
| 2026-09-28 14:05:31 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.029 |  |
| 2026-09-28 14:03:01 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.042 |  |
| 2026-09-28 14:03:51 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.061 |  |
| 2026-09-28 14:04:41 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.130 |  |
| 2026-09-28 14:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.71 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)