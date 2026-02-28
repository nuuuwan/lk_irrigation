# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_11:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 11:11:26 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-28 11:11:10 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:10:19 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:09:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:08:01 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:30 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:06:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:06:49 | Pitabeddara (Nilwala Ganga) | -0.32 | 🟢 Normal | -0.632 |  |
| 2026-02-28 11:06:47 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-02-28 11:06:34 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:06:05 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:06:03 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:05:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:46 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:43 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:39 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:04:48 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:04:39 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:04:32 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:03:51 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:03:49 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:03:20 | Dunamale (Aththanagalu Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:03:13 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-28 11:03:10 | Manampitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-28 11:03:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-02-28 11:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-28 11:02:02 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:01:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-28 11:01:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:01:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-28 11:00:59 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:00:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:00:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 11:02:07 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-02-28 11:03:10 | Manampitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-28 11:01:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-28 11:11:26 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-28 11:04:48 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:01:26 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:04:32 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:03:20 | Dunamale (Aththanagalu Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 11:00:59 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:03:51 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:00:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:00:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:06:54 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-28 10:07:58 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:03:49 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:02:02 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:08:01 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:39 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-28 10:05:40 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:43 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:46 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:05:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:09:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:30 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:10:19 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-28 11:11:10 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:06:05 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:06:34 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:04:39 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-28 11:06:03 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-28 10:00:58 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-02-28 11:01:43 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-02-28 11:03:13 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-02-28 11:06:47 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-02-28 11:03:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-02-28 11:06:49 | Pitabeddara (Nilwala Ganga) | -0.32 | 🟢 Normal | -0.632 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)