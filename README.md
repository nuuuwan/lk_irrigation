# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_10:10:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,903 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 10:10:36 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 10:09:28 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 10:08:38 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 10:08:36 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 10:08:33 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-10 10:07:25 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.251 |  |
| 2026-11-10 10:07:11 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.137 |  |
| 2026-11-10 10:06:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:06:49 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.041 |  |
| 2026-11-10 10:06:30 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-10 10:06:02 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | -0.645 |  |
| 2026-11-10 10:05:55 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:05:37 | Badalgama (Maha Oya) | 3.99 | 🟢 Normal | -0.081 |  |
| 2026-11-10 10:05:07 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.400 |  |
| 2026-11-10 10:05:00 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-11-10 10:04:41 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:04:34 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.053 |  |
| 2026-11-10 10:04:28 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.059 |  |
| 2026-11-10 10:04:12 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-10 10:03:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 10:03:40 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-11-10 10:03:35 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.060 |  |
| 2026-11-10 10:03:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:03:33 | Hanwella (Kelani Ganga) | 5.90 | 🟢 Normal | -0.153 |  |
| 2026-11-10 10:03:09 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.100 |  |
| 2026-11-10 10:03:04 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:53 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 10:02:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-11-10 10:02:14 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.050 |  |
| 2026-11-10 10:02:09 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-11-10 10:01:43 | Moraketiya (Walawe Ganga) | 2.99 | 🟢 Normal | -0.031 |  |
| 2026-11-10 10:01:22 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:14 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:11 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.106 |  |
| 2026-11-10 10:00:13 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-10 10:00:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-11-10 10:08:38 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 10:09:28 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 10:02:14 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.050 |  |
| 2026-11-10 10:08:36 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 10:06:49 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.041 |  |
| 2026-11-10 10:04:12 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-10 10:00:13 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-10 10:03:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-10 10:02:53 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 10:10:36 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 10:03:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:05:55 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:04:41 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:01:14 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:03:04 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:06:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:02:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:00:13 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-10 10:05:00 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-11-10 10:03:40 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2026-11-10 10:06:30 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-10 10:01:43 | Moraketiya (Walawe Ganga) | 2.99 | 🟢 Normal | -0.031 |  |
| 2026-11-10 10:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:01:22 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-11-10 10:08:33 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-10 10:04:34 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.053 |  |
| 2026-11-10 10:04:28 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.059 |  |
| 2026-11-10 10:03:35 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.060 |  |
| 2026-11-10 10:02:09 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-11-10 10:05:37 | Badalgama (Maha Oya) | 3.99 | 🟢 Normal | -0.081 |  |
| 2026-11-10 10:03:09 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.100 |  |
| 2026-11-10 10:01:11 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.106 |  |
| 2026-11-10 10:07:11 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.137 |  |
| 2026-11-10 10:03:33 | Hanwella (Kelani Ganga) | 5.90 | 🟢 Normal | -0.153 |  |
| 2026-11-10 10:07:25 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.251 |  |
| 2026-11-10 10:05:07 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.400 |  |
| 2026-11-10 10:06:02 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | -0.645 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)