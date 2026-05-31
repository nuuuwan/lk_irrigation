# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_17:25:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 17:25:55 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.008 |  |
| 2026-05-31 17:11:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:11:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:09:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:08:08 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 17:07:19 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.013 |  |
| 2026-05-31 17:06:59 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.186 |  |
| 2026-05-31 17:06:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-05-31 17:06:30 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:05:59 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-05-31 17:05:53 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:05:08 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.056 |  |
| 2026-05-31 17:05:07 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-05-31 17:05:07 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-31 17:04:42 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:04:30 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:04:18 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.087 |  |
| 2026-05-31 17:03:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:45 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:36 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-05-31 17:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-31 17:03:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.100 |  |
| 2026-05-31 17:02:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:42 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-31 17:02:36 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:36 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:32 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:08 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:01:57 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.059 |  |
| 2026-05-31 17:01:55 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-31 17:01:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:01:03 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:00:58 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 17:00:49 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:00:43 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:50:07 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 17:01:55 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-31 17:05:07 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-31 17:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-31 17:00:58 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 17:00:49 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:11:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:04:30 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:09:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:00:43 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:01:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:06:59 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:32 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:36 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:25:27 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:01:03 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:06:30 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:36 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:51 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:03:45 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:11:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:05:53 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:02:08 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:04:42 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 17:25:55 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.008 |  |
| 2026-05-31 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-05-31 17:08:08 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 17:02:42 | Dunamale (Aththanagalu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-31 17:07:19 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.013 |  |
| 2026-05-31 17:05:07 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-05-31 17:06:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-05-31 17:03:36 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-05-31 17:05:59 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-05-31 17:05:08 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | -0.056 |  |
| 2026-05-31 17:01:57 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.059 |  |
| 2026-05-31 17:04:18 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.087 |  |
| 2026-05-31 17:03:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.100 |  |
| 2026-05-31 17:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)