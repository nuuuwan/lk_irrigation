# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_13:29:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 13:29:36 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:18:17 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:10:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.035 |  |
| 2026-01-25 13:10:15 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.057 |  |
| 2026-01-25 13:09:51 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-01-25 13:09:45 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:08:37 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:50 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:12 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.009 |  |
| 2026-01-25 13:06:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:05:37 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:05:33 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:04:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:04:08 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 13:04:02 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 13:03:47 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 13:03:44 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:42 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.123 |  |
| 2026-01-25 13:03:40 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:23 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:17 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 13:02:54 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.072 |  |
| 2026-01-25 13:02:46 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:42 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:39 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:10 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-25 13:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:56 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:55 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:47 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-01-25 13:01:43 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 13:01:18 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:01:08 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-25 13:00:55 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:00:50 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.021 |  |
| 2026-01-25 13:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 12:36:47 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 13:01:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-25 13:02:10 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-25 13:04:02 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 13:03:17 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 13:04:08 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 13:03:47 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 13:01:43 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 13:01:56 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:29:36 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:42 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:08:37 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:06:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:05:33 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:39 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:18:17 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:09:45 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:00:55 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:04:52 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:01:08 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:40 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:50 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:44 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:33 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:02:46 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:03:23 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 13:07:12 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.009 |  |
| 2026-01-25 13:05:37 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:01:55 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:01:18 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-25 13:09:51 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-01-25 13:01:47 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-01-25 13:00:50 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.021 |  |
| 2026-01-25 13:10:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.035 |  |
| 2026-01-25 13:10:15 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.057 |  |
| 2026-01-25 13:02:54 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.072 |  |
| 2026-01-25 13:03:42 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)