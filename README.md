# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_09:32:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 09:32:33 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:32:19 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-14 09:13:53 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-14 09:13:12 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.073 |  |
| 2026-09-14 09:11:41 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:10:52 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.057 |  |
| 2026-09-14 09:09:43 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 09:08:39 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:07:46 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-14 09:07:15 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:06:42 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:06:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:05:44 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:04:57 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 09:04:43 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-09-14 09:04:05 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.088 |  |
| 2026-09-14 09:03:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-09-14 09:03:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:30 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-14 09:03:29 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:02 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-09-14 09:02:48 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.103 |  |
| 2026-09-14 09:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-14 09:02:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:21 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.070 |  |
| 2026-09-14 09:02:13 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-09-14 09:01:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.090 |  |
| 2026-09-14 09:01:38 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.052 |  |
| 2026-09-14 09:01:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2026-09-14 09:01:11 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:36 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:27 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 09:04:43 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.496 | 🔺 Rising |
| 2026-09-14 09:07:46 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-14 09:00:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 09:04:57 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 09:09:43 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 09:32:19 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-14 09:32:33 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:13 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:29 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:27 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:07:15 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:04:05 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:08:39 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:06:42 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:06:24 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:03:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:05:44 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:02:21 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:01:11 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:11:41 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:00:36 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 09:13:53 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-14 09:03:30 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-14 09:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-14 09:03:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-09-14 09:03:02 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-09-14 09:02:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.051 |  |
| 2026-09-14 09:01:38 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.052 |  |
| 2026-09-14 09:01:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2026-09-14 09:10:52 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.057 |  |
| 2026-09-14 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.070 |  |
| 2026-09-14 09:13:12 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.073 |  |
| 2026-09-14 09:03:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.088 |  |
| 2026-09-14 09:01:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.090 |  |
| 2026-09-14 09:02:47 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)