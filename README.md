# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_07:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 07:17:29 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:13:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.070 |  |
| 2026-05-26 07:11:26 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-26 07:09:33 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.018 |  |
| 2026-05-26 07:09:12 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-26 07:09:04 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-05-26 07:08:50 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.054 |  |
| 2026-05-26 07:06:46 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 07:05:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:05:54 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 07:05:46 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.037 |  |
| 2026-05-26 07:05:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 07:05:07 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-05-26 07:04:55 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-26 07:04:54 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 07:04:08 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-26 07:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -7.200 |  |
| 2026-05-26 07:03:50 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:03:39 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-26 07:03:34 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:03:26 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 07:03:25 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 07:03:12 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.154 |  |
| 2026-05-26 07:03:01 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -7.200 |  |
| 2026-05-26 07:02:58 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.069 |  |
| 2026-05-26 07:02:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.117 |  |
| 2026-05-26 07:02:37 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:22 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 07:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:01:38 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:01:36 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.032 |  |
| 2026-05-26 07:01:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.018 |  |
| 2026-05-26 07:00:56 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:00:20 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 07:13:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.070 |  |
| 2026-05-26 07:09:12 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-26 07:09:04 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-05-26 07:03:26 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 07:03:39 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-26 06:00:45 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-26 07:11:26 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-26 07:05:54 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-26 07:02:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-26 07:04:54 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 07:06:46 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 07:03:25 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 07:05:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 07:02:37 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:17:29 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:01:38 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:05:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 06:05:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:00:20 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:00:56 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:03:50 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:03:34 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:02:22 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 07:04:55 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-05-26 07:05:07 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-05-26 06:04:02 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.014 |  |
| 2026-05-26 07:09:33 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.018 |  |
| 2026-05-26 07:01:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.018 |  |
| 2026-05-26 07:04:08 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-05-26 07:01:36 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.032 |  |
| 2026-05-26 07:05:46 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.037 |  |
| 2026-05-26 07:08:50 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.054 |  |
| 2026-05-26 07:02:58 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.069 |  |
| 2026-05-26 07:02:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.117 |  |
| 2026-05-26 07:03:12 | Deraniyagala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.154 |  |
| 2026-05-26 07:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -7.200 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)