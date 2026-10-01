# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_23:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 23:06:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:06:49 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-01 23:06:30 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-01 23:05:32 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:05:13 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-01 23:05:07 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:04:49 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:04:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:04:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:37 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:38 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-01 23:02:32 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:02:24 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:02:16 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-01 23:02:13 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-10-01 23:02:02 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:00 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-01 23:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:33 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-01 23:01:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:00:52 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 23:00:46 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:00:17 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 22:59:05 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 22:32:19 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.171 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 23:05:13 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-01 22:32:19 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-01 22:01:09 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-01 23:01:33 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-01 22:02:53 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-01 23:02:38 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-01 23:02:00 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-01 22:09:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-01 23:06:49 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-01 23:06:30 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-01 23:00:52 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 23:01:11 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:00:46 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:04:09 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:02 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:00:17 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 22:05:18 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 22:00:11 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:37 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:06:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:04:02 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 22:13:26 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:01:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:04:49 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-01 23:05:07 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:02:32 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:05:32 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:02:24 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-01 23:02:16 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-01 23:02:13 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-10-01 22:11:42 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)