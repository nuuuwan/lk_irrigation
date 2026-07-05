# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_06:34:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 06:34:19 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.002 |  |
| 2026-07-05 06:21:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:15:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.131 |  |
| 2026-07-05 06:10:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:10:04 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:49 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.050 |  |
| 2026-07-05 06:09:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:37 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:18 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-07-05 06:08:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-07-05 06:07:33 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-05 06:07:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:06:40 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:06:29 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-07-05 06:06:20 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-07-05 06:06:08 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.017 |  |
| 2026-07-05 06:05:59 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.087 |  |
| 2026-07-05 06:05:53 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.047 |  |
| 2026-07-05 06:05:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:05:18 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.099 |  |
| 2026-07-05 06:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.198 |  |
| 2026-07-05 06:04:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:04:04 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.016 |  |
| 2026-07-05 06:03:58 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.041 |  |
| 2026-07-05 06:03:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:03:35 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-07-05 06:03:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:03:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -18.000 |  |
| 2026-07-05 06:03:27 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.030 |  |
| 2026-07-05 06:03:26 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -18.000 |  |
| 2026-07-05 06:02:49 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:02:47 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-05 06:02:32 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:02:30 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2026-07-05 06:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:01:25 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.181 |  |
| 2026-07-05 06:00:58 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:00:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-05 06:00:24 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.077 |  |
| 2026-07-05 05:58:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.198 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 06:06:20 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-07-05 06:07:33 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-07-05 06:00:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-05 06:02:47 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-05 06:34:19 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.002 |  |
| 2026-07-05 06:10:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:00:48 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:03:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:00:58 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:03:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:10:04 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:45 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:37 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:04:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:05:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:06:40 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:07:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:21:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:02:32 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 06:09:18 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-07-05 06:04:04 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.016 |  |
| 2026-07-05 06:06:08 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.017 |  |
| 2026-07-05 06:08:29 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-07-05 06:03:27 | Ellagawa (Kalu Ganga) | 5.81 | 🟢 Normal | -0.030 |  |
| 2026-07-05 06:03:35 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-07-05 06:06:29 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.031 |  |
| 2026-07-05 06:03:58 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.041 |  |
| 2026-07-05 06:05:53 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.047 |  |
| 2026-07-05 06:09:49 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.050 |  |
| 2026-07-05 06:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.071 |  |
| 2026-07-05 06:00:24 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.077 |  |
| 2026-07-05 06:05:59 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.087 |  |
| 2026-07-05 06:05:18 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.099 |  |
| 2026-07-05 06:15:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.131 |  |
| 2026-07-05 06:01:25 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.181 |  |
| 2026-07-05 06:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.198 |  |
| 2026-07-05 06:03:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)