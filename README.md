# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_13:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Rathnapura — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 13:13:05 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | -0.042 |  |
| 2026-09-21 13:10:07 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-09-21 13:08:24 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-09-21 13:08:13 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.084 |  |
| 2026-09-21 13:06:52 | Dunamale (Aththanagalu Oya) | 3.15 | 🟢 Normal | -0.048 |  |
| 2026-09-21 13:06:23 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:05:17 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.092 |  |
| 2026-09-21 13:05:15 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | -0.139 |  |
| 2026-09-21 13:05:09 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.077 |  |
| 2026-09-21 13:05:05 | Rathnapura (Kalu Ganga) | 5.67 | 🟡 Alert | -0.032 |  |
| 2026-09-21 13:05:01 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-21 13:05:00 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 13:04:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:03:52 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:03:36 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 13:03:28 | Magura (Kalu Ganga) | 5.48 | 🟡 Alert | -0.033 |  |
| 2026-09-21 13:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:03:16 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:03:14 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-09-21 13:03:14 | Hanwella (Kelani Ganga) | 6.06 | 🟢 Normal | -0.120 |  |
| 2026-09-21 13:03:04 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:02:42 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:02:35 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.034 |  |
| 2026-09-21 13:02:34 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-21 13:02:34 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-09-21 13:02:30 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.90 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-09-21 13:02:23 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-09-21 13:02:09 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-21 13:02:09 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 13:02:00 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-09-21 13:01:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:16 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:14 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -5.788 |  |
| 2026-09-21 13:01:11 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-21 13:00:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 13:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.90 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-09-21 13:05:01 | Baddegama (Gin Ganga) | 3.97 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 13:05:05 | Rathnapura (Kalu Ganga) | 5.67 | 🟡 Alert | -0.032 |  |
| 2026-09-21 13:03:28 | Magura (Kalu Ganga) | 5.48 | 🟡 Alert | -0.033 |  |
| 2026-09-21 13:13:05 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | -0.042 |  |
| 2026-09-21 13:02:34 | Deraniyagala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-09-21 13:01:11 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-21 13:02:34 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-21 13:03:36 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 13:05:00 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 13:02:09 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-21 13:02:09 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 13:03:04 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:02:30 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:16 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:01:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:03:52 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:04:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:00:49 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:06:23 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 13:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:02:42 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:03:16 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-21 13:02:23 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-09-21 13:10:07 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-09-21 13:03:14 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-09-21 13:08:24 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-09-21 13:02:35 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.034 |  |
| 2026-09-21 13:02:00 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-09-21 13:06:52 | Dunamale (Aththanagalu Oya) | 3.15 | 🟢 Normal | -0.048 |  |
| 2026-09-21 12:03:37 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.072 |  |
| 2026-09-21 13:05:09 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.077 |  |
| 2026-09-21 13:08:13 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.084 |  |
| 2026-09-21 13:05:17 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.092 |  |
| 2026-09-21 13:03:14 | Hanwella (Kelani Ganga) | 6.06 | 🟢 Normal | -0.120 |  |
| 2026-09-21 13:05:15 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | -0.139 |  |
| 2026-09-21 13:01:14 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -5.788 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)