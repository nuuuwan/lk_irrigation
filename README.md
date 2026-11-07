# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_22:24:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 22:24:28 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-07 22:19:50 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:14:20 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:10:29 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-11-07 22:09:56 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.027 |  |
| 2026-11-07 22:09:43 | Thawalama (Gin Ganga) | 3.01 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-11-07 22:09:00 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-07 22:08:23 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-07 22:07:58 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.272 |  |
| 2026-11-07 22:07:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:07:06 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 22:06:07 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-07 22:05:43 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-07 22:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:05:10 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-07 22:04:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.038 |  |
| 2026-11-07 22:04:13 | Urawa (Nilwala Ganga) | 3.82 | 🟡 Alert | -0.021 |  |
| 2026-11-07 22:04:04 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-11-07 22:04:00 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 22:03:32 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 22:03:28 | Wellawaya (Kirindi Oya) | 3.04 | 🟢 Normal | -0.249 |  |
| 2026-11-07 22:03:24 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:03:13 | Moraketiya (Walawe Ganga) | 2.80 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-11-07 22:03:09 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-07 22:03:08 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 22:02:42 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:02:12 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:22 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:01:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-07 22:00:37 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 22:00:17 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 22:03:08 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 22:04:13 | Urawa (Nilwala Ganga) | 3.82 | 🟡 Alert | -0.021 |  |
| 2026-11-07 22:09:43 | Thawalama (Gin Ganga) | 3.01 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-11-07 22:04:04 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-11-07 22:03:13 | Moraketiya (Walawe Ganga) | 2.80 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-11-07 22:09:00 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-07 22:10:29 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-11-07 22:05:10 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-07 22:05:43 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-11-07 22:03:09 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-07 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 22:06:07 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-07 22:24:28 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-07 22:07:06 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 22:00:37 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 22:03:32 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 22:08:23 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-07 22:07:48 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:05:32 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 21:06:31 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:03:24 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:01:22 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 22:05:19 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:01:19 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:02:12 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:06:26 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:02:42 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:19:50 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-07 22:14:20 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 22:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 22:09:56 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.027 |  |
| 2026-11-07 22:04:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.038 |  |
| 2026-11-07 22:00:17 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.053 |  |
| 2026-11-07 22:03:28 | Wellawaya (Kirindi Oya) | 3.04 | 🟢 Normal | -0.249 |  |
| 2026-11-07 22:07:58 | Thaldena (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.272 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)