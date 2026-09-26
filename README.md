# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_08:27:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 08:27:26 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:13:43 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 08:11:48 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 08:11:30 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.058 |  |
| 2026-09-26 08:11:17 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:10:16 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 08:08:51 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.122 |  |
| 2026-09-26 08:08:36 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 3.814 | 🔺 Rising |
| 2026-09-26 08:07:58 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:10 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:05:46 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:05:04 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-26 08:04:53 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-26 08:04:25 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:03:43 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.046 |  |
| 2026-09-26 08:03:38 | Hanwella (Kelani Ganga) | 5.72 | 🟢 Normal | -0.061 |  |
| 2026-09-26 08:03:28 | Deraniyagala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-26 08:03:19 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:13 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 08:03:12 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 08:02:57 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-26 08:02:51 | Glencourse (Kelani Ganga) | 13.34 | 🟢 Normal | -0.102 |  |
| 2026-09-26 08:02:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:02:18 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:02:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:08 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:03 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:56 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.040 |  |
| 2026-09-26 08:01:42 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.060 |  |
| 2026-09-26 08:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:31 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:15 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 08:00:56 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.102 |  |
| 2026-09-26 08:00:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 08:08:36 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 3.814 | 🔺 Rising |
| 2026-09-26 08:11:48 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 08:13:43 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 08:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 08:11:30 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.058 |  |
| 2026-09-26 08:04:53 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-26 08:03:28 | Deraniyagala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-26 08:05:04 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-26 08:01:15 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 08:03:13 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 08:10:16 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 08:00:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:08 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:27:26 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:12 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:10 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:03 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:19 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:07:58 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:05:46 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:02:57 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:11:17 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:01:31 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:03:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 08:04:25 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:02:18 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:02:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-26 08:02:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-26 08:01:56 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.040 |  |
| 2026-09-26 08:03:43 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.046 |  |
| 2026-09-26 08:01:42 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.060 |  |
| 2026-09-26 08:03:38 | Hanwella (Kelani Ganga) | 5.72 | 🟢 Normal | -0.061 |  |
| 2026-09-26 08:02:51 | Glencourse (Kelani Ganga) | 13.34 | 🟢 Normal | -0.102 |  |
| 2026-09-26 08:00:56 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.102 |  |
| 2026-09-26 08:08:51 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)