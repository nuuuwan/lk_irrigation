# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_21:31:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,721 measurements** from **39** stations.
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
| 2026-08-28 21:31:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.027 |  |
| 2026-08-28 21:11:27 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:09:31 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 21:08:53 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:08:01 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:07:42 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:07:23 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-28 21:06:54 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-08-28 21:06:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:05:43 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:05:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:05:10 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-08-28 21:05:05 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-28 21:04:41 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-28 21:04:30 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.061 |  |
| 2026-08-28 21:04:11 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-28 21:03:43 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-28 21:03:42 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.089 |  |
| 2026-08-28 21:03:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-28 21:03:21 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-28 21:03:18 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.079 |  |
| 2026-08-28 21:03:11 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:03:05 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-28 21:02:58 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.050 |  |
| 2026-08-28 21:02:43 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:39 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:36 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:34 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.071 |  |
| 2026-08-28 21:02:27 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:12 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:38 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:19 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:08 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:00:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-28 21:04:41 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-28 21:03:43 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-28 21:03:21 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-28 21:05:05 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-28 21:07:23 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-28 21:09:31 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:43 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:00:30 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:39 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:05:43 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:19 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:12 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:36 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:06:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:07:42 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:11:27 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:02:27 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:03:11 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:08:01 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:08:53 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:01:38 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:05:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 21:03:05 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-28 21:04:11 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-28 21:03:32 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-28 21:06:54 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-08-28 21:05:10 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-08-28 21:31:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.027 |  |
| 2026-08-28 21:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-08-28 21:02:58 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.050 |  |
| 2026-08-28 21:04:30 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.061 |  |
| 2026-08-28 21:02:34 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.071 |  |
| 2026-08-28 21:03:18 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.079 |  |
| 2026-08-28 21:03:42 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)