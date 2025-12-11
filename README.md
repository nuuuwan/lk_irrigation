# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_22:11:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 22:11:13 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2025-12-11 22:10:05 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:09:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 22:09:22 | Urawa (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.018 |  |
| 2025-12-11 22:09:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.073 |  |
| 2025-12-11 22:07:59 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 22:07:50 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 22:07:16 | Thaldena (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.080 |  |
| 2025-12-11 22:07:00 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2025-12-11 22:06:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.047 |  |
| 2025-12-11 22:06:39 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:06:05 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:05:49 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-11 22:05:47 | Rathnapura (Kalu Ganga) | 2.87 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2025-12-11 22:05:26 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:04:59 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-11 22:04:49 | Siyambalanduwa (Heda Oya) | 1.63 | 🟢 Normal | -0.084 |  |
| 2025-12-11 22:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2025-12-11 22:03:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:03:31 | Padiyathalawa (Maduru Oya) | 3.45 | 🟢 Normal | -0.050 |  |
| 2025-12-11 22:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2025-12-11 22:03:29 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:03:20 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:03:20 | Nakkala (Kumbukkan Oya) | 2.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-11 22:03:12 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-11 22:02:53 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:02:07 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.013 |  |
| 2025-12-11 22:01:55 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:01:36 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 22:01:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:01:26 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:01:19 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 22:01:08 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 21:15:13 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 22:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 1.636 | 🔺 Rising |
| 2025-12-11 22:05:47 | Rathnapura (Kalu Ganga) | 2.87 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2025-12-11 22:11:13 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 22:07:00 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2025-12-11 22:04:59 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-11 22:03:12 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-11 22:03:20 | Nakkala (Kumbukkan Oya) | 2.19 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-11 22:07:50 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 22:09:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 22:01:36 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 21:01:23 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 22:01:19 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 22:07:59 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 22:01:08 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:02:53 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:01:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:01:38 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:06:05 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:03:20 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:10:05 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:01:55 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-11 22:06:39 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:11:02 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.009 |  |
| 2025-12-11 22:03:29 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:03:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:01:26 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.010 |  |
| 2025-12-11 22:02:07 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.013 |  |
| 2025-12-11 22:09:22 | Urawa (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.018 |  |
| 2025-12-11 22:05:49 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 22:06:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.047 |  |
| 2025-12-11 22:03:31 | Padiyathalawa (Maduru Oya) | 3.45 | 🟢 Normal | -0.050 |  |
| 2025-12-11 22:09:07 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.073 |  |
| 2025-12-11 22:07:16 | Thaldena (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.080 |  |
| 2025-12-11 22:04:49 | Siyambalanduwa (Heda Oya) | 1.63 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)