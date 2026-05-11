# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_16:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 16:21:03 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.035 |  |
| 2026-05-11 16:14:46 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:14:00 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:13:14 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-11 16:12:11 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:11:30 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:11:29 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:10:57 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-11 16:09:59 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.113 |  |
| 2026-05-11 16:09:02 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.698 | 🔺 Rising |
| 2026-05-11 16:09:02 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-05-11 16:08:24 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.055 |  |
| 2026-05-11 16:08:18 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-11 16:08:18 | Katharagama (Menik Ganga) | 2.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 16:08:07 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 16:07:39 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:07:01 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-05-11 16:06:40 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-05-11 16:06:39 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:06:32 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:06:30 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 16:06:14 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-05-11 16:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-11 16:04:51 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-11 16:04:15 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 16:04:04 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:03:58 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 16:03:57 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 16:03:50 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.059 |  |
| 2026-05-11 16:03:28 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 16:03:27 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 16:03:20 | Thanamalwila (Kirindi Oya) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-05-11 16:03:01 | Thanthirimale (Malwathu Oya) | 2.97 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-11 16:02:57 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:02:36 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 16:02:33 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.090 |  |
| 2026-05-11 16:02:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:01:33 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-11 16:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.058 |  |
| 2026-05-11 16:00:32 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.092 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 16:06:40 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-05-11 16:09:02 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.698 | 🔺 Rising |
| 2026-05-11 16:09:02 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-05-11 16:01:33 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-05-11 16:10:57 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-11 16:04:51 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-11 16:03:01 | Thanthirimale (Malwathu Oya) | 2.97 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-11 16:00:32 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-11 16:03:58 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 15:11:11 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-11 16:08:18 | Katharagama (Menik Ganga) | 2.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 16:04:15 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 16:03:28 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 16:13:14 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-11 16:03:27 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 16:08:07 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-11 16:02:36 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-11 16:03:57 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 16:06:30 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 16:06:39 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:12:11 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:11:30 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:14:00 | Galgamuwa (Mee Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:02:57 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:02:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:04:04 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:06:32 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:14:46 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:07:39 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-11 16:08:18 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-11 16:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-11 16:07:01 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2026-05-11 16:21:03 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.035 |  |
| 2026-05-11 16:08:24 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.055 |  |
| 2026-05-11 16:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.058 |  |
| 2026-05-11 16:03:50 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | -0.059 |  |
| 2026-05-11 16:03:20 | Thanamalwila (Kirindi Oya) | 2.22 | 🟢 Normal | -0.082 |  |
| 2026-05-11 16:02:33 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.090 |  |
| 2026-05-11 16:09:59 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)