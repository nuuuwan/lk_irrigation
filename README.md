# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_11:05:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,296 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 11:05:50 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.047 |  |
| 2026-10-17 11:05:49 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:05:21 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-10-17 11:04:56 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:04:53 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.163 |  |
| 2026-10-17 11:04:44 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:04:25 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-10-17 11:04:00 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-17 11:03:51 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.113 |  |
| 2026-10-17 11:03:50 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-10-17 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | -0.010 |  |
| 2026-10-17 11:03:22 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.057 |  |
| 2026-10-17 11:03:20 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.130 |  |
| 2026-10-17 11:03:12 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | -0.050 |  |
| 2026-10-17 11:03:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:02:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 11:02:45 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-10-17 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 11:02:11 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-17 11:01:58 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-17 11:01:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-17 11:00:58 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-17 11:00:09 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:26:19 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.130 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 10:03:35 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-17 10:09:46 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.034 |  |
| 2026-10-17 11:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.76 | 🟡 Alert | -0.010 |  |
| 2026-10-17 11:01:58 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-17 10:20:21 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-17 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 11:04:00 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-17 11:02:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:07:34 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:02:17 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-17 10:00:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 11:02:11 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-17 11:05:49 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:04:56 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:03:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:04:44 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:02:45 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-17 11:00:09 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-17 10:05:16 | Galgamuwa (Mee Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-10-17 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-10-17 10:04:50 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-10-17 11:01:14 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-17 11:05:21 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-10-17 11:03:50 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-10-17 11:00:58 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:04:39 | Urawa (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-10-17 10:03:50 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.042 |  |
| 2026-10-17 10:01:44 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.042 |  |
| 2026-10-17 11:05:50 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.047 |  |
| 2026-10-17 11:03:12 | Hanwella (Kelani Ganga) | 3.64 | 🟢 Normal | -0.050 |  |
| 2026-10-17 11:03:22 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.057 |  |
| 2026-10-17 10:08:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.061 |  |
| 2026-10-17 10:06:05 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-10-17 09:16:36 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.074 |  |
| 2026-10-17 11:04:25 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.077 |  |
| 2026-10-17 10:01:22 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.097 |  |
| 2026-10-17 11:03:51 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.113 |  |
| 2026-10-17 11:03:20 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.130 |  |
| 2026-10-17 11:04:53 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)