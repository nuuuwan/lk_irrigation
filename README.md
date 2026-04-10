# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_19:14:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,530 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 19:14:38 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-10 19:13:45 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-10 19:08:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:07:51 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-10 19:07:10 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-10 19:06:55 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 19:05:31 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 19:05:30 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-10 19:05:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:04:54 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-10 19:03:55 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 19:03:51 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:03:50 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.049 |  |
| 2026-04-10 19:03:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 19:03:38 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.081 |  |
| 2026-04-10 19:03:32 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:03:28 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-10 19:03:18 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 19:02:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:02:54 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 19:02:17 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:38 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:37 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:01:36 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:01:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-10 19:01:24 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:23 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:17 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 19:00:50 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-04-10 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-10 19:05:30 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-10 19:04:54 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-10 19:13:45 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-10 19:03:28 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-10 19:01:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-10 19:06:55 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 19:01:17 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 19:07:51 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-10 18:01:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 19:03:55 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 19:05:31 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 19:14:38 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-10 19:02:54 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 19:03:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 19:03:18 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 19:00:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:48 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:08:51 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:50 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:03:32 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:02:17 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:00:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:38 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:02:55 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:05:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:23 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:24 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-10 19:01:37 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:03:51 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:01:36 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-10 19:07:10 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-10 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-10 19:00:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-04-10 19:03:50 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.049 |  |
| 2026-04-10 19:03:38 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)