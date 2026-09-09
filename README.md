# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_02:04:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 02:04:11 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.078 |  |
| 2026-09-10 02:03:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-09-10 02:03:44 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:30 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:14 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:12 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:55 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:50 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-10 02:02:40 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-10 02:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:58 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 02:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:12 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:00:57 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:42:02 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:27:45 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:26:25 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:16:47 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 02:02:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-10 01:02:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-10 02:02:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-10 01:02:36 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-10 01:07:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-10 01:03:44 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-09 18:02:14 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 02:01:58 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 02:03:44 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:12 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:40 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:01:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 18:00:54 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:55 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:06:19 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:50 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:14 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:06:45 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:12 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:00:57 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:02:05 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:30 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:42:02 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:02:09 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 00:03:54 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:06:04 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 01:26:25 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 02:03:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-09-10 01:03:27 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-09-10 01:09:51 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-09-10 01:05:21 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.022 |  |
| 2026-09-10 01:12:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-09-10 02:04:11 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.078 |  |
| 2026-09-09 18:06:33 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)