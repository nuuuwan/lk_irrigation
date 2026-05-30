# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_14:21:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 14:21:58 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:17:17 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.008 |  |
| 2026-05-30 14:16:17 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.004 |  |
| 2026-05-30 14:10:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.37 | 🟡 Alert | -0.018 |  |
| 2026-05-30 14:09:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-05-30 14:08:52 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.067 |  |
| 2026-05-30 14:08:51 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-05-30 14:08:51 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | -0.027 |  |
| 2026-05-30 14:07:05 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:06:30 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-30 14:06:18 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:05:31 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-30 14:05:00 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.011 |  |
| 2026-05-30 14:04:36 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-05-30 14:04:31 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.053 |  |
| 2026-05-30 14:03:49 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:03:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-30 14:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 14:03:05 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-05-30 14:03:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-30 14:02:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:06 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:01:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.069 |  |
| 2026-05-30 14:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:01:34 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:01:07 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:01:06 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:54 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:15 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 14:10:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.37 | 🟡 Alert | -0.018 |  |
| 2026-05-30 14:06:30 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-30 14:03:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-30 14:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-30 14:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 13:03:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 14:01:06 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:57 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:08 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:06:18 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:21:58 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:03:49 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:07:05 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:02:19 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:54 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:02:06 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:16:17 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.004 |  |
| 2026-05-30 14:08:51 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-05-30 14:17:17 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.008 |  |
| 2026-05-30 14:09:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-05-30 14:01:34 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:01:07 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:03:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-30 14:00:15 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-05-30 14:05:00 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.011 |  |
| 2026-05-30 14:08:51 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | -0.027 |  |
| 2026-05-30 13:02:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-05-30 14:03:05 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-05-30 14:04:36 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-05-30 14:04:31 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.053 |  |
| 2026-05-30 14:05:31 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.060 |  |
| 2026-05-30 14:08:52 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.067 |  |
| 2026-05-30 14:01:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)