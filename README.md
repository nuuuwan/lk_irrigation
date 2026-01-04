# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_10:17:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 10:17:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:16:03 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:15:57 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 10:13:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-01-04 10:13:11 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-04 10:12:56 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:09:02 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:06:05 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:05:22 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:05:06 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:54 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:34 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:29 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-01-04 10:04:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.066 |  |
| 2026-01-04 10:04:15 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:14 | Galgamuwa (Mee Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:04:14 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-01-04 10:03:58 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:03:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.095 |  |
| 2026-01-04 10:03:21 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.022 |  |
| 2026-01-04 10:03:14 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:03:14 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:03:08 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-01-04 10:03:02 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:02:58 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 10:02:56 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:02:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:02:04 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:52 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-04 10:01:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:01:42 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:01:34 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-04 10:01:23 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:15 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | -0.021 |  |
| 2026-01-04 10:01:08 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:00 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:00 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:00:37 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-01-04 10:00:12 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 10:01:52 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-04 10:13:11 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-04 10:01:34 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-04 10:15:57 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-04 10:02:58 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 10:16:03 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:02:04 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:06:05 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:05:06 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:17:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:02:50 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:34 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:08 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:23 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:03:58 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:15 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:01:00 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:12:56 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:04:14 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 10:05:22 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:03:02 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:01:42 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:04:14 | Galgamuwa (Mee Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:02:56 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-04 10:03:14 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:01:00 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:03:14 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:00:12 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-01-04 10:01:15 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | -0.021 |  |
| 2026-01-04 10:00:37 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-01-04 10:03:21 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.022 |  |
| 2026-01-04 10:13:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.028 |  |
| 2026-01-04 10:04:29 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-01-04 10:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-01-04 10:04:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.066 |  |
| 2026-01-04 10:03:08 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.070 |  |
| 2026-01-04 10:03:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)