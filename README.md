# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_00:09:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,649 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 00:09:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-06-05 00:08:55 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-05 00:07:46 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 00:07:10 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-05 00:06:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-06-05 00:05:59 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-05 00:05:50 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 00:05:42 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.005 |  |
| 2026-06-05 00:05:41 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:05:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-05 00:05:09 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 00:05:02 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-05 00:04:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 00:04:37 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 00:04:27 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:03:33 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.090 |  |
| 2026-06-05 00:03:30 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 00:03:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:03:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:55 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-06-05 00:02:32 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:29 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 00:02:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:18 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 00:02:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-06-05 00:02:17 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:36:57 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-06-04 23:24:57 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:39 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:21 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 00:02:55 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-06-05 00:07:10 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-05 00:08:55 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-05 00:03:30 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-04 23:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 00:07:46 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-05 00:05:59 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-05 00:02:18 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 00:04:37 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-05 00:02:29 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 00:04:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 00:05:09 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-05 00:05:50 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 00:05:42 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.005 |  |
| 2026-06-05 00:05:41 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:03:23 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:23:39 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:17:16 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 23:24:57 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:19 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:05:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:03:24 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:32 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:02:17 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:04:27 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-05 00:05:02 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-05 00:02:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-06-05 00:09:49 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-06-05 00:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-05 00:06:35 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-06-04 22:10:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.037 |  |
| 2026-06-05 00:03:33 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)