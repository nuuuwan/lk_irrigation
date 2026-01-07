# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_14:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 14:18:30 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:17:43 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:10:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-07 14:09:47 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:09:38 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:08:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:06:50 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:06:10 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:05:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:05:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.171 |  |
| 2026-01-07 14:05:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:05:04 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-01-07 14:04:40 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:03:52 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:03:47 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-07 14:03:30 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:03:09 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:03:00 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-01-07 14:02:51 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.092 |  |
| 2026-01-07 14:02:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 14:02:09 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-01-07 14:02:09 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 14:02:08 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-01-07 14:02:06 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:02:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-07 14:01:53 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-07 14:01:50 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:37 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-07 14:01:33 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-07 14:01:23 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | -0.040 |  |
| 2026-01-07 14:01:23 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:01:22 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:00:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-07 14:00:09 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-01-07 13:30:20 | Horowpothana (Yan Oya) | 2.66 | 🟢 Normal | -0.092 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 14:02:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-07 14:00:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-07 14:01:53 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-07 14:03:47 | Padiyathalawa (Maduru Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-07 14:01:33 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-07 14:02:09 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 14:06:50 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:02:06 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:02:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:09:38 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:09:47 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:03:52 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:03:30 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:04:40 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:06:10 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:01:22 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:18:30 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:05:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:08:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:17:43 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:01:23 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:05:04 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-01-07 14:05:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:50 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:03:09 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-07 14:01:37 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-01-07 14:10:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-07 14:03:00 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-01-07 13:02:41 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-07 14:02:09 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-01-07 14:00:09 | Siyambalanduwa (Heda Oya) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-01-07 14:02:08 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-01-07 13:10:18 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.036 |  |
| 2026-01-07 14:01:23 | Weraganthota (Mahaweli Ganga) | -1.11 | 🟢 Normal | -0.040 |  |
| 2026-01-07 14:02:51 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | -0.092 |  |
| 2026-01-07 14:05:22 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)