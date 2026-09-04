# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_05:36:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 05:36:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:35:57 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:13:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-04 05:13:16 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.089 |  |
| 2026-09-04 05:11:01 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.053 |  |
| 2026-09-04 05:10:06 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-09-04 05:09:44 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-04 05:09:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-04 05:09:27 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:08:16 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-09-04 05:08:15 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:08:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:08:08 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:08:03 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -36.000 |  |
| 2026-09-04 05:08:02 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -36.000 |  |
| 2026-09-04 05:05:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:05:52 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:05:45 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:04:52 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-04 05:04:40 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-04 05:04:34 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:03:47 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:03:46 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-04 05:03:35 | Weraganthota (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-09-04 05:03:18 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 05:02:53 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 05:02:43 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:26 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:25 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:23 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 05:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:13 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.139 |  |
| 2026-09-04 05:01:57 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:01:43 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-09-04 05:01:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 05:03:35 | Weraganthota (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-09-04 05:04:40 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-04 05:01:43 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-09-04 05:13:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-04 05:09:44 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-04 05:02:23 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 05:03:18 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 04:01:46 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 05:02:53 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 05:01:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:03:47 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:05:45 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:01:57 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:43 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:02:40 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:25 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:08:15 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:36:25 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 03:03:55 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:09:27 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:02:26 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:35:57 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:01:11 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:05:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:05:52 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:04:34 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-04 05:09:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-04 05:03:46 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-04 04:01:58 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-09-04 05:04:52 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-04 05:10:06 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-09-04 05:08:16 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-09-04 04:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.046 |  |
| 2026-09-04 05:11:01 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.053 |  |
| 2026-09-04 05:13:16 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.089 |  |
| 2026-09-04 05:02:13 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.139 |  |
| 2026-09-04 05:08:03 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)