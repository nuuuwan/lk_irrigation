# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_12:32:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,834 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 12:32:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:16:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-08-08 12:12:36 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:12:22 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:10:44 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-08 12:08:58 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-08 12:08:50 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:07:31 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:07:22 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:52 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-08-08 12:06:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:18 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:06 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:05:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:58 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.164 |  |
| 2026-08-08 12:04:18 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:04 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 12:04:03 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:02 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:03:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:03:39 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:03:35 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:03:33 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 12:03:29 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-08-08 12:03:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-08 12:02:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-08-08 12:02:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:46 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-08 12:02:43 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:43 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.471 |  |
| 2026-08-08 12:02:40 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:31 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:18 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:01:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 12:01:12 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:00:33 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 12:10:44 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-08 12:08:58 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-08 12:02:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-08 12:03:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-08 12:04:04 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 12:01:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 12:03:33 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 12:04:18 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:12:22 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:31 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:46 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:40 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:43 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:32:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:03:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:18 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:01:12 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:12:36 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:03 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:08:50 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:43 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:07:22 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:05:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 11:01:00 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:06:06 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:07:31 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:00:33 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:04:58 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.019 |  |
| 2026-08-08 12:06:52 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-08-08 12:03:29 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-08-08 12:16:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-08-08 12:04:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.164 |  |
| 2026-08-08 12:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.471 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)