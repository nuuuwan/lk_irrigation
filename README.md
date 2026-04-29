# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_05:33:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,910 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 05:33:20 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:23:54 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-04-29 05:22:34 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-29 05:16:51 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 05:14:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.017 |  |
| 2026-04-29 05:13:54 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 05:13:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:12:05 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.033 |  |
| 2026-04-29 05:10:57 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:08:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.261 |  |
| 2026-04-29 05:08:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:07:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 05:06:19 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-29 05:06:16 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.096 |  |
| 2026-04-29 05:06:03 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:05:45 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-04-29 05:04:31 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.004 |  |
| 2026-04-29 05:04:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.055 |  |
| 2026-04-29 05:04:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2026-04-29 05:03:28 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:03:15 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-29 05:02:42 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:30 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:29 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-04-29 05:02:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:22 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-29 05:02:16 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-04-29 05:02:14 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:01:25 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:01:13 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.049 |  |
| 2026-04-29 05:00:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-29 05:00:53 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:00:40 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-04-29 05:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:59:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 05:03:15 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-29 05:06:19 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-29 05:02:22 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-29 05:16:51 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 05:07:23 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 05:13:54 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 05:02:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:42 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:08:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:10:57 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:30 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:03:28 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:04:16 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:13:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:06:03 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:33:20 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:02:14 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:04:31 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.004 |  |
| 2026-04-29 05:23:54 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:01:25 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:00:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:00:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-29 05:14:13 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.017 |  |
| 2026-04-29 05:05:45 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-04-29 05:02:29 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-04-29 05:22:34 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-29 05:12:05 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.033 |  |
| 2026-04-29 05:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2026-04-29 05:00:40 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-04-29 05:01:13 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.049 |  |
| 2026-04-29 05:04:24 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.055 |  |
| 2026-04-29 04:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.073 |  |
| 2026-04-29 05:06:16 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.096 |  |
| 2026-04-29 05:08:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.261 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)