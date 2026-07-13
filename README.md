# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_14:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 14:22:21 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |
| 2026-07-13 14:17:34 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-13 14:12:10 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-13 14:10:07 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:09:44 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-07-13 14:08:57 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-07-13 14:08:24 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-13 14:07:57 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-07-13 14:06:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:06:36 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.018 |  |
| 2026-07-13 14:05:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-07-13 14:05:17 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:05:13 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-07-13 14:04:15 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-13 14:03:58 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 14:03:54 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:03:49 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:03:44 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-13 14:03:06 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-07-13 14:02:49 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 14:02:44 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:40 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:35 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:19 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-13 14:01:53 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:53 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:40 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:29 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-07-13 14:01:21 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:17 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-13 14:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:00:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 13:55:02 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 14:01:29 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-07-13 14:08:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-13 14:04:15 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-13 14:02:49 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-13 14:02:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-13 14:03:44 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-13 14:17:34 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-13 14:00:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-13 14:03:58 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 14:01:53 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:40 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:17 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:19 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:03:49 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:19 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:53 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:08:24 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:06:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:44 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:40 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:03:54 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:05:17 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:02:35 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:05:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:10:07 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:01:21 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 14:09:44 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-07-13 14:05:39 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-07-13 14:12:10 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-13 14:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-07-13 14:08:57 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-07-13 14:07:57 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-07-13 14:06:36 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.018 |  |
| 2026-07-13 14:03:06 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-07-13 14:05:13 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-07-13 14:22:21 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)