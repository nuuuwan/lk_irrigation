# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_21:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,907 measurements** from **39** stations.
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
| 2026-11-23 21:15:08 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:11:02 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:09:42 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-23 21:08:13 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-11-23 21:07:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:05:40 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-11-23 21:05:39 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-23 21:05:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:05:35 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.774 | 🔺 Rising |
| 2026-11-23 21:05:23 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-11-23 21:05:13 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:04:57 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:04:53 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-23 21:04:32 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-11-23 21:04:06 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.042 |  |
| 2026-11-23 21:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-11-23 21:03:23 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-23 21:03:10 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:03:04 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 21:03:04 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:02:52 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:02:51 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-23 21:02:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 21:02:35 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |
| 2026-11-23 21:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-23 21:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:16 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.035 |  |
| 2026-11-23 21:02:14 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.146 |  |
| 2026-11-23 21:02:11 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-11-23 21:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:00:36 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:00:34 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 21:05:35 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.774 | 🔺 Rising |
| 2026-11-23 21:08:13 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-11-23 21:05:39 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-23 21:03:23 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-23 21:02:39 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 21:09:42 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-23 21:00:34 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 21:03:04 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 21:02:52 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:04:57 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 21:00:36 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:04:32 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:15:08 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:05:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:11:02 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:21 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:03:10 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:07:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:01:46 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:11 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-23 21:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-23 21:02:51 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-23 21:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-11-23 21:04:53 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 21:05:23 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-11-23 21:01:46 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-11-23 21:01:31 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:03:04 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.031 |  |
| 2026-11-23 21:02:16 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.035 |  |
| 2026-11-23 21:05:40 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.039 |  |
| 2026-11-23 21:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-11-23 21:04:06 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.042 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-23 21:02:14 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.146 |  |
| 2026-11-23 21:02:35 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)