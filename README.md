# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_12:18:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,477 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 12:18:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:16:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.040 |  |
| 2026-03-20 12:09:59 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.027 |  |
| 2026-03-20 12:09:56 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:09:32 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-03-20 12:08:01 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:06:11 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:06:00 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.021 |  |
| 2026-03-20 12:05:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.058 |  |
| 2026-03-20 12:05:28 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:05:28 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 12:05:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:05:04 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-03-20 12:04:25 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2026-03-20 12:04:01 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:03:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:03:39 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-03-20 12:03:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-03-20 12:03:13 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.048 |  |
| 2026-03-20 12:03:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-20 12:02:51 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:02:34 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.108 |  |
| 2026-03-20 12:02:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-20 12:02:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-20 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-03-20 12:02:04 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:02:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:01:58 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.194 |  |
| 2026-03-20 12:01:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:01:46 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:01:46 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:01:38 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-20 12:01:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:01:11 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:00:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-20 12:00:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:00:13 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:00:10 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-20 11:48:32 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 12:03:24 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-03-20 12:02:24 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-20 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-03-20 12:02:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-20 12:03:02 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-20 12:01:38 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-20 12:05:28 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 12:02:47 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:02:04 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:06:11 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:04:01 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:18:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:02:51 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:01:37 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:05:04 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:05:28 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:01:50 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:09:56 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:08:01 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-20 12:09:32 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-03-20 12:03:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:02:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:00:10 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:00:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-20 12:01:46 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:01:11 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:00:13 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-03-20 12:06:00 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.021 |  |
| 2026-03-20 12:00:53 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-20 12:09:59 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.027 |  |
| 2026-03-20 12:05:04 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-03-20 12:03:39 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-03-20 12:04:25 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2026-03-20 12:16:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.040 |  |
| 2026-03-20 12:03:13 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.048 |  |
| 2026-03-20 12:05:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.058 |  |
| 2026-03-20 12:02:34 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.108 |  |
| 2026-03-20 12:01:58 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)