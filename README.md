# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_17:28:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,809 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 17:28:41 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:18:57 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-31 17:16:03 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:10:50 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:06:56 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:06:50 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.072 |  |
| 2026-01-31 17:06:24 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:05:47 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:05:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:05:35 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:55 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:22 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:09 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-31 17:04:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:56 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:03:43 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:03:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:41 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:36 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-31 17:03:35 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 17:03:23 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-31 17:03:04 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-01-31 17:02:53 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:47 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:44 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:43 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:02:38 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:01:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-01-31 17:01:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-01-31 17:01:19 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:00:43 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-31 17:00:35 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:00:26 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:00:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-31 16:53:51 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.123 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 17:01:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-01-31 17:03:36 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-31 17:00:43 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-31 17:03:35 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 17:00:35 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:02:43 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:10:50 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 17:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:41 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:05:35 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:28:41 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:47 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:23 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:53 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:03:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:55 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:44 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:06:56 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:00:26 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:16:03 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:22 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:00:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:02:38 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-31 17:18:57 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-31 17:04:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:05:38 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:01:19 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:05:47 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:03:56 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:03:43 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:06:24 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 17:03:04 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-01-31 17:04:09 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-31 17:01:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-01-31 17:03:14 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-01-31 17:06:50 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)