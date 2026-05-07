# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_08:27:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 08:27:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:13:42 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-07 08:13:34 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.112 |  |
| 2026-05-07 08:11:44 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.081 |  |
| 2026-05-07 08:09:01 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 08:08:59 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-05-07 08:08:36 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:08:34 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-05-07 08:08:11 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:07:30 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-07 08:07:27 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-05-07 08:06:32 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-07 08:05:40 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-07 08:05:23 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-07 08:05:22 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-07 08:05:16 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-07 08:04:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.098 |  |
| 2026-05-07 08:04:36 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.174 |  |
| 2026-05-07 08:04:25 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:04:03 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-05-07 08:03:57 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 08:03:14 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.202 |  |
| 2026-05-07 08:03:02 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-07 08:02:52 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:02:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 08:02:19 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 08:02:14 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:02:08 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:01:44 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-05-07 08:01:33 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 08:01:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:01:02 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:00:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:00:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-05-07 08:00:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 08:05:40 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-05-07 08:05:23 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-07 08:07:30 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-07 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 08:01:33 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-07 08:06:32 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-07 08:05:16 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-07 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-07 08:13:42 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-07 08:03:57 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 08:02:19 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 08:09:01 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 08:27:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:08:36 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:08:11 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:00:16 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:02:10 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:02:14 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:01:02 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:03:02 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 08:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:02:08 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:02:52 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:01:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-07 08:05:22 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-07 08:04:25 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:02:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:00:40 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.020 |  |
| 2026-05-07 08:01:44 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-05-07 08:04:03 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-05-07 08:00:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.041 |  |
| 2026-05-07 08:07:27 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-05-07 08:08:34 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.058 |  |
| 2026-05-07 08:08:59 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-05-07 08:11:44 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.081 |  |
| 2026-05-07 08:04:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.098 |  |
| 2026-05-07 08:13:34 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.112 |  |
| 2026-05-07 08:04:36 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.174 |  |
| 2026-05-07 08:03:14 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)