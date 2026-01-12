# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_07:24:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 07:24:15 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:19:49 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-12 07:15:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.017 |  |
| 2026-01-12 07:12:23 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:11:39 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:11:19 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.084 |  |
| 2026-01-12 07:11:12 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-12 07:10:46 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:08:19 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.170 |  |
| 2026-01-12 07:08:14 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:07:16 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-01-12 07:06:47 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-12 07:06:38 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:29 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-01-12 07:05:21 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.043 |  |
| 2026-01-12 07:04:49 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-12 07:04:11 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-01-12 07:04:04 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:04:03 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:04:02 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 07:04:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.128 |  |
| 2026-01-12 07:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 07:02:49 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 07:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2026-01-12 07:02:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:02:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:02:19 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:02:04 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-01-12 07:01:36 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:01:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:01:20 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:01:17 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:01:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-12 06:59:22 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:37:10 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 07:06:47 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-12 07:19:49 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-12 07:02:49 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 07:04:02 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 07:04:49 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-12 07:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 06:10:52 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 07:01:36 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:01:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 06:02:30 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:08:14 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:24:15 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:11:39 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:01:20 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:04:04 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:06:38 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:12:23 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:04:03 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:05:29 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:10:46 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:02:30 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 07:02:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:01:09 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:02:19 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:01:17 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-12 07:11:12 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-12 07:15:44 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.017 |  |
| 2026-01-12 07:04:11 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-01-12 07:02:04 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-01-12 06:03:36 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.029 |  |
| 2026-01-12 07:05:28 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.038 |  |
| 2026-01-12 07:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2026-01-12 07:05:21 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.043 |  |
| 2026-01-12 07:07:16 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-01-12 07:11:19 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.084 |  |
| 2026-01-12 07:04:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.128 |  |
| 2026-01-12 07:08:19 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)