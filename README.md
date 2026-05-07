# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_16:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,407 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 16:03:06 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.100 |  |
| 2026-05-07 16:03:05 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-07 16:03:01 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:51 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:32 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:27 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.056 |  |
| 2026-05-07 16:02:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 16:01:59 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-07 16:01:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:07 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:03 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:00:58 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:25 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 15:19:44 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.056 |  |
| 2026-05-07 15:12:34 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 16:03:05 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-07 15:05:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-07 16:01:59 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-07 15:03:17 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 16:02:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 15:01:00 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 15:00:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 16:00:25 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 15:01:20 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-07 15:03:53 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-07 15:05:14 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 15:12:34 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-07 16:02:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 15:01:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:02:09 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:51 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:01:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:04:14 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:03 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:05:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:08:59 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:07 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 15:04:28 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:32 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-07 15:01:56 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:58 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:03:01 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 15:02:34 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-05-07 15:05:17 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-05-07 15:06:42 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-07 15:05:00 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.042 |  |
| 2026-05-07 15:00:19 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.044 |  |
| 2026-05-07 16:02:27 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.056 |  |
| 2026-05-07 15:05:01 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.076 |  |
| 2026-05-07 16:03:06 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)