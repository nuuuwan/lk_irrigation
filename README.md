# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_07:36:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,645 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 07:36:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:27:13 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-05-21 07:14:28 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:12:56 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:10:02 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.080 |  |
| 2026-05-21 07:08:52 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-21 07:08:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:08:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-05-21 07:08:00 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:07:21 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 07:04:49 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:43 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:39 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 07:04:34 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:30 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-05-21 07:04:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:03:39 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-21 07:03:23 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:09 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:07 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:02 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:00 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:46 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.148 |  |
| 2026-05-21 07:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.161 |  |
| 2026-05-21 07:02:30 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-05-21 07:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-05-21 07:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:01:54 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 07:01:53 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 07:01:51 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:01:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-05-21 07:01:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:01:12 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-05-21 07:00:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:00:51 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:00:40 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.061 |  |
| 2026-05-21 07:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.023 |  |
| 2026-05-21 07:00:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:00:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 07:07:21 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 07:04:13 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:00:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:00:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 07:04:39 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 07:01:54 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 07:01:53 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 07:03:02 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:30 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:34 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:07 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:01:51 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:00:51 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:12:56 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:09 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:23 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:03:00 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:49 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:36:29 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:14:28 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:08:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:04:43 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:46 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:01:34 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 07:02:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-05-21 07:01:12 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-05-21 07:08:16 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.009 |  |
| 2026-05-21 07:08:52 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-21 07:03:39 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-05-21 07:04:30 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-05-21 07:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-05-21 07:27:13 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.023 |  |
| 2026-05-21 06:12:11 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-05-21 07:01:41 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.051 |  |
| 2026-05-21 07:00:40 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.061 |  |
| 2026-05-21 07:10:02 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.080 |  |
| 2026-05-21 07:02:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.148 |  |
| 2026-05-21 07:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)