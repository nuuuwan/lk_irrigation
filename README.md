# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_19:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 19:02:56 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.040 |  |
| 2026-10-31 19:02:43 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 19:02:21 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-10-31 19:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 19:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:02:03 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:01:36 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.031 |  |
| 2026-10-31 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:01:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 19:00:39 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-10-31 19:00:24 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:00:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:59:17 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 19:00:39 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | -0.031 |  |
| 2026-10-31 18:01:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-31 18:05:06 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-31 18:07:24 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-31 18:06:25 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 18:03:23 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-31 19:02:43 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 19:01:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 19:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 19:00:24 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:02:03 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:02:41 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:05:39 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 18:01:33 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:47 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:11 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-31 19:00:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:02:25 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:00:20 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-10-31 18:05:54 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:06:07 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:02:37 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.024 |  |
| 2026-10-31 18:09:33 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.027 |  |
| 2026-10-31 18:08:19 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.030 |  |
| 2026-10-31 19:02:21 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-10-31 19:01:36 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.031 |  |
| 2026-10-31 19:02:56 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.040 |  |
| 2026-10-31 18:01:08 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.041 |  |
| 2026-10-31 18:01:56 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.052 |  |
| 2026-10-31 18:08:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.056 |  |
| 2026-10-31 18:59:17 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.070 |  |
| 2026-10-31 18:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | -0.080 |  |
| 2026-10-31 18:01:45 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.084 |  |
| 2026-10-31 18:01:23 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)