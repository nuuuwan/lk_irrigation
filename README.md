# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_07:19:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 07:19:39 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:18:02 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.016 |  |
| 2026-05-15 07:17:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-05-15 07:10:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:10:44 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:09:45 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -1.206 |  |
| 2026-05-15 07:09:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:09:08 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 07:08:50 | Moragaswewa (Deduru Oya) | 3.68 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 07:08:41 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:08:11 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:08:02 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.065 |  |
| 2026-05-15 07:07:38 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 07:06:54 | Galgamuwa (Mee Oya) | 3.35 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-15 07:06:09 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:06:07 | Glencourse (Kelani Ganga) | 13.59 | 🟢 Normal | -0.175 |  |
| 2026-05-15 07:05:18 | Hanwella (Kelani Ganga) | 6.21 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:05:13 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:05:12 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-15 07:05:04 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:04:59 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-05-15 07:04:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:04:57 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-15 07:03:30 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:03:15 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-05-15 07:03:06 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.080 |  |
| 2026-05-15 07:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-15 07:02:25 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-05-15 07:02:23 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.089 |  |
| 2026-05-15 07:02:23 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 07:02:15 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:02:14 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-15 07:02:14 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.032 |  |
| 2026-05-15 07:01:39 | Thanthirimale (Malwathu Oya) | 3.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-15 07:01:21 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:00:58 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-15 07:00:57 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 07:00:43 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 07:17:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-05-15 07:02:23 | Dunamale (Aththanagalu Oya) | 4.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 07:18:02 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | -0.016 |  |
| 2026-05-15 06:00:30 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.766 | 🔺 Rising |
| 2026-05-15 07:04:57 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-15 07:04:59 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-05-15 07:06:54 | Galgamuwa (Mee Oya) | 3.35 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-15 07:08:50 | Moragaswewa (Deduru Oya) | 3.68 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 07:01:39 | Thanthirimale (Malwathu Oya) | 3.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-15 07:02:14 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-15 07:00:57 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 07:07:38 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 07:09:08 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 07:04:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:06:09 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:01:21 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:00:43 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:05:04 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:08:41 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:19:39 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:10:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:10:44 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:08:11 | Badalgama (Maha Oya) | 4.72 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:05:18 | Hanwella (Kelani Ganga) | 6.21 | 🟢 Normal | -0.009 |  |
| 2026-05-15 07:05:12 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-15 07:00:58 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-15 07:05:13 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:09:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:03:30 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-15 07:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-15 07:00:36 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |
| 2026-05-15 07:02:25 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-05-15 07:02:14 | Rathnapura (Kalu Ganga) | 4.81 | 🟢 Normal | -0.032 |  |
| 2026-05-15 07:03:15 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-05-15 07:08:02 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.065 |  |
| 2026-05-15 07:03:06 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.080 |  |
| 2026-05-15 07:02:23 | Deraniyagala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.089 |  |
| 2026-05-15 07:06:07 | Glencourse (Kelani Ganga) | 13.59 | 🟢 Normal | -0.175 |  |
| 2026-05-15 07:09:45 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -1.206 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)