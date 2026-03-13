# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_21:14:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,568 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 21:14:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-13 21:10:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.042 |  |
| 2026-03-13 21:08:35 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:07:51 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 21:07:42 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:07:15 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:06:44 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 21:06:38 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-03-13 21:06:06 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-03-13 21:05:50 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-03-13 21:05:09 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:04:53 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 21:04:30 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:04:27 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.051 |  |
| 2026-03-13 21:04:16 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:04:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:04:11 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-13 21:04:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-03-13 21:03:56 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-13 21:03:19 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:02:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-13 21:02:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-13 21:02:44 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 21:02:27 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-03-13 21:02:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:02:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:02:17 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:02:06 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:02:00 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 21:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:01:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:01:19 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-03-13 21:00:53 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-03-13 21:00:52 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:00:21 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.077 |  |
| 2026-03-13 21:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-13 20:27:58 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 21:06:06 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-03-13 21:03:56 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-13 21:02:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-13 21:14:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-13 21:06:44 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 21:02:44 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 21:04:53 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 21:07:51 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 21:02:00 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 21:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:02:19 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:04:30 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:04:16 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:05:09 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 21:02:17 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:00:52 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:01:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:02:17 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:07:15 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:04:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:03:19 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:07:42 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:08:35 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 21:04:11 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-03-13 21:02:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-13 21:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-13 20:01:04 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-03-13 21:01:19 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-03-13 21:05:50 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-03-13 21:06:38 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-03-13 21:02:27 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-03-13 21:00:53 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-03-13 21:04:00 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.041 |  |
| 2026-03-13 21:10:48 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.042 |  |
| 2026-03-13 21:04:27 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.051 |  |
| 2026-03-13 21:00:21 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.077 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)