# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_03:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,617 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 03:12:26 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-22 03:10:15 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:09:14 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | -0.112 |  |
| 2026-02-22 03:08:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-22 03:07:16 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.160 |  |
| 2026-02-22 03:06:56 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:06:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-22 03:05:58 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.050 |  |
| 2026-02-22 03:05:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:05:02 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.395 |  |
| 2026-02-22 03:05:01 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.053 |  |
| 2026-02-22 03:04:51 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-02-22 03:04:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 03:04:47 | Manampitiya (Mahaweli Ganga) | 4.00 | 🟡 Alert | 0.276 | 🔺 Rising |
| 2026-02-22 03:04:37 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.434 |  |
| 2026-02-22 03:04:35 | Thanamalwila (Kirindi Oya) | 2.58 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-02-22 03:04:33 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-22 03:04:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:04:13 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-02-22 03:04:02 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-22 03:03:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-22 03:03:37 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-22 03:03:27 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-02-22 03:03:27 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-22 03:03:24 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-02-22 03:03:09 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-22 03:02:39 | Nakkala (Kumbukkan Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-02-22 03:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.072 |  |
| 2026-02-22 03:02:18 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 03:02:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:01:43 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.578 | 🔺 Rising |
| 2026-02-22 03:01:40 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:01:40 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-22 03:01:12 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.191 |  |
| 2026-02-22 03:00:30 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:59:21 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 03:04:47 | Manampitiya (Mahaweli Ganga) | 4.00 | 🟡 Alert | 0.276 | 🔺 Rising |
| 2026-02-22 03:09:14 | Urawa (Nilwala Ganga) | 2.81 | 🟡 Alert | -0.112 |  |
| 2026-02-22 03:01:43 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.578 | 🔺 Rising |
| 2026-02-22 03:04:35 | Thanamalwila (Kirindi Oya) | 2.58 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-02-22 03:03:24 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-02-22 03:03:27 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-02-22 03:04:33 | Thawalama (Gin Ganga) | 3.14 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-02-22 03:03:27 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-02-22 03:03:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-02-22 03:06:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-22 03:02:18 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 03:03:37 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-02-22 03:03:09 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-22 03:08:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-22 03:04:02 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-22 03:12:26 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-22 03:04:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 03:05:42 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:01:40 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:04:25 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:10:15 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:00:30 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:02:10 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 03:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-02-22 02:01:22 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-22 03:01:40 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-02-22 03:04:51 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 03:04:13 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.042 |  |
| 2026-02-22 03:05:58 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.050 |  |
| 2026-02-22 03:05:01 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.053 |  |
| 2026-02-22 03:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.072 |  |
| 2026-02-22 03:02:39 | Nakkala (Kumbukkan Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-02-22 03:07:16 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.160 |  |
| 2026-02-22 03:01:12 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.191 |  |
| 2026-02-22 03:05:02 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.395 |  |
| 2026-02-22 03:04:37 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.434 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)