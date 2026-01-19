# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_14:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,921 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 14:18:27 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:16:44 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:11:43 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-19 14:11:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-19 14:11:09 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-01-19 14:10:44 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.012 |  |
| 2026-01-19 14:09:57 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:08:55 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:07:23 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.037 |  |
| 2026-01-19 14:06:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:05:19 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:05:19 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-19 14:04:45 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:04:37 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-19 14:04:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-19 14:04:02 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-19 14:03:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:39 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-01-19 14:03:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:35 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:23 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:23 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:09 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-19 14:03:02 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.084 |  |
| 2026-01-19 14:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.014 |  |
| 2026-01-19 14:02:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:21 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-19 14:02:12 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:52 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:32 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:25 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-19 14:01:10 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:00:51 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 14:04:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-19 14:11:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-19 14:11:43 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-19 14:05:19 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-19 14:01:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-19 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-19 14:04:37 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-19 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:23 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:00:51 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:08:55 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:05:19 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:18:27 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:16:44 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:25 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:52 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:21 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:35 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:39 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:04:45 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 13:08:41 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:15 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:02:12 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:03:23 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:06:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:09:57 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:01:32 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 14:04:02 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-01-19 14:10:44 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.012 |  |
| 2026-01-19 14:11:09 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.013 |  |
| 2026-01-19 14:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.014 |  |
| 2026-01-19 14:03:09 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-19 14:07:23 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.037 |  |
| 2026-01-19 14:03:39 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-01-19 14:03:02 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)