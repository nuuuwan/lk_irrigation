# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_09:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 09:19:54 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:10:06 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-31 09:09:09 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:08:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:07:17 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-01-31 09:07:02 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:07:01 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-31 09:06:04 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 09:06:00 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.048 |  |
| 2026-01-31 09:05:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.029 |  |
| 2026-01-31 09:05:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:04:39 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 09:04:37 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:04:26 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-31 09:04:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-31 09:04:11 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:15 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-31 09:03:03 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 09:02:52 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:02:39 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.105 |  |
| 2026-01-31 09:02:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:02:12 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:01:34 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:01:31 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-31 09:01:30 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-31 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 09:01:23 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:01:18 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-31 09:01:01 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:00:58 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-31 09:00:44 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:00:07 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 09:01:18 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-01-31 09:04:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-31 09:01:30 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-31 09:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-31 09:04:26 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-31 09:10:06 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-31 09:03:03 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 09:04:39 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 09:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 09:04:37 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:02:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:02:12 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:07:01 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 09:06:04 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 09:00:07 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:01:23 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:02:39 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:07:02 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 08:08:14 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:09:09 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:08:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:04:11 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:28 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:01:34 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:00:44 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:48 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:05:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:01:01 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:19:54 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 09:03:15 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-31 09:01:31 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-01-31 09:05:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.029 |  |
| 2026-01-31 09:07:17 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.037 |  |
| 2026-01-31 09:06:00 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.048 |  |
| 2026-01-31 09:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)