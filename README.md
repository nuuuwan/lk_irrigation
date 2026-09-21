# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_06:16:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,696 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 06:16:15 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:12:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:11:53 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:11:33 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:09:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:08:56 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.032 |  |
| 2026-09-21 06:07:51 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.100 |  |
| 2026-09-21 06:07:50 | Hanwella (Kelani Ganga) | 6.79 | 🟢 Normal | -0.047 |  |
| 2026-09-21 06:07:24 | Glencourse (Kelani Ganga) | 14.63 | 🟢 Normal | -0.221 |  |
| 2026-09-21 06:07:04 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.097 |  |
| 2026-09-21 06:05:54 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.456 |  |
| 2026-09-21 06:05:50 | Baddegama (Gin Ganga) | 3.86 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 06:05:40 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.098 |  |
| 2026-09-21 06:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.154 | 🔺 Rising |
| 2026-09-21 06:05:26 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:05:06 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:04:53 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.080 |  |
| 2026-09-21 06:03:55 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.084 |  |
| 2026-09-21 06:03:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 06:03:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:03:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:03:35 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.056 |  |
| 2026-09-21 06:03:24 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | -0.020 |  |
| 2026-09-21 06:03:04 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:02:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:02:36 | Thawalama (Gin Ganga) | 4.63 | 🟡 Alert | -0.225 |  |
| 2026-09-21 06:02:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-21 06:02:31 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.089 |  |
| 2026-09-21 06:02:30 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.073 |  |
| 2026-09-21 06:02:30 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-21 06:02:26 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.695 |  |
| 2026-09-21 06:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:01:29 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-21 06:01:14 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-09-21 06:00:42 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:00:07 | Magura (Kalu Ganga) | 5.66 | 🟡 Alert | -0.022 |  |
| 2026-09-21 06:00:01 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 06:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.154 | 🔺 Rising |
| 2026-09-21 05:02:02 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-09-21 06:05:50 | Baddegama (Gin Ganga) | 3.86 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 06:03:24 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | -0.020 |  |
| 2026-09-21 06:00:07 | Magura (Kalu Ganga) | 5.66 | 🟡 Alert | -0.022 |  |
| 2026-09-21 06:08:56 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.032 |  |
| 2026-09-21 06:07:04 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.097 |  |
| 2026-09-21 06:02:36 | Thawalama (Gin Ganga) | 4.63 | 🟡 Alert | -0.225 |  |
| 2026-09-21 06:02:30 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 06:03:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 06:01:29 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-21 06:05:26 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:00:42 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:05:06 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:11:53 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:09:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:16:15 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:03:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:03:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:02:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:12:16 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:03:04 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 06:02:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-21 06:07:50 | Hanwella (Kelani Ganga) | 6.79 | 🟢 Normal | -0.047 |  |
| 2026-09-21 06:00:01 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.053 |  |
| 2026-09-21 06:03:35 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.056 |  |
| 2026-09-21 06:01:14 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.061 |  |
| 2026-09-21 06:02:30 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.073 |  |
| 2026-09-21 06:04:53 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.080 |  |
| 2026-09-21 06:03:55 | Deraniyagala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.084 |  |
| 2026-09-21 06:02:31 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.089 |  |
| 2026-09-21 06:05:40 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.098 |  |
| 2026-09-21 06:07:51 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.100 |  |
| 2026-09-21 06:07:24 | Glencourse (Kelani Ganga) | 14.63 | 🟢 Normal | -0.221 |  |
| 2026-09-21 06:05:54 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.456 |  |
| 2026-09-21 06:02:26 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.695 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)