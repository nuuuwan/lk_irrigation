# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_18:18:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,975 measurements** from **39** stations.
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
| 2026-09-13 18:18:24 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-13 18:17:50 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:07:53 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-09-13 18:06:22 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:05:35 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2026-09-13 18:05:28 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:05:24 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:05:20 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:56 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-13 18:04:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:04 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:56 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.051 |  |
| 2026-09-13 18:03:52 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:52 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-13 18:03:50 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.091 |  |
| 2026-09-13 18:03:36 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:08 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-09-13 18:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:41 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.032 |  |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:34 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:24 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 18:02:23 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-13 18:02:17 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-09-13 18:02:09 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-13 18:02:07 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 18:02:00 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 18:01:33 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-09-13 18:01:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |
| 2026-09-13 18:00:52 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-13 18:00:24 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 18:03:52 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-13 18:04:56 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-13 18:18:24 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-13 18:02:07 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 18:02:09 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-13 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 17:04:01 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 18:02:00 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:34 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:00:24 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:00:52 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:24 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:06:22 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:17:50 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:52 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:03:36 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:04 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:05:24 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:05:20 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:07:53 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-09-13 18:02:23 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-13 18:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-13 18:02:17 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-09-13 18:02:41 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.032 |  |
| 2026-09-13 18:01:33 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-09-13 18:00:20 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.034 |  |
| 2026-09-13 18:05:35 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2026-09-13 18:03:08 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-09-13 18:03:56 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.051 |  |
| 2026-09-13 18:03:50 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.091 |  |
| 2026-09-13 18:00:11 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.105 |  |
| 2026-09-13 18:01:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)