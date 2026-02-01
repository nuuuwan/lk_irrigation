# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_15:13:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 15:13:23 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-01 15:11:33 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-01 15:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-02-01 15:07:37 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-01 15:07:37 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:06:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:06:38 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:06:28 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:06:18 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:05:46 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:05:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:04:48 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:28 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:08 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-02-01 15:03:49 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.107 |  |
| 2026-02-01 15:03:44 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 15:03:22 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 15:03:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:09 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-02-01 15:03:08 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:03:05 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:02:35 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-01 15:02:32 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:02:31 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.052 |  |
| 2026-02-01 15:02:30 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:02:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-01 15:02:05 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.056 |  |
| 2026-02-01 15:01:48 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.056 |  |
| 2026-02-01 15:01:48 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:01:35 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:29 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-01 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:09 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:00 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:00:38 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-01 15:00:22 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 15:02:35 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-02-01 15:07:37 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-01 15:01:29 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-01 15:03:44 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 15:00:38 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-01 15:03:22 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 15:01:00 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:35 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:07:37 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:02:30 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:59 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:05 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:01:09 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:05:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:00:22 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:06:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:03:09 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-02-01 15:13:23 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-01 15:11:33 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-01 15:06:18 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:06:38 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:05:46 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:08 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:02:32 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:01:48 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:06:28 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:03:08 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:48 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:04:28 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:02:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-01 15:04:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-02-01 15:08:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-02-01 15:02:31 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.052 |  |
| 2026-02-01 15:02:05 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.056 |  |
| 2026-02-01 15:01:48 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.056 |  |
| 2026-02-01 15:03:49 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)