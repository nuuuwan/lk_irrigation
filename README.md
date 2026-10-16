# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_11:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 11:08:00 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.037 |  |
| 2026-10-16 11:07:07 | Galgamuwa (Mee Oya) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-10-16 11:05:48 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | -0.069 |  |
| 2026-10-16 11:05:30 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-10-16 11:05:19 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 11:05:06 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-10-16 11:04:56 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:54 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:52 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:04:50 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-10-16 11:04:25 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:12 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-10-16 11:04:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:03:55 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:03:38 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:03:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-16 11:03:05 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.021 |  |
| 2026-10-16 11:02:54 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:02:31 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 11:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:02:13 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 11:02:12 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:01:54 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.321 |  |
| 2026-10-16 11:01:50 | Moragaswewa (Deduru Oya) | 2.06 | 🟢 Normal | -0.032 |  |
| 2026-10-16 11:01:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:01:28 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.032 |  |
| 2026-10-16 11:01:12 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:01:05 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-16 11:00:50 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:00:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 10:00:07 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 10:05:57 | Panadugama (Nilwala Ganga) | 6.65 | 🟠 Minor Flood | -0.019 |  |
| 2026-10-16 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-16 11:08:00 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | -0.037 |  |
| 2026-10-16 11:01:05 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-16 10:07:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-16 10:06:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-16 11:03:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-16 11:02:31 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 11:05:19 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 11:00:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:56 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:25 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:02:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-16 10:05:20 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:03:55 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:00:50 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 11:04:02 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:02:13 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:01:36 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:02:12 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-10-16 11:04:50 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-10-16 11:03:38 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:04:52 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:02:54 | Ellagawa (Kalu Ganga) | 7.46 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:01:12 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-10-16 11:03:05 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.021 |  |
| 2026-10-16 11:07:07 | Galgamuwa (Mee Oya) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-10-16 11:01:50 | Moragaswewa (Deduru Oya) | 2.06 | 🟢 Normal | -0.032 |  |
| 2026-10-16 11:01:28 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.032 |  |
| 2026-10-16 11:05:30 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-10-16 11:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-16 11:04:12 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-10-16 10:04:03 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.065 |  |
| 2026-10-16 11:05:48 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | -0.069 |  |
| 2026-10-16 11:05:06 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-10-16 11:01:54 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)