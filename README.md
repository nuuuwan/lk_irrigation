# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_01:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,535 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 01:06:50 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.181 |  |
| 2026-02-22 01:06:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-22 01:06:02 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-22 01:06:02 | Rathnapura (Kalu Ganga) | 5.28 | 🟡 Alert | -0.097 |  |
| 2026-02-22 01:05:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 01:05:32 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-22 01:04:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 01:04:51 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.079 |  |
| 2026-02-22 01:04:30 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-22 01:04:06 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 01:04:01 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-02-22 01:03:54 | Holombuwa (Kelani Ganga) | 2.06 | 🟢 Normal | -0.245 |  |
| 2026-02-22 01:03:52 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 01:02:55 | Nakkala (Kumbukkan Oya) | 2.09 | 🟢 Normal | -0.166 |  |
| 2026-02-22 01:02:52 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.089 |  |
| 2026-02-22 01:02:46 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | 0.711 | 🔺 Rising |
| 2026-02-22 01:02:36 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.127 |  |
| 2026-02-22 01:02:29 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-22 01:02:17 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-22 01:02:06 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-22 01:02:03 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 01:01:58 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 01:01:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 01:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-02-22 01:01:10 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-22 01:00:16 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | 0.372 | 🔺 Rising |
| 2026-02-22 00:20:18 | Moraketiya (Walawe Ganga) | 1.55 | 🟢 Normal | -0.181 |  |
| 2026-02-22 00:15:00 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-02-22 00:13:23 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 00:13:18 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | 0.214 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 01:00:16 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | 0.372 | 🔺 Rising |
| 2026-02-22 00:13:18 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | 0.214 | 🔺 Rising |
| 2026-02-22 01:06:02 | Rathnapura (Kalu Ganga) | 5.28 | 🟡 Alert | -0.097 |  |
| 2026-02-22 01:02:46 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | 0.711 | 🔺 Rising |
| 2026-02-22 00:00:33 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2026-02-22 01:04:30 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-02-22 00:13:23 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-02-22 01:06:02 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-22 01:04:01 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-02-22 00:03:01 | Padiyathalawa (Maduru Oya) | 1.69 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-02-22 01:05:32 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-02-22 01:02:29 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-22 01:02:17 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-22 01:06:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-22 01:02:06 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-22 01:05:58 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 01:01:58 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-22 01:02:03 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 00:07:37 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-22 00:01:49 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 01:03:52 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:01:38 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 01:01:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 00:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-02-22 01:04:06 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-22 01:01:10 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-22 01:04:57 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 00:15:00 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-02-22 01:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-02-22 01:04:51 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.079 |  |
| 2026-02-22 01:02:52 | Thaldena (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.089 |  |
| 2026-02-22 01:02:36 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.127 |  |
| 2026-02-22 01:02:55 | Nakkala (Kumbukkan Oya) | 2.09 | 🟢 Normal | -0.166 |  |
| 2026-02-22 01:06:50 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.181 |  |
| 2026-02-22 01:03:54 | Holombuwa (Kelani Ganga) | 2.06 | 🟢 Normal | -0.245 |  |
| 2026-02-22 00:07:13 | Wellawaya (Kirindi Oya) | 3.25 | 🟢 Normal | -0.284 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)