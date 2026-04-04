# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_04:23:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 04:23:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-04-05 04:23:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.015 |  |
| 2026-04-05 04:17:39 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.032 |  |
| 2026-04-05 04:12:00 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-05 04:11:06 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-04-05 04:10:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:07:04 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:04:45 | Rathnapura (Kalu Ganga) | 8.99 | 🟠 Minor Flood | 8.371 | 🔺 Rising |
| 2026-04-05 04:04:22 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-04-05 04:04:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-05 04:04:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-04-05 04:04:00 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:03:55 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:03:32 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:03:29 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-05 04:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-04-05 04:03:12 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-05 04:03:11 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-04-05 04:03:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-05 04:03:04 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.063 |  |
| 2026-04-05 04:02:30 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:02:18 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 04:02:18 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-05 04:02:09 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:01:42 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:01:36 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 04:01:34 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 04:01:32 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:01:28 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.095 |  |
| 2026-04-05 04:01:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 04:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:00:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 04:04:45 | Rathnapura (Kalu Ganga) | 8.99 | 🟠 Minor Flood | 8.371 | 🔺 Rising |
| 2026-04-05 03:09:29 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 1854.000 | 🔺 Rising |
| 2026-04-05 04:23:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-04-05 04:03:29 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-05 04:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-05 04:04:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-05 04:12:00 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-05 04:01:36 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 04:01:34 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 04:01:13 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 04:00:29 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:10:39 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:01:42 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:03:32 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 03:05:32 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:02:30 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:07:04 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:01:32 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:02:09 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-05 04:03:55 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:04:00 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:02:18 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 04:03:12 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-04-05 04:23:16 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.015 |  |
| 2026-04-05 04:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-04-05 04:04:22 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-04-05 04:02:18 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 03:01:43 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-05 04:03:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-05 04:11:06 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 04:17:39 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | -0.032 |  |
| 2026-04-05 04:04:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-04-05 04:03:11 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 04:03:04 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.063 |  |
| 2026-04-05 04:01:28 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)