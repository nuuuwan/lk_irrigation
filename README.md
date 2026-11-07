# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_13:30:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,341 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 13:30:02 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.014 |  |
| 2026-11-07 13:28:22 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 13:27:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 13:26:10 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:23:03 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.055 |  |
| 2026-11-07 13:21:56 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:10:26 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-07 13:09:15 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:06:35 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:06:30 | Badalgama (Maha Oya) | 3.89 | 🟢 Normal | -0.118 |  |
| 2026-11-07 13:06:11 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.195 |  |
| 2026-11-07 13:05:30 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 13:05:06 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:04:58 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.070 |  |
| 2026-11-07 13:04:57 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2026-11-07 13:04:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.009 |  |
| 2026-11-07 13:04:11 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.097 |  |
| 2026-11-07 13:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-11-07 13:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.030 |  |
| 2026-11-07 13:03:23 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-07 13:02:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-11-07 13:02:55 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-11-07 13:02:52 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:50 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:46 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:43 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 13:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-07 13:02:33 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-11-07 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 13:02:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-11-07 13:01:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:46 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.015 |  |
| 2026-11-07 13:01:24 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-11-07 13:01:19 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.143 |  |
| 2026-11-07 13:00:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 13:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.030 |  |
| 2026-11-07 13:04:58 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.070 |  |
| 2026-11-07 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 13:02:43 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 13:28:22 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 13:05:30 | Holombuwa (Kelani Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 13:03:23 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 13:10:26 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-07 13:27:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 13:02:52 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:24 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:09:15 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:26:10 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:02:50 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:05:06 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-07 13:04:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.009 |  |
| 2026-11-07 13:06:35 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:01:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:46 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-07 13:02:55 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-11-07 13:30:02 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.014 |  |
| 2026-11-07 13:01:46 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.015 |  |
| 2026-11-07 13:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-11-07 13:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-07 13:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-07 13:00:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-07 13:01:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.022 |  |
| 2026-11-07 13:02:55 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-11-07 13:01:19 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 13:04:57 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2026-11-07 13:01:24 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-11-07 13:23:03 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.055 |  |
| 2026-11-07 13:04:11 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.097 |  |
| 2026-11-07 13:02:33 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.101 |  |
| 2026-11-07 13:06:30 | Badalgama (Maha Oya) | 3.89 | 🟢 Normal | -0.118 |  |
| 2026-11-07 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.143 |  |
| 2026-11-07 13:06:11 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)