# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_20:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 20:12:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:10:15 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:10:08 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:07:35 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:07:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-31 20:07:05 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.121 |  |
| 2026-05-31 20:05:38 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 20:05:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-05-31 20:05:29 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:04:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 20:04:54 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.060 |  |
| 2026-05-31 20:04:52 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:04:49 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-05-31 20:04:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-05-31 20:04:32 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.056 |  |
| 2026-05-31 20:04:27 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-31 20:04:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:04:08 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:03:46 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.031 |  |
| 2026-05-31 20:03:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:03:01 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:02:59 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-05-31 20:02:55 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:02:51 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:02:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:02:34 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-31 20:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.039 |  |
| 2026-05-31 20:02:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:02:00 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.218 |  |
| 2026-05-31 20:01:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 20:01:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:00:59 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:00:35 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-05-31 20:00:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 19:42:21 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 20:04:27 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-31 20:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 20:05:38 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 20:04:58 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:03:01 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:00:59 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:04:23 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:10:08 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:05:29 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:02:51 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:00:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:10:15 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:02:55 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:12:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-31 19:01:13 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:17 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:05:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-05-31 20:07:35 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:02:42 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:02:28 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:03:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:04:08 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-05-31 20:00:35 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-05-31 20:07:16 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.020 |  |
| 2026-05-31 20:02:34 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-31 20:03:46 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.031 |  |
| 2026-05-31 20:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.039 |  |
| 2026-05-31 20:02:59 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-05-31 20:04:32 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.056 |  |
| 2026-05-31 20:04:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-05-31 20:04:49 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-05-31 20:04:54 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.060 |  |
| 2026-05-31 20:07:05 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.121 |  |
| 2026-05-31 20:02:00 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)