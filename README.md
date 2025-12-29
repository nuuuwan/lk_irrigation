# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_05:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 05:03:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-30 05:03:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:03:06 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:48 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:46 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:38 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:38 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:31 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:17 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:09 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:04 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.189 |  |
| 2025-12-30 05:01:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-30 05:01:34 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-30 05:01:12 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:00:54 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.003 |  |
| 2025-12-30 05:00:51 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2025-12-30 05:00:46 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:32:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:32:10 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:31:50 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:24:47 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.008 |  |
| 2025-12-30 04:22:53 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:12:48 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.037 |  |
| 2025-12-30 04:10:05 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:09:28 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:08:35 | Panadugama (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 01:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2025-12-30 04:05:25 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-30 05:01:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 04:02:35 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 05:00:54 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.003 |  |
| 2025-12-30 05:01:12 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:22:53 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:17 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:03:06 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:48 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:02:45 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:30:28 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:31 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:02:05 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:46 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:05:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:09 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:38 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:00:46 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:02:38 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:03:20 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 02:02:12 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:03:45 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:05:54 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 03:10:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:03:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:01:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-30 05:01:34 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 04:24:47 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.008 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 05:03:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-30 05:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-30 04:02:48 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.013 |  |
| 2025-12-30 04:04:29 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.030 |  |
| 2025-12-30 05:00:51 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.037 |  |
| 2025-12-30 04:04:30 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.080 |  |
| 2025-12-30 05:02:04 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)