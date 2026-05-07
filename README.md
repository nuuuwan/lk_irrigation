# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_22:21:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 22:21:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-05-07 22:18:24 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-07 22:12:40 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -675.000 |  |
| 2026-05-07 22:12:28 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-05-07 22:12:24 | Panadugama (Nilwala Ganga) | 6.79 | 🟠 Minor Flood | -675.000 |  |
| 2026-05-07 22:10:22 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.215 |  |
| 2026-05-07 22:09:00 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.073 |  |
| 2026-05-07 22:08:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-07 22:08:21 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-05-07 22:07:40 | Thanamalwila (Kirindi Oya) | 2.67 | 🟢 Normal | -0.223 |  |
| 2026-05-07 22:07:38 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 22:07:35 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.056 |  |
| 2026-05-07 22:07:10 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.091 |  |
| 2026-05-07 22:06:25 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 22:04:48 | Holombuwa (Kelani Ganga) | 2.44 | 🟢 Normal | -0.162 |  |
| 2026-05-07 22:04:44 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.029 |  |
| 2026-05-07 22:04:27 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-07 22:04:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:04:04 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:04:03 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.184 |  |
| 2026-05-07 22:03:56 | Nakkala (Kumbukkan Oya) | 2.58 | 🟢 Normal | 0.816 | 🔺 Rising |
| 2026-05-07 22:03:50 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-05-07 22:02:44 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.732 | 🔺 Rising |
| 2026-05-07 22:02:07 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-07 22:01:54 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2026-05-07 22:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:31 | Kuda Oya (Kirindi Oya) | 3.65 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-05-07 22:01:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:23 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-05-07 22:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:20 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.038 |  |
| 2026-05-07 22:01:17 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 22:01:14 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:00:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:00:43 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.235 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 22:03:56 | Nakkala (Kumbukkan Oya) | 2.58 | 🟢 Normal | 0.816 | 🔺 Rising |
| 2026-05-07 22:02:44 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.732 | 🔺 Rising |
| 2026-05-07 22:01:31 | Kuda Oya (Kirindi Oya) | 3.65 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-05-07 22:08:21 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-05-07 22:04:27 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-07 22:02:07 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-07 22:18:24 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-07 22:07:38 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 22:01:17 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 22:06:25 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 22:01:14 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:00:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:04:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:04:04 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 22:08:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-07 22:01:23 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-05-07 22:21:19 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.017 |  |
| 2026-05-07 22:12:28 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-05-07 18:02:13 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.029 |  |
| 2026-05-07 22:04:44 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.029 |  |
| 2026-05-07 22:01:20 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.038 |  |
| 2026-05-07 22:03:50 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-05-07 22:01:54 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2026-05-07 22:07:35 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.056 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-07 22:09:00 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.073 |  |
| 2026-05-07 22:07:10 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.091 |  |
| 2026-05-07 22:04:48 | Holombuwa (Kelani Ganga) | 2.44 | 🟢 Normal | -0.162 |  |
| 2026-05-07 22:04:03 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.184 |  |
| 2026-05-07 22:10:22 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.215 |  |
| 2026-05-07 22:07:40 | Thanamalwila (Kirindi Oya) | 2.67 | 🟢 Normal | -0.223 |  |
| 2026-05-07 22:00:43 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.235 |  |
| 2026-05-07 22:12:40 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -675.000 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)