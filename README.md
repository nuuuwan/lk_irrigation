# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_14:27:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 14:27:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-05 14:23:58 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:18:53 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.106 |  |
| 2026-04-05 14:14:10 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.037 |  |
| 2026-04-05 14:10:52 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:10:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:09:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:07:50 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-04-05 14:07:46 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-04-05 14:07:40 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2026-04-05 14:07:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:06:56 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2026-04-05 14:06:42 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 14:05:27 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.009 |  |
| 2026-04-05 14:04:40 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-05 14:04:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:04:08 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.070 |  |
| 2026-04-05 14:03:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:03:48 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:03:43 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-05 14:03:28 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:03:27 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:03:14 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-05 14:03:11 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-05 14:02:54 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:02:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-05 14:02:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.124 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 14:04:40 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-05 14:02:26 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-05 14:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-05 14:27:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-05 14:02:49 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-05 14:00:38 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 14:06:42 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 14:01:32 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 14:02:08 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:13:26 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:00:50 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:10:52 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:10:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:02:54 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:03:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:23:58 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:03:28 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:04:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:01:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:07:40 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-05 14:07:46 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-04-05 14:05:27 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.009 |  |
| 2026-04-05 14:03:27 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:03:48 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:09:07 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:07:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-05 14:07:50 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-04-05 14:03:43 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-05 14:02:03 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-05 14:03:11 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-05 14:03:14 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-05 14:06:56 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.028 |  |
| 2026-04-05 14:01:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-04-05 14:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.036 |  |
| 2026-04-05 14:14:10 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.037 |  |
| 2026-04-05 14:04:08 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.070 |  |
| 2026-04-05 14:01:10 | Thanthirimale (Malwathu Oya) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-04-05 14:18:53 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.106 |  |
| 2026-04-05 14:01:54 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)