# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_16:16:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 16:16:27 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 23.831 | 🔺 Rising |
| 2026-01-07 16:16:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:15:16 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 23.831 | 🔺 Rising |
| 2026-01-07 16:15:01 | Manampitiya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-01-07 16:11:04 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:08:30 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:06:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:06:50 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-07 16:06:02 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:05:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:05:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 16:05:05 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:04:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:04:30 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:04:12 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:04:06 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-07 16:03:55 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | -0.048 |  |
| 2026-01-07 16:03:39 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-07 16:03:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 16:03:34 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:03:04 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:03:04 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 16:03:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 16:03:00 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-01-07 16:02:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-07 16:02:50 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:02:38 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:36 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:02:30 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-07 16:02:24 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:19 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.039 |  |
| 2026-01-07 16:02:15 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:01:57 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:01:31 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-01-07 16:01:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:01:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-07 16:01:00 | Siyambalanduwa (Heda Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-01-07 16:00:59 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 16:16:27 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 23.831 | 🔺 Rising |
| 2026-01-07 16:03:00 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-01-07 16:02:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-07 16:01:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-07 16:03:04 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 16:03:39 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-07 16:03:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 16:03:02 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 16:05:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 16:02:24 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:16:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:04:12 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:11:04 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:01:57 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:06:02 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:38 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:30 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:05:05 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:06:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:02:15 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:03:34 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-07 16:06:50 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-01-07 16:08:30 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:04:30 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:03:04 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:00:59 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:04:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:05:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:01:24 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:02:36 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:02:50 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-07 16:04:06 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-07 16:01:00 | Siyambalanduwa (Heda Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-01-07 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-07 16:15:01 | Manampitiya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-01-07 16:02:19 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.039 |  |
| 2026-01-07 16:03:55 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | -0.048 |  |
| 2026-01-07 16:01:31 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)