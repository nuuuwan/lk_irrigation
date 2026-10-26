# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_11:09:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 11:09:35 | Urawa (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-10-26 11:08:09 | Glencourse (Kelani Ganga) | 12.24 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-26 11:07:42 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-26 11:06:48 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 11:06:31 | Kithulgala (Kelani Ganga) | 2.93 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-26 11:06:20 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.028 |  |
| 2026-10-26 11:06:19 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-26 11:06:16 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-26 11:06:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:05:48 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-26 11:05:42 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-10-26 11:05:38 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.019 |  |
| 2026-10-26 11:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-10-26 11:04:51 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-10-26 11:04:48 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-10-26 11:04:13 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:04:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 11:04:04 | Rathnapura (Kalu Ganga) | 7.30 | 🟡 Alert | 0.650 | 🔺 Rising |
| 2026-10-26 11:03:47 | Holombuwa (Kelani Ganga) | 3.97 | 🟠 Minor Flood | 1.036 | 🔺 Rising |
| 2026-10-26 11:03:47 | Moragaswewa (Deduru Oya) | 4.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:03:27 | Norwood (Kelani Ganga) | 2.01 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-10-26 11:03:13 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-26 11:03:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.688 | 🔺 Rising |
| 2026-10-26 11:02:56 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 11:02:45 | Nawalapitiya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-10-26 11:02:42 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-26 11:02:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-26 11:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:02:07 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 11:01:53 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:01:29 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:01:12 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-26 11:00:53 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.041 |  |
| 2026-10-26 11:00:47 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 11:00:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 11:03:47 | Holombuwa (Kelani Ganga) | 3.97 | 🟠 Minor Flood | 1.036 | 🔺 Rising |
| 2026-10-26 11:04:04 | Rathnapura (Kalu Ganga) | 7.30 | 🟡 Alert | 0.650 | 🔺 Rising |
| 2026-10-26 11:03:27 | Norwood (Kelani Ganga) | 2.01 | 🟡 Alert | 0.223 | 🔺 Rising |
| 2026-10-26 11:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-10-26 11:00:53 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | -0.041 |  |
| 2026-10-26 11:04:51 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 120.000 | 🔺 Rising |
| 2026-10-26 11:03:08 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.688 | 🔺 Rising |
| 2026-10-26 11:09:35 | Urawa (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-10-26 11:05:42 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-10-26 11:02:45 | Nawalapitiya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-10-26 11:06:31 | Kithulgala (Kelani Ganga) | 2.93 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-26 11:03:13 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-26 10:05:54 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-26 11:07:42 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-26 11:08:09 | Glencourse (Kelani Ganga) | 12.24 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-26 11:02:42 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-26 11:06:48 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 11:06:19 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-26 10:07:23 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-26 11:06:16 | Putupaula (Kalu Ganga) | 2.27 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-26 11:01:12 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-26 11:02:07 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 11:00:47 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 11:04:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 11:02:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:01:53 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:04:13 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:03:47 | Moragaswewa (Deduru Oya) | 4.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 11:05:48 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-26 11:00:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 11:02:56 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 11:06:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:03:27 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:01:29 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 10:08:32 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-26 11:05:38 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.019 |  |
| 2026-10-26 11:02:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-26 11:06:20 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.028 |  |
| 2026-10-26 10:06:43 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)