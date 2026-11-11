# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_13:31:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 13:31:33 | Moragaswewa (Deduru Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:16:42 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.051 |  |
| 2026-11-11 13:15:00 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 13:13:24 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-11 13:12:05 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 13:09:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-11 13:08:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:08:14 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-11 13:07:10 | Moragaswewa (Deduru Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:07:03 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:50 | Dunamale (Aththanagalu Oya) | 3.97 | 🟡 Alert | -0.047 |  |
| 2026-11-11 13:06:37 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:30 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-11 13:06:17 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.056 |  |
| 2026-11-11 13:05:55 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.028 |  |
| 2026-11-11 13:05:55 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-11 13:05:40 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | -0.098 |  |
| 2026-11-11 13:05:22 | Rathnapura (Kalu Ganga) | 4.11 | 🟢 Normal | -0.120 |  |
| 2026-11-11 13:05:14 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.121 |  |
| 2026-11-11 13:04:32 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:03:46 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-11-11 13:03:41 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 13:03:39 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:03:28 | Hanwella (Kelani Ganga) | 4.26 | 🟢 Normal | -0.100 |  |
| 2026-11-11 13:03:22 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 13:03:05 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.068 |  |
| 2026-11-11 13:02:50 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:02:38 | Panadugama (Nilwala Ganga) | 5.59 | 🟡 Alert | -0.030 |  |
| 2026-11-11 13:02:36 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:35 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:35 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:27 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-11-11 13:02:21 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.57 | 🟠 Minor Flood | -0.107 |  |
| 2026-11-11 13:02:05 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:01:25 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:01:13 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:01:11 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 13:01:08 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.156 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 13:15:00 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 13:13:24 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-11 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.57 | 🟠 Minor Flood | -0.107 |  |
| 2026-11-11 13:02:38 | Panadugama (Nilwala Ganga) | 5.59 | 🟡 Alert | -0.030 |  |
| 2026-11-11 13:06:50 | Dunamale (Aththanagalu Oya) | 3.97 | 🟡 Alert | -0.047 |  |
| 2026-11-11 13:06:30 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-11 13:09:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-11 13:08:14 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-11 13:03:41 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 13:05:55 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-11 13:01:11 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 13:03:22 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 13:12:05 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 13:31:33 | Moragaswewa (Deduru Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:34 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:37 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:03:39 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:35 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:07:03 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:36 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:50 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:04:32 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:02:05 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:02:21 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:01:25 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:08:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:01:13 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:03:46 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-11-11 13:05:55 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.028 |  |
| 2026-11-11 13:02:27 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-11-11 13:16:42 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.051 |  |
| 2026-11-11 13:06:17 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.056 |  |
| 2026-11-11 13:03:05 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.068 |  |
| 2026-11-11 13:05:40 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | -0.098 |  |
| 2026-11-11 13:03:28 | Hanwella (Kelani Ganga) | 4.26 | 🟢 Normal | -0.100 |  |
| 2026-11-11 13:05:22 | Rathnapura (Kalu Ganga) | 4.11 | 🟢 Normal | -0.120 |  |
| 2026-11-11 13:05:14 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.121 |  |
| 2026-11-11 13:01:08 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)