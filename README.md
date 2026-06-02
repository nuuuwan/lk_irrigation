# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_04:39:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 04:39:14 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 04:33:52 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 04:33:46 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:26:21 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:21:48 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-06-03 04:21:30 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:15:06 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-06-03 04:12:21 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-03 04:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-03 04:08:57 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 04:08:20 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:07:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-06-03 04:07:01 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:06:47 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-03 04:06:44 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-03 04:05:45 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:05:27 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:05:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:04:34 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:50 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:21 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:20 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:18 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:10 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.345 |  |
| 2026-06-03 04:02:49 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-06-03 04:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:02:21 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-03 04:01:49 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:38 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.130 |  |
| 2026-06-03 04:01:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-03 04:01:24 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -0.861 |  |
| 2026-06-03 04:01:12 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-03 04:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:00 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:00:58 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:00:45 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-03 03:58:49 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:57:57 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.345 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 04:12:21 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-03 04:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-03 04:06:47 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-03 04:01:12 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-03 04:00:45 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-03 04:08:57 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 04:33:52 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 04:39:14 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 04:05:27 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:21:30 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:13:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:05:11 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:33:46 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:21 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:08:20 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:03:31 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:00 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:01:49 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:04:34 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:07:01 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-03 04:26:21 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:05:05 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-06-03 04:01:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-03 04:02:21 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-03 03:08:02 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-06-03 04:15:06 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.023 |  |
| 2026-06-03 04:07:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-06-03 04:02:49 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-06-03 04:21:48 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-06-03 04:01:38 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.130 |  |
| 2026-06-03 04:03:10 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.345 |  |
| 2026-06-03 04:01:24 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -0.861 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)