# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_17:16:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,773 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 17:16:38 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-24 17:16:24 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-24 17:14:26 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-24 17:09:29 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:09:09 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.076 |  |
| 2025-12-24 17:08:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:07:17 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.059 |  |
| 2025-12-24 17:06:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-24 17:06:20 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 17:06:11 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:05:50 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:05:49 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.063 |  |
| 2025-12-24 17:05:48 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:04:59 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:04:34 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.038 |  |
| 2025-12-24 17:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 17:03:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 17:03:34 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 17:03:26 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:03:23 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 17:03:12 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:03:04 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2025-12-24 17:02:41 | Weraganthota (Mahaweli Ganga) | -1.08 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-24 17:02:39 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:02:35 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:02:34 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:02:28 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:02:21 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:02:12 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | -0.052 |  |
| 2025-12-24 17:02:08 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.048 |  |
| 2025-12-24 17:02:03 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.052 |  |
| 2025-12-24 17:02:03 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:01:28 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-24 17:01:18 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2025-12-24 17:00:47 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:00:26 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:58:09 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 17:01:28 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-24 17:14:26 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-24 17:02:41 | Weraganthota (Mahaweli Ganga) | -1.08 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-24 17:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-24 16:58:09 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-24 17:06:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-24 17:03:23 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 17:06:20 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 16:07:02 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 17:03:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 17:03:34 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 17:02:35 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:03:15 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:03:26 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:04:59 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 16:00:03 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:05:50 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:00:26 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:09:29 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:08:07 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:02:21 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:05:48 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:16:24 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-24 17:06:11 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:00:47 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:02:28 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:03:12 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:02:03 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:02:39 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-24 17:03:04 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.011 |  |
| 2025-12-24 17:04:34 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.038 |  |
| 2025-12-24 17:01:18 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2025-12-24 17:02:08 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.048 |  |
| 2025-12-24 17:16:38 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-24 17:02:03 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.052 |  |
| 2025-12-24 17:02:12 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | -0.052 |  |
| 2025-12-24 17:07:17 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.059 |  |
| 2025-12-24 17:05:49 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.063 |  |
| 2025-12-24 17:09:09 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)