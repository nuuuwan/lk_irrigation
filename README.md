# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_23:34:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,646 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 23:34:54 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:31:18 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.007 |  |
| 2026-06-13 23:29:36 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-06-13 23:10:04 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 23:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-13 23:07:35 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:06:55 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-06-13 23:06:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:06:51 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.018 |  |
| 2026-06-13 23:06:18 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:05:40 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:04:39 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-06-13 23:04:36 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.039 |  |
| 2026-06-13 23:04:30 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-06-13 23:04:07 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.091 |  |
| 2026-06-13 23:04:00 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:03:50 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:03:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:03:24 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-13 23:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.029 |  |
| 2026-06-13 23:03:13 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 23:02:43 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-13 23:02:36 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:02:30 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 23:02:07 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-13 23:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:01:45 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.075 |  |
| 2026-06-13 23:01:39 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:01:33 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:01:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:00:38 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:00:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-13 23:00:29 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 23:09:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-13 23:00:38 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-13 23:02:07 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 23:02:43 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-13 23:02:30 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 22:02:18 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 23:10:04 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 23:05:40 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-13 22:02:10 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:01:39 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:07:35 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:03:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:01:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:06:51 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:00:38 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:34:54 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:04:00 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:31:18 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.007 |  |
| 2026-06-13 23:29:36 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-06-13 23:02:36 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:03:50 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-06-13 21:03:19 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:04:36 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:06:18 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:01:33 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-06-13 23:06:51 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.018 |  |
| 2026-06-13 23:03:24 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-13 23:04:39 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 23:03:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.029 |  |
| 2026-06-13 23:04:30 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-06-13 23:04:35 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.039 |  |
| 2026-06-13 23:03:13 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 23:06:55 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-06-13 23:01:45 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.075 |  |
| 2026-06-13 23:04:07 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)