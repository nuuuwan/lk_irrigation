# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_17:12:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 17:12:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-06-27 17:12:34 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:10:58 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-27 17:09:25 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:08:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:07:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.086 |  |
| 2026-06-27 17:07:05 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-27 17:06:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:06:25 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:05:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:44 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-27 17:05:42 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:30 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:24 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -1.685 |  |
| 2026-06-27 17:05:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:05:01 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-06-27 17:04:09 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:53 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-27 17:03:27 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:20 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.092 |  |
| 2026-06-27 17:02:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:02:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-27 17:02:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:02:30 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:02:26 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:02:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-27 17:01:48 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:01:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:01:38 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 17:01:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-06-27 17:01:25 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 17:01:21 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:00:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 17:02:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-27 17:10:58 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-27 17:03:35 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-27 17:01:25 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 17:01:38 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 17:02:30 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:53 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:20 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:02:39 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 16:00:58 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:42 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:09:25 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:02:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:03:27 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:06:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 15:04:01 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:04:09 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:08:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:01:48 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:12:34 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:05:30 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 17:07:05 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-27 17:05:09 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:01:21 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:02:26 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:06:25 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:01:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:00:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:05:24 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-06-27 17:12:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-06-27 17:01:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-06-27 17:05:01 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-06-27 17:05:44 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-27 17:02:00 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-27 17:07:39 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.086 |  |
| 2026-06-27 17:03:12 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.092 |  |
| 2026-06-27 17:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -1.685 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)