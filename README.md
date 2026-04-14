# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_21:10:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 21:10:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:10:26 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-14 21:10:21 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:09:29 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:08:42 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:08:39 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.005 |  |
| 2026-04-14 21:08:36 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:08:35 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-04-14 21:08:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-04-14 21:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.031 |  |
| 2026-04-14 21:05:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.060 |  |
| 2026-04-14 21:05:14 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:05:13 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 21:05:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:04:23 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-04-14 21:03:57 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.054 |  |
| 2026-04-14 21:03:40 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:03:31 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.089 |  |
| 2026-04-14 21:02:58 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-14 21:02:56 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.020 |  |
| 2026-04-14 21:02:48 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:48 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-04-14 21:02:47 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:47 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:02:39 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:33 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:02:15 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:01:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:01:07 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:00:57 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:00:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:23 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 21:02:58 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-14 21:05:13 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 21:05:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:00:57 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:02:33 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 21:10:26 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-14 21:00:23 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:01:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:39 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:10:21 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:48 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:02:47 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:08:42 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:00:13 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:03:40 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:09:29 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:10:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 21:08:39 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.005 |  |
| 2026-04-14 21:08:10 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-04-14 21:08:36 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:01:07 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:02:15 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:02:47 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:05:14 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-14 21:04:23 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-04-14 21:02:56 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 21:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.031 |  |
| 2026-04-14 21:02:48 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-04-14 21:08:35 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-04-14 21:03:57 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.054 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 21:05:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 21:03:31 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)