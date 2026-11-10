# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_23:14:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 23:14:05 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:10:45 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.061 |  |
| 2026-11-10 23:08:56 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:08:20 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-11-10 23:07:02 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.393 |  |
| 2026-11-10 23:06:08 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:05:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:05:06 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 23:05:01 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -324.000 |  |
| 2026-11-10 23:05:00 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -324.000 |  |
| 2026-11-10 23:04:58 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -324.000 |  |
| 2026-11-10 23:04:51 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.070 |  |
| 2026-11-10 23:04:11 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 23:03:59 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.017 |  |
| 2026-11-10 23:03:44 | Moraketiya (Walawe Ganga) | 2.41 | 🟢 Normal | -0.054 |  |
| 2026-11-10 23:03:44 | Glencourse (Kelani Ganga) | 13.11 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-10 23:03:35 | Thawalama (Gin Ganga) | 4.34 | 🟡 Alert | 0.248 | 🔺 Rising |
| 2026-11-10 23:03:26 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:03:20 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-10 23:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:03:05 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | -0.218 |  |
| 2026-11-10 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-10 23:02:39 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.034 |  |
| 2026-11-10 23:02:38 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-10 23:02:37 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-10 23:02:27 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-10 23:02:03 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:02:01 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:01:30 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:01:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-10 23:01:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:00:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 23:05:06 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-11-10 23:04:11 | Baddegama (Gin Ganga) | 4.27 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 22:07:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | -0.009 |  |
| 2026-11-10 23:02:27 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-10 23:01:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-10 23:03:35 | Thawalama (Gin Ganga) | 4.34 | 🟡 Alert | 0.248 | 🔺 Rising |
| 2026-11-10 22:08:28 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.020 |  |
| 2026-11-10 23:04:51 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.070 |  |
| 2026-11-10 23:03:05 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | -0.218 |  |
| 2026-11-10 23:03:44 | Glencourse (Kelani Ganga) | 13.11 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-10 23:02:47 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-10 23:02:38 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 22:02:07 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-10 23:03:20 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-10 23:02:03 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:01:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:14:05 | Pitabeddara (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-10 23:08:56 | Thanamalwila (Kirindi Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-10 22:25:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.003 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-10 22:06:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-11-10 23:01:30 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:05:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-10 23:03:59 | Urawa (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.017 |  |
| 2026-11-10 23:03:26 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:06:08 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-11-10 23:02:36 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-10 23:02:37 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-11-10 23:02:39 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.034 |  |
| 2026-11-10 23:03:44 | Moraketiya (Walawe Ganga) | 2.41 | 🟢 Normal | -0.054 |  |
| 2026-11-10 23:00:27 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.060 |  |
| 2026-11-10 23:10:45 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.061 |  |
| 2026-11-10 23:02:01 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.080 |  |
| 2026-11-10 23:08:20 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.110 |  |
| 2026-11-10 23:07:02 | Holombuwa (Kelani Ganga) | 2.36 | 🟢 Normal | -0.393 |  |
| 2026-11-10 23:05:01 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)