# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_10:08:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 10:08:49 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-16 10:08:47 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 10:08:38 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | -0.193 |  |
| 2026-10-16 10:07:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-16 10:07:46 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.082 |  |
| 2026-10-16 10:07:42 | Pitabeddara (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.116 |  |
| 2026-10-16 10:06:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-16 10:06:07 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.192 |  |
| 2026-10-16 10:05:57 | Panadugama (Nilwala Ganga) | 6.65 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-16 10:05:27 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-16 10:05:20 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:05:17 | Moraketiya (Walawe Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-10-16 10:05:12 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.030 |  |
| 2026-10-16 10:05:07 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.049 |  |
| 2026-10-16 10:05:03 | Moragaswewa (Deduru Oya) | 2.09 | 🟢 Normal | -0.040 |  |
| 2026-10-16 10:04:41 | Urawa (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.120 |  |
| 2026-10-16 10:04:40 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.058 |  |
| 2026-10-16 10:04:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:04:03 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.065 |  |
| 2026-10-16 10:03:41 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | -0.040 |  |
| 2026-10-16 10:03:10 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2026-10-16 10:03:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-10-16 10:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 10:03:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:02:57 | Ellagawa (Kalu Ganga) | 7.48 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:02:48 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:02:44 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:42 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-10-16 10:02:41 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-10-16 10:02:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:26 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 10:02:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:01:52 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:01:48 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 10:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-10-16 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:01:17 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:00:41 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-10-16 10:00:07 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 10:00:07 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 10:05:57 | Panadugama (Nilwala Ganga) | 6.65 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-16 10:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 10:03:41 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | -0.040 |  |
| 2026-10-16 10:03:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-10-16 10:07:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-16 10:06:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-16 10:08:49 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-16 10:01:48 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 10:08:47 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-16 10:02:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:04:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:01:52 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-16 09:09:44 | Galgamuwa (Mee Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:44 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:05:20 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:00:41 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:26 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-16 10:05:27 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-16 10:03:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:02:57 | Ellagawa (Kalu Ganga) | 7.48 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:01:17 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:02:48 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-16 10:05:12 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.030 |  |
| 2026-10-16 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-10-16 10:03:10 | Hanwella (Kelani Ganga) | 3.63 | 🟢 Normal | -0.040 |  |
| 2026-10-16 10:05:03 | Moragaswewa (Deduru Oya) | 2.09 | 🟢 Normal | -0.040 |  |
| 2026-10-16 10:05:07 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.049 |  |
| 2026-10-16 10:05:17 | Moraketiya (Walawe Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-10-16 10:04:40 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.058 |  |
| 2026-10-16 10:04:03 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.065 |  |
| 2026-10-16 10:07:46 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.082 |  |
| 2026-10-16 10:01:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.090 |  |
| 2026-10-16 10:07:42 | Pitabeddara (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.116 |  |
| 2026-10-16 10:04:41 | Urawa (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.120 |  |
| 2026-10-16 10:06:07 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.192 |  |
| 2026-10-16 10:08:38 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)