# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_05:04:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,753 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 05:04:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:03:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-09-30 05:03:42 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:03:39 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 05:03:24 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-09-30 05:02:47 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-09-30 05:02:35 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-30 05:02:16 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:02:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-09-30 05:01:38 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:01:36 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-30 05:01:25 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-09-30 05:01:22 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-30 05:01:21 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.020 |  |
| 2026-09-30 05:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 05:01:13 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:01:08 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:01:07 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.164 |  |
| 2026-09-30 05:01:07 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-09-30 05:01:05 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-09-30 05:00:22 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.021 |  |
| 2026-09-30 04:43:54 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-09-30 04:37:31 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:37:30 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:37:09 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-30 04:36:52 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 05:01:22 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-30 05:02:35 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-30 04:37:09 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-30 05:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 05:03:39 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-30 03:03:56 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:03:42 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:37:31 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:01:38 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:04:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:00:33 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:04:10 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:05:45 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:03:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:01:08 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:02:26 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 05:02:16 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-30 04:43:54 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-09-30 05:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-09-30 05:01:36 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-30 05:01:25 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-09-30 04:04:22 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-09-30 05:02:47 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-09-30 04:20:26 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.016 |  |
| 2026-09-30 05:01:21 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.020 |  |
| 2026-09-30 04:11:02 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-09-30 05:01:05 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-09-30 04:03:03 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-09-30 05:01:07 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-09-30 05:00:22 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.021 |  |
| 2026-09-30 04:03:47 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.022 |  |
| 2026-09-30 05:03:24 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-09-30 04:03:27 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.042 |  |
| 2026-09-30 04:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | -0.051 |  |
| 2026-09-30 05:02:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-09-30 05:01:07 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)