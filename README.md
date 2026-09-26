# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_20:33:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,773 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 20:33:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:24:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:15:36 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | -0.062 |  |
| 2026-09-26 20:11:51 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.026 |  |
| 2026-09-26 20:09:56 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:09:42 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.046 |  |
| 2026-09-26 20:07:25 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 20:07:10 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-09-26 20:06:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-09-26 20:06:23 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 20:06:18 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-26 20:06:04 | Hanwella (Kelani Ganga) | 5.23 | 🟢 Normal | -0.030 |  |
| 2026-09-26 20:05:58 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:05:44 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-09-26 20:04:21 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 20:04:21 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:04:17 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-26 20:04:12 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:04:03 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.115 |  |
| 2026-09-26 20:02:46 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:02:41 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-26 20:02:36 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 20:02:28 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.020 |  |
| 2026-09-26 20:02:24 | Kithulgala (Kelani Ganga) | 2.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-26 20:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.88 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-26 20:02:19 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.042 |  |
| 2026-09-26 20:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:02:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-26 20:01:52 | Nawalapitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.043 |  |
| 2026-09-26 20:01:52 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | -0.020 |  |
| 2026-09-26 20:01:30 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:01:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:01:06 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:00:08 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 20:06:23 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 20:07:25 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 20:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.88 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-26 20:02:28 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.020 |  |
| 2026-09-26 20:02:24 | Kithulgala (Kelani Ganga) | 2.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-26 20:04:17 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-09-26 20:00:08 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 20:02:36 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-26 20:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:01:06 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:33:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:24:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:05 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:09:56 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:02:46 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:05:58 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:04:12 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:04:21 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:01:30 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:01:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 20:06:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-09-26 20:06:18 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-26 20:04:21 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 20:05:44 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.019 |  |
| 2026-09-26 20:01:52 | Ellagawa (Kalu Ganga) | 8.86 | 🟢 Normal | -0.020 |  |
| 2026-09-26 20:02:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.021 |  |
| 2026-09-26 20:11:51 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.026 |  |
| 2026-09-26 20:06:04 | Hanwella (Kelani Ganga) | 5.23 | 🟢 Normal | -0.030 |  |
| 2026-09-26 20:02:41 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-26 20:02:19 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.042 |  |
| 2026-09-26 20:07:10 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-09-26 20:01:52 | Nawalapitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.043 |  |
| 2026-09-26 20:09:42 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.046 |  |
| 2026-09-26 20:15:36 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | -0.062 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-26 20:04:03 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)