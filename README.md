# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_12:12:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 12:12:57 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-07-04 12:08:50 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:08:36 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:08:35 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 12:08:31 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-07-04 12:07:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:49 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.204 |  |
| 2026-07-04 12:06:44 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:14 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-07-04 12:06:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:03 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:05:29 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.110 |  |
| 2026-07-04 12:05:25 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-07-04 12:05:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 12:05:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.038 |  |
| 2026-07-04 12:04:32 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:04:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 12:04:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:04:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 12:03:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-04 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:17 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-07-04 12:03:16 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 12:03:08 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-07-04 12:03:08 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 12:03:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 12:02:50 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 12:02:35 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 12:01:48 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 12:01:45 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:32 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-07-04 12:01:32 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 11:54:34 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 12:06:14 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-07-04 12:05:25 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-07-04 12:01:48 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 12:04:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 12:03:16 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-07-04 12:01:50 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-04 12:03:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-04 12:05:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 12:03:08 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 12:08:35 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 12:02:50 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 12:03:02 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 12:04:21 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 12:02:35 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:44 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:07:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:08:50 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:03 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:04:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:32 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:08:36 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:45 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:04:32 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:03:08 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-07-04 12:08:31 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-07-04 12:12:57 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-07-04 12:03:17 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.019 |  |
| 2026-07-04 12:05:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.038 |  |
| 2026-07-04 12:01:32 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-07-04 12:05:29 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.110 |  |
| 2026-07-04 12:06:49 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)