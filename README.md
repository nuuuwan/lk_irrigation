# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_14:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,939 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 14:03:23 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 14:03:19 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.049 |  |
| 2026-11-11 14:02:39 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 14:02:26 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-11-11 14:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:20 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.043 |  |
| 2026-11-11 14:02:08 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-11-11 14:02:06 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 14:02:06 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:01:51 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:01:40 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-11 14:01:24 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.119 |  |
| 2026-11-11 14:01:07 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:01:02 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.033 |  |
| 2026-11-11 14:00:39 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-11 14:00:20 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-11-11 14:00:15 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | -0.087 |  |
| 2026-11-11 13:31:33 | Moragaswewa (Deduru Oya) | 2.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 14:02:06 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 13:13:24 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-11 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 13:06:50 | Dunamale (Aththanagalu Oya) | 3.97 | 🟡 Alert | -0.047 |  |
| 2026-11-11 14:03:19 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.049 |  |
| 2026-11-11 14:00:20 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-11-11 14:00:39 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-11 14:01:40 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-11 13:05:55 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-11 14:03:23 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 13:12:05 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 14:02:39 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:31:33 | Moragaswewa (Deduru Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:20 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:06:37 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:03:39 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:01:51 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:35 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:07:03 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:36 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-11 13:02:21 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:01:07 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:01:25 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:02:06 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 13:08:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:01:13 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-11 13:03:46 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-11-11 13:02:27 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-11-11 14:02:08 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-11-11 14:01:02 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.033 |  |
| 2026-11-11 14:02:26 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-11-11 14:02:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.043 |  |
| 2026-11-11 13:16:42 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.051 |  |
| 2026-11-11 14:00:15 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | -0.087 |  |
| 2026-11-11 13:05:40 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | -0.098 |  |
| 2026-11-11 13:03:28 | Hanwella (Kelani Ganga) | 4.26 | 🟢 Normal | -0.100 |  |
| 2026-11-11 14:01:24 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.119 |  |
| 2026-11-11 13:05:14 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)