# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_22:08:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 22:08:19 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-02-01 22:08:07 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.029 |  |
| 2026-02-01 22:07:38 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.039 |  |
| 2026-02-01 22:07:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 22:05:35 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:04:58 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-02-01 22:04:56 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-02-01 22:04:52 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 22:04:39 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 22:04:23 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-01 22:03:53 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:34 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:02:55 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-01 22:02:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:02:47 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 22:02:47 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.172 |  |
| 2026-02-01 22:02:25 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 22:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 22:01:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-01 22:01:26 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:01:21 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:01:15 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 22:01:02 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:20 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 22:00:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:13 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:21:05 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 22:04:23 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-01 22:01:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-01 22:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 22:04:52 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 22:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 21:03:19 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-01 22:04:39 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 22:02:25 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-01 22:02:47 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 21:21:05 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-01 22:00:20 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 22:01:15 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 22:01:26 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:05:35 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:22 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:07:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:01:02 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:34 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-01 21:01:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:13 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:03:53 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:02:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:01:21 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:18 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 22:02:55 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-01 22:04:58 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-02-01 21:01:59 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-02-01 22:08:19 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-02-01 22:08:07 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.029 |  |
| 2026-02-01 22:07:38 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.039 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 22:04:56 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-02-01 22:02:47 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)