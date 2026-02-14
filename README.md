# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_19:10:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 19:10:59 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-14 19:10:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:46 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:36 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:07:23 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-14 19:06:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:06:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:06:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:05:48 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:05:37 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-14 19:05:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:05:14 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-02-14 19:04:58 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:04:35 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-14 19:04:32 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:44 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.685 |  |
| 2026-02-14 19:03:43 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 19:03:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:21 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-14 19:03:01 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-02-14 19:02:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:02:27 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 19:02:20 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:02:07 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:02:05 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-02-14 19:01:51 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:47 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:47 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:32 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:06 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.025 |  |
| 2026-02-14 19:00:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 19:00:22 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:00:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 19:04:35 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-14 19:00:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-14 19:07:23 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-14 19:03:43 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 19:05:37 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-14 19:10:59 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-14 19:00:18 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 19:02:27 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 19:02:20 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:32 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:04:32 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:05:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:00:22 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:46 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:06:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:47 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:47 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:01:51 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:02:48 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:05:48 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:06:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:03:41 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:02:07 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:36 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:04:58 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:06:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-02-14 19:02:05 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-02-14 19:03:01 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-02-14 19:03:21 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-14 19:05:14 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2026-02-14 19:01:06 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.025 |  |
| 2026-02-14 19:03:44 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.685 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)