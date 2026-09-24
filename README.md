# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_19:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 19:14:57 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:11:56 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.244 |  |
| 2026-09-24 19:10:53 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 19:10:26 | Panadugama (Nilwala Ganga) | 6.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 19:08:27 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-24 19:07:12 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 19:06:47 | Rathnapura (Kalu Ganga) | 5.93 | 🟡 Alert | 0.000 |  |
| 2026-09-24 19:06:08 | Glencourse (Kelani Ganga) | 14.00 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-24 19:06:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 19:05:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-09-24 19:05:21 | Kithulgala (Kelani Ganga) | 3.75 | 🟡 Alert | 0.912 | 🔺 Rising |
| 2026-09-24 19:05:12 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 19:04:59 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:04:35 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-24 19:04:29 | Urawa (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.049 |  |
| 2026-09-24 19:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-09-24 19:03:47 | Deraniyagala (Kelani Ganga) | 4.40 | 🟢 Normal | 1.506 | 🔺 Rising |
| 2026-09-24 19:03:29 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2026-09-24 19:03:10 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-24 19:02:58 | Thawalama (Gin Ganga) | 5.18 | 🟡 Alert | -0.050 |  |
| 2026-09-24 19:02:46 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-24 19:02:43 | Nawalapitiya (Mahaweli Ganga) | 3.88 | 🟡 Alert | 0.763 | 🔺 Rising |
| 2026-09-24 19:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:02:33 | Baddegama (Gin Ganga) | 4.48 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 19:02:23 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-24 19:02:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:02:19 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 19:02:12 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 19:02:00 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:59 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:48 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-24 19:01:31 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:12 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:00:29 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 19:02:33 | Baddegama (Gin Ganga) | 4.48 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 19:06:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.73 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-24 19:10:26 | Panadugama (Nilwala Ganga) | 6.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 19:10:53 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 19:05:21 | Kithulgala (Kelani Ganga) | 3.75 | 🟡 Alert | 0.912 | 🔺 Rising |
| 2026-09-24 19:02:43 | Nawalapitiya (Mahaweli Ganga) | 3.88 | 🟡 Alert | 0.763 | 🔺 Rising |
| 2026-09-24 19:02:23 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-24 19:06:47 | Rathnapura (Kalu Ganga) | 5.93 | 🟡 Alert | 0.000 |  |
| 2026-09-24 19:02:58 | Thawalama (Gin Ganga) | 5.18 | 🟡 Alert | -0.050 |  |
| 2026-09-24 19:03:47 | Deraniyagala (Kelani Ganga) | 4.40 | 🟢 Normal | 1.506 | 🔺 Rising |
| 2026-09-24 19:03:29 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2026-09-24 19:03:10 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-24 19:02:46 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-24 19:02:12 | Hanwella (Kelani Ganga) | 5.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 19:06:08 | Glencourse (Kelani Ganga) | 14.00 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-24 19:08:27 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-24 19:04:35 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-24 19:07:12 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 19:05:12 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 19:02:19 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:25 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:02:00 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:14:57 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:12 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:02:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:59 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:04:59 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:31 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 19:01:48 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-24 19:00:29 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-09-24 19:05:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.019 |  |
| 2026-09-24 19:04:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-09-24 19:04:29 | Urawa (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.049 |  |
| 2026-09-24 19:11:56 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)