# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_11:38:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 11:38:05 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 11:16:13 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.043 |  |
| 2026-05-08 11:13:38 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-05-08 11:10:51 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.141 |  |
| 2026-05-08 11:10:48 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.130 |  |
| 2026-05-08 11:10:09 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:09:58 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:08:44 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:06:45 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:06:21 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-05-08 11:06:18 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.077 |  |
| 2026-05-08 11:06:14 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:05:22 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.030 |  |
| 2026-05-08 11:05:18 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.029 |  |
| 2026-05-08 11:05:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-05-08 11:05:07 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-08 11:04:53 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 11:04:19 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-08 11:04:17 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-05-08 11:04:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-05-08 11:03:32 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.048 |  |
| 2026-05-08 11:03:29 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 11:03:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.049 |  |
| 2026-05-08 11:03:07 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.122 |  |
| 2026-05-08 11:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.95 | 🟢 Normal | -0.069 |  |
| 2026-05-08 11:02:46 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:02:17 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-08 11:02:15 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:01:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:01:46 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-08 11:01:43 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.040 |  |
| 2026-05-08 11:01:41 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:01:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.054 |  |
| 2026-05-08 11:01:23 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:50 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:43 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 11:00:37 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-08 11:00:18 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 11:04:19 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-05-08 11:02:17 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-08 11:00:43 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 11:04:53 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 11:03:29 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 11:38:05 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-08 11:06:45 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:02:35 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:06:14 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:08:44 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:01:23 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:00:50 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:10:09 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:02:15 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:02:46 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:01:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:01:41 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-08 11:00:15 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-08 11:04:01 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-05-08 11:13:38 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-05-08 11:06:21 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-05-08 11:00:37 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-08 11:05:07 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-08 11:05:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-05-08 11:05:18 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.029 |  |
| 2026-05-08 11:01:46 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-08 11:05:22 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.030 |  |
| 2026-05-08 11:04:17 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-05-08 11:01:43 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.040 |  |
| 2026-05-08 11:16:13 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.043 |  |
| 2026-05-08 11:03:32 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.048 |  |
| 2026-05-08 11:03:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.049 |  |
| 2026-05-08 11:01:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.054 |  |
| 2026-05-08 11:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.95 | 🟢 Normal | -0.069 |  |
| 2026-05-08 11:06:18 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.077 |  |
| 2026-05-08 11:03:07 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.122 |  |
| 2026-05-08 11:10:48 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.130 |  |
| 2026-05-08 11:10:51 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)