# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_04:05:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 04:05:56 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-05 04:05:33 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:04:40 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:04:13 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 04:03:49 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 04:03:41 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:03:12 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 04:02:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-05 04:02:09 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:02:08 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-05 04:02:00 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.377 |  |
| 2026-01-05 04:01:45 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:01:41 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 04:01:15 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 04:00:59 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:20:19 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-01-05 03:19:13 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-01-05 03:13:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:10:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:09:01 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-01-05 03:08:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 02:17:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-05 04:02:08 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-05 04:02:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-05 03:04:19 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 04:01:41 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 04:03:12 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-04 18:04:42 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-05 04:03:49 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 03:05:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 04:01:15 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 04:04:13 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 04:03:41 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:01:45 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:02:50 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:03:10 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:13:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:04:40 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:00:59 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:04:50 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:02:09 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 00:02:57 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:08:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 04:05:33 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 18:02:32 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:10:40 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:07:10 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-05 03:19:13 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.008 |  |
| 2026-01-05 03:01:07 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-05 03:04:28 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-05 04:05:56 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-05 03:01:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.014 |  |
| 2026-01-05 03:20:19 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-01-05 02:08:26 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.028 |  |
| 2026-01-05 03:09:01 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-01-04 18:15:36 | Galgamuwa (Mee Oya) | 2.40 | 🟢 Normal | -0.048 |  |
| 2026-01-05 04:02:00 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.377 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)