# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_16:23:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,905 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **71** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 16:23:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:17:50 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.017 |  |
| 2026-02-05 16:15:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:15:32 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:14:50 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:47 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:45 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:43 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:40 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:37 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:35 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:33 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:31 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:29 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:27 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:22 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:19 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:16 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:13 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:07 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:05 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:14:01 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:54 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:52 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:47 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:44 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:42 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:39 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:36 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:33 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:30 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:27 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:21 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:15 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:13 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:06 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:13:00 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:10:14 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:09:35 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-05 16:09:08 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 16:06:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 16:06:23 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-02-05 16:06:18 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:06:06 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:05:58 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-02-05 16:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:04:39 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:04:24 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:03:21 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-05 16:03:10 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:03:03 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 16:02:55 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.019 |  |
| 2026-02-05 16:02:45 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:39 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:26 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:02:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:09 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:09 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-05 16:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-05 16:01:21 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-05 16:01:11 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:00:55 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 16:14:50 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 96.000 | 🔺 Rising |
| 2026-02-05 16:03:21 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 16:01:21 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-02-05 16:09:35 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 16:02:09 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-05 16:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-05 16:06:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 16:03:03 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 16:09:08 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-05 15:04:06 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.003 |  |
| 2026-02-05 16:06:18 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:15:34 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:23:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:39 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:45 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:28 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:04:39 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:09 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:04:24 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:10:14 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:02:19 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 16:01:11 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 16:06:06 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:02:26 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:03:10 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-05 16:17:50 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.017 |  |
| 2026-02-05 16:02:55 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.019 |  |
| 2026-02-05 16:00:55 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-02-05 16:06:23 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-02-05 16:05:58 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)