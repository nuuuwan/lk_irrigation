# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_16:16:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,304 measurements** from **39** stations.
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
| 2026-10-09 16:16:47 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 16:13:14 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2026-10-09 16:08:51 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |
| 2026-10-09 16:08:28 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-09 16:07:54 | Urawa (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-10-09 16:07:46 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 16:07:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 16:07:06 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-09 16:06:26 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-09 16:05:33 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.124 |  |
| 2026-10-09 16:05:17 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:05:10 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:05:08 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.071 |  |
| 2026-10-09 16:05:08 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-09 16:04:52 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-09 16:04:50 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 16:04:46 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 16:04:43 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:04:34 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.060 |  |
| 2026-10-09 16:04:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:04:20 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.089 |  |
| 2026-10-09 16:04:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:03:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:03:40 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.068 |  |
| 2026-10-09 16:03:05 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-10-09 16:03:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:02:55 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.114 |  |
| 2026-10-09 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-10-09 16:02:45 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-09 16:02:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-09 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | -0.061 |  |
| 2026-10-09 16:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:01:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 16:00:58 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-09 16:00:48 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 16:00:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-10-09 16:00:18 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:00:13 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 16:07:54 | Urawa (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-10-09 16:05:08 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-09 16:06:26 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-09 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-09 16:02:18 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-09 16:02:45 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-09 16:00:58 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-09 16:07:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-09 16:08:28 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-09 16:04:50 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 16:04:46 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 16:01:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 16:00:48 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 16:07:06 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 16:16:47 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 16:05:17 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:00:18 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:04:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:04:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:03:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:04:43 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:03:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:05:10 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-09 16:07:46 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-09 16:04:52 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-09 16:13:14 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2026-10-09 16:03:05 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-10-09 16:00:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.034 |  |
| 2026-10-09 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-10-09 16:00:13 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.051 |  |
| 2026-10-09 16:04:34 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.060 |  |
| 2026-10-09 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.69 | 🟢 Normal | -0.061 |  |
| 2026-10-09 16:03:40 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | -0.068 |  |
| 2026-10-09 16:05:08 | Badalgama (Maha Oya) | 4.03 | 🟢 Normal | -0.071 |  |
| 2026-10-09 16:08:51 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |
| 2026-10-09 16:04:20 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.089 |  |
| 2026-10-09 16:02:55 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.114 |  |
| 2026-10-09 16:05:33 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)