# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_07:23:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,592 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 07:23:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:22:39 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:52 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:35 | Horowpothana (Yan Oya) | 3.85 | 🟢 Normal | -0.091 |  |
| 2025-12-22 07:13:45 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.017 |  |
| 2025-12-22 07:11:06 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.017 |  |
| 2025-12-22 07:09:48 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -18.000 |  |
| 2025-12-22 07:09:46 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | -18.000 |  |
| 2025-12-22 07:08:47 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:08:30 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-22 07:07:38 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.028 |  |
| 2025-12-22 07:06:15 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:06:05 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.067 |  |
| 2025-12-22 07:05:50 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-22 07:05:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:05:23 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:05:01 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-22 07:04:59 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:04:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:04:05 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-22 07:03:39 | Manampitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.059 |  |
| 2025-12-22 07:03:35 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 07:03:30 | Weraganthota (Mahaweli Ganga) | -1.00 | 🟢 Normal | -0.246 |  |
| 2025-12-22 07:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:31 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:22 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:22 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:14 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2025-12-22 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.062 |  |
| 2025-12-22 07:02:04 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-22 07:01:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-22 07:01:38 | Thanthirimale (Malwathu Oya) | 4.85 | 🟢 Normal | -0.008 |  |
| 2025-12-22 07:01:38 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:01:35 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2025-12-22 07:01:25 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:01:19 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.020 |  |
| 2025-12-22 07:00:29 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:29:01 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 07:08:30 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-22 07:05:01 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-22 07:04:05 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-22 07:03:35 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 07:01:25 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:00:29 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:01:38 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:06:15 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:22 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:22 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:22:39 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:08:47 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:31 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:03:16 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:02:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:04:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:19:52 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:05:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:23:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:05:23 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 07:01:38 | Thanthirimale (Malwathu Oya) | 4.85 | 🟢 Normal | -0.008 |  |
| 2025-12-22 07:01:35 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:04:59 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 07:02:04 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-22 07:02:14 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 07:13:45 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.017 |  |
| 2025-12-22 07:11:06 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.017 |  |
| 2025-12-22 07:05:50 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2025-12-22 07:01:19 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.020 |  |
| 2025-12-22 07:01:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-22 07:07:38 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.028 |  |
| 2025-12-22 07:03:39 | Manampitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.059 |  |
| 2025-12-22 07:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.062 |  |
| 2025-12-22 07:06:05 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.067 |  |
| 2025-12-22 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2025-12-22 07:19:35 | Horowpothana (Yan Oya) | 3.85 | 🟢 Normal | -0.091 |  |
| 2025-12-22 07:03:30 | Weraganthota (Mahaweli Ganga) | -1.00 | 🟢 Normal | -0.246 |  |
| 2025-12-22 07:09:48 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)