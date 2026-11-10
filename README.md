# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_11:03:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,922 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 11:03:36 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.226 |  |
| 2026-11-10 11:03:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 11:03:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:03:06 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:58 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-11-10 11:02:41 | Moraketiya (Walawe Ganga) | 2.95 | 🟢 Normal | -0.039 |  |
| 2026-11-10 11:02:37 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.088 |  |
| 2026-11-10 11:02:33 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 11:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-10 11:02:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 11:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:01:35 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-10 11:01:25 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-10 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-10 11:00:49 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-10 11:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-10 10:08:38 | Baddegama (Gin Ganga) | 4.20 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 10:09:28 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 10:02:14 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.050 |  |
| 2026-11-10 10:08:36 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 10:06:49 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.041 |  |
| 2026-11-10 11:01:25 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-10 11:02:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-10 11:00:45 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-10 11:01:35 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-10 11:03:35 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 10:10:36 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-10 10:03:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 10:05:55 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:02:20 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:03:06 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-10 11:03:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:01:56 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:00:49 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-10 11:02:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 11:02:33 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:00:12 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-10 11:02:58 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-11-10 10:06:30 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-10 11:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-10 11:02:41 | Moraketiya (Walawe Ganga) | 2.95 | 🟢 Normal | -0.039 |  |
| 2026-11-10 10:08:33 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-10 10:04:34 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.053 |  |
| 2026-11-10 10:04:28 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.059 |  |
| 2026-11-10 10:03:35 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.060 |  |
| 2026-11-10 10:05:37 | Badalgama (Maha Oya) | 3.99 | 🟢 Normal | -0.081 |  |
| 2026-11-10 11:02:37 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.088 |  |
| 2026-11-10 10:03:09 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.100 |  |
| 2026-11-10 10:07:11 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.137 |  |
| 2026-11-10 10:03:33 | Hanwella (Kelani Ganga) | 5.90 | 🟢 Normal | -0.153 |  |
| 2026-11-10 11:03:36 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.226 |  |
| 2026-11-10 10:07:25 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.251 |  |
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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)