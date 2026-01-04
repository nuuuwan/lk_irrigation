# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_15:07:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 15:07:52 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-04 15:07:45 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2026-01-04 15:06:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:06:52 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.038 |  |
| 2026-01-04 15:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.066 |  |
| 2026-01-04 15:05:46 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | -0.029 |  |
| 2026-01-04 15:04:46 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-04 15:04:44 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.077 |  |
| 2026-01-04 15:04:31 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-01-04 15:04:24 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-04 15:04:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:04:02 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:03:29 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.060 |  |
| 2026-01-04 15:03:26 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 15:03:07 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:03:01 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:59 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 15:02:50 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-01-04 15:02:45 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-01-04 15:02:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:02:39 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-01-04 15:02:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:29 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:23 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:16 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:00 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.027 |  |
| 2026-01-04 15:01:58 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:54 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:46 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-04 15:01:38 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:16 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:12 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:07 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-01-04 15:00:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:00:44 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:00:36 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 15:04:24 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-04 15:04:46 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-04 15:01:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-04 15:07:52 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-04 15:02:59 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 15:03:26 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 15:00:36 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:58 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:16 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:16 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:54 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:29 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:38 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:23 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:03:07 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:01:50 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:03:01 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:02:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 15:04:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:02:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:04:02 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:06:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:00:44 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:46 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:00:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:12 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-04 15:01:07 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-01-04 15:02:39 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-01-04 15:02:45 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-01-04 15:02:50 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-01-04 15:02:00 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.027 |  |
| 2026-01-04 15:05:46 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | -0.029 |  |
| 2026-01-04 15:04:31 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-01-04 15:06:52 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.038 |  |
| 2026-01-04 15:07:45 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2026-01-04 15:03:29 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.060 |  |
| 2026-01-04 15:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.066 |  |
| 2026-01-04 15:04:44 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)