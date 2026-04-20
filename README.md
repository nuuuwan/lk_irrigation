# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_11:22:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,113 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 11:22:46 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.026 |  |
| 2026-04-20 11:17:17 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-20 11:16:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:12:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-20 11:12:02 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:11:45 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-04-20 11:09:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-04-20 11:09:23 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 11:07:47 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:47 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:45 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:41 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:39 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 11:04:53 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:04:45 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.077 |  |
| 2026-04-20 11:04:15 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:04:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:03:56 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-04-20 11:03:53 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-20 11:03:36 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:03:29 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-20 11:03:16 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:03:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.041 |  |
| 2026-04-20 11:03:00 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-20 11:02:54 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-04-20 11:02:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:02:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:02:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:02:17 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:02:12 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 11:01:43 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-20 11:01:33 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:01:15 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:01:15 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:00:32 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 11:00:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:00:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-20 11:00:07 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.507 |  |
| 2026-04-20 10:58:56 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.507 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 11:02:54 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-04-20 11:01:43 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-20 11:00:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-20 11:03:00 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-20 11:09:23 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 11:06:39 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 11:02:12 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 11:00:32 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 11:17:17 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-20 11:02:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 10:02:31 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:16:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:02:44 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:00:29 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:03:16 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:12:02 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:45 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:03:36 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:04:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:07:47 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:01:15 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:02:49 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:47 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:04:15 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:06:41 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:12:57 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-04-20 11:03:53 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-20 11:03:56 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-04-20 11:09:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-04-20 11:03:29 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-20 11:22:46 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.026 |  |
| 2026-04-20 11:02:17 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:01:33 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:01:15 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2026-04-20 11:03:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.041 |  |
| 2026-04-20 11:11:45 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.045 |  |
| 2026-04-20 11:04:45 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.077 |  |
| 2026-04-20 11:00:07 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.507 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)