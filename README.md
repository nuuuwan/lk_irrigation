# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_09:12:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 09:12:43 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-27 09:10:01 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.029 |  |
| 2025-12-27 09:09:49 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:09:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:36 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:35 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-27 09:07:08 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:07 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:06:57 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:06:48 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:06:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.119 |  |
| 2025-12-27 09:05:41 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:05:33 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2025-12-27 09:05:22 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:11 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:03:42 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:03:36 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:03:27 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-27 09:03:24 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 09:03:10 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:02:56 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 09:02:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:34 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:29 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2025-12-27 09:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.058 |  |
| 2025-12-27 09:02:20 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2025-12-27 09:01:50 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.270 |  |
| 2025-12-27 09:01:48 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:01:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:01:32 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.003 |  |
| 2025-12-27 09:01:25 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:01:20 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:00:47 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:00:41 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:34:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:26:25 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-27 08:16:59 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 08:26:25 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-27 09:03:24 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 09:02:56 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 09:12:43 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-27 09:01:32 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.003 |  |
| 2025-12-27 09:01:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:11 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:34 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:01:25 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:36 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:05:41 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:09:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:02:36 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:31 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:04:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:05:22 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:03:36 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:06:48 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:07:08 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-27 09:01:48 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 08:02:17 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:06:57 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:00:47 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:01:20 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:03:42 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-27 09:07:07 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:03:10 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:09:49 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2025-12-27 09:03:27 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-27 09:05:33 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2025-12-27 09:07:35 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2025-12-27 09:02:20 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2025-12-27 09:10:01 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.029 |  |
| 2025-12-27 09:02:29 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2025-12-27 09:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.058 |  |
| 2025-12-27 09:06:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.119 |  |
| 2025-12-27 09:01:50 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)