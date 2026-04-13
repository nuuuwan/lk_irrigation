# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_11:27:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,881 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 11:27:50 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:16:36 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.096 |  |
| 2026-04-13 11:15:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:11:47 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-13 11:11:04 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-04-13 11:09:49 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:08:56 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:08:33 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:08:23 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-04-13 11:07:25 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.045 |  |
| 2026-04-13 11:06:50 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.047 |  |
| 2026-04-13 11:06:45 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-13 11:06:34 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-04-13 11:06:16 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-04-13 11:05:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:04:59 | Katharagama (Menik Ganga) | -0.90 | 🟢 Normal | -0.759 |  |
| 2026-04-13 11:04:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 11:03:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-13 11:03:07 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.019 |  |
| 2026-04-13 11:02:45 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.150 |  |
| 2026-04-13 11:02:44 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 11:02:41 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 11:02:31 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-13 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 11:02:14 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.133 |  |
| 2026-04-13 11:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:51 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-13 11:01:25 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-13 11:01:21 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.070 |  |
| 2026-04-13 11:01:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:11 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:05 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-13 11:00:49 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 11:00:44 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 11:00:40 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:00:35 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-04-13 11:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 11:06:34 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-04-13 11:06:45 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-13 11:01:25 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-13 11:04:03 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 11:02:44 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 11:00:49 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 11:00:44 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 10:05:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 11:11:47 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-13 11:02:41 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-13 11:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 11:01:11 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:27:50 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:08:33 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:51 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:15:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:08:56 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:00:40 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:05:08 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:09:49 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:01:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-13 11:11:04 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-04-13 11:01:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-13 11:03:07 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.019 |  |
| 2026-04-13 11:08:23 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-04-13 11:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-04-13 11:01:05 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-04-13 11:03:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-13 11:02:31 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-13 11:06:16 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-04-13 11:00:35 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-04-13 11:07:25 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.045 |  |
| 2026-04-13 11:06:50 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.047 |  |
| 2026-04-13 11:01:21 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.070 |  |
| 2026-04-13 11:16:36 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.096 |  |
| 2026-04-13 11:02:14 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.133 |  |
| 2026-04-13 11:02:45 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.150 |  |
| 2026-04-13 11:04:59 | Katharagama (Menik Ganga) | -0.90 | 🟢 Normal | -0.759 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)