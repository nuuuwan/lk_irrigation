# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_00:50:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,792 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 00:50:53 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 00:50:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:24:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:23:04 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-01 00:22:49 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:17:35 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-01 00:10:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-03-01 00:10:05 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:10:04 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:08:53 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:08:25 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-01 00:07:38 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-01 00:06:45 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:06:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:05:06 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 00:03:44 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-01 00:03:35 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.011 |  |
| 2026-03-01 00:03:32 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-01 00:03:31 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:03:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:26 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 00:02:06 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:52 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:46 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:44 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:35 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:00:16 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 23:56:21 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 00:03:32 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-01 00:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-01 00:02:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-28 18:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-28 23:08:02 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 00:03:44 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-01 00:50:53 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 00:05:06 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 00:23:04 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-01 00:00:16 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 00:02:26 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:17:35 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:07 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:24:21 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:03:24 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:03:31 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:06 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:04:16 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:08:53 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:06:45 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:03:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:10:05 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:50:05 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:44 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:22:49 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 23:04:08 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:35 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:06:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:46 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:02:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:17:10 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 22:59:46 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:01:52 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:10:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-03-01 00:08:25 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-01 00:07:38 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-01 00:03:35 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.011 |  |
| 2026-02-28 23:56:21 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.026 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)