# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_14:28:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,668 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 14:28:00 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:16:39 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.018 |  |
| 2026-05-31 14:14:41 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:12:02 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.77 | 🟢 Normal | -0.096 |  |
| 2026-05-31 14:07:33 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:07:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-31 14:06:55 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.057 |  |
| 2026-05-31 14:06:40 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:06:25 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:06:04 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:05:21 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-31 14:05:15 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.029 |  |
| 2026-05-31 14:04:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 14:04:20 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:04:20 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 14:04:07 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:04:07 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -7.500 |  |
| 2026-05-31 14:04:02 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:03:43 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -7.500 |  |
| 2026-05-31 14:03:27 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 14:03:19 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:03:02 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:03:02 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-05-31 14:02:44 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:36 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.055 |  |
| 2026-05-31 14:02:33 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:28 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-05-31 14:02:19 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-31 14:02:19 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.029 |  |
| 2026-05-31 14:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:01:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.005 |  |
| 2026-05-31 14:00:47 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:00:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:00:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 14:02:19 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-05-31 14:05:21 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-31 14:07:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-31 14:03:27 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-31 14:04:20 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 14:02:33 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:00:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:14:41 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 13:05:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:00:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:28 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:04:07 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:06:40 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:28:00 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:44 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:01:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:02:19 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:03:02 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:04:20 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:04:02 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:00:47 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:12:02 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 14:01:12 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.005 |  |
| 2026-05-31 14:07:33 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:03:19 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:06:25 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:06:04 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-31 14:16:39 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.018 |  |
| 2026-05-31 14:04:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-05-31 14:02:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-05-31 14:03:02 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-05-31 14:05:15 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.029 |  |
| 2026-05-31 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.029 |  |
| 2026-05-31 13:01:42 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.040 |  |
| 2026-05-31 14:02:36 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.055 |  |
| 2026-05-31 14:06:55 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.057 |  |
| 2026-05-31 14:11:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.77 | 🟢 Normal | -0.096 |  |
| 2026-05-31 14:04:07 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -7.500 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)