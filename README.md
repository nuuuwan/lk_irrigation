# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_01:06:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,721 measurements** from **39** stations.
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
| 2026-10-09 01:06:41 | Holombuwa (Kelani Ganga) | 2.46 | 🟢 Normal | -0.344 |  |
| 2026-10-09 01:06:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:06:13 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-09 01:05:38 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-09 01:04:31 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.052 |  |
| 2026-10-09 01:04:24 | Thawalama (Gin Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 01:04:19 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | 0.476 | 🔺 Rising |
| 2026-10-09 01:04:07 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-09 01:03:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 01:03:18 | Giriulla (Maha Oya) | 4.72 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-09 01:03:16 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-10-09 01:02:59 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-09 01:02:44 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 01:02:19 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:02:01 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 01:02:01 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:01:56 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-10-09 01:01:44 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 01:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-09 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-10-09 01:01:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:00:51 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:00:48 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.252 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 01:04:19 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | 0.476 | 🔺 Rising |
| 2026-10-09 01:05:38 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-08 23:04:29 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-09 01:03:18 | Giriulla (Maha Oya) | 4.72 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-09 00:03:25 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-09 01:06:13 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-09 00:17:09 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-09 00:04:41 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-09 01:02:59 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-09 00:04:01 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-09 00:11:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-09 01:02:44 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 01:03:29 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 01:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-09 01:02:01 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 01:04:24 | Thawalama (Gin Ganga) | 3.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 01:01:44 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:12:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:06:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:00:51 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:03:48 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:01:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 00:00:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:06:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 23:14:10 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:02:19 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:02:01 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:04:07 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-09 00:06:28 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-10-09 01:01:56 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-10-09 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-10-09 01:03:16 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-10-09 01:04:31 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.052 |  |
| 2026-10-09 00:03:11 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.113 |  |
| 2026-10-09 01:00:48 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.252 |  |
| 2026-10-09 01:06:41 | Holombuwa (Kelani Ganga) | 2.46 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)