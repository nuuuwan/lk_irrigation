# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_22:21:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 22:21:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:17:35 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.024 |  |
| 2026-05-29 22:13:47 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.009 |  |
| 2026-05-29 22:13:31 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-05-29 22:12:14 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-05-29 22:10:06 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.009 |  |
| 2026-05-29 22:08:10 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-05-29 22:06:49 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:06:47 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:06:46 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | 19.453 | 🔺 Rising |
| 2026-05-29 22:06:43 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:05:51 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-05-29 22:05:35 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.030 |  |
| 2026-05-29 22:05:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-29 22:05:21 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:05:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 22:05:09 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:03:52 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-29 22:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.069 |  |
| 2026-05-29 22:03:49 | Rathnapura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.059 |  |
| 2026-05-29 22:03:42 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.049 |  |
| 2026-05-29 22:03:33 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.100 |  |
| 2026-05-29 22:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:03:03 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.049 |  |
| 2026-05-29 22:02:59 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-05-29 22:02:31 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.051 |  |
| 2026-05-29 22:02:30 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-05-29 22:02:06 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-05-29 22:02:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:01:24 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 19.453 | 🔺 Rising |
| 2026-05-29 22:00:57 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:21 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 21:26:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.031 |  |
| 2026-05-29 22:06:46 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | 19.453 | 🔺 Rising |
| 2026-05-29 22:02:06 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-05-29 22:05:23 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-29 22:05:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 22:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:57 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 21:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:18 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:03:04 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:21:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:06:43 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:05:09 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:21 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:13:31 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.008 |  |
| 2026-05-29 22:13:47 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.009 |  |
| 2026-05-29 22:10:06 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.009 |  |
| 2026-05-29 22:06:49 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:05:21 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:06:47 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:02:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-29 22:03:52 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-05-29 22:12:14 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-05-29 22:05:51 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-05-29 22:02:59 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.020 |  |
| 2026-05-29 22:02:30 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-05-29 22:08:10 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.021 |  |
| 2026-05-29 22:17:35 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.024 |  |
| 2026-05-29 22:05:35 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.030 |  |
| 2026-05-29 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-29 22:03:03 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.049 |  |
| 2026-05-29 22:03:42 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.049 |  |
| 2026-05-29 22:02:31 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.051 |  |
| 2026-05-29 22:03:49 | Rathnapura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.059 |  |
| 2026-05-29 22:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.069 |  |
| 2026-05-29 22:03:33 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)