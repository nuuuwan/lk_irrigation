# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_13:14:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,728 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 13:14:54 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.016 |  |
| 2026-01-01 13:11:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-01 13:10:09 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:09:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:08:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-01-01 13:08:04 | Siyambalanduwa (Heda Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-01-01 13:07:35 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 13:06:49 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.020 |  |
| 2026-01-01 13:06:33 | Horowpothana (Yan Oya) | 3.21 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-01 13:06:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-01-01 13:05:24 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:05:17 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:04:42 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-01-01 13:04:07 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 13:03:58 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:03:54 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 13:03:26 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-01-01 13:03:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:03:09 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-01 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-01 13:02:55 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.050 |  |
| 2026-01-01 13:02:53 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:49 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:40 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:02:23 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:02:15 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:01:51 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:01:34 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.050 |  |
| 2026-01-01 13:01:20 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.168 |  |
| 2026-01-01 13:01:16 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-01-01 13:01:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-01-01 13:01:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:01:08 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-01 13:01:00 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 13:00:58 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 13:00:07 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 13:06:33 | Horowpothana (Yan Oya) | 3.21 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-01 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-01 13:11:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-01 13:00:58 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-01 13:01:08 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-01 13:03:09 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-01 13:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-01 13:01:00 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 13:07:35 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 13:01:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:49 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:01:51 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:05:17 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:10:09 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:05:24 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:53 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:03:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:02:15 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 13:03:54 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:09:07 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:00:07 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:02:40 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:02:23 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:03:58 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-01 13:01:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-01-01 13:04:42 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2026-01-01 13:08:05 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-01-01 12:08:41 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.013 |  |
| 2026-01-01 13:14:54 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.016 |  |
| 2026-01-01 13:08:04 | Siyambalanduwa (Heda Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-01-01 13:03:26 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-01-01 13:04:07 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-01-01 13:06:49 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.020 |  |
| 2026-01-01 13:01:16 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-01-01 13:06:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-01-01 13:01:34 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.050 |  |
| 2026-01-01 13:02:55 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.050 |  |
| 2026-01-01 13:01:20 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)