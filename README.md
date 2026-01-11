# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_16:16:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 16:16:17 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:14:38 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:12:52 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:10:19 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-01-11 16:09:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:08:56 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:06:55 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.019 |  |
| 2026-01-11 16:05:53 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:05:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-11 16:05:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-01-11 16:05:06 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 16:04:54 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:30 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:27 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:12 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-01-11 16:04:08 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 16:03:58 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:03:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-11 16:03:10 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.046 |  |
| 2026-01-11 16:03:02 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:54 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:44 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:22 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:19 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:09 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 16:01:59 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:58 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:48 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 16:01:39 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.021 |  |
| 2026-01-11 16:01:28 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-01-11 16:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:00:54 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 16:00:50 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-11 16:00:39 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-01-11 16:00:18 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-11 15:24:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 15:23:53 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 16:01:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-01-11 16:00:50 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-11 16:05:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-11 16:00:18 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-11 16:02:09 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-11 16:04:08 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 16:05:06 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 16:00:54 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 16:01:48 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 16:02:22 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:28 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:44 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:54 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:58 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:14:38 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:54 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:03:58 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:03:02 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:19 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:01:59 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:27 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:16:17 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:08:56 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:39 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:12:52 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:05:53 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:02:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:04:30 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:09:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:10:19 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-01-11 16:03:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-11 16:00:39 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-01-11 16:06:55 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.019 |  |
| 2026-01-11 16:05:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-01-11 16:01:39 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.021 |  |
| 2026-01-11 16:04:12 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-01-11 16:03:10 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)