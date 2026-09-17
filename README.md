# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_05:15:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 05:15:14 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-09-17 05:10:38 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-17 05:08:03 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-17 05:07:20 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.002 |  |
| 2026-09-17 05:06:36 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 05:04:32 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.178 |  |
| 2026-09-17 05:04:23 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:04:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-09-17 05:04:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:04:05 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:04:02 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-17 05:03:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-09-17 05:03:26 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-17 05:03:23 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:03:06 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 05:03:03 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.083 |  |
| 2026-09-17 05:02:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:57 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-17 05:02:51 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:50 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-17 05:02:43 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 05:02:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:34 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:21 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:20 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-09-17 05:02:19 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-09-17 05:02:15 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:02:13 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-17 05:02:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:35 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.065 |  |
| 2026-09-17 05:01:07 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 05:02:20 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-09-17 05:08:03 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-09-17 05:02:13 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-17 05:10:38 | Magura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-17 04:06:24 | Baddegama (Gin Ganga) | 3.42 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-17 05:03:26 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-17 05:02:43 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 05:03:06 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 05:06:36 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 05:01:07 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:04:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:02:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 05:02:15 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 04:09:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 05:07:20 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.002 |  |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:35 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:03:23 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:04:23 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:51 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:01:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:04:05 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:02:34 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-17 05:04:02 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-17 05:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-17 04:06:15 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-09-17 05:03:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-09-17 05:15:14 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-09-17 05:02:50 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-09-17 05:02:57 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-17 05:04:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-09-17 05:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.065 |  |
| 2026-09-17 05:03:03 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.083 |  |
| 2026-09-17 05:04:32 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)