# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_12:06:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 12:06:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-07 12:06:16 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-07 12:06:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:06:13 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.072 |  |
| 2026-05-07 12:06:00 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | 1.136 | 🔺 Rising |
| 2026-05-07 12:05:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 12:05:41 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.072 |  |
| 2026-05-07 12:04:54 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.067 |  |
| 2026-05-07 12:04:40 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.086 |  |
| 2026-05-07 12:04:15 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.019 |  |
| 2026-05-07 12:04:09 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.185 |  |
| 2026-05-07 12:04:05 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:56 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:47 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-05-07 12:03:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-07 12:03:15 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 12:03:15 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-07 12:03:13 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:12 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:02:54 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.091 |  |
| 2026-05-07 12:02:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.029 |  |
| 2026-05-07 12:02:46 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-07 12:02:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-07 12:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-07 12:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-05-07 12:01:52 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:45 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 12:01:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:33 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 12:01:25 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:18 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 12:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:00:51 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.087 |  |
| 2026-05-07 11:20:35 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:14:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 1.136 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 12:06:00 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | 1.136 | 🔺 Rising |
| 2026-05-07 12:03:42 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-07 12:02:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-07 12:01:45 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 12:06:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-07 12:05:43 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 12:01:33 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 12:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-07 12:02:46 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-07 12:03:15 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 12:01:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:41 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:20:35 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:13 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:56 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:53 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:52 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:03:12 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:06:13 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:25 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:04:05 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 12:01:18 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 12:06:16 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:04:10 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-07 12:03:47 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-05-07 12:04:15 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.019 |  |
| 2026-05-07 12:02:50 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.029 |  |
| 2026-05-07 11:06:23 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2026-05-07 12:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.030 |  |
| 2026-05-07 12:03:15 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.040 |  |
| 2026-05-07 11:06:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.048 |  |
| 2026-05-07 12:04:54 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.067 |  |
| 2026-05-07 12:05:41 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.072 |  |
| 2026-05-07 12:06:13 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.072 |  |
| 2026-05-07 12:04:40 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.086 |  |
| 2026-05-07 12:00:51 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.087 |  |
| 2026-05-07 12:02:54 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.091 |  |
| 2026-05-07 12:04:09 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)