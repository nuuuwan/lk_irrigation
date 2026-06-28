# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_12:09:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 12:09:22 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:08:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:08:48 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.099 |  |
| 2026-06-28 12:08:07 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:07:26 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:07:08 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 12:06:26 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-28 12:05:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-06-28 12:05:19 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:05:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:05:07 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:04:48 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.021 |  |
| 2026-06-28 12:04:46 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:04:02 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:03:54 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:03:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-28 12:03:37 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:03:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:03:12 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-28 12:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-28 12:03:11 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 12:02:43 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 12:02:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-06-28 12:02:17 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 12:02:13 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-06-28 12:02:10 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:02:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:01:59 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.228 |  |
| 2026-06-28 12:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:21 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.005 |  |
| 2026-06-28 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-06-28 12:01:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:01:09 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:00:56 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-28 12:00:24 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 11:26:10 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 12:02:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 20.571 | 🔺 Rising |
| 2026-06-28 12:06:26 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-28 12:03:54 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-28 11:15:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-28 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-28 12:03:11 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-28 12:07:08 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 12:02:43 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 12:02:10 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:07:26 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:05:07 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:04:02 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:05:19 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:08:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:05:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:08:07 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:03:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:02:17 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:09 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:00:24 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:21 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 12:01:18 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.005 |  |
| 2026-06-28 12:01:57 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:04:46 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:02:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:09:22 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:01:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:03:37 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-06-28 12:03:54 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-06-28 11:26:10 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-06-28 12:03:11 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-06-28 12:03:12 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-28 12:04:48 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.021 |  |
| 2026-06-28 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-06-28 12:05:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-06-28 12:00:56 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-28 12:08:48 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.099 |  |
| 2026-06-28 12:01:59 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)