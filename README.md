# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_06:30:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 06:30:59 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:23:45 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:09:52 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:09:21 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:08:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:08:06 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:07:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:07:02 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:06:49 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.114 |  |
| 2026-02-28 06:05:09 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:04:30 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:04:20 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 06:04:14 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:04:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-02-28 06:03:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:03:42 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:37 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:36 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-02-28 06:03:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:28 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.041 |  |
| 2026-02-28 06:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:02:59 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-28 06:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:02:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:02:36 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.164 |  |
| 2026-02-28 06:02:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-28 06:02:06 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 06:02:03 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:01:59 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.023 |  |
| 2026-02-28 06:01:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-28 06:01:27 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.033 |  |
| 2026-02-28 06:01:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:15 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 06:02:59 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-28 06:01:40 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-28 06:04:20 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 06:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 06:02:06 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 06:01:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:23 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:05:09 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:09:52 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:30:59 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:37 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:42 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:07:25 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:07:02 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:08:06 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:59 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:04:14 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:04 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:28 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:01:15 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:09:21 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:02:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:23:45 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:08:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-28 06:03:44 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:04:30 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:02:03 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-02-28 06:02:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-28 06:01:46 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.023 |  |
| 2026-02-28 06:01:27 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.033 |  |
| 2026-02-28 06:03:36 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-02-28 06:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.041 |  |
| 2026-02-28 06:04:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-02-28 06:06:49 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.114 |  |
| 2026-02-28 06:02:36 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)