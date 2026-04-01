# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_09:08:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,096 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 09:08:46 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:08:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:08:07 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:37 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:34 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:25 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:06:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:04:59 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:04:48 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -18.000 |  |
| 2026-04-01 09:04:46 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -18.000 |  |
| 2026-04-01 09:04:35 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:04:25 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.068 |  |
| 2026-04-01 09:04:18 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.068 |  |
| 2026-04-01 09:03:59 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:03:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:03:55 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-01 09:03:54 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:03:52 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-04-01 09:03:29 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:03:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:03:20 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-04-01 09:03:09 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:03:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:03:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-04-01 09:02:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:47 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:36 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:23 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:02:00 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.102 |  |
| 2026-04-01 09:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:57 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:48 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:01:39 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:34 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:01:13 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-01 09:01:04 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 09:01:13 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-01 09:03:55 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-01 09:03:54 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:03:09 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:02:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:03:29 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 09:02:47 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:34 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:57 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:25 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:04:35 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:08:07 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:39 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:03:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:08:08 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:03:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:06:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:03:59 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:37 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:01:04 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:08:46 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:23 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:07:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:36 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:03:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:03:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:04:59 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:01:48 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:01:34 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-01 09:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-04-01 09:03:52 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.049 |  |
| 2026-04-01 09:03:20 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.060 |  |
| 2026-04-01 09:04:25 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.068 |  |
| 2026-04-01 09:04:18 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.068 |  |
| 2026-04-01 09:02:00 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.102 |  |
| 2026-04-01 09:04:48 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)