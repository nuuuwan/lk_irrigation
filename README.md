# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_14:06:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 14:06:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 14:06:31 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-04-13 14:06:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:05:45 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.086 |  |
| 2026-04-13 14:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 14:05:17 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:05:08 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.038 |  |
| 2026-04-13 14:04:12 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-04-13 14:04:03 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-04-13 14:03:43 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:03:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-13 14:03:26 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-04-13 14:03:11 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:03:08 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.157 |  |
| 2026-04-13 14:02:53 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-04-13 14:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:02:14 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 14:02:12 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:02:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:02:08 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 14:02:04 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:01:49 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-13 14:01:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.065 |  |
| 2026-04-13 14:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:01:30 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-13 14:01:29 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:01:09 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-13 14:00:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:00:45 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 14:00:39 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:00:29 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 13:20:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-13 13:15:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.106 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 14:04:12 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-04-13 14:03:41 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-13 14:01:49 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-13 14:01:09 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-13 14:01:30 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-13 14:00:29 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 14:05:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-13 14:06:31 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 13:03:33 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 14:02:12 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 14:02:08 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 14:00:45 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 13:10:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 13:05:37 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 14:02:14 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 14:01:37 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:00:39 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:03:43 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:01:29 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:02:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:00:59 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 13:20:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-13 14:06:10 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:03:11 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:02:04 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:05:17 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-13 13:07:39 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-13 14:03:26 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-04-13 14:06:31 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-04-13 14:05:08 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.038 |  |
| 2026-04-13 14:02:53 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-04-13 14:04:03 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.051 |  |
| 2026-04-13 14:01:43 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.065 |  |
| 2026-04-13 14:05:45 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.086 |  |
| 2026-04-13 13:15:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.106 |  |
| 2026-04-13 14:03:08 | Rathnapura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)