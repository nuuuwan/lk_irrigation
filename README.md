# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_06:38:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 06:38:29 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | -0.104 |  |
| 2026-05-10 06:27:46 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -4.500 |  |
| 2026-05-10 06:27:22 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -4.500 |  |
| 2026-05-10 06:10:46 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-10 06:09:59 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:09:00 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-05-10 06:08:59 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 06:08:03 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.027 |  |
| 2026-05-10 06:07:17 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.036 |  |
| 2026-05-10 06:06:24 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.044 |  |
| 2026-05-10 06:06:14 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.357 |  |
| 2026-05-10 06:06:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:05:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 06:04:49 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -54.000 |  |
| 2026-05-10 06:04:47 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -54.000 |  |
| 2026-05-10 06:04:46 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -54.000 |  |
| 2026-05-10 06:04:44 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | -54.000 |  |
| 2026-05-10 06:04:35 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-10 06:04:33 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-10 06:04:29 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -504.000 |  |
| 2026-05-10 06:04:28 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -504.000 |  |
| 2026-05-10 06:04:24 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.122 |  |
| 2026-05-10 06:04:23 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:03:41 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:03:18 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2026-05-10 06:03:02 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.168 |  |
| 2026-05-10 06:02:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:02:46 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.103 |  |
| 2026-05-10 06:02:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:02:30 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.020 |  |
| 2026-05-10 06:02:28 | Thanamalwila (Kirindi Oya) | 2.51 | 🟢 Normal | -0.647 |  |
| 2026-05-10 06:02:27 | Kuda Oya (Kirindi Oya) | 2.56 | 🟢 Normal | -0.039 |  |
| 2026-05-10 06:02:26 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-05-10 06:02:25 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.067 |  |
| 2026-05-10 06:02:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:02:08 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:01:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-10 06:01:39 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:01:07 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-10 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.812 |  |
| 2026-05-10 06:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 06:00:47 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.133 |  |
| 2026-05-10 06:00:42 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-05-10 05:54:29 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.357 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 06:10:46 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-10 06:01:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-10 06:01:07 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-10 06:01:06 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-10 06:05:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-10 06:08:59 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-10 06:01:39 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:02:08 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:06:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:04:23 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:00:42 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:02:12 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-10 06:09:00 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-05-10 06:09:59 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:02:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:02:37 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-10 06:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-05-10 06:02:30 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.020 |  |
| 2026-05-10 06:02:26 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-05-10 06:03:18 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.022 |  |
| 2026-05-10 06:08:03 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.027 |  |
| 2026-05-10 06:04:33 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-05-10 06:04:35 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-10 06:07:17 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.036 |  |
| 2026-05-10 06:02:27 | Kuda Oya (Kirindi Oya) | 2.56 | 🟢 Normal | -0.039 |  |
| 2026-05-10 06:06:24 | Moragaswewa (Deduru Oya) | 3.24 | 🟢 Normal | -0.044 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 06:02:25 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.067 |  |
| 2026-05-10 06:02:46 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.103 |  |
| 2026-05-10 06:38:29 | Galgamuwa (Mee Oya) | 0.95 | 🟢 Normal | -0.104 |  |
| 2026-05-10 06:04:24 | Wellawaya (Kirindi Oya) | 1.97 | 🟢 Normal | -0.122 |  |
| 2026-05-10 06:00:47 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.133 |  |
| 2026-05-10 06:03:02 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.168 |  |
| 2026-05-10 06:06:14 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.357 |  |
| 2026-05-10 06:02:28 | Thanamalwila (Kirindi Oya) | 2.51 | 🟢 Normal | -0.647 |  |
| 2026-05-10 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.812 |  |
| 2026-05-10 06:27:46 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -4.500 |  |
| 2026-05-10 06:04:49 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -54.000 |  |
| 2026-05-10 06:04:29 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | -504.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)