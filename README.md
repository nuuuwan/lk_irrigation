# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_15:26:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,865 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 15:26:10 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:16:00 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-09-23 15:13:56 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-09-23 15:12:51 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.026 |  |
| 2026-09-23 15:11:15 | Baddegama (Gin Ganga) | 3.72 | 🟡 Alert | -0.010 |  |
| 2026-09-23 15:10:42 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:10:11 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:09:30 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 15:07:25 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:07:17 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-09-23 15:07:10 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:07:02 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:06:18 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.040 |  |
| 2026-09-23 15:05:52 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 15:05:44 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:05:25 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.027 |  |
| 2026-09-23 15:05:22 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.009 |  |
| 2026-09-23 15:05:07 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-23 15:04:14 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-23 15:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:55 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:30 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:30 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.021 |  |
| 2026-09-23 15:03:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-09-23 15:03:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:11 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.011 |  |
| 2026-09-23 15:03:02 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:02:49 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 15:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 15:02:33 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:07 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:02:07 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:02:00 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:01:56 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:01:17 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:01:10 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-23 15:00:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 15:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | -0.020 |  |
| 2026-09-23 15:11:15 | Baddegama (Gin Ganga) | 3.72 | 🟡 Alert | -0.010 |  |
| 2026-09-23 15:03:11 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | -0.011 |  |
| 2026-09-23 15:01:10 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-23 15:05:07 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-23 15:04:14 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-23 15:09:30 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-23 15:05:52 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 15:02:49 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 15:02:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:10:11 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:26:10 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:10:42 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:01:56 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:07:02 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:02:07 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:55 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:03:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:02:07 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 15:13:56 | Thalgahagoda (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-09-23 15:05:22 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.009 |  |
| 2026-09-23 15:07:10 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:14 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:33 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:05:44 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:03:02 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:07:25 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:02:00 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-09-23 15:07:17 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-09-23 15:00:27 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-09-23 15:03:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-09-23 15:03:30 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.021 |  |
| 2026-09-23 15:16:00 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-09-23 15:12:51 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.026 |  |
| 2026-09-23 15:05:25 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.027 |  |
| 2026-09-23 15:06:18 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)