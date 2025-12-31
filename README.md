# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_21:16:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,154 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 21:16:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:09:22 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:09:15 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 21:08:40 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-31 21:07:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:47 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.039 |  |
| 2025-12-31 21:07:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:29 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:06:51 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2025-12-31 21:05:35 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:05:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:05:28 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2025-12-31 21:04:54 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:47 | Katharagama (Menik Ganga) | 1.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 21:04:47 | Kuda Oya (Kirindi Oya) | 2.21 | 🟢 Normal | 0.693 | 🔺 Rising |
| 2025-12-31 21:04:38 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.062 |  |
| 2025-12-31 21:04:07 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:07 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:03 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:03:54 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 21:03:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:03:48 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 21:03:45 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 21:03:43 | Siyambalanduwa (Heda Oya) | 3.16 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2025-12-31 21:03:24 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:03:11 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-31 21:02:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-31 21:02:47 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:02:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:02:40 | Nakkala (Kumbukkan Oya) | 3.75 | 🟢 Normal | -0.153 |  |
| 2025-12-31 21:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 21:01:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.092 |  |
| 2025-12-31 21:01:19 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-31 21:00:41 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 21:00:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-31 21:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 21:04:47 | Kuda Oya (Kirindi Oya) | 2.21 | 🟢 Normal | 0.693 | 🔺 Rising |
| 2025-12-31 21:05:28 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2025-12-31 21:03:43 | Siyambalanduwa (Heda Oya) | 3.16 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2025-12-31 21:00:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-31 21:02:56 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-31 21:01:19 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-31 21:03:11 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-31 21:03:48 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 21:09:15 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-31 21:03:45 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 21:03:54 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 21:04:47 | Katharagama (Menik Ganga) | 1.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 21:08:40 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 21:00:41 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 21:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 21:05:35 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:03 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:54 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:07 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:02:47 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:16:12 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:09:22 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:05 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:02:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:03:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:29 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:04:07 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:05:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:07:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 21:06:51 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2025-12-31 21:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 21:07:47 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.039 |  |
| 2025-12-31 21:04:38 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.062 |  |
| 2025-12-31 21:01:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.092 |  |
| 2025-12-31 21:02:40 | Nakkala (Kumbukkan Oya) | 3.75 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)