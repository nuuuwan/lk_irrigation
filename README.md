# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_15:14:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 15:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.027 |  |
| 2026-04-15 15:12:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:12:20 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:09:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:08:27 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.088 |  |
| 2026-04-15 15:07:11 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:07:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.022 |  |
| 2026-04-15 15:06:36 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:05:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.300 |  |
| 2026-04-15 15:05:05 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:04:58 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-15 15:04:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:04:42 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:04:38 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:04:29 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:03:58 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-04-15 15:03:31 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.055 |  |
| 2026-04-15 15:03:24 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-15 15:03:01 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 15:03:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:59 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:02:51 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:37 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-15 15:02:35 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-15 15:02:12 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:02:12 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:09 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:08 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:05 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.117 |  |
| 2026-04-15 15:01:55 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:01:53 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.024 |  |
| 2026-04-15 15:01:46 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 15:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:26 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:01:25 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:17 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 15:00:43 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.041 |  |
| 2026-04-15 15:00:41 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:00:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 14:40:55 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.300 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 15:02:37 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-15 15:02:35 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-15 15:03:01 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 15:01:46 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 15:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 15:07:11 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:12 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:09:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:51 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:17 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:04:38 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:12:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:01:25 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:02:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:04:29 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-15 15:04:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:08 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:00:41 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:01:55 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:03:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:09 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-15 15:02:59 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:01:26 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:02:12 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-04-15 15:06:36 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:04:42 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:05:05 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-04-15 15:03:24 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-15 15:03:58 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-04-15 15:04:58 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-15 15:07:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.022 |  |
| 2026-04-15 15:01:53 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.024 |  |
| 2026-04-15 15:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.027 |  |
| 2026-04-15 15:00:43 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.041 |  |
| 2026-04-15 15:03:31 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.055 |  |
| 2026-04-15 15:08:27 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.088 |  |
| 2026-04-15 15:02:05 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.117 |  |
| 2026-04-15 15:05:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)