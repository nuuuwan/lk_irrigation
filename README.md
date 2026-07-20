# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_19:24:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 19:24:11 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-07-20 19:14:45 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-20 19:13:13 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:09:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-07-20 19:07:57 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-20 19:07:41 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.099 |  |
| 2026-07-20 19:07:03 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-07-20 19:07:00 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-20 19:06:54 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-20 19:06:21 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:05:27 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2026-07-20 19:05:13 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:52 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:46 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:38 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-20 19:04:30 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-07-20 19:04:24 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-20 19:04:12 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:03:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-07-20 19:03:38 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:03:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:02:44 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-20 19:02:21 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 19:02:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:02:09 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:58 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.022 |  |
| 2026-07-20 19:01:54 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:52 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-07-20 19:01:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:00:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 19:01:52 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-07-20 19:04:38 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-20 19:07:00 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-20 19:07:57 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-20 19:02:44 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-20 19:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-20 19:02:21 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 19:14:45 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-20 19:03:38 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:13:13 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:05:13 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:22 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:46 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:00:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:06:21 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:54 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:24 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:12 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:02:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:03:23 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:04:52 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:55 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:24:11 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:01:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:02:09 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-20 19:06:54 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-20 19:09:59 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-07-20 19:05:27 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2026-07-20 19:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-07-20 18:02:09 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-07-20 19:04:30 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-07-20 19:07:03 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-07-20 19:01:58 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.022 |  |
| 2026-07-20 19:03:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-20 19:07:41 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)