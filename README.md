# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_07:14:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 07:14:48 | Thawalama (Gin Ganga) | 3.32 | 🟢 Normal | -0.253 |  |
| 2026-09-15 07:13:27 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-09-15 07:11:55 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.094 |  |
| 2026-09-15 07:10:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-15 07:10:03 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.179 |  |
| 2026-09-15 07:09:58 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-09-15 07:09:12 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.084 |  |
| 2026-09-15 07:08:58 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-15 07:06:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-09-15 07:05:59 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-15 07:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-09-15 07:05:39 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:05:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-09-15 07:05:12 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-15 07:04:59 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:54 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:45 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-09-15 07:04:44 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-09-15 07:04:19 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-15 07:04:19 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.022 |  |
| 2026-09-15 07:04:19 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:13 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-15 07:03:49 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-15 07:03:09 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-15 07:02:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.231 |  |
| 2026-09-15 07:02:55 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.140 | 🔺 Rising |
| 2026-09-15 07:02:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:02:50 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-15 07:02:50 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:02:47 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-15 07:02:35 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 07:02:06 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 07:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:01:22 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-09-15 07:01:22 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.064 |  |
| 2026-09-15 07:01:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:00:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:00:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:30:32 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 07:02:55 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | 0.140 | 🔺 Rising |
| 2026-09-15 07:13:27 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-09-15 07:04:45 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 756.000 | 🔺 Rising |
| 2026-09-15 06:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-09-15 07:09:58 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-09-15 07:04:19 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-15 07:02:47 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-15 07:08:58 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-15 07:05:59 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-15 07:02:35 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-15 07:02:50 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-15 07:03:49 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-15 07:05:12 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-15 07:10:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-15 07:02:06 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 06:10:05 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:00:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:59 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:01:46 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:54 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:02:50 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:05:39 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:02:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:04:17 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:01:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-15 07:03:09 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-15 07:00:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-15 07:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-09-15 07:04:13 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-15 07:04:19 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.022 |  |
| 2026-09-15 07:01:22 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-09-15 07:05:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-09-15 07:01:22 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.064 |  |
| 2026-09-15 07:09:12 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.084 |  |
| 2026-09-15 07:11:55 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.094 |  |
| 2026-09-15 07:06:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-09-15 07:10:03 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.179 |  |
| 2026-09-15 07:02:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.231 |  |
| 2026-09-15 07:14:48 | Thawalama (Gin Ganga) | 3.32 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)