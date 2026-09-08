# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_18:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,486 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 18:10:13 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:09:04 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-09-08 18:07:35 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-08 18:06:46 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:06:25 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.010 |  |
| 2026-09-08 18:05:11 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:59 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:38 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:03:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 18:03:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-08 18:03:37 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:03:13 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-08 18:03:06 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:59 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:52 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-09-08 18:02:46 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-08 18:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-09-08 18:02:30 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:20 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:10 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-09-08 18:02:05 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:01:35 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.062 |  |
| 2026-09-08 18:01:34 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-09-08 18:01:32 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:01:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.074 |  |
| 2026-09-08 18:01:07 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.074 |  |
| 2026-09-08 18:00:51 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:48 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:44 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:44 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-08 18:00:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:27 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-08 18:00:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 18:07:35 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-08 18:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-08 18:03:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-08 18:00:44 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-08 18:03:13 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-08 18:03:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 18:02:05 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:27 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:48 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:03:37 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:46 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:59 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:01:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:03:06 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:10:13 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:20 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:51 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:37 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:04:38 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:59 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:11 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:06:46 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:44 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:02:30 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:06:25 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.010 |  |
| 2026-09-08 18:02:52 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-09-08 18:01:34 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-09-08 18:09:04 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-09-08 18:02:07 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-08 18:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-09-08 18:01:35 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.062 |  |
| 2026-09-08 18:01:07 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.074 |  |
| 2026-09-08 18:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)