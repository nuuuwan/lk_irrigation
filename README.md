# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_19:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 19:22:58 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.080 |  |
| 2026-04-18 19:17:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:16:02 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-18 19:13:02 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.035 |  |
| 2026-04-18 19:10:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:07:20 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:06:46 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-18 19:06:28 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:06:23 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:05:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:05:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:05:33 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:05:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.130 |  |
| 2026-04-18 19:05:17 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:04:13 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:02 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:01 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:03:40 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:03:21 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-18 19:03:07 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:54 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:50 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-18 19:02:47 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:37 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:02:32 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-04-18 19:02:21 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.041 |  |
| 2026-04-18 19:01:24 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-18 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:01:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:01:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-18 19:00:57 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:00:10 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 19:06:46 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-18 19:01:24 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-18 19:03:21 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-18 19:03:07 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:17:52 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:13 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:10:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:01:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:05:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:54 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:01 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:06:28 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:00:57 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:02 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:47 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:05:46 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:07:20 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:03:40 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:02:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-18 19:06:23 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:05:33 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:02:37 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:05:17 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-18 19:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-18 18:01:26 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-18 19:02:32 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.012 |  |
| 2026-04-18 19:01:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-18 19:02:50 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-04-18 19:00:10 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-04-18 19:16:02 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-18 19:13:02 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.035 |  |
| 2026-04-18 19:02:21 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.041 |  |
| 2026-04-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.068 |  |
| 2026-04-18 19:22:58 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.080 |  |
| 2026-04-18 19:05:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)