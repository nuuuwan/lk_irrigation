# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_09:26:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,894 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 09:26:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:18:08 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-01-27 09:17:46 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:11:41 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 10.277 | 🔺 Rising |
| 2026-01-27 09:10:54 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:08:59 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-27 09:08:43 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 09:06:53 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:06:02 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 09:05:40 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:05:31 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.060 |  |
| 2026-01-27 09:05:21 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-27 09:05:17 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.254 |  |
| 2026-01-27 09:04:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-01-27 09:04:28 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:04:22 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-01-27 09:03:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 09:03:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:03:40 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:03:33 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:03:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:03:20 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.048 |  |
| 2026-01-27 09:03:16 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-01-27 09:03:02 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:03:01 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:02:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:02:13 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-01-27 09:01:54 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:01:49 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:44 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:01:42 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 10.277 | 🔺 Rising |
| 2026-01-27 09:01:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:40 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:35 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-01-27 09:01:21 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:58 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:40 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 09:11:41 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 10.277 | 🔺 Rising |
| 2026-01-27 09:01:35 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.411 | 🔺 Rising |
| 2026-01-27 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 09:03:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 09:06:02 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 09:05:21 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-27 09:08:43 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 09:01:40 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:49 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:41 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:02:13 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 09:01:54 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:03:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:58 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:03:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:02:40 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:00:40 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:03:01 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:05:40 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:01:21 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:26:06 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:06:53 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 09:18:08 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-01-27 09:03:33 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:03:40 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:01:44 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:03:02 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:04:28 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:10:54 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-27 09:08:59 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-27 09:04:58 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-01-27 09:04:22 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.029 |  |
| 2026-01-27 09:03:16 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-01-27 09:03:20 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.048 |  |
| 2026-01-27 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-01-27 09:05:31 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.060 |  |
| 2026-01-27 09:05:17 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.254 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)