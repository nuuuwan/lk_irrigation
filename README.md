# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_12:20:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,746 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 12:20:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:08:52 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-04-24 12:08:19 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:07:51 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.019 |  |
| 2026-04-24 12:07:25 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.068 |  |
| 2026-04-24 12:06:57 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 12:06:35 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-24 12:06:32 | Katharagama (Menik Ganga) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-04-24 12:06:31 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-04-24 12:06:18 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-24 12:05:47 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.061 |  |
| 2026-04-24 12:05:28 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.083 |  |
| 2026-04-24 12:05:10 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:04:44 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-04-24 12:04:37 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-24 12:03:44 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-24 12:03:38 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:03:31 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:03:26 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-24 12:03:25 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 12:03:01 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-24 12:03:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:58 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:02:57 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:50 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:32 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-04-24 12:02:31 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.051 |  |
| 2026-04-24 12:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 12:02:11 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-24 12:01:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 12:01:54 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:01:38 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:01:26 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-24 12:01:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:00:55 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-04-24 12:00:38 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:00:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 12:04:44 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-04-24 12:04:37 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-24 12:02:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-24 12:03:26 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-24 12:06:57 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-24 12:01:26 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-24 12:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 12:03:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 12:01:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 12:01:54 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:01:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:02:58 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:05:10 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:08:19 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:03:31 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:00:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:02:31 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:00:38 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:20:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-24 12:06:18 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-04-24 12:03:25 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:11 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:01:38 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:57 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:03:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:02:50 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-24 12:06:35 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-04-24 12:06:32 | Katharagama (Menik Ganga) | 2.04 | 🟢 Normal | -0.018 |  |
| 2026-04-24 12:07:51 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.019 |  |
| 2026-04-24 12:06:31 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-04-24 12:00:55 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-04-24 12:03:01 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-24 12:08:52 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-04-24 12:03:44 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-04-24 12:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.051 |  |
| 2026-04-24 12:05:47 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | -0.061 |  |
| 2026-04-24 12:07:25 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.068 |  |
| 2026-04-24 12:02:32 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.075 |  |
| 2026-04-24 12:05:28 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)