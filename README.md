# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_03:17:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,005 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 03:17:06 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:16:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:16:00 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:12:36 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-07 03:11:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.048 |  |
| 2026-10-07 03:10:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.102 |  |
| 2026-10-07 03:08:28 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.055 |  |
| 2026-10-07 03:08:27 | Pitabeddara (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-07 03:07:48 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:07:47 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:07:40 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:07:18 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-07 03:06:54 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-07 03:06:28 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:06:26 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-10-07 03:05:36 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.180 | 🔺 Rising |
| 2026-10-07 03:05:33 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.017 |  |
| 2026-10-07 03:05:29 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 03:05:13 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:05:12 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-07 03:05:00 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-07 03:04:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-07 03:04:45 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:35 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:29 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:07 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-07 03:04:05 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-07 03:03:57 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-07 03:03:36 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.039 |  |
| 2026-10-07 03:02:54 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 03:02:35 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:02:24 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:02:01 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-07 03:00:58 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 03:05:36 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.180 | 🔺 Rising |
| 2026-10-07 03:07:18 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-07 03:02:54 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 03:04:07 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-07 03:08:27 | Pitabeddara (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-07 02:38:56 | Dunamale (Aththanagalu Oya) | 2.13 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 03:05:12 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-07 03:06:54 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-07 03:12:36 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-07 03:04:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-07 03:04:05 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-07 01:57:19 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-07 03:05:29 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 03:05:13 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:03:36 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:16:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:35 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:45 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:02:24 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:02:35 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:07:48 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:17:06 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:04:29 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 03:05:00 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-10-07 03:03:57 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-07 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-07 03:05:33 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.017 |  |
| 2026-10-07 03:06:26 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-10-07 03:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.039 |  |
| 2026-10-07 03:00:58 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-10-07 03:11:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.048 |  |
| 2026-10-07 02:02:22 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.049 |  |
| 2026-10-07 02:04:58 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-07 03:08:28 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.055 |  |
| 2026-10-07 03:10:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)