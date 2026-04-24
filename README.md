# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_17:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 17:12:10 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:11:12 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:10:40 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-24 17:09:19 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.022 |  |
| 2026-04-24 17:08:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:08:14 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:08:01 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-24 17:07:39 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:06:51 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-04-24 17:06:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:06:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:06:41 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:06:17 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:05:55 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.171 |  |
| 2026-04-24 17:05:39 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.038 |  |
| 2026-04-24 17:05:13 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 17:04:35 | Katharagama (Menik Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-04-24 17:04:22 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-24 17:03:51 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 17:03:12 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 17:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-04-24 17:03:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 17:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-04-24 17:02:48 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-24 17:02:31 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:18 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-04-24 17:02:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 17:02:06 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-04-24 17:01:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-24 17:01:05 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:00:45 | Thanthirimale (Malwathu Oya) | 2.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 17:00:34 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:00:18 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:00:13 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-24 16:43:26 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-24 16:29:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 17:04:22 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-24 17:00:13 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-24 17:10:40 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-24 17:02:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 17:05:13 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 17:00:45 | Thanthirimale (Malwathu Oya) | 2.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 17:03:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 17:03:51 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 17:07:39 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:00:18 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:31 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:06:17 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:12:10 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:00:34 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:06:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:02:48 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:01:05 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-24 17:08:14 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 16:29:37 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.007 |  |
| 2026-04-24 16:02:31 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-24 17:01:23 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-24 17:03:12 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2026-04-24 17:06:51 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-04-24 17:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-04-24 17:11:12 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:06:41 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:08:24 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.018 |  |
| 2026-04-24 17:08:01 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-04-24 17:02:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-04-24 17:09:19 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.022 |  |
| 2026-04-24 17:02:06 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-04-24 17:05:39 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.038 |  |
| 2026-04-24 17:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-04-24 17:02:18 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-04-24 17:04:35 | Katharagama (Menik Ganga) | 1.88 | 🟢 Normal | -0.059 |  |
| 2026-04-24 17:05:55 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)