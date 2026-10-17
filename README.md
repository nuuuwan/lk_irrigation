# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_14:08:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 14:08:29 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | -0.028 |  |
| 2026-10-17 14:07:58 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 14:06:30 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:06:26 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.300 |  |
| 2026-10-17 14:05:41 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-17 14:05:37 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:04:41 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | -0.011 |  |
| 2026-10-17 14:04:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:04:24 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.053 |  |
| 2026-10-17 14:04:12 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-10-17 14:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:03:54 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-17 14:03:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-17 14:03:37 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.022 |  |
| 2026-10-17 14:03:30 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:03:23 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-10-17 14:03:21 | Ellagawa (Kalu Ganga) | 7.54 | 🟢 Normal | -0.019 |  |
| 2026-10-17 14:03:18 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-10-17 14:03:03 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:02:53 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 14:02:53 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-17 14:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.030 |  |
| 2026-10-17 14:02:31 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.091 |  |
| 2026-10-17 14:02:16 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:02:03 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:01:53 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:01:42 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:01:38 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-17 14:01:04 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-10-17 14:00:50 | Thanthirimale (Malwathu Oya) | 2.54 | 🟢 Normal | -0.046 |  |
| 2026-10-17 14:00:49 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:36 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 14:00:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:00:23 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:13 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-10-17 13:34:48 | Thanthirimale (Malwathu Oya) | 2.56 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 14:02:53 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 14:03:54 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-17 14:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.70 | 🟡 Alert | -0.030 |  |
| 2026-10-17 14:03:23 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-10-17 14:03:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-17 14:02:53 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-17 14:00:36 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 14:07:58 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 14:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:03:30 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:04:35 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 14:02:03 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:01:53 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:06:30 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:03:03 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:02:16 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:49 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:23 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-10-17 14:00:13 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-10-17 14:04:41 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | -0.011 |  |
| 2026-10-17 14:04:12 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-10-17 14:05:41 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-17 14:03:21 | Ellagawa (Kalu Ganga) | 7.54 | 🟢 Normal | -0.019 |  |
| 2026-10-17 14:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:05:37 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:01:42 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-10-17 14:03:37 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | -0.022 |  |
| 2026-10-17 14:08:29 | Galgamuwa (Mee Oya) | 1.64 | 🟢 Normal | -0.028 |  |
| 2026-10-17 14:01:38 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-17 14:01:04 | Dunamale (Aththanagalu Oya) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-10-17 13:05:43 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.041 |  |
| 2026-10-17 14:00:50 | Thanthirimale (Malwathu Oya) | 2.54 | 🟢 Normal | -0.046 |  |
| 2026-10-17 14:03:18 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-10-17 14:04:24 | Hanwella (Kelani Ganga) | 3.46 | 🟢 Normal | -0.053 |  |
| 2026-10-17 13:02:21 | Glencourse (Kelani Ganga) | 11.11 | 🟢 Normal | -0.073 |  |
| 2026-10-17 14:02:31 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.091 |  |
| 2026-10-17 14:06:26 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.300 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)