# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_10:17:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 10:17:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-25 10:12:08 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-25 10:11:02 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-25 10:09:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:08:54 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 10:07:43 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:07:03 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-25 10:06:33 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:05:54 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-10-25 10:05:49 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 10:05:40 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:05:10 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.086 |  |
| 2026-10-25 10:05:08 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 10:05:01 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-25 10:04:35 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:04:33 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:04:30 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 10:03:24 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:58 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-25 10:02:58 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-25 10:02:37 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:36 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 10:02:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:30 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.171 |  |
| 2026-10-25 10:02:16 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 10:02:06 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:55 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:01:55 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:01:52 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-10-25 10:01:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:01:39 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:24 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-25 10:01:22 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:00:32 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 10:01:52 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-10-25 10:01:24 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-25 10:02:58 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-25 10:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 10:02:58 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-25 10:07:03 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-25 10:08:54 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 10:12:08 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-25 10:02:16 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 10:11:02 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-25 10:02:36 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 10:05:08 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 10:05:49 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 10:17:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-25 10:03:24 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:00:32 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:37 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:22 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:06:33 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:09:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:06 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:04:35 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:07:43 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:39 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:04:33 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:01:55 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:05:40 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-25 10:05:01 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-10-25 10:01:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:01:55 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:04:30 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-10-25 10:05:54 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-10-25 10:05:10 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.086 |  |
| 2026-10-25 10:02:30 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)