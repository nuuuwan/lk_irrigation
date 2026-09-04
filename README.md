# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_08:28:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,445 measurements** from **39** stations.
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
| 2026-09-04 08:28:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:20:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.035 |  |
| 2026-09-04 08:17:59 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-04 08:14:20 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:12:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.017 |  |
| 2026-09-04 08:11:57 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:10:54 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:10:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:10:05 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:05:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:05:22 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:05:15 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-09-04 08:05:04 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:04:59 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-09-04 08:04:32 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 08:03:55 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-09-04 08:03:20 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-09-04 08:03:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:16 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:05 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:00 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 08:02:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:45 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-09-04 08:02:37 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:33 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-04 08:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-09-04 08:02:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:14 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:09 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:01:25 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:01:14 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.034 |  |
| 2026-09-04 08:00:57 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:00:46 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.083 |  |
| 2026-09-04 08:00:11 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 07:04:33 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 08:17:59 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-04 08:02:33 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-04 08:03:00 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 08:04:32 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 08:03:16 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:01:25 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:14 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:28:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:09 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:00:11 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:10:05 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:05 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:05:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:37 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:14:20 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:17 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:03:55 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:00:57 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:05:04 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:10:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:02:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 08:10:54 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:05:22 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:11:57 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-09-04 08:02:45 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-09-04 08:12:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.017 |  |
| 2026-09-04 08:04:59 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-09-04 08:03:20 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-09-04 08:01:14 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.034 |  |
| 2026-09-04 08:20:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.035 |  |
| 2026-09-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-09-04 08:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-09-04 08:05:15 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.050 |  |
| 2026-09-04 08:00:46 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.083 |  |
| 2026-09-04 07:02:28 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)