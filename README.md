# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_21:11:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 21:11:27 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-01 21:10:04 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:08:58 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 21:07:20 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-01 21:06:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:06:12 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-02-01 21:06:01 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:05:57 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.052 |  |
| 2026-02-01 21:05:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-01 21:05:26 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-02-01 21:05:11 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-01 21:04:57 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 21:04:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-02-01 21:04:03 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-02-01 21:03:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:03:43 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:03:19 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-01 21:03:16 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 21:03:15 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-01 21:02:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:53 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-01 21:02:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:33 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:15 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:15 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 21:02:06 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:01:59 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-02-01 21:01:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:01:46 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 21:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 21:00:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:00:17 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:00:16 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-01 20:59:55 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 20:34:07 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 21:04:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-02-01 21:05:50 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-01 21:03:15 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-01 21:07:20 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 21:08:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 21:03:19 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-01 21:02:15 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 21:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 21:04:57 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-01 20:59:55 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 21:03:16 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 21:01:46 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 20:06:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 21:02:33 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:00:17 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:06 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:10:04 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:15 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:08:58 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:06:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:01:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:02:59 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:03:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:03:43 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:00:21 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:06:01 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:11:27 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-02-01 21:00:16 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 21:02:53 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-02-01 21:05:11 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.019 |  |
| 2026-02-01 21:01:59 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-02-01 21:06:12 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-02-01 21:05:26 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 21:05:57 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)