# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_22:19:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 22:19:55 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:11:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:10:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:08:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:08:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:07:34 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 22:07:23 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:07:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-01 22:06:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-01 22:06:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:06:08 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:05:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:05:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:05:30 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:05:09 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-04-01 22:04:20 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:03:42 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:03:01 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:37 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:02:28 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-01 22:02:28 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:25 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:13 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:54 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:51 | Rathnapura (Kalu Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-01 22:01:30 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-01 22:01:28 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:11 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 22:02:28 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-01 22:01:30 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-01 22:01:11 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-01 22:01:51 | Rathnapura (Kalu Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-01 22:07:00 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-01 22:07:34 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-01 22:11:39 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:54 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 21:02:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:04:20 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:19:55 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:06:08 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:13 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:28 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 21:04:58 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 21:10:02 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:08:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:07:23 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:01:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:28 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:05:30 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:03:01 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:10:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:05:41 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:02:25 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:06:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:08:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:02:37 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:05:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-01 22:06:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-01 22:05:09 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-01 21:27:44 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)