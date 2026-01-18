# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_15:05:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 15:05:00 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-18 15:04:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:49 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:41 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:04:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:24 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 15:03:43 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.079 |  |
| 2026-01-18 15:03:36 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-01-18 15:03:20 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:03:18 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:03:02 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:02:59 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.043 |  |
| 2026-01-18 15:02:56 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:53 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-18 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 15:02:52 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:02:29 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:40 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:01:31 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:31 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:21 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:01:03 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 15:00:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:27:40 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-18 14:12:21 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.080 |  |
| 2026-01-18 14:10:31 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 14:04:12 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-18 14:27:40 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-18 15:02:53 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-18 15:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 15:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 15:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 15:04:49 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:50 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:00:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:01:41 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:23 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:01:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:03:18 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:56 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:24 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:03:20 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:31 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:04:22 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:52 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:31 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:04:57 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:07:09 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:01:03 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:03:37 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:29 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 14:05:57 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 15:02:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:04:41 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:02:30 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:03:02 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:01:40 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:01:21 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-18 15:05:00 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-18 15:03:36 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-01-18 15:02:59 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.043 |  |
| 2026-01-18 15:03:43 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.079 |  |
| 2026-01-18 14:12:21 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)