# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_08:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **51** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 08:05:19 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.032 |  |
| 2025-12-22 08:05:15 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.009 |  |
| 2025-12-22 08:05:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:51 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2025-12-22 08:04:48 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.064 |  |
| 2025-12-22 08:04:42 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:34 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:33 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:22 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:04:14 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:09 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:04:00 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -0.119 |  |
| 2025-12-22 08:04:00 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-22 08:03:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.062 |  |
| 2025-12-22 08:03:36 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.012 |  |
| 2025-12-22 08:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:25 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2025-12-22 08:03:23 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:23 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2025-12-22 08:03:03 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |
| 2025-12-22 08:02:29 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:02:16 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 08:02:13 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:02:09 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:02:07 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:02:04 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:02:03 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:02:02 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:02:00 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:01:57 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:01:55 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -36.000 |  |
| 2025-12-22 08:01:26 | Thanthirimale (Malwathu Oya) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-22 08:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:01:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:01:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 08:01:02 | Horowpothana (Yan Oya) | 3.81 | 🟢 Normal | -0.058 |  |
| 2025-12-22 08:00:42 | Manampitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.105 |  |
| 2025-12-22 08:00:39 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:00:06 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:23:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:22:39 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:52 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:35 | Horowpothana (Yan Oya) | 3.85 | 🟢 Normal | -0.058 |  |
| 2025-12-22 07:13:45 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.012 |  |
| 2025-12-22 07:11:06 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:09:48 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2025-12-22 07:09:46 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 08:01:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 08:02:16 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 08:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:01:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:42 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:22:39 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:04:34 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:02:13 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:01:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:23 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:23 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:52 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:05:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:05:01 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:03:03 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 08:05:15 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.009 |  |
| 2025-12-22 08:04:22 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:04:09 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:02:29 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:00:39 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-22 08:00:06 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:02:14 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2025-12-22 08:04:00 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2025-12-22 08:03:36 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.012 |  |
| 2025-12-22 08:04:51 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2025-12-22 08:03:25 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2025-12-22 08:01:26 | Thanthirimale (Malwathu Oya) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-22 07:07:38 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.028 |  |
| 2025-12-22 08:05:19 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.032 |  |
| 2025-12-22 08:01:02 | Horowpothana (Yan Oya) | 3.81 | 🟢 Normal | -0.058 |  |
| 2025-12-22 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2025-12-22 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |
| 2025-12-22 08:03:53 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.062 |  |
| 2025-12-22 08:04:48 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.064 |  |
| 2025-12-22 08:00:42 | Manampitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.105 |  |
| 2025-12-22 08:04:00 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -0.119 |  |
| 2025-12-22 08:02:09 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)