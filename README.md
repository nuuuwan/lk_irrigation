# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_14:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 14:11:52 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-11 14:11:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:11:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:08:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-05-11 14:07:51 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2026-05-11 14:07:39 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-11 14:07:35 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 14:07:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:07:03 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:06:48 | Moragaswewa (Deduru Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:06:16 | Moragaswewa (Deduru Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:06:11 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-11 14:05:58 | Moragaswewa (Deduru Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:05:37 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.089 |  |
| 2026-05-11 14:05:12 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:05:04 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:04:50 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-05-11 14:04:28 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:04:18 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-11 14:04:09 | Katharagama (Menik Ganga) | 2.29 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-11 14:04:07 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 14:03:52 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-11 14:03:41 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 14:03:34 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:03:30 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:03:11 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:02:53 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:02:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:02:20 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:02:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-11 14:02:07 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 14:02:06 | Kuda Oya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.071 |  |
| 2026-05-11 14:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-11 14:01:37 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:01:28 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | -0.093 |  |
| 2026-05-11 14:01:21 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:01:19 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.044 |  |
| 2026-05-11 14:00:53 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:00:47 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.030 |  |
| 2026-05-11 14:00:30 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-05-11 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-05-11 13:59:11 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 14:07:39 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-11 14:04:09 | Katharagama (Menik Ganga) | 2.29 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-11 14:06:11 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-11 14:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.71 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-11 14:03:52 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-11 14:11:52 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-11 14:04:18 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-11 14:04:07 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 14:02:07 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 14:03:41 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 14:07:35 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 14:02:20 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:06:48 | Moragaswewa (Deduru Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:02:53 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:11:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:03:30 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:05:12 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:07:03 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:03:34 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:07:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:00:53 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:02:26 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:05:04 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:11:46 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-11 14:04:28 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:03:11 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:01:21 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:01:37 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-11 14:00:30 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-05-11 14:02:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-05-11 14:07:51 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.019 |  |
| 2026-05-11 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-05-11 14:08:14 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-05-11 14:00:47 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.030 |  |
| 2026-05-11 14:04:50 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-05-11 14:01:19 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.044 |  |
| 2026-05-11 14:02:06 | Kuda Oya (Kirindi Oya) | 2.55 | 🟢 Normal | -0.071 |  |
| 2026-05-11 14:05:37 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.089 |  |
| 2026-05-11 14:01:28 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)