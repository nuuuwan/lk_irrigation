# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_06:14:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,549 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 06:14:38 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-03-17 06:14:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:11:54 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.072 |  |
| 2026-03-17 06:11:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:08:44 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.002 |  |
| 2026-03-17 06:08:09 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:08:04 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:07:24 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:06:57 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:06:44 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.144 |  |
| 2026-03-17 06:06:40 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-17 06:06:39 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:05:33 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.123 |  |
| 2026-03-17 06:05:24 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 06:04:51 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.067 |  |
| 2026-03-17 06:04:43 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 06:04:24 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:04:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-17 06:03:58 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:03:56 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:03:21 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:06 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-17 06:03:00 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:02:17 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:02:13 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:01:32 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:01:19 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:01:13 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:01:11 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 06:00:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:00:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.075 |  |
| 2026-03-17 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:00:22 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:00:19 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-03-17 05:31:07 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-17 05:31:05 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-17 05:31:04 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-17 05:31:02 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.068 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 06:03:06 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-17 06:06:40 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-17 06:04:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-17 06:04:43 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 06:05:24 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 06:01:11 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 06:00:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:45 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:14:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:00 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 05:02:51 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:00:22 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:08:09 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:02:13 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:06:39 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:02:17 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:56 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:07:24 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:01:32 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:08:04 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:11:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:03:21 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-17 06:08:44 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.002 |  |
| 2026-03-17 06:03:58 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:03:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:01:19 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:04:24 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-17 06:00:19 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-03-17 06:14:38 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-03-17 06:04:51 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.067 |  |
| 2026-03-17 06:11:54 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.072 |  |
| 2026-03-17 06:00:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.075 |  |
| 2026-03-17 06:05:33 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.123 |  |
| 2026-03-17 06:06:44 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.144 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)