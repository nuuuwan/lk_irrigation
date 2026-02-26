# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_08:05:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,380 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 08:05:46 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:05:36 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 08:05:28 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-02-26 08:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:04:33 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 08:03:17 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:03:16 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.102 |  |
| 2026-02-26 08:03:12 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-02-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:57 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-02-26 08:02:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:44 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:42 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-02-26 08:02:40 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.101 |  |
| 2026-02-26 08:02:36 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:18 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:15 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.048 |  |
| 2026-02-26 08:02:14 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.061 |  |
| 2026-02-26 08:02:09 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-02-26 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:43 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-02-26 08:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:29 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-02-26 08:01:24 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 08:01:24 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:19 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.040 |  |
| 2026-02-26 08:01:11 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 07:15:02 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-02-26 07:14:43 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.013 |  |
| 2026-02-26 07:11:50 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 07:11:19 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 07:02:00 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-02-26 08:04:33 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-26 08:01:24 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 08:05:36 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 08:01:36 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:24 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:06 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:03:17 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 07:06:11 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:44 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 07:04:54 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-26 07:07:03 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:14 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:01:11 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:05:46 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:36 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:02:18 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-26 08:05:28 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-02-26 08:01:43 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-02-26 07:01:53 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-26 07:00:22 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.010 |  |
| 2026-02-26 08:02:09 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-02-26 08:01:29 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-02-26 07:02:30 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-02-26 08:02:42 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-02-26 08:02:57 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.019 |  |
| 2026-02-26 08:03:12 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-02-26 07:03:10 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | -0.029 |  |
| 2026-02-26 08:01:19 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.040 |  |
| 2026-02-26 08:02:15 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.048 |  |
| 2026-02-26 07:11:19 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.049 |  |
| 2026-02-26 03:03:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-02-26 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.061 |  |
| 2026-02-26 08:02:40 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.101 |  |
| 2026-02-26 08:03:16 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)