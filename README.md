# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_20:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,278 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 20:14:16 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:11:29 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-06-25 20:09:59 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.048 |  |
| 2026-06-25 20:07:40 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-06-25 20:06:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:06:51 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.049 |  |
| 2026-06-25 20:06:40 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.014 |  |
| 2026-06-25 20:05:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-25 20:05:25 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-25 20:04:44 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-06-25 20:04:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-25 20:04:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:04:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-25 20:04:07 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:53 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:46 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:25 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:03:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:03:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:02:36 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.149 |  |
| 2026-06-25 20:02:23 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-06-25 20:02:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:02:18 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:02:17 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 20:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 20:02:06 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.060 |  |
| 2026-06-25 20:01:29 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:01:23 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:01:03 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.969 |  |
| 2026-06-25 20:00:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:00:53 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:00:27 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 20:02:23 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-06-25 20:07:40 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-06-25 20:04:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-25 20:02:17 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 20:02:08 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 20:00:27 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 19:00:54 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:00:53 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:14:16 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:02:21 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:01:29 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:00:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:02:18 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:04:07 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:04:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:46 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:03:53 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:01:23 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 20:05:47 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-25 20:05:25 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 20:04:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.011 |  |
| 2026-06-25 20:04:44 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-06-25 20:06:40 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.014 |  |
| 2026-06-25 20:11:29 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-06-25 20:03:14 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:03:25 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:06:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-25 20:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | -0.024 |  |
| 2026-06-25 20:09:59 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.048 |  |
| 2026-06-25 20:06:51 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.049 |  |
| 2026-06-25 20:02:06 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.060 |  |
| 2026-06-25 20:02:36 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.149 |  |
| 2026-06-25 20:01:03 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.969 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)