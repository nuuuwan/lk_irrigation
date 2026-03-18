# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_22:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 22:13:52 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 22:11:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.043 |  |
| 2026-03-18 22:07:41 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.112 |  |
| 2026-03-18 22:07:32 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-18 22:07:07 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-18 22:06:50 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-03-18 22:06:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:06:11 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:05:49 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:05:05 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:04:44 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-18 22:04:02 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:03:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-18 22:03:34 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:03:30 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:29 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:20 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:20 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-03-18 22:03:09 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 22:03:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:02:44 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:42 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:02:41 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:36 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:35 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-03-18 22:02:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-03-18 22:02:15 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-18 22:02:08 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:01:37 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:01:28 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:01:13 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:00:49 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 22:03:20 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-03-18 22:02:15 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-18 22:04:44 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-18 22:07:32 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-18 22:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-18 22:03:09 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 22:02:08 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:03:00 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:04:02 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 22:13:52 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-18 22:01:13 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 21:02:21 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:44 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:00:49 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:01:28 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:36 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:05:49 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:30 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:06:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:07:07 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:20 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:02:41 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:29 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:05:05 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:06:11 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 22:03:34 | Manampitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:01:37 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:02:42 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-18 22:02:31 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-03-18 22:02:35 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-03-18 22:03:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-18 22:11:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.043 |  |
| 2026-03-18 22:06:50 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.066 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-18 22:07:41 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)