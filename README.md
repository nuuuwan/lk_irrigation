# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_04:22:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 04:22:49 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-08 04:07:42 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:32 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:06:36 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-02-08 04:05:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-08 04:05:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:56 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:23 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-02-08 04:03:28 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:03:27 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.002 |  |
| 2026-02-08 04:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:03:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 |  |
| 2026-02-08 04:02:57 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-08 04:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:02:31 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-02-08 04:02:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:02:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:01:51 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.414 |  |
| 2026-02-08 04:01:27 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-02-08 04:01:05 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:00:49 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:00:37 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:00:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-08 03:59:23 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:58:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-08 03:49:41 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-08 04:22:49 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-08 04:05:58 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-08 02:38:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-08 03:58:32 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-08 04:02:57 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-08 04:00:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-08 03:05:59 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-08 04:03:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 |  |
| 2026-02-08 03:59:23 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:00:37 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:02:31 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:02:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:56 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:42 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:01:05 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:32 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:00:49 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:23 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:05:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:07:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:04:23 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:02:29 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:03:28 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 04:03:27 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.002 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-08 03:12:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:11:57 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-02-08 04:06:36 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:06:01 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-08 04:04:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-02-08 02:11:27 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-02-08 04:02:31 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-08 04:01:27 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.040 |  |
| 2026-02-08 03:05:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-02-08 04:01:51 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.414 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)