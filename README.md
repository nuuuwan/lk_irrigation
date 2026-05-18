# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_17:16:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,370 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 17:16:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-05-18 17:14:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-18 17:13:49 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:09:50 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:08:05 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:07:27 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | -0.046 |  |
| 2026-05-18 17:06:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:05:17 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.089 |  |
| 2026-05-18 17:05:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:05:06 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:04:51 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-18 17:04:38 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-05-18 17:04:33 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:04:32 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:04:16 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 17:04:05 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 17:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:03:54 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:03:30 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:03:29 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:03:21 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:03:20 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-18 17:03:18 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-18 17:03:10 | Thanthirimale (Malwathu Oya) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-05-18 17:02:52 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.040 |  |
| 2026-05-18 17:02:28 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 17:02:21 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-18 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | -0.100 |  |
| 2026-05-18 17:02:10 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:43 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:29 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:12 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:11 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:00:21 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:00:16 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | -0.100 |  |
| 2026-05-18 17:14:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-18 17:02:21 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-18 16:01:20 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-18 17:04:16 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 17:04:05 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 17:02:28 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 17:05:17 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 17:13:49 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:43 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:03:29 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:04:32 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:04:33 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:03:30 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:00:21 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:05:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:29 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:09:50 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:08:05 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:01:12 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-05-18 17:02:10 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 16:10:20 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-05-18 17:05:06 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:03:54 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:03:21 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:00:16 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:06:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:01:11 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-18 17:16:10 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.018 |  |
| 2026-05-18 17:04:38 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-05-18 17:03:20 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-18 17:03:18 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-18 17:04:51 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.038 |  |
| 2026-05-18 17:02:52 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.040 |  |
| 2026-05-18 17:07:27 | Galgamuwa (Mee Oya) | 1.70 | 🟢 Normal | -0.046 |  |
| 2026-05-18 17:03:10 | Thanthirimale (Malwathu Oya) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-05-18 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)