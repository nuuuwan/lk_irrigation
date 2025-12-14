# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_07:20:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 07:20:50 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:14:10 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-14 07:13:51 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-14 07:12:35 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-14 07:12:30 | Thanthirimale (Malwathu Oya) | 4.40 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-14 07:12:07 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:11:50 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:11:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.026 |  |
| 2025-12-14 07:10:45 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2025-12-14 07:09:04 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 07:09:02 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-14 07:07:48 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2025-12-14 07:07:46 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-14 07:07:28 | Horowpothana (Yan Oya) | 4.78 | 🟢 Normal | -0.083 |  |
| 2025-12-14 07:07:12 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:06:59 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-14 07:06:45 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:05:28 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.029 |  |
| 2025-12-14 07:05:13 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.064 |  |
| 2025-12-14 07:05:11 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:05:11 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.159 |  |
| 2025-12-14 07:04:32 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 07:04:09 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.188 |  |
| 2025-12-14 07:04:05 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 07:03:56 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-14 07:03:27 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2025-12-14 07:03:24 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.051 |  |
| 2025-12-14 07:03:17 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 07:03:16 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2025-12-14 07:03:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-14 07:03:02 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:02:59 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-14 07:02:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:02:23 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:49 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:42 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:29 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:00:48 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.062 |  |
| 2025-12-14 07:00:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 06:46:21 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.064 |  |
| 2025-12-14 06:46:00 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.064 |  |
| 2025-12-14 06:45:37 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.064 |  |
| 2025-12-14 06:45:02 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | -0.188 |  |
| 2025-12-14 06:33:18 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 07:06:59 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-14 07:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-14 07:14:10 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-14 07:03:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-14 07:09:04 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-14 07:03:17 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-14 07:12:35 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-14 07:04:32 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 07:04:05 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 07:12:30 | Thanthirimale (Malwathu Oya) | 4.40 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-14 07:02:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:00:18 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:20:50 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:49 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:12:07 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:03:02 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:42 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:01:29 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:07:12 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:11:50 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:06:45 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:05:11 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:02:23 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 07:13:51 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2025-12-14 07:07:46 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-14 07:02:59 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-14 07:10:45 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2025-12-14 07:09:02 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-14 07:03:27 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2025-12-14 07:11:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.026 |  |
| 2025-12-14 07:05:28 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.029 |  |
| 2025-12-14 07:07:48 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2025-12-14 07:03:24 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.051 |  |
| 2025-12-14 07:03:16 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2025-12-14 07:00:48 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.062 |  |
| 2025-12-14 07:05:13 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.064 |  |
| 2025-12-14 07:07:28 | Horowpothana (Yan Oya) | 4.78 | 🟢 Normal | -0.083 |  |
| 2025-12-14 07:05:11 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.159 |  |
| 2025-12-14 07:04:09 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)