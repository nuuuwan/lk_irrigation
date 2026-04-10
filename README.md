# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_15:18:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,376 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 15:18:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 15:16:34 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:13:41 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-10 15:12:18 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:12:09 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.073 |  |
| 2026-04-10 15:08:21 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:59 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:29 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:18 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:05:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-10 15:05:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:05:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-10 15:05:05 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:05:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 15:04:46 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-04-10 15:04:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:16 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:03:58 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.073 |  |
| 2026-04-10 15:03:57 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 15:03:43 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:03:36 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:03:28 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.031 |  |
| 2026-04-10 15:03:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-04-10 15:02:48 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-10 15:02:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:02:34 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 15:02:16 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:02:11 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.049 |  |
| 2026-04-10 15:02:10 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:02:05 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:52 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:42 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-10 15:01:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:38 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.088 |  |
| 2026-04-10 15:01:04 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-10 15:01:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:00:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 15:13:41 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-10 15:05:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-10 15:01:42 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-10 15:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-10 15:18:37 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-10 15:02:34 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 15:05:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 15:05:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-10 15:02:36 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:02:10 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:12:18 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:18 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:08:21 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:16:34 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:16 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:00 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:00:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:05:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:05:05 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:04 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:02:48 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:06:59 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:03:36 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:01:52 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-10 15:04:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:03:43 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:02:16 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-10 15:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-10 15:04:46 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-04-10 15:03:57 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 15:03:28 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.031 |  |
| 2026-04-10 15:03:19 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-04-10 15:02:11 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.049 |  |
| 2026-04-10 15:12:09 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | -0.073 |  |
| 2026-04-10 15:01:38 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)