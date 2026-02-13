# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_14:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 14:16:05 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-13 14:15:31 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:13:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:12:04 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:09:20 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.031 |  |
| 2026-02-13 14:07:55 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 14:07:13 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-02-13 14:06:52 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:06:47 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:06:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-13 14:06:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.058 |  |
| 2026-02-13 14:06:03 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:05:37 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 14:05:21 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:05:18 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:04:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-02-13 14:04:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:04:05 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-13 14:03:59 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:47 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:42 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-13 14:03:27 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-02-13 14:03:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-02-13 14:03:20 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-02-13 14:02:58 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:02:56 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:02:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-13 14:02:29 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-02-13 14:02:19 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.041 |  |
| 2026-02-13 14:02:05 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:01:43 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 14:01:19 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.080 |  |
| 2026-02-13 14:01:10 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:01:09 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-13 14:01:00 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:00:34 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 14:00:09 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 14:01:09 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-13 14:03:27 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 14:01:43 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 14:06:41 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-13 14:05:37 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 14:00:34 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 14:07:55 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 14:16:05 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-13 14:02:05 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:04:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:02:58 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:02:56 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:05:18 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:01:10 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:42 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:12:04 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:05:21 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:59 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:06:52 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:06:47 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:03:47 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:01:00 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:06:03 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:13:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:15:31 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 14:02:47 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-13 14:04:05 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-13 14:00:09 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-02-13 14:04:52 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-02-13 14:02:29 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-02-13 14:09:20 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.031 |  |
| 2026-02-13 14:07:13 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-02-13 14:02:19 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.041 |  |
| 2026-02-13 14:03:20 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-02-13 14:06:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.058 |  |
| 2026-02-13 14:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-13 14:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-02-13 14:01:19 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.080 |  |
| 2026-02-13 14:03:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)